
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
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para fotos

# =============================
# Gestão de Usuários (Segurança)
# =============================
def carregar_usuarios():
    if os.path.exists(ARQ_USUARIOS):
        df = pd.read_csv(ARQ_USUARIOS, encoding="utf-8-sig")
    else:
        df = pd.DataFrame([{"usuario": "admin", "senha": "1234", "nivel": "admin"}])
        df.to_csv(ARQ_USUARIOS, index=False, encoding="utf-8")
    df["usuario"] = df["usuario"].astype(str).str.strip().str.lower()
    df["senha"]   = df["senha"].astype(str).str.strip()
    df["nivel"]   = df["nivel"].astype(str).str.strip().str.lower()
    return df

def salvar_usuarios(df):
    df.to_csv(ARQ_USUARIOS, index=False, encoding="utf-8")

usuarios_df = carregar_usuarios()

# =============================
# Login
# =============================
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.nivel = None

if not st.session_state.logado:
    st.image("logo.png", width=300)
    st.title("🔐 Acesso ao Sistema")

    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        usuarios_df = carregar_usuarios()
        user_norm  = (user or "").strip().lower()
        senha_norm = (senha or "").strip()

        u = usuarios_df[(usuarios_df["usuario"] == user_norm) & (usuarios_df["senha"] == senha_norm)]

        if not u.empty:
            st.session_state.logado = True
            st.session_state.usuario = user_norm
            st.session_state.nivel = u.iloc[0]["nivel"]
            st.success(f"Bem-vindo, {user_norm}!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()

# =============================
# Menu Único de Navegação
# =============================
menu_opcoes = ["Dashboard"]
if st.session_state.nivel == "admin":
    menu_opcoes += ["Produtos", "Vendas", "Clientes", "Fluxo de Caixa", "Promoções", "Segurança"]
elif st.session_state.nivel == "user":
    menu_opcoes += ["Produtos", "Vendas", "Clientes"]

st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", menu_opcoes, index=0)

st.sidebar.markdown("---")
st.sidebar.write(f"👤 Usuário: {st.session_state.usuario} ({st.session_state.nivel})")
if st.sidebar.button("🚪 Sair"):
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.nivel = None
    st.rerun()
