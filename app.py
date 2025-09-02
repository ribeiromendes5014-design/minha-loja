import streamlit as st
import pandas as pd
import io, os, re, base64, requests
from datetime import datetime, date, timedelta

# ====================== Configurações ======================
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")

# CSVs no GitHub
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"

# Pasta para fotos dentro do repositório
FOTOS_DIR = "fotos_produtos"

# Fator de ajuste para preço no cartão
FATOR_CARTAO   = 0.8872

# ====================== Funções auxiliares ======================
def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c != "Valor" else 0.0
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    if "Status" in df.columns:
        df["Status"] = df["Status"].replace("", "Aberto")
    return df[cols]

def garantir_colunas_vendas(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c not in ["Quantidade","PrecoUnitario","Total"] else 0
    df["Quantidade"]    = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    df["PrecoUnitario"] = pd.to_numeric(df["PrecoUnitario"], errors="coerce").fillna(0.0).astype(float)
    df["Total"]         = pd.to_numeric(df["Total"], errors="coerce").fillna(0.0).astype(float)
    return df[cols]

def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(pd.to_numeric(df[col], errors="coerce").fillna(0).max()) + 1) if not df.empty else 1

# Simulações (normalmente viriam do GitHub)
if "clientes" not in st.session_state:
    st.session_state.clientes = garantir_colunas_clientes(pd.DataFrame())

if "vendas" not in st.session_state:
    st.session_state.vendas = garantir_colunas_vendas(pd.DataFrame())

clientes = st.session_state.clientes
vendas   = st.session_state.vendas

# ====================== Sidebar ======================
st.sidebar.title("📚 Menu")
opcoes = ["Dashboard","Clientes"]
view = st.sidebar.radio("Navegar", opcoes, index=1)

# ====================== Views ======================
if view == "Dashboard":
    st.title("📊 Dashboard")
    st.write("Resumo do sistema em construção.")

if view == "Clientes":
    st.header("👥 Clientes / Fiado")
    with st.expander("Lançar novo fiado"):
        cliente = st.text_input("Cliente")
        produto_f = st.text_input("Produto")
        valor = st.number_input("Valor", 0.0, step=0.01)
        data_pag = st.date_input("Data prevista de pagamento", value=date.today())
        if st.button("Lançar"):
            novo = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": cliente, "Produto": produto_f,
                "Valor": float(valor), "DataPagamento": str(data_pag), "Status": "Aberto"
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.clientes = clientes
            st.success("Lançamento criado e salvo.")

    st.subheader("Contas em aberto")
    st.dataframe(clientes, use_container_width=True)

    with st.expander("Baixar/Pagar conta"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None
        forma_pg = None
        if id_sel is not None:
            forma_pg = st.selectbox("Forma de pagamento", ["Dinheiro", "PIX", "Cartão"])
        if st.button("Marcar como Pago") and id_sel is not None:
            row = clientes.loc[clientes["ID"]==id_sel].iloc[0]
            valor = row["Valor"]
            if forma_pg == "Cartão":
                valor = round(valor / FATOR_CARTAO, 2)
            clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
            st.session_state.clientes = clientes

            nova_venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": "",
                "NomeProduto": row["Produto"],
                "FormaPagamento": forma_pg,
                "Quantidade": 1,
                "PrecoUnitario": float(valor),
                "Total": float(valor)
            }
            vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
            st.session_state.vendas = vendas

            st.success(f"Lançamento pago via {forma_pg} e registrado em vendas.")

    with st.expander("Excluir dívida"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_exc = st.selectbox("ID da dívida para excluir", ids) if ids else None
        if st.button("Excluir dívida") and id_exc is not None:
            prod = clientes.loc[clientes["ID"]==id_exc, "Produto"].iloc[0]
            val  = clientes.loc[clientes["ID"]==id_exc, "Valor"].iloc[0]

            clientes = clientes[clientes["ID"] != id_exc].reset_index(drop=True)
            st.session_state.clientes = clientes

            vendas = vendas[~((vendas["NomeProduto"]==prod) & (vendas["Total"]==val))].reset_index(drop=True)
            st.session_state.vendas = vendas

            st.success("Dívida excluída de clientes e vendas.")
