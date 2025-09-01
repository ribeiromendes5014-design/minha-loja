import streamlit as st
import pandas as pd
from drive_store import load_csv, save_csv
import datetime
import plotly.express as px

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

    # Filtro de busca
    st.subheader("📋 Lista de Produtos")
    filtro = st.text_input("🔍 Buscar produto pelo nome ou categoria")
    if filtro:
        filtrados = produtos[produtos["Nome"].str.contains(filtro, case=False, na=False) | produtos["Categoria"].str.contains(filtro, case=False, na=False)]
    else:
        filtrados = produtos
    st.dataframe(filtrados)

    # Opções de editar e excluir
    if not produtos.empty:
        st.subheader("✏️ Editar / ❌ Excluir Produto")
        escolha = st.selectbox("Selecione um produto", produtos["Nome"])
        if escolha:
            idx = produtos[produtos["Nome"] == escolha].index[0]
            with st.form("editar_produto"):
                novo_nome = st.text_input("Nome", produtos.at[idx, "Nome"])
                nova_marca = st.text_input("Marca", produtos.at[idx, "Marca"])
                nova_categoria = st.text_input("Categoria", produtos.at[idx, "Categoria"])
                nova_validade = st.date_input("Validade", pd.to_datetime(produtos.at[idx, "Validade"]))
                nova_qtd = st.number_input("Quantidade", value=int(produtos.at[idx, "Quantidade"]), min_value=0, step=1)
                novo_preco_custo = st.number_input("Preço de Custo", value=float(produtos.at[idx, "PrecoCusto"]), min_value=0.0, step=0.01)
                novo_preco_vista = st.number_input("Preço à Vista", value=float(produtos.at[idx, "PrecoVista"]), min_value=0.0, step=0.01)
                novo_preco_cartao = round(novo_preco_vista * 1.13, 2)
                st.markdown(f"**💳 Preço no Cartão:** R$ {novo_preco_cartao:.2f}")

                salvar = st.form_submit_button("Salvar Alterações")
                excluir = st.form_submit_button("Excluir Produto")

                if salvar:
                    produtos.at[idx, "Nome"] = novo_nome
                    produtos.at[idx, "Marca"] = nova_marca
                    produtos.at[idx, "Categoria"] = nova_categoria
                    produtos.at[idx, "Validade"] = nova_validade
                    produtos.at[idx, "Quantidade"] = nova_qtd
                    produtos.at[idx, "PrecoCusto"] = novo_preco_custo
                    produtos.at[idx, "PrecoVista"] = novo_preco_vista
                    produtos.at[idx, "PrecoCartao"] = novo_preco_cartao
                    salvar_dados(PRODUTOS_FILE, produtos)
                    st.success("✅ Produto atualizado!")

                if excluir:
                    produtos = produtos.drop(idx).reset_index(drop=True)
                    salvar_dados(PRODUTOS_FILE, produtos)
                    st.success("🗑️ Produto excluído!")

    # Aviso de estoque baixo + gráfico de estoque
    if not produtos.empty:
        baixos = produtos[produtos["Quantidade"] <= 1]
        if not baixos.empty:
            st.warning("⚠️ Produtos com estoque baixo:")
            st.table(baixos[["Nome", "Quantidade"]])

        st.subheader("📉 Níveis de Estoque")
        fig = px.bar(produtos, x="Nome", y="Quantidade", title="Estoque Atual por Produto", color="Quantidade", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

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
                    "ID": len(vendas) + 1,
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

    # Editar e excluir vendas
    if not vendas.empty:
        st.subheader("✏️ Editar / ❌ Excluir Venda")
        escolha_venda = st.selectbox("Selecione uma venda pelo ID", vendas["ID"])
        if escolha_venda:
            idx_venda = vendas[vendas["ID"] == escolha_venda].index[0]
            with st.form("editar_venda"):
                novo_produto = st.selectbox("Produto", produtos["Nome"].unique(), index=produtos[produtos["Nome"] == vendas.at[idx_venda, "Produto"]].index[0])
                nova_qtd = st.number_input("Quantidade", value=int(vendas.at[idx_venda, "Quantidade"]), min_value=1, step=1)
                novo_metodo = st.radio("Forma de Pagamento", ["À Vista", "Cartão"], index=0 if vendas.at[idx_venda, "Metodo"] == "À Vista" else 1)
                salvar_venda = st.form_submit_button("Salvar Alterações")
                excluir_venda = st.form_submit_button("Excluir Venda")

                if salvar_venda:
                    preco = produtos.loc[produtos["Nome"] == novo_produto, "PrecoVista"].values[0] if novo_metodo == "À Vista" else produtos.loc[produtos["Nome"] == novo_produto, "PrecoCartao"].values[0]
                    vendas.at[idx_venda, "Produto"] = novo_produto
                    vendas.at[idx_venda, "Quantidade"] = nova_qtd
                    vendas.at[idx_venda, "Metodo"] = novo_metodo
                    vendas.at[idx_venda, "Total"] = preco * nova_qtd
                    salvar_dados(VENDAS_FILE, vendas)
                    st.success("✅ Venda atualizada!")

                if excluir_venda:
                    vendas = vendas.drop(idx_venda).reset_index(drop=True)
                    salvar_dados(VENDAS_FILE, vendas)
                    st.success("🗑️ Venda excluída!")

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
        opcao_filtro = st.radio("Filtrar por:", ["Diário", "Mensal"])
        if opcao_filtro == "Diário":
            filtro_data = st.date_input("Selecione a data", datetime.date.today())
            vendas_dia = vendas[vendas["Data"] == pd.to_datetime(filtro_data)]
            total_dia = vendas_dia["Total"].sum()
            st.metric("💰 Total de Vendas no Dia", f"R$ {total_dia:.2f}")
            st.dataframe(vendas_dia)

            if not vendas_dia.empty:
                fig = px.bar(vendas_dia, x="Produto", y="Total", color="Metodo", title="Vendas do Dia por Produto")
                st.plotly_chart(fig, use_container_width=True)

        else:
            mes = st.selectbox("Selecione o mês", list(range(1, 13)), index=datetime.date.today().month - 1)
            ano = st.number_input("Ano", value=datetime.date.today().year, step=1)
            vendas_mes = vendas[pd.to_datetime(vendas["Data"]).dt.month == mes]
            vendas_mes = vendas_mes[pd.to_datetime(vendas_mes["Data"]).dt.year == ano]
            total_mes = vendas_mes["Total"].sum()
            st.metric("💰 Total de Vendas no Mês", f"R$ {total_mes:.2f}")
            st.dataframe(vendas_mes)

            if not vendas_mes.empty:
                fig1 = px.pie(vendas_mes, names="Produto", values="Total", title="Participação por Produto")
                st.plotly_chart(fig1, use_container_width=True)

                fig2 = px.line(vendas_mes, x="Data", y="Total", color="Produto", title="Evolução das Vendas no Mês")
                st.plotly_chart(fig2, use_container_width=True)
