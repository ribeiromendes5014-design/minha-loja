import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

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

# =============================
# Gestão de Usuários (Segurança)
# =============================
def carregar_usuarios():
    if os.path.exists(ARQ_USUARIOS):
        df = pd.read_csv(ARQ_USUARIOS, encoding="utf-8-sig")
    else:
        df = pd.DataFrame([{"usuario": "admin", "senha": "1234", "nivel": "admin"}])
        df.to_csv(ARQ_USUARIOS, index=False, encoding="utf-8")

    # normalizar
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
# Menu de Navegação
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

# =============================
# Segurança (apenas Admin)
# =============================
if view == "Segurança" and st.session_state.nivel == "admin":
    st.title("🔒 Gerenciar Usuários")

    usuarios_df = carregar_usuarios()

    # Listar usuários
    st.subheader("📋 Usuários cadastrados")
    st.dataframe(usuarios_df, use_container_width=True)

    # Criar usuário
    st.subheader("➕ Criar novo usuário")
    with st.form("form_novo_usuario", clear_on_submit=True):
        novo_user = st.text_input("Usuário")
        nova_senha = st.text_input("Senha", type="password")
        nivel = st.selectbox("Nível", ["user", "admin"])
        criar = st.form_submit_button("Criar")

        if criar:
            novo_user_norm = (novo_user or "").strip().lower()
            nova_senha_norm = (nova_senha or "").strip()
            nivel_norm = (nivel or "").strip().lower()

            if not novo_user_norm or not nova_senha_norm:
                st.error("Usuário e senha são obrigatórios.")
            elif novo_user_norm in usuarios_df["usuario"].values:
                st.error("Usuário já existe!")
            else:
                usuarios_df = pd.concat([usuarios_df, pd.DataFrame([{
                    "usuario": novo_user_norm,
                    "senha": nova_senha_norm,
                    "nivel": nivel_norm
                }])], ignore_index=True)
                salvar_usuarios(usuarios_df)
                st.success(f"Usuário {novo_user_norm} criado com sucesso!")
                st.rerun()

    # Excluir usuário
    st.subheader("🗑️ Excluir usuário")
    excluir_user = st.selectbox("Selecione o usuário", usuarios_df["usuario"].tolist())
    if st.button("Excluir usuário selecionado"):
        if excluir_user == "admin":
            st.error("Não é permitido excluir o usuário admin principal!")
        else:
            usuarios_df = usuarios_df[usuarios_df["usuario"] != excluir_user].reset_index(drop=True)
            salvar_usuarios(usuarios_df)
            st.warning(f"Usuário {excluir_user} excluído com sucesso!")
            st.rerun()

# =============================
# A partir daqui entra seu código original de Dashboard, Produtos, Vendas, etc.
# Basta colar tudo abaixo normalmente.
# =============================
