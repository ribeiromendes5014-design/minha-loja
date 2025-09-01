import streamlit as st
import pandas as pd
import os

# Função para carregar CSV com tratamento de vazio
def carregar_csv(caminho, colunas_esperadas):
    if not os.path.exists(caminho):
        return pd.DataFrame(columns=colunas_esperadas)
    try:
        df = pd.read_csv(caminho)
        if df.empty:
            return pd.DataFrame(columns=colunas_esperadas)
        return df
    except Exception:
        return pd.DataFrame(columns=colunas_esperadas)

# Arquivos
ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_PROMOCOES = "promocoes.csv"

# Carregar dados
produtos = carregar_csv(ARQ_PRODUTOS, ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"])
vendas = carregar_csv(ARQ_VENDAS, ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"])
promocoes = carregar_csv(ARQ_PROMOCOES, ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"])

# Abas
aba = st.sidebar.radio("Navegação", ["Dashboard","Produtos","Vendas","Promoções"])

# Dashboard
if aba == "Dashboard":
    st.header("📊 Dashboard")
    if vendas.empty:
        st.info("Nenhuma venda registrada.")
    else:
        st.dataframe(vendas)

# Produtos
elif aba == "Produtos":
    st.header("📦 Produtos")
    if produtos.empty:
        st.info("Nenhum produto cadastrado.")
    else:
        st.dataframe(produtos)

# Vendas
elif aba == "Vendas":
    st.header("🛒 Vendas")
    if vendas.empty:
        st.info("Nenhuma venda registrada.")
    else:
        st.dataframe(vendas)

# Promoções
elif aba == "Promoções":
    st.header("🏷️ Promoções")
    if promocoes.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promocoes)
