import streamlit as st
import pandas as pd
from drive_store import load_csv, save_csv

# Configurações iniciais
st.set_page_config(page_title="Loja Cosméticos", layout="wide")

# Pega ID da pasta do Drive do secrets
FOLDER_ID = st.secrets["DRIVE_FOLDER_ID"]

# Carrega os dados
produtos = load_csv("produtos.csv", FOLDER_ID)
vendas = load_csv("vendas.csv", FOLDER_ID)
promocoes = load_csv("promocoes.csv", FOLDER_ID)

st.title("💄 Loja Cosméticos - Versão Online")

st.sidebar.title("Menu")
aba = st.sidebar.radio("Ir para:", ["Produtos", "Vendas", "Dashboard"])

# Aba de Produtos
if aba == "Produtos":
    st.subheader("📦 Cadastro de Produtos")
    st.dataframe(produtos)

# Aba de Vendas
elif aba == "Vendas":
    st.subheader("🛒 Registro de Vendas")
    st.dataframe(vendas)

# Aba de Dashboard
elif aba == "Dashboard":
    st.subheader("📊 Relatórios")
    st.dataframe(promocoes)
