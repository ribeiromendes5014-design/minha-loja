
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
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para CSVs e fotos

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
        # Não existe no Drive → retorna DataFrame vazio (não salva no Drive ainda)
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
    # criar novo (somente se houver dados ou colunas corretas)
    if df is not None and not df.empty:
        df.to_csv(filename, index=False)
        media = MediaFileUpload(filename, mimetype="text/csv")
        metadata = {"name": filename, "parents": [FOLDER_FOTOS]}
        service.files().create(body=metadata, media_body=media, fields="id").execute()
        os.remove(filename)

# =============================
# Aqui continuam as funções auxiliares e o restante do sistema
# (produtos, vendas, clientes, promoções, etc.)
# Sempre que houver alteração nos dados, chamar upload_csv_to_drive(df, "arquivo.csv")
# =============================
