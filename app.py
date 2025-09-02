import streamlit as st
import pandas as pd
import io, os, re, base64, requests
from datetime import datetime, date, timedelta

# ====================== Configurações ======================
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")

# CSVs no GitHub
ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_CLIENTES = "clientes.csv"

FATOR_CARTAO = 0.9715  # Taxa de desconto no cartão

# ====================== Funções ======================
@st.cache_data
def carregar_csv_github(arquivo):
    try:
        return pd.read_csv(arquivo)
    except:
        return pd.DataFrame()

def salvar_csv_github(df, arquivo):
    df.to_csv(arquivo, index=False)

# ====================== Sessão ======================
if "produtos" not in st.session_state:
    st.session_state.produtos = carregar_csv_github(ARQ_PRODUTOS)
if "vendas" not in st.session_state:
    st.session_state.vendas = carregar_csv_github(ARQ_VENDAS)
if "clientes" not in st.session_state:
    st.session_state.clientes = carregar_csv_github(ARQ_CLIENTES)

produtos = st.session_state.produtos
vendas = st.session_state.vendas
clientes = st.session_state.clientes

# ====================== Layout ======================
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio("Navegação", ["Produtos","Vendas","Clientes","Dashboard"])

# ====================== Produtos ======================
if menu == "Produtos":
    st.header("Cadastro de Produtos")
    with st.form("cad_prod"):
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        qtd = st.number_input("Quantidade", min_value=0, step=1)
        salvar = st.form_submit_button("Salvar")
        if salvar and nome:
            novo = pd.DataFrame([[nome,preco,qtd]],columns=["Nome","Preço","Quantidade"])
            produtos = pd.concat([produtos, novo], ignore_index=True)
            st.session_state.produtos = produtos
            salvar_csv_github(produtos, ARQ_PRODUTOS)
            st.success("Produto salvo!")

    st.subheader("📦 Lista de Produtos")
    st.dataframe(produtos)

# ====================== Vendas ======================
elif menu == "Vendas":
    st.header("Registro de Vendas")
    if not produtos.empty:
        with st.form("cad_venda"):
            prod = st.selectbox("Produto", produtos["Nome"].tolist())
            qtd = st.number_input("Qtd", min_value=1, step=1)
            forma = st.selectbox("Forma de Pagamento",["Dinheiro","PIX","Cartão","Fiado"])
            cliente = st.text_input("Cliente (se fiado)") if forma=="Fiado" else ""
            dt_pgto = st.date_input("Data de pagamento (Fiado)", value=date.today()+timedelta(days=30)) if forma=="Fiado" else None
            salvar = st.form_submit_button("Lançar Venda")

            if salvar:
                preco_unit = float(produtos.loc[produtos["Nome"]==prod,"Preço"].values[0])
                total = preco_unit*qtd
                if forma=="Cartão":
                    total = round(total*FATOR_CARTAO,2)

                venda = pd.DataFrame([[prod,qtd,total,forma,datetime.now().strftime("%Y-%m-%d %H:%M:%S")]],
                                     columns=["NomeProduto","Qtd","Total","FormaPagamento","Data"])
                vendas = pd.concat([vendas,venda], ignore_index=True)
                st.session_state.vendas = vendas
                salvar_csv_github(vendas, ARQ_VENDAS)

                if forma=="Fiado":
                    id_fiado = len(clientes)+1
                    lanc = pd.DataFrame([[id_fiado,cliente,prod,total,"Aberto",dt_pgto.strftime("%Y-%m-%d")]],
                                        columns=["ID","Cliente","Produto","Valor","Status","DataPagamento"])
                    clientes = pd.concat([clientes,lanc], ignore_index=True)
                    st.session_state.clientes = clientes
                    salvar_csv_github(clientes, ARQ_CLIENTES)

                st.success("Venda registrada!")
    st.subheader("🧾 Vendas")
    st.dataframe(vendas)

# ====================== Clientes ======================
elif menu == "Clientes":
    st.header("Controle de Clientes e Fiados")

    st.subheader("📋 Lançamentos Fiado")
    st.dataframe(clientes)

    with st.expander("Baixar/Pagar conta / Excluir dívida"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None

        if id_sel is not None:
            lanc = clientes.loc[clientes["ID"]==id_sel].iloc[0]
            st.write(f"Cliente: **{lanc['Cliente']}** | Produto: **{lanc['Produto']}** | Valor: R$ {lanc['Valor']:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

            forma_pg = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão"])
            valor_final = float(lanc["Valor"])
            if forma_pg == "Cartão":
                valor_final = round(valor_final / FATOR_CARTAO, 2)
            st.info(f"Valor final a receber: R$ {valor_final:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

            c1, c2 = st.columns(2)
            with c1:
                if st.button("💵 Marcar como Pago"):
                    clientes.loc[clientes["ID"]==id_sel, "Status"] = f"Pago ({forma_pg})"
                    st.session_state.clientes = clientes
                    salvar_csv_github(clientes, ARQ_CLIENTES)
                    st.success("Conta marcada como paga!")

            with c2:
                if st.button("🗑️ Excluir dívida"):
                    # Remove do clientes
                    clientes = clientes[clientes["ID"] != id_sel].reset_index(drop=True)
                    st.session_state.clientes = clientes
                    salvar_csv_github(clientes, ARQ_CLIENTES)

                    # Também remove do vendas
                    vendas = st.session_state.vendas
                    vendas = vendas[~((vendas["NomeProduto"]==lanc["Produto"]) & (vendas["Total"]==lanc["Valor"]) & (vendas["FormaPagamento"]=="Fiado"))].reset_index(drop=True)
                    st.session_state.vendas = vendas
                    salvar_csv_github(vendas, ARQ_VENDAS)

                    st.success("Dívida excluída de clientes e vendas.")

# ====================== Dashboard ======================
elif menu == "Dashboard":
    st.header("📊 Dashboard")
    if not vendas.empty:
        st.metric("Total de vendas", f"R$ {vendas['Total'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
        st.bar_chart(vendas.groupby("FormaPagamento")["Total"].sum())
    else:
        st.info("Nenhuma venda registrada ainda.")
