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
# Normalizadores
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
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
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

def reset_admin_user():
    df = norm_usuarios(pd.DataFrame())
    if (df["Usuario"] == "admin").any():
        df.loc[df["Usuario"]=="admin", "Senha"] = "123"
    else:
        df.loc[len(df)] = {"Usuario":"admin","Senha":"123"}
    save_csv(df, ARQ_USUARIOS)
    return True

# =====================================
# Formatação BRL
# =====================================
def brl(v: float) -> str:
    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

# =====================================
# Sessão de login
# =====================================
def do_login():
    st.session_state.setdefault("logado", False)
    st.session_state.setdefault("usuario_logado", None)

    if st.session_state.get("logado"):
        return True

    st.title("🔐 Login")
    user = st.text_input("Usuário")
    pwd  = st.text_input("Senha", type="password")
    manter = st.checkbox("Manter conectado")

    if st.button("Entrar"):
        reset_admin_user()
        usuarios = norm_usuarios(pd.DataFrame())
        cred_ok = not usuarios[(usuarios["Usuario"]==user) & (usuarios["Senha"]==pwd)].empty
        if cred_ok or (user == "admin" and pwd == "123"):
            st.session_state["logado"] = True
            st.session_state["usuario_logado"] = user if manter else None
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    st.stop()

def boot_session():
    if "produtos" not in st.session_state:
        st.session_state["produtos"] = norm_produtos(pd.DataFrame())
    if "vendas" not in st.session_state:
        st.session_state["vendas"] = norm_vendas(pd.DataFrame())
    if "clientes" not in st.session_state:
        st.session_state["clientes"] = norm_clientes(pd.DataFrame())
    if "estoque_minimo" not in st.session_state:
        st.session_state["estoque_minimo"] = ESTOQUE_MINIMO_PADRAO

# =====================================
# Start
# =====================================
do_login()
boot_session()

produtos = st.session_state["produtos"]
vendas   = st.session_state["vendas"]
clientes = st.session_state["clientes"]

# =====================================
# Sidebar
# =====================================
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Promoções","Sair"], index=0)

if view == "Sair":
    st.session_state.clear()
    st.success("Sessão encerrada.")
    st.stop()

# =====================================
# VENDAS (mantive igual ao revisado antes)
# =====================================
if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        df_sel = produtos.copy()
        df_sel["Rotulo"] = df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)
        escolha = st.selectbox("Produto", df_sel["Rotulo"].tolist())
        pid = int(escolha.split(" - ")[0])
        rowp = df_sel[df_sel["ID"]==str(pid)].iloc[0]
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])

        preco_unit = float(rowp["PrecoVista"])
        if forma == "Cartão":
            preco_unit = round(preco_unit / FATOR_CARTAO, 2)
        total = round(preco_unit * int(qtd), 2)
        st.info(f"💰 Total do pedido: {brl(total)}")

        if forma != "Fiado":
            if st.button("Registrar venda"):
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": str(pid),
                    "NomeProduto": rowp["Nome"],
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                produtos.loc[produtos["ID"]==str(pid), "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                st.session_state["vendas"] = vendas
                st.session_state["produtos"] = produtos
                save_csv(vendas, ARQ_VENDAS)
                save_csv(produtos, ARQ_PRODUTOS)
                st.success("Venda registrada!")
        else:
            st.markdown("#### Vender fiado")
            cliente_nome = st.text_input("Nome do cliente")
            data_pag = st.date_input("Data prevista de pagamento", value=date.today()+timedelta(days=7))
            if st.button("Confirmar fiado"):
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": str(pid),
                    "NomeProduto": rowp["Nome"],
                    "FormaPagamento": "Fiado",
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                save_csv(vendas, ARQ_VENDAS)

                novo_cli = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome.strip(),
                    "Produto": rowp["Nome"],
                    "Valor": float(total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_cli])], ignore_index=True)
                save_csv(clientes, ARQ_CLIENTES)

                produtos.loc[produtos["ID"]==str(pid), "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                save_csv(produtos, ARQ_PRODUTOS)

                st.session_state["vendas"] = vendas
                st.session_state["clientes"] = clientes
                st.session_state["produtos"] = produtos
                st.success("Fiado lançado para o cliente.")

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False), use_container_width=True)

    st.subheader("Excluir venda")
    if vendas.empty:
        st.info("Não há vendas para excluir.")
    else:
        id_list = vendas["IDVenda"].astype(str).tolist()
        sel = st.selectbox("Selecione a venda (ID)", id_list)
        if st.button("Excluir venda"):
            venda_sel = vendas[vendas["IDVenda"].astype(str)==str(sel)].iloc[0]
            pid = str(venda_sel["IDProduto"])
            qtd = int(venda_sel["Quantidade"])
            if pid in produtos["ID"].astype(str).values:
                produtos.loc[produtos["ID"]==pid, "Quantidade"] += qtd
                save_csv(produtos, ARQ_PRODUTOS)
            vendas = vendas[vendas["IDVenda"].astype(str) != str(sel)]
            st.session_state["vendas"] = vendas
            save_csv(vendas, ARQ_VENDAS)
            st.warning(f"Venda {sel} excluída e estoque atualizado!")
