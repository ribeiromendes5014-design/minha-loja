import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
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

def load_csv(filename):
    folder_id = st.secrets["DRIVE_FOLDER_ID"]
    file_id = get_file_id(filename, folder_id)
    if not file_id:
        return pd.DataFrame()
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    data = io.BytesIO()
    downloader = MediaIoBaseDownload(data, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    data.seek(0)
    return pd.read_csv(data)

def save_csv(filename, df):
    folder_id = st.secrets["DRIVE_FOLDER_ID"]
    service = get_drive_service()
    file_id = get_file_id(filename, folder_id)
    data = io.BytesIO()
    df.to_csv(data, index=False)
    data.seek(0)
    media = MediaIoBaseUpload(data, mimetype="text/csv", resumable=True)
    if file_id:
        service.files().update(fileId=file_id, media_body=media).execute()
    else:
        file_metadata = {"name": filename, "parents": [folder_id]}
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
