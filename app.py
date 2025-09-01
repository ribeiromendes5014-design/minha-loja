import streamlit as st
import pandas as pd
from drive_store import load_csv, save_csv
import datetime

# Configurações iniciais
st.set_page_config(page_title="Minha Loja", layout="wide")

# Nome dos arquivos no Drive
PRODUTOS_FILE = "produtos.csv"
VENDAS_FILE = "vendas.csv"

# Funções utilitárias
def carregar_dados(nome_arquivo):
    try:
        return load_csv(nome_arquivo)
    except Exception:
        return pd.DataFrame()

def salvar_dados(nome_arquivo, df):
    save_csv(nome_arquivo, df)

# Carregar dados
produtos = carregar_dados(PRODUTOS_FILE)
vendas = carregar_dados(VENDAS_FILE)

# Tabs principais
aba = st.sidebar.radio("Navegar", ["Produtos", "Vendas", "Promoções", "Dashboard"])

# ========================= ABA PRODUTOS =========================
if aba == "Produtos":
    st.header("📦 Cadastro de Produtos")

    with st.form("form_produto"):
        nome = st.text_input("Nome do Produto")
        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        validade = st.date_input("Validade", datetime.date.today())
        quantidade = st.number_input("Quantidade", min_value=0, step=1)
        preco_custo = st.number_input("Preço de Custo", min_value=0.0, step=0.01, format="%.2f")
        preco_vista = st.number_input("Preço à Vista", min_value=0.0, step=0.01, format="%.2f")
        preco_cartao = round(preco_vista * 1.13, 2)

        st.markdown(f"**💳 Preço no Cartão:** R$ {preco_cartao:.2f}")

        submit = st.form_submit_button("Adicionar Produto")

        if submit:
            novo = pd.DataFrame([{
                "ID": len(produtos) + 1,
                "Nome": nome,
                "Marca": marca,
                "Categoria": categoria,
                "Quantidade": quantidade,
                "PrecoCusto": preco_custo,
                "PrecoVista": preco_vista,
                "PrecoCartao": preco_cartao,
                "Validade": validade
            }])
            produtos = pd.concat([produtos, novo], ignore_index=True)
            salvar_dados(PRODUTOS_FILE, produtos)
            st.success("✅ Produto cadastrado!")

    st.subheader("📋 Lista de Produtos")
    st.dataframe(produtos)

    # Aviso de estoque baixo
    if not produtos.empty:
        baixos = produtos[produtos["Quantidade"] <= 1]
        if not baixos.empty:
            st.warning("⚠️ Produtos com estoque baixo:")
            st.table(baixos[["Nome", "Quantidade"]])

# ========================= ABA VENDAS =========================
elif aba == "Vendas":
    st.header("🛒 Registro de Vendas")

    if produtos.empty:
        st.info("Cadastre produtos antes de lançar vendas.")
    else:
        with st.form("form_venda"):
            produto = st.selectbox("Produto", produtos["Nome"].unique())
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
            metodo = st.radio("Forma de Pagamento", ["À Vista", "Cartão"])
            registrar = st.form_submit_button("Registrar Venda")

            if registrar:
                prod = produtos[produtos["Nome"] == produto].iloc[0]
                preco = prod["PrecoVista"] if metodo == "À Vista" else prod["PrecoCartao"]
                total = preco * quantidade
                nova_venda = pd.DataFrame([{
                    "Produto": produto,
                    "Quantidade": quantidade,
                    "Metodo": metodo,
                    "Total": total,
                    "Data": datetime.date.today()
                }])
                vendas = pd.concat([vendas, nova_venda], ignore_index=True)

                # Atualizar estoque
                produtos.loc[produtos["Nome"] == produto, "Quantidade"] -= quantidade

                salvar_dados(VENDAS_FILE, vendas)
                salvar_dados(PRODUTOS_FILE, produtos)
                st.success(f"✅ Venda registrada! Total R$ {total:.2f}")

    st.subheader("📊 Histórico de Vendas")
    st.dataframe(vendas)

# ========================= ABA PROMOÇÕES =========================
elif aba == "Promoções":
    st.header("🏷️ Gerenciar Promoções")

    if produtos.empty:
        st.info("Cadastre produtos antes de criar promoções.")
    else:
        with st.form("form_promo"):
            produto = st.selectbox("Produto", produtos["Nome"].unique())
            desconto = st.slider("Desconto (%)", 0, 50, 10)
            aplicar = st.form_submit_button("Aplicar Promoção")

            if aplicar:
                idx = produtos[produtos["Nome"] == produto].index[0]
                produtos.at[idx, "PrecoVista"] *= (1 - desconto/100)
                produtos.at[idx, "PrecoCartao"] = round(produtos.at[idx, "PrecoVista"] * 1.13, 2)
                salvar_dados(PRODUTOS_FILE, produtos)
                st.success(f"✅ Promoção aplicada no produto {produto}!")

    st.subheader("📦 Produtos com Promoções")
    st.dataframe(produtos)

# ========================= ABA DASHBOARD =========================
elif aba == "Dashboard":
    st.header("📊 Dashboard de Vendas")

    if vendas.empty:
        st.info("Nenhuma venda registrada ainda.")
    else:
        filtro_data = st.date_input("Filtrar por data", datetime.date.today())

        vendas_dia = vendas[vendas["Data"] == pd.to_datetime(filtro_data)]
        total_dia = vendas_dia["Total"].sum()

        st.metric("💰 Total de Vendas no Dia", f"R$ {total_dia:.2f}")
        st.dataframe(vendas_dia)
