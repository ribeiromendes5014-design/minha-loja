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

# (demais funções iguais ao seu app original até a view Clientes)...

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
            salvar_csv_github(clientes, ARQ_CLIENTES)
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
            salvar_csv_github(clientes, ARQ_CLIENTES)

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
            salvar_csv_github(vendas, ARQ_VENDAS)

            st.success(f"Lançamento pago via {forma_pg} e registrado em vendas.")

    with st.expander("Excluir dívida"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_exc = st.selectbox("ID da dívida para excluir", ids) if ids else None
        if st.button("Excluir dívida") and id_exc is not None:
            prod = clientes.loc[clientes["ID"]==id_exc, "Produto"].iloc[0]
            val  = clientes.loc[clientes["ID"]==id_exc, "Valor"].iloc[0]

            clientes = clientes[clientes["ID"] != id_exc].reset_index(drop=True)
            st.session_state.clientes = clientes
            salvar_csv_github(clientes, ARQ_CLIENTES)

            vendas = vendas[~((vendas["NomeProduto"]==prod) & (vendas["Total"]==val))].reset_index(drop=True)
            st.session_state.vendas = vendas
            salvar_csv_github(vendas, ARQ_VENDAS)

            st.success("Dívida excluída de clientes e vendas.")
