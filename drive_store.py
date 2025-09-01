import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2 import service_account
import streamlit as st

def get_drive_service():
    creds = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

def get_file_id(filename, folder_id):
    service = get_drive_service()
    query = f"'{folder_id}' in parents and name='{filename}' and trashed=false"
    results = service.files().list(q=query, fields="files(id)").execute()
    files = results.get("files", [])
    return files[0]["id"] if files else None

def load_csv(filename, folder_id):
    service = get_drive_service()
    file_id = get_file_id(filename, folder_id)
    if not file_id:
        return pd.DataFrame()
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = service._http.request(request.uri)
    fh.write(downloader[1])
    fh.seek(0)
    return pd.read_csv(fh)

def salvar_csv(df, filename, folder_id):
    service = get_drive_service()
    file_id = get_file_id(filename, folder_id)
    csv_buffer = io.BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    media = MediaIoBaseUpload(csv_buffer, mimetype="text/csv")
    if file_id:
        service.files().update(fileId=file_id, media_body=media).execute()
    else:
        file_metadata = {"name": filename, "parents": [folder_id]}
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
