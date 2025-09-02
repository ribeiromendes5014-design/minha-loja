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
ARQ_USUARIOS = "usuarios.csv"
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para fotos

# =============================
# Gestão de Usuários (Segurança)
# =============================
def carregar_usuarios():
    if os.path.exists(ARQ_USUARIOS):
        return pd.read_csv(ARQ_USUARIOS)
    else:
        df = pd.DataFrame([{"usuario": "admin", "senha": "1234", "nivel": "admin"}])
        df.to_csv(ARQ_USUARIOS, index=False)
        return df

def salvar_usuarios(df):
    df.to_csv(ARQ_USUARIOS, index=False)

usuarios_df = carregar_usuarios()

# =============================
# Login
# =============================
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.nivel = None

if not st.session_state.logado:
    st.image("logo.png", width=300)  # coloque sua logo na mesma pasta
    st.title("🔐 Acesso ao Sistema")

    user = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        u = usuarios_df[(usuarios_df["usuario"] == user) & (usuarios_df["senha"] == senha)]
        if not u.empty:
            st.session_state.logado = True
            st.session_state.usuario = user
            st.session_state.nivel = u.iloc[0]["nivel"]
            st.success(f"Bem-vindo, {user}!")
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
            if novo_user in usuarios_df["usuario"].values:
                st.error("Usuário já existe!")
            else:
                usuarios_df = pd.concat([usuarios_df, pd.DataFrame([{
                    "usuario": novo_user,
                    "senha": nova_senha,
                    "nivel": nivel
                }])], ignore_index=True)
                salvar_usuarios(usuarios_df)
                st.success(f"Usuário {novo_user} criado com sucesso!")
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
# A partir daqui continua o código original (Dashboard, Produtos, Vendas, etc.)
# =============================

# ... (cole aqui todo o restante do seu código original de Dashboard, Produtos, Vendas, Fluxo de Caixa, Promoções, Clientes)
