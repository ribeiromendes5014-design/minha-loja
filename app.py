import streamlit as st
import pandas as pd
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# =========================
# CONFIGURAÇÃO GOOGLE DRIVE
# =========================
FOLDER_ID = "10MKzmsYsVyN42J_yLHH4KnJUPCmy6IkQ"

# Carregar credenciais do secrets
creds = service_account.Credentials.from_service_account_info(
    st.secrets["GOOGLE_CREDENTIALS"],
    scopes=["https://www.googleapis.com/auth/drive"]
)

# Inicializar serviço do Drive
service = build("drive", "v3", credentials=creds)

# =========================
# FUNÇÕES AUXILIARES
# =========================

def baixar_arquivo_drive(nome_arquivo):
    """Baixa um arquivo CSV do Google Drive pela pasta configurada"""
    try:
        query = f"'{FOLDER_ID}' in parents and name = '{nome_arquivo}' and trashed = false"
        results = service.files().list(q=query, fields="files(id, name)").execute()
        items = results.get("files", [])
        if not items:
            return pd.DataFrame()  # Arquivo não encontrado
        file_id = items[0]["id"]
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        fh.seek(0)
        return pd.read_csv(fh)
    except Exception as e:
        st.error(f"Erro ao carregar {nome_arquivo}: {e}")
        return pd.DataFrame()

# =========================
# CARREGAR DADOS
# =========================
produtos = baixar_arquivo_drive("produtos.csv")
vendas = baixar_arquivo_drive("vendas.csv")
promocoes = baixar_arquivo_drive("promocoes.csv")

# Garantir colunas mínimas se vazio
if produtos.empty:
    produtos = pd.DataFrame(columns=["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"])

if vendas.empty:
    vendas = pd.DataFrame(columns=["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"])

if promocoes.empty:
    promocoes = pd.DataFrame(columns=["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"])

# =========================
# INTERFACE STREAMLIT
# =========================
aba = st.sidebar.radio("Navegação", ["Dashboard","Produtos","Vendas","Promoções"])

if aba == "Dashboard":
    st.header("📊 Dashboard")
    if vendas.empty:
        st.info("Nenhuma venda registrada.")
    else:
        st.dataframe(vendas)

elif aba == "Produtos":
    st.header("📦 Produtos")
    if produtos.empty:
        st.info("Nenhum produto cadastrado.")
    else:
        st.dataframe(produtos)

elif aba == "Vendas":
    st.header("🛒 Vendas")
    if vendas.empty:
        st.info("Nenhuma venda registrada.")
    else:
        st.dataframe(vendas)

elif aba == "Promoções":
    st.header("🏷️ Promoções")
    if promocoes.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promocoes)
