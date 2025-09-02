import streamlit as st
import pandas as pd
import io, os, re, base64, requests
from datetime import datetime, date, timedelta

# ====================== Configurações ======================
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")

# ======== Arquivos CSV no repositório ========
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"

# Pasta para fotos dentro do repositório
FOTOS_DIR = "fotos_produtos"

# Fator de ajuste para preço no cartão (preço no cartão = preço_vista / FATOR_CARTAO)
FATOR_CARTAO   = 0.8872

# ====================== Garantia de colunas ======================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","FotoPath"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c not in ["Quantidade","PrecoCusto","PrecoVista","PrecoCartao"] else 0
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    return df[cols]

# ====================== Views ======================
# ----- Dashboard -----
if view == "Dashboard":
    st.title("📊 Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    total_vendas = vendas["Total"].sum() if not vendas.empty else 0.0
    hoje = str(date.today())
    vendas_hoje = vendas[vendas["Data"] == hoje]["Total"].sum() if not vendas.empty else 0.0
    qntd_vendas = len(vendas) if not vendas.empty else 0
    em_aberto = len(clientes[clientes["Status"].astype(str).str.lower()=="aberto"]) if not clientes.empty else 0
    with col1:
        st.metric("Faturamento Total", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    with col2:
        st.metric("Vendas Hoje", f"R$ {vendas_hoje:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    with col3:
        st.metric("Qtde de Vendas", qntd_vendas)
    with col4:
        st.metric("Fiados em Aberto", em_aberto)

    # Alertas
    st.markdown("### ⚠️ Alertas")
    hoje = date.today()
    validade_proxima = produtos[pd.to_datetime(produtos["Validade"], errors="coerce") <= hoje + timedelta(days=60)]
    estoque_baixo = produtos[produtos["Quantidade"] <= 5]

    if validade_proxima.empty and estoque_baixo.empty:
        st.success("Nenhum alerta no momento!")
    else:
        if not validade_proxima.empty:
            st.warning("Produtos com validade próxima (≤60 dias):")
            st.dataframe(validade_proxima[["Nome","Validade","Quantidade"]], use_container_width=True)
        if not estoque_baixo.empty:
            st.error("Produtos com estoque baixo (≤5):")
            st.dataframe(estoque_baixo[["Nome","Quantidade"]], use_container_width=True)

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False).tail(50), use_container_width=True)

# ----- Produtos -----
if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar produto"):
        pass  # formulário já existente no código original

    st.markdown("### Lista de produtos")
    if not produtos.empty:
        for _, row in produtos.iterrows():
            with st.container():
                cols = st.columns([1,2,2,2,2])
                if row["FotoURL"]:
                    cols[0].image(row["FotoURL"], width=80)
                cols[1].write(f"**{row['Nome']}**")
                cols[2].write(f"Estoque: {row['Quantidade']}")
                cols[3].write(f"Validade: {row['Validade']}")
                if cols[4].button("✏️ Editar", key=f"edit_{row['ID']}"):
                    st.session_state["edit_produto"] = row.to_dict()
                if cols[4].button("🗑️ Excluir", key=f"del_{row['ID']}"):
                    produtos = produtos[produtos["ID"] != row["ID"]]
                    st.session_state.produtos = produtos
                    salvar_csv_github(produtos, ARQ_PRODUTOS)
                    st.warning(f"Produto {row['Nome']} excluído!")

    if "edit_produto" in st.session_state:
        st.subheader("Editar produto")
        edit = st.session_state["edit_produto"]
        novo_nome = st.text_input("Nome", edit["Nome"])
        nova_qtd = st.number_input("Quantidade", 0, step=1, value=int(edit["Quantidade"]))
        nova_validade = st.date_input("Validade", value=pd.to_datetime(edit["Validade"]).date() if edit["Validade"] else date.today())
        if st.button("Salvar alterações"):
            produtos.loc[produtos["ID"]==edit["ID"], ["Nome","Quantidade","Validade"]] = [novo_nome, nova_qtd, str(nova_validade)]
            st.session_state.produtos = produtos
            salvar_csv_github(produtos, ARQ_PRODUTOS)
            del st.session_state["edit_produto"]
            st.success("Produto atualizado!")

# ----- Vendas -----
if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        df_sel = produtos.copy()
        df_sel["Rotulo"] = df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)
        escolha = st.selectbox("Produto", df_sel["Rotulo"].tolist())
        pid = int(escolha.split(" - ")[0])
        rowp = df_sel[df_sel["ID"]==pid].iloc[0]
        qtd = st.number_input("Quantidade", 1, step=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])

        preco_unit = float(rowp["PrecoVista"])
        total = preco_unit * qtd
        if forma == "Cartão":
            preco_unit = round(preco_unit / FATOR_CARTAO, 2)
            total = round(preco_unit * qtd, 2)

        st.info(f"💰 Total do pedido: R$ {total:,.2f}".replace(",","X").replace(".",",").replace("X","."))

        if st.button("Registrar venda"):
            if forma != "Fiado":
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": pid,
                    "NomeProduto": rowp["Nome"],
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                st.session_state.vendas = vendas
                produtos.loc[produtos["ID"]==pid, "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                st.session_state.produtos = produtos
                salvar_csv_github(vendas, ARQ_VENDAS)
                salvar_csv_github(produtos, ARQ_PRODUTOS)
                st.success("Venda registrada!")
            else:
                cliente_nome = st.text_input("Nome do cliente (fiado)", key="fiado_nome")
                data_pag = st.date_input("Data prevista de pagamento", value=date.today()+timedelta(days=7))
                if st.button("Confirmar fiado"):
                    novo = {
                        "ID": prox_id(clientes, "ID"),
                        "Cliente": cliente_nome,
                        "Produto": rowp["Nome"],
                        "Valor": float(total),
                        "DataPagamento": str(data_pag),
                        "Status": "Aberto"
                    }
                    clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
                    st.session_state.clientes = clientes
                    salvar_csv_github(clientes, ARQ_CLIENTES)
                    st.success("Fiado lançado para o cliente.")

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False), use_container_width=True)

    # Excluir venda
    st.subheader("Excluir venda")
    if not vendas.empty:
        id_sel = st.selectbox("Selecione a venda pelo ID", vendas["IDVenda"].tolist())
        if st.button("Excluir venda"):
            vendas = vendas[vendas["IDVenda"] != id_sel]
            st.session_state.vendas = vendas
            salvar_csv_github(vendas, ARQ_VENDAS)
            st.warning(f"Venda {id_sel} excluída!")