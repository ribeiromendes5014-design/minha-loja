
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

# ===== NOVO: PDF (recibo)
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm

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

# (restante do código segue igual ao anterior, já corrigido)
