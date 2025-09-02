
import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

# Integração Google Drive (opcional)
try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from google.oauth2 import service_account
    GOOGLE_OK = True
except Exception:
    GOOGLE_OK = False

# =============================
# Configurações
# =============================
st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")
FATOR_CARTAO = 0.8872

ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_PROMOCOES = "promocoes.csv"
ARQ_CLIENTES = "clientes.csv"
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para fotos

# =============================
# Utilidades
# =============================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID"]
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

def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
    if "Status" not in df.columns:
        df["Status"] = "Aberto"
    df["Status"] = df["Status"].fillna("Aberto").astype(str)
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

def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
    if "Status" not in df.columns:
        df["Status"] = "Aberto"
    df["Status"] = df["Status"].fillna("Aberto").astype(str)
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

def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
    if "Status" not in df.columns:
        df["Status"] = "Aberto"
    df["Status"] = df["Status"].fillna("Aberto").astype(str)
    return df[cols].reset_index(drop=True)


def carregar_csv(caminho: str, cols_func) -> pd.DataFrame:
    if os.path.exists(caminho):
        try:
            df = pd.read_csv(caminho)
        except Exception:
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()
    return cols_func(df)

def salvar_csv(df: pd.DataFrame, caminho: str):
    df.to_csv(caminho, index=False)

def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(df[col].max()) + 1) if not df.empty else 1

def upload_foto_to_drive(file, filename, folder_id=FOLDER_FOTOS):
    """Envia a imagem para o Google Drive e retorna o file ID."""
    if not GOOGLE_OK:
        raise RuntimeError('Google Drive não disponível (bibliotecas ausentes).')
    from tempfile import NamedTemporaryFile
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive','v3', credentials=creds)
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.getbuffer())
        temp_path = tmp.name
    media = MediaFileUpload(temp_path, mimetype=getattr(file,'type','application/octet-stream'))
    metadata = {'name': filename, 'parents': [folder_id]}
    res = service.files().create(body=metadata, media_body=media, fields='id').execute()
    try:
        os.remove(temp_path)
    except Exception:
        pass
    return res.get('id')

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
clientes = carregar_csv(ARQ_CLIENTES, garantir_colunas_clientes)

st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Fluxo de Caixa","Promoções","Clientes"], index=0)

# =============================
# DASHBOARD
# =============================
if view == "Dashboard":
    st.title("📊 Dashboard Geral")

    col1, col2, col3 = st.columns(3)

    with col1:
        total_estoque = produtos["Quantidade"].sum()
        st.metric("📦 Total em Estoque", total_estoque)

    with col2:
        vendas_hoje = vendas[vendas["Data"].str.startswith(datetime.now().strftime("%Y-%m-%d"))]
        total_hoje = vendas_hoje["Total"].sum()
        st.metric("🛒 Vendas de Hoje", f"R$ {total_hoje:.2f}")

    with col3:
        hoje = date.today()
        prom_ativas = promocoes[
            (pd.to_datetime(promocoes["DataInicio"]) <= pd.to_datetime(hoje)) &
            (pd.to_datetime(promocoes["DataFim"]) >= pd.to_datetime(hoje))
        ]
        st.metric("🏷️ Promoções Ativas", len(prom_ativas))

    
    # =============================
    # ALERTAS DE VALIDADE (60 dias)
    # =============================
    hoje = date.today()
    produtos["Validade"] = pd.to_datetime(produtos["Validade"], errors="coerce").dt.date

    vencidos = produtos[produtos["Validade"] < hoje]
    a_vencer = produtos[(produtos["Validade"] >= hoje) & (produtos["Validade"] <= hoje + timedelta(days=60))]

    col4, col5 = st.columns(2)
    with col4:
        st.metric("⚠️ Produtos Vencidos", len(vencidos))
    with col5:
        st.metric("⏳ Produtos a Vencer (60 dias)", len(a_vencer))

    if not vencidos.empty:
        st.error("🚨 Produtos vencidos:")
        st.dataframe(vencidos[["Nome","Marca","Quantidade","Validade"]], use_container_width=True)

    if not a_vencer.empty:
        st.warning("⚠️ Produtos que vencem nos próximos 60 dias:")
        st.dataframe(a_vencer[["Nome","Marca","Quantidade","Validade"]], use_container_width=True)

    st.markdown("---")
    st.subheader("Resumo de Vendas por Mês")
    if not vendas.empty:
        vendas["DataMes"] = pd.to_datetime(vendas["Data"]).dt.to_period("M").astype(str)
        resumo = vendas.groupby("DataMes")["Total"].sum()

        # 🔽 Filtro de meses passados
        mes_escolhido = st.selectbox("📅 Selecionar mês", resumo.index.tolist())
        total_mes = resumo.loc[mes_escolhido]
        st.metric("🛒 Vendas no mês selecionado", f"R$ {total_mes:.2f}")

        st.bar_chart(resumo)
    else:
        st.info("Sem vendas registradas.")

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
        foto = st.file_uploader("Foto do Produto", type=["png","jpg","jpeg"])
        salvar = st.form_submit_button("➕ Adicionar Produto")

        if salvar:
            if not nome.strip():
                st.error("O nome do produto é obrigatório.")
            else:
                novo_id = prox_id(produtos, "ID")
                foto_id = None
                if 'foto' in locals() and foto is not None:
                    try:
                        foto_id = upload_foto_to_drive(foto, f"produto_{novo_id}.jpg")
                    except Exception as e:
                        st.warning(f"Falha ao enviar foto ao Drive: {e}")
                novo = {
                    "ID": novo_id,
                    "Nome": nome.strip(),
                    "Marca": marca.strip(),
                    "Categoria": categoria.strip(),
                    "Quantidade": int(quantidade),
                    "PrecoCusto": float(preco_custo),
                    "PrecoVista": float(preco_vista),
                    "PrecoCartao": float(preco_cartao),
                    "Validade": str(validade),
                    "FotoID": foto_id
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
        forma = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão","Fiado"])
        nome_cliente_fiado = None
        data_pagamento_fiado = None
        if forma == "Fiado":
            nome_cliente_fiado = st.text_input("Nome do Cliente (Fiado)")
            data_pagamento_fiado = st.date_input("Data de Pagamento (Fiado)", value=date.today())

        if forma in ("Pix", "Dinheiro", "Fiado"):
            preco_unit = float(p["PrecoVista"])
        else:
            preco_unit = float(p["PrecoCartao"])
        preco_unit, tem_promo, promo_txt = preco_com_promocao(pid, preco_unit)
        preco_final = preco_unit
        total = preco_final * int(qtd)
        if tem_promo and promo_txt:
            st.info(promo_txt)

        colA, colB = st.columns(2)
        with colA:
            st.metric("Preço unitário aplicado", f"R$ {preco_final:.2f}")
        with colB:
            st.metric("Total", f"R$ {total:.2f}")

        if st.button("Registrar Venda"):
            if int(qtd) > int(p["Quantidade"]):
                st.error("Estoque insuficiente.")
            else:
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

                # Se for fiado, registrar na base de clientes
                if forma == "Fiado" and nome_cliente_fiado and data_pagamento_fiado:
                    if "Status" not in clientes.columns:
                        clientes["Status"] = "Aberto"
                    nova_div = {
                        "ID": prox_id(clientes, "ID"),
                        "Cliente": str(nome_cliente_fiado).strip(),
                        "Produto": str(p["Nome"]),
                        "Valor": float(total),
                        "DataPagamento": str(data_pagamento_fiado),
                        "Status": "Aberto",
                    }
                    clientes = pd.concat([clientes, pd.DataFrame([nova_div])], ignore_index=True)
                    salvar_csv(clientes, ARQ_CLIENTES)

                st.success(f"Venda registrada! Total R$ {total:.2f}")

    st.markdown("---")
    st.subheader("Histórico de Vendas")
    st.dataframe(vendas, use_container_width=True)

elif view ==  "Fluxo de Caixa":
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

        col1, col2, col3 = st.columns(3)
        col1.metric("Receita Bruta", f"R$ {receita_bruta:.2f}")
        col2.metric("Receita Líquida (pós taxa)", f"R$ {receita_liquida:.2f}")
        col3.metric("Lucro Líquido", f"R$ {lucro_liquido:.2f}")

        st.markdown("---")
        st.subheader("📈 Gráficos")

        # Vendas por forma de pagamento
        forma_pg = vendas.groupby("FormaPagamento")["Total"].sum()

        fig, ax = plt.subplots()
        ax.pie(forma_pg, labels=forma_pg.index, autopct="%1.1f%%")
        ax.set_title("Distribuição por Forma de Pagamento")
        st.pyplot(fig)

        # Exportação CSV
        st.download_button("⬇️ Exportar Vendas (CSV)", vendas.to_csv(index=False), "vendas_exportadas.csv", "text/csv")

# =============================
# PROMOÇÕES (adições de validação)
# =============================

elif view == "Promoções":
    st.title("🏷️ Promoções")

    if produtos.empty:
        st.info("Cadastre produtos antes de criar promoções.")
    else:
        with st.form("form_promo", clear_on_submit=True):
            produto_options = [f"{int(r.ID)} - {r.Nome}" for r in produtos.itertuples(index=False)]
            produto_opt = st.selectbox("Produto", produto_options) if produto_options else None

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                nome_prod = produtos.loc[produtos["ID"] == pid, "Nome"].iloc[0]
            else:
                pid = None
                nome_prod = None

            desconto = st.number_input("Desconto (%)", min_value=1.0, max_value=100.0, step=1.0, value=10.0)
            di = st.date_input("Data início", value=date.today())
            dfim = st.date_input("Data fim", value=date.today())
            salvar = st.form_submit_button("➕ Criar promoção")

            if salvar:
                if pid is None:
                    st.error("Selecione um produto.")
                elif dfim < di:
                    st.error("A data final não pode ser antes da inicial.")
                elif not promocoes[(promocoes["IDProduto"] == pid)].empty:
                    st.warning("Já existe uma promoção cadastrada para este produto.")
                else:
                    nova = {
                        "IDPromo": prox_id(promocoes, "IDPromo"),
                        "IDProduto": pid,
                        "NomeProduto": nome_prod,
                        "Desconto": float(desconto),
                        "DataInicio": str(di),
                        "DataFim": str(dfim),
                    }
                    promocoes = pd.concat([promocoes, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promocoes, ARQ_PROMOCOES)
                    st.success("Promoção criada com sucesso!")

    st.markdown("### 📋 Promoções cadastradas")
    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        st.dataframe(promocoes, use_container_width=True)
        promo_options = [f"{int(r.IDPromo)} - {r.NomeProduto}" for r in promocoes.itertuples(index=False)]
        promo_opt = st.selectbox("Selecionar promoção para excluir", promo_options) if promo_options else None
        if st.button("🗑️ Excluir promoção selecionada") and promo_opt:
            pid_del = int(promo_opt.split(" - ")[0])
            promocoes = promocoes[promocoes["IDPromo"] != pid_del].reset_index(drop=True)
            salvar_csv(promocoes, ARQ_PROMOCOES)
            st.warning("Promoção excluída com sucesso!")


elif view == "Clientes":
    st.title("👥 Clientes (Fiado)")

    # Cadastro manual de fiado
    with st.form("form_fiado"):
        col1, col2, col3 = st.columns([2,2,1])
        with col1:
            nome = st.text_input("Cliente")
        with col2:
            prod_nome = st.text_input("Produto")
        with col3:
            valor = st.number_input("Valor", min_value=0.0, step=1.0)
        data_pag = st.date_input("Data de Pagamento", value=date.today())
        if st.form_submit_button("Adicionar Venda Fiado"):
            if nome and prod_nome and float(valor) > 0:
                nova = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": nome,
                    "Produto": prod_nome,
                    "Valor": float(valor),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto",
                }
                clientes = pd.concat([clientes, pd.DataFrame([nova])], ignore_index=True)
                salvar_csv(clientes, ARQ_CLIENTES)
                st.success("Fiado adicionado.")

    st.subheader("📋 Dívidas cadastradas")
    st.dataframe(clientes, use_container_width=True)

    # Gerenciar em aberto
    if "Status" not in clientes.columns:
        clientes["Status"] = "Aberto"
    abertas = clientes[clientes["Status"] != "Pago"].copy()
    st.subheader("🔓 Dívidas em Aberto")
    st.dataframe(abertas, use_container_width=True)

    # Excluir dívida manualmente

# Pagar dívida selecionada
st.subheader("💰 Quitar dívida")
if not clientes.empty:
    opts_pay = [f"{i} - {row.Cliente} - {row.Produto} - R$ {row.Valor:.2f} - {row.DataPagamento}" for i, row in clientes.iterrows() if row.Status != "Pago"]
    escolha_pay = st.selectbox("Selecione a dívida para pagar", opts_pay, key="sel_pagar_divida")
    forma_pg = st.selectbox("Forma de pagamento", ["Dinheiro","Pix","Cartão"], key="forma_pg_divida")
    if st.button("Marcar como Pago", key="btn_pagar_divida"):
        if escolha_pay:
            idx_pay = int(escolha_pay.split(" - ")[0])
            valor_original = float(clientes.loc[idx_pay, "Valor"])
            if forma_pg in ["Dinheiro","Pix"]:
                valor_pago = valor_original
            else:
                valor_pago = valor_original * 1.05
            clientes.loc[idx_pay, "Status"] = "Pago"
            salvar_csv(clientes, ARQ_CLIENTES)
            st.success(f"Dívida quitada com {forma_pg}! Valor pago: R$ {valor_pago:.2f}")


    st.subheader("🗑️ Excluir dívida")
    if not clientes.empty:
        opts_del = [f"{i} - {row.Cliente} - {row.Produto} - R$ {row.Valor:.2f} - {row.DataPagamento}" for i, row in clientes.iterrows()]
        escolha_del = st.selectbox("Selecione a dívida para excluir", opts_del, key="sel_excluir_divida")
        if st.button("Excluir dívida selecionada"):
            try:
                idx_del = int(escolha_del.split(" - ")[0])
                clientes.drop(index=idx_del, inplace=True)
                clientes.reset_index(drop=True, inplace=True)
                salvar_csv(clientes, ARQ_CLIENTES)
                st.warning("Dívida excluída!")
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")

    hoje = date.today()
    base_alerta = clientes[clientes.get("Status", "Aberto") != "Pago"].copy()
    if not base_alerta.empty:
        base_alerta["DataPagamento"] = pd.to_datetime(base_alerta["DataPagamento"], errors="coerce").dt.date
    else:
        base_alerta["DataPagamento"] = pd.to_datetime(base_alerta["DataPagamento"], errors="coerce").dt.date  # garante coluna

    vencidas = base_alerta[base_alerta["DataPagamento"] < hoje]
    a_vencer = base_alerta[(base_alerta["DataPagamento"] >= hoje) & (base_alerta["DataPagamento"] <= hoje + timedelta(days=3))]

    st.info("⏳ Dívidas a vencer (próximos 3 dias)")
    st.dataframe(a_vencer[["Cliente","Produto","Valor","DataPagamento"]], use_container_width=True)

    if not vencidas.empty:
        st.error("⚠️ Dívidas vencidas")
        st.dataframe(vencidas[["Cliente","Produto","Valor","DataPagamento"]], use_container_width=True)
