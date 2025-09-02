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

# =============================
# Utilidades
# =============================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    df["Validade"] = df["Validade"].astype(str)
    return df[cols].reset_index(drop=True)

def garantir_colunas_vendas(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    df["Data"] = df["Data"].astype(str)
    return df[cols].reset_index(drop=True)

def garantir_colunas_promocoes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Desconto"] = pd.to_numeric(df["Desconto"], errors="coerce").fillna(0.0).astype(float)
    df["DataInicio"] = pd.to_datetime(df["DataInicio"], errors="coerce").dt.date.astype(str)
    df["DataFim"] = pd.to_datetime(df["DataFim"], errors="coerce").dt.date.astype(str)
    return df[cols].reset_index(drop=True)

def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    if df is None or df.empty:
        return pd.DataFrame(columns=cols)
    for c in cols:
        if c not in df.columns:
            df[c] = None
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
    if "Status" not in df.columns:
        df["Status"] = "Aberto"
    df["Status"] = df["Status"].fillna("Aberto").astype(str)
    return df[cols].reset_index(drop=True)

def carregar_csv(caminho: str, cols_func) -> pd.DataFrame:
    if os.path.exists(caminho):
        try:
            df = pd.read_csv(caminho)
        except Exception:
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()
    return cols_func(df)

def salvar_csv(df: pd.DataFrame, caminho: str):
    df.to_csv(caminho, index=False)

def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(df[col].max()) + 1) if not df.empty else 1

def preco_com_promocao(pid, preco_normal):
    hoje = date.today()
    promos = promocoes[promocoes["IDProduto"] == pid]
    if promos.empty:
        return preco_normal, False, None
    for _, r in promos.iterrows():
        try:
            di = pd.to_datetime(r["DataInicio"]).date()
            dfim = pd.to_datetime(r["DataFim"]).date()
        except Exception:
            continue
        if di <= hoje <= dfim:
            preco_desc = preco_normal * (1 - float(r["Desconto"]) / 100)
            return preco_desc, True, f"Promoção ativa: {r['Desconto']}% de desconto!"
    return preco_normal, False, None

# =============================
# Carregar dados
# =============================
produtos = carregar_csv(ARQ_PRODUTOS, garantir_colunas_produtos)
vendas = carregar_csv(ARQ_VENDAS, garantir_colunas_vendas)
promocoes = carregar_csv(ARQ_PROMOCOES, garantir_colunas_promocoes)
clientes = carregar_csv(ARQ_CLIENTES, garantir_colunas_clientes)

st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Fluxo de Caixa","Promoções","Clientes"], index=0)

# =============================
# DASHBOARD
# =============================
if view == "Dashboard":
    st.title("📊 Dashboard Geral")
    st.info("Em construção...")

# =============================
# PRODUTOS
# =============================
elif view == "Produtos":
    st.title("🛍️ Produtos")
    st.info("Gestão de produtos em construção...")

# =============================
# VENDAS
# =============================
elif view == "Vendas":
    st.title("🧾 Vendas")
    st.info("Gestão de vendas em construção...")

# =============================
# FLUXO DE CAIXA
# =============================
elif view ==  "Fluxo de Caixa":
    st.title("💵 Fluxo de Caixa")
    st.info("Fluxo de caixa em construção...")

# =============================
# PROMOÇÕES
# =============================
elif view == "Promoções":
    st.title("🏷️ Promoções")
    if produtos.empty:
        st.info("Cadastre produtos antes de criar promoções.")
    else:
        with st.form("form_promo", clear_on_submit=True):
            produto_options = [f"{int(r.ID)} - {r.Nome}" for r in produtos.itertuples(index=False)]
            produto_opt = st.selectbox("Produto", produto_options) if produto_options else None

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                nome_prod = produtos.loc[produtos["ID"] == pid, "Nome"].iloc[0]
            else:
                pid = None
                nome_prod = None

            desconto = st.number_input("Desconto (%)", min_value=1.0, max_value=100.0, step=1.0, value=10.0)
            di = st.date_input("Data início", value=date.today())
            dfim = st.date_input("Data fim", value=date.today())
            salvar = st.form_submit_button("➕ Criar promoção")

            if salvar:
                if pid is None:
                    st.error("Selecione um produto.")
                elif dfim < di:
                    st.error("A data final não pode ser antes da inicial.")
                elif not promocoes[(promocoes["IDProduto"] == pid)].empty:
                    st.warning("Já existe uma promoção cadastrada para este produto.")
                else:
                    nova = {
                        "IDPromo": prox_id(promocoes, "IDPromo"),
                        "IDProduto": pid,
                        "NomeProduto": nome_prod,
                        "Desconto": float(desconto),
                        "DataInicio": str(di),
                        "DataFim": str(dfim),
                    }
                    promocoes = pd.concat([promocoes, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promocoes, ARQ_PROMOCOES)
                    st.success("Promoção criada com sucesso!")

    st.markdown("### 📋 Promoções cadastradas")
    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        st.dataframe(promocoes, use_container_width=True)
        promo_options = [f"{int(r.IDPromo)} - {r.NomeProduto}" for r in promocoes.itertuples(index=False)]
        promo_opt = st.selectbox("Selecionar promoção para excluir", promo_options) if promo_options else None
        if st.button("🗑️ Excluir promoção selecionada") and promo_opt:
            pid_del = int(promo_opt.split(" - ")[0])
            promocoes = promocoes[promocoes["IDPromo"] != pid_del].reset_index(drop=True)
            salvar_csv(promocoes, ARQ_PROMOCOES)
            st.warning("Promoção excluída com sucesso!")

# =============================
# CLIENTES
# =============================
elif view == "Clientes":
    st.title("👥 Clientes (Fiado)")
    st.info("Gestão de clientes em construção...")
