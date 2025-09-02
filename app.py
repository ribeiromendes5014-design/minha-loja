import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import os

# =====================================
# Configurações básicas
# =====================================
LOGO_URL = os.environ.get("LOGO_URL", "").strip()
LOGO_CANDIDATES = ["logo.png", "assets/logo.png", "static/logo.png"]
PAGE_ICON = "🛍️"

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_USUARIOS  = "usuarios.csv"
FATOR_CARTAO  = 0.8872
ESTOQUE_MINIMO_PADRAO = 5

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
    return df[columns]

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
# Normalizadores de dados
# =====================================
def norm_produtos(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_vendas(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status","FormaPagamento"]
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

# =====================================
# Formatação BRL
# =====================================
def brl(v: float) -> str:
    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

# =====================================
# Sessão
# =====================================
def boot_session():
    if "produtos" not in st.session_state:
        st.session_state["produtos"] = norm_produtos(pd.DataFrame())
    if "vendas" not in st.session_state:
        st.session_state["vendas"] = norm_vendas(pd.DataFrame())
    if "clientes" not in st.session_state:
        st.session_state["clientes"] = norm_clientes(pd.DataFrame())
    if "pedido_atual" not in st.session_state:
        st.session_state["pedido_atual"] = []
    if "valor_pago" not in st.session_state:
        st.session_state["valor_pago"] = 0.0

boot_session()

produtos = st.session_state["produtos"]
vendas   = st.session_state["vendas"]
clientes = st.session_state["clientes"]

# =====================================
# Sidebar
# =====================================
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Promoções"], index=2)

# =====================================
# VENDAS - Novo Layout
# =====================================
if view == "Vendas":
    st.header("🧾 Vendas Detalhadas")

    # Seleção de produto
    st.subheader("Itens do pedido")
    c1,c2,c3,c4 = st.columns([2,3,2,2])
    with c1:
        codigo = st.text_input("Código do Produto")
    with c2:
        nome_filtro = st.text_input("Pesquisar por nome")

    df_sel = produtos.copy()
    if codigo:
        df_sel = df_sel[df_sel["ID"].astype(str).str.contains(codigo)]
    if nome_filtro:
        df_sel = df_sel[df_sel["Nome"].str.contains(nome_filtro, case=False, na=False)]

    if not df_sel.empty:
        escolha = st.selectbox("Selecione o produto", df_sel["ID"].astype(str) + " - " + df_sel["Nome"])
        pid = escolha.split(" - ")[0].strip()
        rowp = df_sel[df_sel["ID"].astype(str)==pid].iloc[0]
        with c3:
            qtd = st.number_input("Qtd", min_value=1, value=1, step=1)
        with c4:
            preco_unit = float(rowp["PrecoVista"])
            st.write("Preço:", brl(preco_unit))

        if st.button("Adicionar ao pedido"):
            st.session_state["pedido_atual"].append({
                "IDProduto": pid,
                "NomeProduto": rowp["Nome"],
                "Quantidade": qtd,
                "PrecoUnitario": preco_unit,
                "Total": qtd*preco_unit
            })

    pedido = pd.DataFrame(st.session_state["pedido_atual"])
    if not pedido.empty:
        st.table(pedido)

    # Pagamento
    st.subheader("Forma de Pagamento")
    forma = st.radio("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"], horizontal=True)

    valor_total = pedido["Total"].sum() if not pedido.empty else 0.0
    valor_pago = st.session_state.get("valor_pago", 0.0)
    troco = 0.0

    if forma == "Dinheiro":
        valor_pago = st.number_input("Valor pago", min_value=0.0, value=float(valor_pago), step=1.0)
        troco = max(valor_pago - valor_total, 0.0)
        st.session_state["valor_pago"] = valor_pago

    colA, colB, colC = st.columns(3)
    colA.metric("Valor Total", brl(valor_total))
    colB.metric("Valor Pago", brl(valor_pago))
    colC.metric("Troco", brl(troco))

    # Ações
    st.markdown("---")
    b1,b2,b3,b4,b5,b6 = st.columns(6)
    if b1.button("✅ Finalizar Venda"):
        if not pedido.empty:
            for item in pedido.to_dict(orient="records"):
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": item["IDProduto"],
                    "NomeProduto": item["NomeProduto"],
                    "FormaPagamento": forma,
                    "Quantidade": item["Quantidade"],
                    "PrecoUnitario": item["PrecoUnitario"],
                    "Total": item["Total"]
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                if item["IDProduto"] in produtos["ID"].astype(str).values:
                    produtos.loc[produtos["ID"]==item["IDProduto"], "Quantidade"] -= int(item["Quantidade"])
            save_csv(vendas, ARQ_VENDAS)
            save_csv(produtos, ARQ_PRODUTOS)
            st.session_state["pedido_atual"] = []
            st.success("Venda finalizada!")

    if b2.button("🆕 Nova Venda"):
        st.session_state["pedido_atual"] = []
        st.session_state["valor_pago"] = 0.0
        st.info("Novo pedido iniciado")

    if b3.button("↩️ Devolução"):
        st.warning("Função de devolução em construção.")

    if b4.button("📦 Fechar Caixa"):
        st.info("Caixa fechado (simulação).")

    if b5.button("✏️ Editar Pedido"):
        st.warning("Função de edição em construção.")

    if b6.button("❌ Sair"):
        st.session_state["pedido_atual"] = []
        st.stop()

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False).head(20), use_container_width=True)
