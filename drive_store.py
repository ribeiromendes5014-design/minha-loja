# -*- coding: utf-8 -*-
import io
import json
import pandas as pd
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import streamlit as st

# Lê segredos
DRIVE_FOLDER_ID = st.secrets["DRIVE_FOLDER_ID"]
GCP_INFO = st.secrets["gcp_service_account"]

def _service():
    creds = service_account.Credentials.from_service_account_info(
        GCP_INFO,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    return build('drive', 'v3', credentials=creds)

def _find_file_by_name(name, folder_id):
    svc = _service()
    q = f"name = '{name}' and '{folder_id}' in parents and trashed = false"
    res = svc.files().list(q=q, fields="files(id, name)").execute()
    files = res.get('files', [])
    return files[0] if files else None

def _ensure_folder(name, parent_id):
    svc = _service()
    q = f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed = false"
    res = svc.files().list(q=q, fields="files(id, name)").execute()
    files = res.get('files', [])
    if files:
        return files[0]['id']
    meta = {'name': name, 'mimeType': 'application/vnd.google-apps.folder', 'parents':[parent_id]}
    created = svc.files().create(body=meta, fields="id").execute()
    return created['id']

def ensure_file(filename, header_cols):
    """Garante que o arquivo exista no Drive; se não existir, cria com cabeçalho."""
    svc = _service()
    f = _find_file_by_name(filename, DRIVE_FOLDER_ID)
    if f:
        return f['id']
    # cria
    csv_bytes = (",".join(header_cols) + "\n").encode("utf-8")
    media = MediaIoBaseUpload(io.BytesIO(csv_bytes), mimetype='text/csv', resumable=False)
    meta = {'name': filename, 'parents':[DRIVE_FOLDER_ID]}
    new = svc.files().create(body=meta, media_body=media, fields="id").execute()
    return new['id']

def list_files_in_folder(folder_id):
    svc = _service()
    res = svc.files().list(q=f"'{folder_id}' in parents and trashed=false", fields="files(id,name,mimeType,modifiedTime)").execute()
    return res.get("files", [])

def load_csv(filename):
    """Baixa CSV do Drive -> DataFrame (auto cria se não existir)."""
    file = _find_file_by_name(filename, DRIVE_FOLDER_ID)
    if not file:
        # cria com cabeçalho vazio
        return pd.DataFrame()
    file_id = file['id']
    svc = _service()
    req = svc.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, req)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    try:
        df = pd.read_csv(fh)
    except Exception:
        fh.seek(0)
        df = pd.read_csv(fh, sep=";")
    return df

def save_csv(filename, df: pd.DataFrame):
    """Envia CSV para o Drive (atualiza ou cria)."""
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    svc = _service()
    f = _find_file_by_name(filename, DRIVE_FOLDER_ID)
    media = MediaIoBaseUpload(io.BytesIO(csv_bytes), mimetype='text/csv', resumable=False)
    if f:
        svc.files().update(fileId=f['id'], media_body=media).execute()
    else:
        meta = {'name': filename, 'parents':[DRIVE_FOLDER_ID]}
        svc.files().create(body=meta, media_body=media).execute()

def backup_csv(filename, df: pd.DataFrame):
    """Salva uma cópia com timestamp na subpasta 'backup'."""
    try:
        backup_id = _ensure_folder("backup", DRIVE_FOLDER_ID)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"{ts}_{filename}"
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        svc = _service()
        media = MediaIoBaseUpload(io.BytesIO(csv_bytes), mimetype='text/csv', resumable=False)
        meta = {'name': name, 'parents':[backup_id]}
        svc.files().create(body=meta, media_body=media).execute()
    except Exception as e:
        # Não quebra a app por falha de backup
        print("Backup falhou:", e)
