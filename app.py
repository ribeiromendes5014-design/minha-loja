import streamlit as st
import pandas as pd
import io, os
from datetime import datetime, date

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")
FOLDER_FOTOS = "1Zhb6lZVOUST2WR08C9SYIYAS1q0BwF6k"
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"
FATOR_CARTAO   = 0.8872

# ========= Helpers e funções utilitárias =========
# ... (mantive o código existente igual ao seu até a parte de cada aba)

# ================= VENDAS =================
if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.warning("Cadastre produtos antes de registrar vendas.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])
        idp = mapa[prod_sel]
        preco = float(produtos.loc[produtos["ID"]==idp, "PrecoVista"].iloc[0])
        if forma == "Cartão":
            preco = round(preco / FATOR_CARTAO, 2)
        total = preco * qtd
        st.info(f"Preço unitário: R$ {preco:,.2f} | Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

        cliente_nome, data_pag = None, None
        if forma == "Fiado":
            cliente_nome = st.text_input("Nome do cliente")
            data_pag = st.date_input("Data de pagamento prevista", value=date.today())

        if st.button("Registrar venda"):
            venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": idp,
                "NomeProduto": prod_sel.split(" (ID")[0],
                "FormaPagamento": forma,
                "Quantidade": int(qtd),
                "PrecoUnitario": float(preco),
                "Total": float(total)
            }
            vendas = pd.concat([vendas, pd.DataFrame([venda])], ignore_index=True)
            st.session_state.vendas = vendas

            produtos.loc[produtos["ID"]==idp, "Quantidade"] = produtos.loc[produtos["ID"]==idp, "Quantidade"].astype(int) - int(qtd)
            st.session_state.produtos = produtos

            # Se for fiado, já cria registro em clientes
            if forma == "Fiado" and cliente_nome:
                novo_fiado = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome,
                    "Produto": prod_sel.split(" (ID")[0],
                    "Valor": float(total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_fiado])], ignore_index=True)
                st.session_state.clientes = clientes

            st.success("Venda registrada!")

    st.subheader("Histórico de vendas")
    st.dataframe(vendas.sort_values("Data", ascending=False), use_container_width=True)

    with st.expander("Excluir venda"):
        ids = vendas["IDVenda"].tolist() if not vendas.empty else []
        id_exc = st.selectbox("ID da venda para excluir", ids) if ids else None
        if st.button("Excluir venda") and id_exc is not None:
            vendas = vendas[vendas["IDVenda"] != id_exc].reset_index(drop=True)
            st.session_state.vendas = vendas
            st.success("Venda excluída.")

# ================= CLIENTES =================
if view == "Clientes":
    st.header("👥 Clientes / Fiado")
    with st.expander("Lançar novo fiado"):
        cliente = st.text_input("Cliente")
        produto = st.text_input("Produto")
        valor = st.number_input("Valor", 0.0, step=0.01)
        data_pag = st.date_input("Data prevista de pagamento", value=date.today())
        if st.button("Lançar"):
            novo = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": cliente, "Produto": produto,
                "Valor": float(valor), "DataPagamento": str(data_pag), "Status": "Aberto"
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.clientes = clientes
            st.success("Lançamento criado.")

    st.subheader("Contas em aberto")
    st.dataframe(clientes, use_container_width=True)

    with st.expander("Baixar/Pagar conta"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None
        if st.button("Marcar como Pago") and id_sel is not None:
            clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
            st.session_state.clientes = clientes
            st.success("Lançamento atualizado.")
