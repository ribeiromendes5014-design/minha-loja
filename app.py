
import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

# Integração Google Drive
try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
    from google.oauth2 import service_account
    import io
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQ_USUARIOS = os.path.join(BASE_DIR, "usuarios.csv")
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para fotos

# =============================
# Autenticação Google Drive
# =============================
def get_drive_service():
    creds = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

def download_csv_from_drive(filename, cols_func):
    if not GOOGLE_OK:
        return cols_func(pd.DataFrame())
    service = get_drive_service()
    query = f"name='{filename}' and '{FOLDER_FOTOS}' in parents"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        return cols_func(pd.DataFrame())
    file_id = items[0]['id']
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.seek(0)
    try:
        df = pd.read_csv(fh)
    except Exception:
        df = pd.DataFrame()
    return cols_func(df)

def upload_csv_to_drive(df: pd.DataFrame, filename: str):
    if not GOOGLE_OK:
        return
    service = get_drive_service()
    # excluir antigo se existir
    query = f"name='{filename}' and '{FOLDER_FOTOS}' in parents"
    results = service.files().list(q=query, fields="files(id)").execute()
    for item in results.get("files", []):
        service.files().delete(fileId=item["id"]).execute()
    # criar novo
    df.to_csv(filename, index=False)
    media = MediaFileUpload(filename, mimetype="text/csv")
    metadata = {"name": filename, "parents": [FOLDER_FOTOS]}
    service.files().create(body=metadata, media_body=media, fields="id").execute()
    os.remove(filename)

# =============================
# Gestão de Usuários (Segurança)
# =============================
def carregar_usuarios():
    if os.path.exists(ARQ_USUARIOS):
        df = pd.read_csv(ARQ_USUARIOS, encoding="utf-8-sig")
    else:
        df = pd.DataFrame([{"usuario": "admin", "senha": "1234", "nivel": "admin"}])
        df.to_csv(ARQ_USUARIOS, index=False, encoding="utf-8")
    df["usuario"] = df["usuario"].astype(str).str.strip().str.lower()
    df["senha"]   = df["senha"].astype(str).str.strip()
    df["nivel"]   = df["nivel"].astype(str).str.strip().str.lower()
    return df

def salvar_usuarios(df):
    df.to_csv(ARQ_USUARIOS, index=False, encoding="utf-8")

usuarios_df = carregar_usuarios()

# =============================
# Login
# =============================
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.nivel = None

if not st.session_state.logado:
    st.image("logo.png", width=300)
    st.title("🔐 Acesso ao Sistema")

    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuarios_df = carregar_usuarios()
        user_norm  = (user or "").strip().lower()
        senha_norm = (senha or "").strip()

        u = usuarios_df[(usuarios_df["usuario"] == user_norm) & (usuarios_df["senha"] == senha_norm)]

        if not u.empty:
            st.session_state.logado = True
            st.session_state.usuario = user_norm
            st.session_state.nivel = u.iloc[0]["nivel"]
            st.success(f"Bem-vindo, {user_norm}!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()

# =============================
# Funções auxiliares de colunas
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

def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(df[col].max()) + 1) if not df.empty else 1

# =============================
# Carregar dados do Drive
# =============================
produtos = download_csv_from_drive(ARQ_PRODUTOS, garantir_colunas_produtos)
vendas = download_csv_from_drive(ARQ_VENDAS, garantir_colunas_vendas)
promocoes = download_csv_from_drive(ARQ_PROMOCOES, garantir_colunas_promocoes)
clientes = download_csv_from_drive(ARQ_CLIENTES, garantir_colunas_clientes)

# =============================
# Menu Único de Navegação
# =============================
menu_opcoes = ["Dashboard"]
if st.session_state.nivel == "admin":
    menu_opcoes += ["Produtos", "Vendas", "Clientes", "Fluxo de Caixa", "Promoções", "Segurança"]
elif st.session_state.nivel == "user":
    menu_opcoes += ["Produtos", "Vendas", "Clientes"]

st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", menu_opcoes, index=0)

st.sidebar.markdown("---")
st.sidebar.write(f"👤 Usuário: {st.session_state.usuario} ({st.session_state.nivel})")
if st.sidebar.button("🚪 Sair"):
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.nivel = None
    st.rerun()

# Obs.: As abas (Dashboard, Produtos, Vendas, etc.) devem ser adaptadas para usar upload_csv_to_drive() sempre que salvar alterações.
