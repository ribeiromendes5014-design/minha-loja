
import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2 import service_account
import streamlit as st

# Cria serviço do Google Drive
def get_drive_service():
    creds = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

# Busca arquivo pelo nome
def get_file_id(filename, folder_id):
    service = get_drive_service()
    q = f"name='{filename}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=q, fields="files(id)").execute()
    files = results.get("files", [])
    return files[0]["id"] if files else None

# Carrega CSV
def load_csv(filename, folder_id):
    service = get_drive_service()
    file_id = get_file_id(filename, folder_id)
    if not file_id:
        return pd.DataFrame()
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseUpload(fh, mimetype="text/csv", resumable=True)
    # Aqui ajustamos para leitura
    fh = io.BytesIO(service.files().get_media(fileId=file_id).execute())
    return pd.read_csv(fh)

# Salva CSV substituindo
def salvar_csv(df, filename, folder_id):
    service = get_drive_service()

    # Apaga arquivo antigo se existir
    q = f"name='{filename}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=q, fields="files(id)").execute()
    for f in results.get("files", []):
        service.files().delete(fileId=f["id"]).execute()

    # Upload novo
    file_metadata = {"name": filename, "parents": [folder_id]}
    media = MediaIoBaseUpload(
        io.BytesIO(df.to_csv(index=False).encode("utf-8")),
        mimetype="text/csv"
    )
    service.files().create(body=file_metadata, media_body=media, fields="id").execute()
