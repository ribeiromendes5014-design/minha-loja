import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google.oauth2 import service_account
import streamlit as st

# Carrega credenciais do Streamlit Secrets
def get_drive_service():
    creds = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

# Procura arquivo dentro da pasta do Drive
def get_file_id(filename, folder_id):
    service = get_drive_service()
    query = f"name='{filename}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])
    return files[0]["id"] if files else None

# Carrega CSV do Drive
def load_csv(filename, folder_id):
    file_id = get_file_id(filename, folder_id)
    if not file_id:
        return pd.DataFrame()  # Se não existir, retorna vazio

    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)
    return pd.read_csv(fh)

# Salva CSV no Drive
def save_csv(df, filename, folder_id):
    service = get_drive_service()
    file_id = get_file_id(filename, folder_id)

    df.to_csv(filename, index=False)
    media = MediaFileUpload(filename, mimetype="text/csv")

    if file_id:
        service.files().update(fileId=file_id, media_body=media).execute()
    else:
        file_metadata = {"name": filename, "parents": [folder_id]}
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
