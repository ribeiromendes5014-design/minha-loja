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
    for c in columns:
        if c not in df.columns:
            df[c] = ""
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
# Normalizadores
# =====================================
def norm_produtos(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","CodigoBarras"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_vendas(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","CodigoBarras","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","CodigoBarras","Valor","DataPagamento","Status","FormaPagamento"]
    df = ensure_csv(ARQ_CLIENTES, cols)
    df["Valor"] = df["Valor"].apply(to_float)
    return df

def norm_usuarios(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["Usuario","Senha"]
    df = ensure_csv(ARQ_USUARIOS, cols)
    if df.empty:
        df = pd.DataFrame([{"Usuario":"admin","Senha":"123"}])
        save_csv(df, ARQ_USUARIOS)
    return df

def norm_promocoes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    df = ensure_csv(ARQ_PROMOCOES, cols)
    df["IDProduto"] = df["IDProduto"].astype(str)
    df["Desconto"] = df["Desconto"].apply(to_float)
    df["DataInicio"] = df["DataInicio"].astype(str)
    df["DataFim"] = df["DataFim"].astype(str)
    return df

# =====================================
# Sessão: login
# =====================================
def reset_admin_user():
    df = norm_usuarios(pd.DataFrame())
    if "Usuario" not in df.columns:
        df = pd.DataFrame(columns=["Usuario","Senha"])
    if (df["Usuario"] == "admin").any():
        df.loc[df["Usuario"]=="admin", "Senha"] = "123"
    else:
        df.loc[len(df)] = {"Usuario":"admin","Senha":"123"}
    save_csv(df, ARQ_USUARIOS)
    return True

def do_login():
    st.session_state.setdefault("logado", False)
    st.session_state.setdefault("usuario_logado", None)
    if st.session_state.get("logado"):
        return True

    st.title("🔐 Login")

    user = st.text_input("Usuário")
    pwd  = st.text_input("Senha", type="password")
    manter = st.checkbox("Manter conectado", value=False)

    if st.button("Entrar", use_container_width=True):
        usuarios = norm_usuarios(pd.DataFrame())

        # Sempre aceita admin/123
        if (user == "admin" and pwd == "123"):
            reset_admin_user()
            st.session_state["logado"] = True
            st.session_state["usuario_logado"] = "admin" if manter else None
            st.rerun()
        elif not usuarios[(usuarios["Usuario"]==user) & (usuarios["Senha"]==pwd)].empty:
            st.session_state["logado"] = True
            st.session_state["usuario_logado"] = user if manter else None
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    st.stop()

# =====================================
# (restante do código do app vai aqui, sem mudanças...)
# =====================================
