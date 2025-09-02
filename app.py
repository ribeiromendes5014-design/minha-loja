
import streamlit as st
import pandas as pd
import os
from datetime import datetime, date
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io

try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
    from google.oauth2 import service_account
    GOOGLE_OK = True
except Exception:
    GOOGLE_OK = False

st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")

# IDs no Google Drive
ARQ_PRODUTOS_ID = "1p1UyY7DdkNG1RlEwOKwLaJ9mgwFTpkAC"
ARQ_VENDAS_ID = "1EIREc1zPSRY0OS7xz8d5hpOMI2c43mBI"
ARQ_PROMOCOES_ID = "1CqwlBWv43XO0XWsgRvBjfXgurZlqslIk"
ARQ_CLIENTES_ID = "1DO60F8Eu43xurBDhIxvp0ysMac7LSDkE"
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"

# ================= GOOGLE DRIVE =================
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
def garantir_colunas_produtos(df):
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    return df[cols].reset_index(drop=True)

def garantir_colunas_clientes(df):
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    return df[cols].reset_index(drop=True)

def garantir_colunas_vendas(df):
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    return df[cols].reset_index(drop=True)

def garantir_colunas_promocoes(df):
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    return df[cols].reset_index(drop=True)

# Utils
def prox_id(df, col):
    return (int(df[col].max()) + 1) if not df.empty else 1

# Função para gerar recibo PDF
def gerar_recibo(venda, produto, logo_path="ChatGPT Image 1_09_2025, 21_52_48.png"):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Logo
    try:
        logo = ImageReader(logo_path)
        c.drawImage(logo, 40, height-120, width=100, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass

    # Cabeçalho
    c.setFont("Helvetica-Bold", 14)
    c.drawString(160, height-60, "Loja de Cosméticos")
    c.setFont("Helvetica", 10)
    c.drawString(160, height-80, "WhatsApp: (00) 00000-0000")
    c.drawString(160, height-95, "Instagram: @loja")

    # Info
    c.setFont("Helvetica", 9)
    c.drawString(40, height-140, f"Data: {venda['Data']}")
    c.drawString(250, height-140, f"Forma de Pagamento: {venda['FormaPagamento']}")

    # Tabela
    y = height - 180
    c.setFont("Helvetica-Bold", 9)
    c.drawString(40, y, "Produto")
    c.drawString(250, y, "Qtd")
    c.drawString(300, y, "Unitário")
    c.drawString(400, y, "Total")
    y -= 15

    c.setFont("Helvetica", 9)
    c.drawString(40, y, str(venda['NomeProduto']))
    c.drawString(250, y, str(venda['Quantidade']))
    c.drawString(300, y, f"R$ {venda['PrecoUnitario']:.2f}")
    c.drawString(400, y, f"R$ {venda['Total']:.2f}")

    # Total
    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y, "TOTAL:")
    c.drawString(400, y, f"R$ {venda['Total']:.2f}")

    # Rodapé
    c.setFont("Helvetica", 10)
    c.drawString(40, 80, "Obrigado pela preferência!")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Carregar dados
df_produtos = carregar_csv_drive(ARQ_PRODUTOS_ID, garantir_colunas_produtos)
df_vendas = carregar_csv_drive(ARQ_VENDAS_ID, garantir_colunas_vendas)
df_promocoes = carregar_csv_drive(ARQ_PROMOCOES_ID, garantir_colunas_promocoes)
df_clientes = carregar_csv_drive(ARQ_CLIENTES_ID, garantir_colunas_clientes)

# Sidebar
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Fluxo de Caixa","Promoções","Clientes"])

# Vendas
if view == "Vendas":
    st.title("🧾 Vendas")
    if df_produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        opt = st.selectbox("Produto", [f'{int(r.ID)} - {r.Nome} (Estoque: {int(r.Quantidade)})' for r in df_produtos.itertuples(index=False)])
        pid = int(opt.split(" - ")[0])
        p = df_produtos[df_produtos["ID"] == pid].iloc[0]
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão","Fiado"])

        preco_unit = float(p["PrecoVista"]) if forma in ("Pix","Dinheiro","Fiado") else float(p["PrecoCartao"])
        total = preco_unit * qtd

        if st.button("Registrar Venda"):
            nova = {
                "IDVenda": prox_id(df_vendas, "IDVenda"),
                "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "IDProduto": int(p["ID"]),
                "NomeProduto": str(p["Nome"]),
                "FormaPagamento": forma,
                "Quantidade": int(qtd),
                "PrecoUnitario": float(preco_unit),
                "Total": float(total),
            }
            df_vendas = pd.concat([df_vendas, pd.DataFrame([nova])], ignore_index=True)
            salvar_csv_drive(df_vendas, ARQ_VENDAS_ID)

            st.success(f"Venda registrada! Total R$ {total:.2f}")

            # Gerar recibo
            recibo = gerar_recibo(nova, p)
            st.download_button(
                label="⬇️ Baixar Recibo",
                data=recibo,
                file_name=f"recibo_venda_{nova['IDVenda']}.pdf",
                mime="application/pdf"
            )
