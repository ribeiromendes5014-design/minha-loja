
import streamlit as st
import pandas as pd
import os
from datetime import datetime, date

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
import io

# =============================
# Integração Google Drive
# =============================
DRIVE_FOLDER_ID = st.secrets.get("DRIVE_FOLDER_ID", "")
# Usa seção [gcp_service_account] conforme configurado no secrets do Streamlit
_creds = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/drive"]
)
_drive = build("drive", "v3", credentials=_creds)

def _drive_get_file_id(filename: str) -> str | None:
    try:
        query = f"'{DRIVE_FOLDER_ID}' in parents and name = '{filename}' and trashed = false"
        resp = _drive.files().list(q=query, fields="files(id,name)").execute()
        items = resp.get("files", [])
        return items[0]["id"] if items else None
    except Exception:
        return None

def _drive_download_csv(filename: str) -> pd.DataFrame:
    file_id = _drive_get_file_id(filename)
    if not file_id:
        return pd.DataFrame()
    req = _drive.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, req)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    buf.seek(0)
    try:
        return pd.read_csv(buf)
    except Exception:
        return pd.DataFrame()

def _drive_upload_csv(filename: str, df: pd.DataFrame):
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    media = MediaIoBaseUpload(io.BytesIO(csv_bytes), mimetype="text/csv", resumable=False)
    file_id = _drive_get_file_id(filename)
    if file_id:
        _drive.files().update(fileId=file_id, media_body=media, body={"name": filename}).execute()
    else:
        meta = {"name": filename, "parents": [DRIVE_FOLDER_ID], "mimeType": "text/csv"}
        _drive.files().create(body=meta, media_body=media, fields="id").execute()


# =============================
# Configurações
# =============================
st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")
FATOR_CARTAO = 0.8872

ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_PROMOCOES = "promocoes.csv"

# =============================
# Utilidades
# =============================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    df["Validade"] = df["Validade"].astype(str)
    return df[cols].reset_index(drop=True)

def garantir_colunas_vendas(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    df["Data"] = df["Data"].astype(str)
    return df[cols].reset_index(drop=True)

def garantir_colunas_promocoes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Desconto"] = pd.to_numeric(df["Desconto"], errors="coerce").fillna(0.0).astype(float)
    df["DataInicio"] = pd.to_datetime(df["DataInicio"], errors="coerce").dt.date.astype(str)
    df["DataFim"] = pd.to_datetime(df["DataFim"], errors="coerce").dt.date.astype(str)
    return df[cols].reset_index(drop=True)


def carregar_csv(caminho: str, cols_func) -> pd.DataFrame:
    # Ignora caminho local; usa Google Drive
    filename = os.path.basename(caminho)
    df = _drive_download_csv(filename)
    return cols_func(df)



def salvar_csv(df: pd.DataFrame, caminho: str):
    # Ignora caminho local; salva no Google Drive
    filename = os.path.basename(caminho)
    try:
        _drive_upload_csv(filename, df)
    except Exception as e:
        st.error(f"Erro ao salvar {filename} no Google Drive: {e}")




def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(df[col].max()) + 1) if not df.empty else 1

def preco_com_promocao(pid, preco_normal):
    hoje = date.today()
    promos = promocoes[promocoes["IDProduto"] == pid]
    if promos.empty:
        return preco_normal, False, None
    for _, r in promos.iterrows():
        try:
            di = pd.to_datetime(r["DataInicio"]).date()
            df = pd.to_datetime(r["DataFim"]).date()
        except Exception:
            continue
        if di <= hoje <= df:
            preco_desc = preco_normal * (1 - float(r["Desconto"]) / 100)
            return preco_desc, True, r
    return preco_normal, False, None

# =============================
# Carregar dados
# =============================
produtos = carregar_csv(ARQ_PRODUTOS, garantir_colunas_produtos)
vendas = carregar_csv(ARQ_VENDAS, garantir_colunas_vendas)
promocoes = carregar_csv(ARQ_PROMOCOES, garantir_colunas_promocoes)

st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Produtos","Vendas","Fluxo de Caixa","Promoções"], index=0)

# =============================
# PRODUTOS
# =============================
if view == "Produtos":
    st.title("🛍️ Produtos")
    # 🔔 Alerta de estoque baixo
    baixo_estoque = produtos[produtos["Quantidade"] <= 1]
    if not baixo_estoque.empty:
        nomes_alerta = ", ".join([f"{row['Nome']} (Estoque: {row['Quantidade']})" for _, row in baixo_estoque.iterrows()])
        st.warning(f"⚠️ Produtos com estoque baixo: {nomes_alerta}")


    # Cadastro de produtos
    with st.form("form_produto", clear_on_submit=True):
        st.subheader("Cadastrar novo produto")
        nome = st.text_input("Nome do Produto")
        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        validade = st.date_input("Validade", value=date.today())
        quantidade = st.number_input("Quantidade", min_value=0, step=1, value=0)
        preco_custo = st.number_input("Preço de Custo", min_value=0.0, step=0.01, format="%.2f")
        preco_vista = st.number_input("Preço à Vista", min_value=0.0, step=0.01, format="%.2f")
        preco_cartao = preco_vista / FATOR_CARTAO if preco_vista > 0 else 0.0
        st.metric("Preço no Cartão (automático)", f"R$ {preco_cartao:.2f}")
        salvar = st.form_submit_button("➕ Adicionar Produto")

        if salvar:
            if not nome.strip():
                st.error("O nome do produto é obrigatório.")
            else:
                novo = {
                    "ID": prox_id(produtos, "ID"),
                    "Nome": nome.strip(),
                    "Marca": marca.strip(),
                    "Categoria": categoria.strip(),
                    "Quantidade": int(quantidade),
                    "PrecoCusto": float(preco_custo),
                    "PrecoVista": float(preco_vista),
                    "PrecoCartao": float(preco_cartao),
                    "Validade": str(validade)
                }
                produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
                salvar_csv(produtos, ARQ_PRODUTOS)
                st.success(f"Produto '{nome}' adicionado com sucesso!")

    # Filtros de busca
    st.markdown("---")
    st.subheader("🔎 Buscar Produtos")
    col1, col2, col3 = st.columns(3)
    with col1:
        filtro_nome = st.text_input("Buscar por Nome")
    with col2:
        filtro_marca = st.selectbox("Filtrar por Marca", [""] + sorted(produtos["Marca"].dropna().unique().tolist()))
    with col3:
        max_preco = st.number_input("Preço máximo", min_value=0.0, step=0.01, value=0.0)

    df_filtrado = produtos.copy()
    if filtro_nome:
        df_filtrado = df_filtrado[df_filtrado["Nome"].str.contains(filtro_nome, case=False, na=False)]
    if filtro_marca:
        df_filtrado = df_filtrado[df_filtrado["Marca"] == filtro_marca]
    if max_preco > 0:
        df_filtrado = df_filtrado[df_filtrado["PrecoVista"] <= max_preco]

    st.markdown("### 📋 Lista de Produtos")
    if df_filtrado.empty:
        st.info("Nenhum produto encontrado com os filtros.")
    else:
        st.dataframe(df_filtrado, use_container_width=True)

    # Edição/Exclusão
    if not produtos.empty:
        opt = st.selectbox("Selecionar produto para editar/excluir", [f'{int(r.ID)} - {r.Nome}' for r in produtos.itertuples(index=False)])
        if opt:
            pid = int(opt.split(" - ")[0])
            prod_sel = produtos[produtos["ID"] == pid].iloc[0]

            with st.form("form_editar_produto", clear_on_submit=False):
                nome_e = st.text_input("Nome", value=prod_sel["Nome"])
                marca_e = st.text_input("Marca", value=prod_sel["Marca"])
                categoria_e = st.text_input("Categoria", value=prod_sel["Categoria"])
                validade_e = st.date_input("Validade", value=pd.to_datetime(prod_sel["Validade"]).date())
                quantidade_e = st.number_input("Quantidade", min_value=0, step=1, value=int(prod_sel["Quantidade"]))
                preco_custo_e = st.number_input("Preço de Custo", min_value=0.0, step=0.01, value=float(prod_sel["PrecoCusto"]))
                preco_vista_e = st.number_input("Preço à Vista", min_value=0.0, step=0.01, value=float(prod_sel["PrecoVista"]))
                preco_cartao_e = preco_vista_e / FATOR_CARTAO if preco_vista_e > 0 else 0.0
                st.metric("Preço no Cartão (automático)", f"R$ {preco_cartao_e:.2f}")

                salvar_edicao = st.form_submit_button("💾 Salvar alterações")
                excluir_prod = st.form_submit_button("🗑️ Excluir produto")

                if salvar_edicao:
                    produtos.loc[produtos["ID"] == pid, ["Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"]] = [
                        nome_e.strip(),
                        marca_e.strip(),
                        categoria_e.strip(),
                        int(quantidade_e),
                        float(preco_custo_e),
                        float(preco_vista_e),
                        float(preco_cartao_e),
                        str(validade_e),
                    ]
                    salvar_csv(produtos, ARQ_PRODUTOS)
                    st.success("Produto atualizado com sucesso!")

                if excluir_prod:
                    produtos = produtos[produtos["ID"] != pid].reset_index(drop=True)
                    salvar_csv(produtos, ARQ_PRODUTOS)
                    st.warning("Produto excluído com sucesso!")

# =============================
# VENDAS
# =============================
elif view == "Vendas":
    st.title("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        opt = st.selectbox("Produto", [f'{int(r.ID)} - {r.Nome} (Estoque: {int(r.Quantidade)})' for r in produtos.itertuples(index=False)])
        pid = int(opt.split(" - ")[0])
        p = produtos[produtos["ID"] == pid].iloc[0]
        st.metric("Preço à vista", f'R$ {p["PrecoVista"]:.2f}')
        st.metric("Preço no cartão", f'R$ {p["PrecoCartao"]:.2f}')
        st.metric("Estoque", int(p["Quantidade"]))

        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão"])
        preco_unit = float(p["PrecoVista"]) if forma in ("Pix","Dinheiro") else float(p["PrecoCartao"])
        preco_final, em_promo, promo = preco_com_promocao(pid, preco_unit)
        if em_promo:
            st.markdown(f"<span style='color:red; font-weight:bold'>💥 Promoção: R$ {preco_final:.2f}</span> <del>R$ {preco_unit:.2f}</del>", unsafe_allow_html=True)
        else:
            st.info(f"Valor unitário selecionado: R$ {preco_final:.2f} ({forma})")

        if st.button("Registrar Venda"):
            if qtd > int(p["Quantidade"]):
                st.error("Estoque insuficiente.")
            else:
                total = float(qtd) * preco_final
                nova = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "IDProduto": int(p["ID"]),
                    "NomeProduto": str(p["Nome"]),
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_final),
                    "Total": float(total),
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova])], ignore_index=True)
                salvar_csv(vendas, ARQ_VENDAS)
                produtos.loc[produtos["ID"] == pid, "Quantidade"] = int(p["Quantidade"]) - int(qtd)
                salvar_csv(produtos, ARQ_PRODUTOS)
                st.success(f"Venda registrada! Total R$ {total:.2f}")

    st.markdown("---")
    st.subheader("Histórico de Vendas")
    st.dataframe(vendas, use_container_width=True)

    if not vendas.empty:
        sel_v = st.selectbox("Selecionar venda para excluir", [f'{int(r.IDVenda)} - {r.NomeProduto}' for r in vendas.itertuples(index=False)])
        if sel_v:
            vid = int(sel_v.split(" - ")[0])
            venda_sel = vendas[vendas["IDVenda"] == vid].iloc[0]
            if st.button("🗑️ Excluir venda selecionada"):
                pid = int(venda_sel["IDProduto"])
                qtd_vendida = int(venda_sel["Quantidade"])
                if pid in produtos["ID"].values:
                    produtos.loc[produtos["ID"] == pid, "Quantidade"] += qtd_vendida
                    salvar_csv(produtos, ARQ_PRODUTOS)
                vendas = vendas[vendas["IDVenda"] != vid].reset_index(drop=True)
                salvar_csv(vendas, ARQ_VENDAS)
                st.warning("Venda excluída e estoque atualizado.")

# =============================
# FLUXO DE CAIXA
# =============================
elif view == "Fluxo de Caixa":
    st.title("💵 Fluxo de Caixa")
    if vendas.empty:
        st.info("Sem vendas ainda.")
    else:
        receita_bruta = float(vendas["Total"].sum())
        vendas["Liquido"] = vendas.apply(
            lambda r: float(r["Total"]) * (FATOR_CARTAO if str(r["FormaPagamento"]) == "Cartão" else 1.0),
            axis=1
        )
        receita_liquida = float(vendas["Liquido"].sum())
        custo_total = 0.0
        for _, v in vendas.iterrows():
            pid = int(v["IDProduto"])
            prod = produtos[produtos["ID"] == pid]
            if not prod.empty:
                custo_total += float(v["Quantidade"]) * float(prod.iloc[0]["PrecoCusto"])
        lucro_liquido = receita_liquida - custo_total

        st.metric("Receita Bruta", f"R$ {receita_bruta:.2f}")
        st.metric("Receita Líquida (pós taxa)", f"R$ {receita_liquida:.2f}")
        st.metric("Lucro Líquido", f"R$ {lucro_liquido:.2f}")
        st.dataframe(vendas, use_container_width=True)

# =============================
# PROMOÇÕES
# =============================
elif view == "Promoções":
    st.title("🏷️ Promoções")
    with st.form("form_promo", clear_on_submit=True):
        produto_opt = st.selectbox("Produto", [f'{int(r.ID)} - {r.Nome}' for r in produtos.itertuples(index=False)])
        pid = int(produto_opt.split(" - ")[0])
        nome_prod = produtos[produtos["ID"] == pid].iloc[0]["Nome"]
        desconto = st.number_input("Desconto (%)", min_value=1.0, max_value=100.0, step=1.0)
        di = st.date_input("Data início", value=date.today())
        df = st.date_input("Data fim", value=date.today())

        salvar = st.form_submit_button("➕ Criar promoção")
        if salvar:
            nova = {
                "IDPromo": prox_id(promocoes, "IDPromo"),
                "IDProduto": pid,
                "NomeProduto": nome_prod,
                "Desconto": float(desconto),
                "DataInicio": str(di),
                "DataFim": str(df),
            }
            promocoes = pd.concat([promocoes, pd.DataFrame([nova])], ignore_index=True)
            salvar_csv(promocoes, ARQ_PROMOCOES)
            st.success("Promoção criada com sucesso!")

    st.markdown("### 📋 Promoções")
    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        st.dataframe(promocoes, use_container_width=True)
        promo_opt = st.selectbox("Selecionar promoção para excluir", [f'{int(r.IDPromo)} - {r.NomeProduto}' for r in promocoes.itertuples(index=False)])
        if st.button("🗑️ Excluir promoção selecionada"):
            pid = int(promo_opt.split(" - ")[0])
            promocoes = promocoes[promocoes["IDPromo"] != pid].reset_index(drop=True)
            salvar_csv(promocoes, ARQ_PROMOCOES)
            st.warning("Promoção excluída com sucesso!")
