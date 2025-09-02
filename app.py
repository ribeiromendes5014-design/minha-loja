import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
    from google.oauth2 import service_account
    import io
    GOOGLE_OK = True
except Exception:
    GOOGLE_OK = False

st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")
FATOR_CARTAO = 0.8872

# IDs dos arquivos no Google Drive
ARQ_PRODUTOS_ID = "1p1UyY7DdkNG1RlEwOKwLaJ9mgwFTpkAC"
ARQ_VENDAS_ID = "1EIREc1zPSRY0OS7xz8d5hpOMI2c43mBI"
ARQ_PROMOCOES_ID = "1CqwlBWv43XO0XWsgRvBjfXgurZlqslIk"
ARQ_CLIENTES_ID = "1DO60F8Eu43xurBDhIxvp0ysMac7LSDkE"
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"

# Funções de integração com Google Drive
def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)

def carregar_csv_drive(file_id: str, cols_func) -> pd.DataFrame:
    if not GOOGLE_OK:
        raise RuntimeError("Google Drive não disponível.")
    service = get_drive_service()
    req = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, req)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    try:
        df = pd.read_csv(fh)
    except Exception:
        df = pd.DataFrame()
    return cols_func(df)

def salvar_csv_drive(df: pd.DataFrame, file_id: str):
    if not GOOGLE_OK:
        raise RuntimeError("Google Drive não disponível.")
    service = get_drive_service()
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    media = MediaFileUpload(csv_buffer, mimetype='text/csv', resumable=True)
    service.files().update(fileId=file_id, media_body=media).execute()

# Garantia de colunas
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

# Utilidades
def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(df[col].max()) + 1) if not df.empty else 1

def upload_foto_to_drive(file, filename, folder_id=FOLDER_FOTOS):
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

# Carregar dados do Drive
produtos = carregar_csv_drive(ARQ_PRODUTOS_ID, garantir_colunas_produtos)
vendas = carregar_csv_drive(ARQ_VENDAS_ID, garantir_colunas_vendas)
promocoes = carregar_csv_drive(ARQ_PROMOCOES_ID, garantir_colunas_promocoes)
clientes = carregar_csv_drive(ARQ_CLIENTES_ID, garantir_colunas_clientes)

# ============ Interface Streamlit ============
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Fluxo de Caixa","Promoções","Clientes"], index=0)

# Produtos
if view == "Produtos":
    st.title("📦 Produtos")
    st.dataframe(produtos, use_container_width=True, editable=True, key="produtos_edit")
    if "produtos_edit" in st.session_state:
        produtos = st.session_state.produtos_edit
        salvar_csv_drive(produtos, ARQ_PRODUTOS_ID)
        st.success("Produtos atualizados automaticamente no Drive!")

# Clientes
if view == "Clientes":
    st.title("👥 Clientes")
    st.dataframe(clientes, use_container_width=True, editable=True, key="clientes_edit")
    if "clientes_edit" in st.session_state:
        clientes = st.session_state.clientes_edit
        salvar_csv_drive(clientes, ARQ_CLIENTES_ID)
        st.success("Clientes atualizados automaticamente no Drive!")

# Promoções
if view == "Promoções":
    st.title("🔥 Promoções")
    st.dataframe(promocoes, use_container_width=True, editable=True, key="promocoes_edit")
    if "promocoes_edit" in st.session_state:
        promocoes = st.session_state.promocoes_edit
        salvar_csv_drive(promocoes, ARQ_PROMOCOES_ID)
        st.success("Promoções atualizadas automaticamente no Drive!")

# Fluxo de Caixa (Dashboard simplificado)
if view == "Fluxo de Caixa" or view == "Dashboard":
    st.title("📊 Fluxo de Caixa / Dashboard")
    if not vendas.empty:
        vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
        resumo = vendas.groupby(vendas["Data"].dt.date)["Total"].sum()
        st.line_chart(resumo)
    else:
        st.info("Nenhuma venda registrada ainda.")

# Vendas
if view == "Vendas":
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
                salvar_csv_drive(vendas, ARQ_VENDAS_ID)
                produtos.loc[produtos["ID"] == pid, "Quantidade"] = int(p["Quantidade"]) - int(qtd)
                salvar_csv_drive(produtos, ARQ_PRODUTOS_ID)

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
                    salvar_csv_drive(clientes, ARQ_CLIENTES_ID)

                st.success(f"Venda registrada! Total R$ {total:.2f}")

    st.markdown("---")
    st.subheader("Histórico de Vendas")
    st.dataframe(vendas, use_container_width=True)

    if not vendas.empty:
        opt_venda = st.selectbox(
            "Selecionar venda para editar/excluir",
            [f'{int(r.IDVenda)} - {r.NomeProduto} - {r.FormaPagamento} - R$ {r.Total:.2f}' 
             for r in vendas.itertuples(index=False)],
            key="sel_venda"
        )

        if opt_venda:
            vid = int(opt_venda.split(" - ")[0])
            venda_sel = vendas[vendas["IDVenda"] == vid].iloc[0]
            produto_sel = produtos[produtos["ID"] == int(venda_sel["IDProduto"])].iloc[0]

            with st.form("form_editar_venda", clear_on_submit=False):
                qtd_e = st.number_input("Quantidade", min_value=1, step=1, value=int(venda_sel["Quantidade"]))
                forma_e = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão","Fiado"], 
                                       index=["Pix","Dinheiro","Cartão","Fiado"].index(venda_sel["FormaPagamento"]))
                preco_unit_e = st.number_input("Preço Unitário", min_value=0.0, step=0.01, value=float(venda_sel["PrecoUnitario"]))
                total_e = qtd_e * preco_unit_e
                st.metric("Novo Total", f"R$ {total_e:.2f}")

                salvar_edicao = st.form_submit_button("💾 Salvar alterações")
                excluir_venda = st.form_submit_button("🗑️ Excluir venda")

                if salvar_edicao:
                    diff_qtd = int(qtd_e) - int(venda_sel["Quantidade"])
                    produtos.loc[produtos["ID"] == int(venda_sel["IDProduto"]), "Quantidade"] -= diff_qtd
                    salvar_csv_drive(produtos, ARQ_PRODUTOS_ID)

                    vendas.loc[vendas["IDVenda"] == vid, ["Quantidade","FormaPagamento","PrecoUnitario","Total"]] = [
                        int(qtd_e), forma_e, float(preco_unit_e), float(total_e)
                    ]
                    salvar_csv_drive(vendas, ARQ_VENDAS_ID)
                    st.success("Venda atualizada com sucesso!")

                if excluir_venda:
                    produtos.loc[produtos["ID"] == int(venda_sel["IDProduto"]), "Quantidade"] += int(venda_sel["Quantidade"])
                    salvar_csv_drive(produtos, ARQ_PRODUTOS_ID)

                    vendas = vendas[vendas["IDVenda"] != vid].reset_index(drop=True)
                    salvar_csv_drive(vendas, ARQ_VENDAS_ID)
                    st.warning("Venda excluída com sucesso e estoque ajustado!")