
import streamlit as st
import pandas as pd
from datetime import datetime
from drive_store import load_csv, salvar_csv

# IDs e Config
FOLDER_ID = st.secrets["DRIVE_FOLDER_ID"]

# Arquivos no Drive
ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_PROMOCOES = "promocoes.csv"
ARQ_FLUXO = "fluxo_caixa.csv"

# Funções utilitárias
def carregar_dados():
    produtos = load_csv(ARQ_PRODUTOS, FOLDER_ID)
    vendas = load_csv(ARQ_VENDAS, FOLDER_ID)
    promocoes = load_csv(ARQ_PROMOCOES, FOLDER_ID)
    fluxo = load_csv(ARQ_FLUXO, FOLDER_ID)
    return produtos, vendas, promocoes, fluxo

def salvar_dados(produtos, vendas, promocoes, fluxo):
    salvar_csv(produtos, ARQ_PRODUTOS, FOLDER_ID)
    salvar_csv(vendas, ARQ_VENDAS, FOLDER_ID)
    salvar_csv(promocoes, ARQ_PROMOCOES, FOLDER_ID)
    salvar_csv(fluxo, ARQ_FLUXO, FOLDER_ID)

# App
st.set_page_config(page_title="Minha Loja", layout="wide")

menu = ["Dashboard", "Produtos", "Vendas", "Promoções", "Fluxo de Caixa"]
choice = st.sidebar.selectbox("Menu", menu)

produtos, vendas, promocoes, fluxo = carregar_dados()

if choice == "Dashboard":
    st.title("📊 Dashboard")
    if not vendas.empty:
        vendas['Data'] = pd.to_datetime(vendas['Data'])
        vendas['Mes'] = vendas['Data'].dt.to_period('M')
        resumo = vendas.groupby('Mes')['Total'].sum().reset_index()
        resumo['Mes'] = resumo['Mes'].astype(str)
        st.bar_chart(resumo.set_index('Mes'))
    else:
        st.info("Nenhuma venda registrada ainda.")

elif choice == "Produtos":
    st.title("📦 Cadastro de Produtos")
    with st.form("novo_produto"):
        nome = st.text_input("Nome")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        qtd = st.number_input("Quantidade", min_value=0, step=1)
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            novo = pd.DataFrame([[nome, preco, qtd]], columns=["Nome", "Preco", "Quantidade"])
            produtos = pd.concat([produtos, novo], ignore_index=True)
            salvar_csv(produtos, ARQ_PRODUTOS, FOLDER_ID)
            st.success("Produto cadastrado!")
    st.dataframe(produtos)

elif choice == "Vendas":
    st.title("🛒 Registro de Vendas")
    if produtos.empty:
        st.warning("Cadastre produtos antes de registrar vendas.")
    else:
        with st.form("nova_venda"):
            produto = st.selectbox("Produto", produtos["Nome"])
            qtd = st.number_input("Quantidade", min_value=1, step=1)
            submitted = st.form_submit_button("Registrar Venda")
            if submitted:
                preco_unit = float(produtos.loc[produtos["Nome"] == produto, "Preco"].values[0])
                total = preco_unit * qtd
                nova = pd.DataFrame([[produto, qtd, preco_unit, total, datetime.today().strftime("%Y-%m-%d")]],
                                    columns=["Produto", "Quantidade", "Preco_Unit", "Total", "Data"])
                vendas = pd.concat([vendas, nova], ignore_index=True)
                salvar_csv(vendas, ARQ_VENDAS, FOLDER_ID)
                st.success("Venda registrada!")
    st.dataframe(vendas)

elif choice == "Promoções":
    st.title("💸 Promoções")
    with st.form("nova_promo"):
        produto = st.text_input("Produto")
        desconto = st.number_input("Desconto (%)", min_value=0, max_value=100, step=1)
        submitted = st.form_submit_button("Adicionar Promoção")
        if submitted:
            nova = pd.DataFrame([[produto, desconto]], columns=["Produto", "Desconto"])
            promocoes = pd.concat([promocoes, nova], ignore_index=True)
            salvar_csv(promocoes, ARQ_PROMOCOES, FOLDER_ID)
            st.success("Promoção adicionada!")
    st.dataframe(promocoes)

elif choice == "Fluxo de Caixa":
    st.title("💰 Fluxo de Caixa")
    if not vendas.empty:
        total_vendas = vendas["Total"].sum()
    else:
        total_vendas = 0
    st.metric("Total em Vendas", f"R$ {total_vendas:,.2f}")
    st.dataframe(fluxo)
