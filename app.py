import streamlit as st
import pandas as pd
from datetime import date

# =================== Config ===================
st.set_page_config(page_title="Minha Loja", layout="wide")

# =================== Sessão ===================
if "produtos" not in st.session_state:
    st.session_state.produtos = pd.DataFrame(columns=["ID","Nome","Preco","Quantidade"])
if "vendas" not in st.session_state:
    st.session_state.vendas = pd.DataFrame(columns=["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"])
if "clientes" not in st.session_state:
    st.session_state.clientes = pd.DataFrame(columns=["ID","Cliente","Produto","Valor","DataPagamento","Status"])

produtos = st.session_state.produtos
vendas = st.session_state.vendas
clientes = st.session_state.clientes

# =================== Funções auxiliares ===================
def prox_id(df, col):
    return (df[col].max() + 1) if not df.empty else 1

# =================== Menu ===================
st.sidebar.title("Menu")
view = st.sidebar.radio("Ir para:", ["Dashboard","Produtos","Vendas","Clientes"])

# =================== Dashboard ===================
if view == "Dashboard":
    st.title("📊 Dashboard")
    st.metric("Total de Vendas", len(vendas))
    st.metric("Clientes Fiado", len(clientes))

# =================== Produtos ===================
if view == "Produtos":
    st.title("📦 Produtos")
    st.dataframe(produtos)

# =================== Vendas ===================
if view == "Vendas":
    st.title("🧾 Vendas")

    if produtos.empty:
        st.warning("Cadastre produtos primeiro.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])

        idp = mapa[prod_sel]
        preco = float(produtos.loc[produtos["ID"]==idp, "Preco"].iloc[0])
        total = preco * qtd

        cliente_nome, data_pag = None, None
        if forma == "Fiado":
            cliente_nome = st.text_input("Nome do cliente")
            data_pag = st.date_input("Data prevista de pagamento", value=date.today())

        if st.button("Registrar venda"):
            nova = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": idp,
                "NomeProduto": prod_sel.split(" (ID")[0],
                "FormaPagamento": forma,
                "Quantidade": int(qtd),
                "PrecoUnitario": float(preco),
                "Total": float(total)
            }
            vendas = pd.concat([vendas, pd.DataFrame([nova])], ignore_index=True)
            st.session_state.vendas = vendas

            produtos.loc[produtos["ID"]==idp, "Quantidade"] = produtos.loc[produtos["ID"]==idp, "Quantidade"].astype(int) - int(qtd)
            st.session_state.produtos = produtos

            if forma == "Fiado" and cliente_nome:
                novo = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome,
                    "Produto": prod_sel.split(" (ID")[0],
                    "Valor": float(total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
                st.session_state.clientes = clientes

            st.success("Venda registrada!")

    st.subheader("Histórico de vendas")
    st.dataframe(vendas)

    # Excluir venda
    with st.expander("Excluir venda"):
        ids = vendas["IDVenda"].tolist() if not vendas.empty else []
        id_exc = st.selectbox("Selecione ID da venda para excluir", ids) if ids else None
        if st.button("Excluir venda") and id_exc is not None:
            vendas = vendas[vendas["IDVenda"] != id_exc].reset_index(drop=True)
            st.session_state.vendas = vendas
            st.success("Venda excluída!")

# =================== Clientes ===================
if view == "Clientes":
    st.title("👥 Clientes Fiado")
    st.dataframe(clientes)