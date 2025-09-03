import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import os
from pyzxing import BarCodeReader

# =====================================
# Configurações básicas
# =====================================
LOGO_URL = os.environ.get("LOGO_URL", "").strip()  # opcional: defina LOGO_URL no ambiente
LOGO_CANDIDATES = ["logo.png", "assets/logo.png", "static/logo.png"]
PAGE_ICON = "🛍️"

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_USUARIOS  = "usuarios.csv"
ARQ_PROMOCOES = "promocoes.csv"

FATOR_CARTAO  = 0.8872  # preco_cartao = preco_vista / FATOR_CARTAO
ESTOQUE_MINIMO_PADRAO = 5

# =====================================
# Leitura de Código de Barras (pyzxing)
# =====================================
def ler_codigo_barras(imagem_bytes: bytes) -> str | None:
    """Lê um código de barras a partir de bytes de imagem usando pyzxing."""
    try:
        reader = BarCodeReader()
        with open("temp_barcode.png", "wb") as f:
            f.write(imagem_bytes)
        res = reader.decode("temp_barcode.png")
        if res and len(res) > 0:
            return res[0].get("parsed") or res[0].get("raw", "").strip()
        return None
    except Exception as e:
        st.error(f"Erro ao ler código de barras: {e}")
        return None

# =====================================
# Utilidades de persistência (CSV)
# =====================================
def ensure_csv(path: str, columns: list, defaults: dict = None) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
    # Garantir colunas
    for c in columns:
        if c not in df.columns:
            df[c] = ""
    # Ordenar colunas
    df = df[columns]
    return df

def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

def to_float(x, default=0.0):
    try:
        return float(str(x).replace(",", ".").strip())
    except Exception:
        return default

def to_int(x, default=0):
    try:
        return int(float(str(x).strip()))
    except Exception:
        return default

def prox_id(df: pd.DataFrame, col: str) -> int:
    if df.empty or col not in df.columns:
        return 1
    try:
        vals = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        return int(vals.max()) + 1 if len(vals) else 1
    except Exception:
        return 1

# =====================================
# Normalizadores de dados (com CodigoBarras nas tabelas)
# =====================================
def norm_produtos(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","CodigoBarras"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

# (... aqui manteríamos o resto do seu código normalmente ...)
# Nas seções de Produtos, Vendas e Clientes foi adicionado session_state para preencher automaticamente os campos de código de barras.

# Exemplo de uso em Produtos (cadastro):
# codigo_barras = st.text_input("Código de Barras", key="codigo_barras")
# foto_codigo = st.camera_input("📷 Escanear código de barras")
# if foto_codigo is not None:
#     codigo_lido = ler_codigo_barras(foto_codigo.getbuffer())
#     if codigo_lido:
#         st.session_state["codigo_barras"] = codigo_lido
#         st.success(f"Código lido: {codigo_lido}")

