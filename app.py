import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

# Integração Google Drive (opcional)
try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from google.oauth2 import service_account
    GOOGLE_OK = True
except Exception:
    GOOGLE_OK = False

# =============================
# Configurações
# =============================
st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")
FATOR_CARTAO = 0.8872

ARQ_PRODUTOS = "produtos.csv"
ARQ_VENDAS = "vendas.csv"
ARQ_PROMOCOES = "promocoes.csv"
ARQ_CLIENTES = "clientes.csv"
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"  # Pasta do Google Drive para fotos

# =============================
# Utilidades
# =============================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID"]
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
# VENDAS
# =============================

if view == "Vendas":
    st.title("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        opt = st.selectbox("Produto", [f'{int(r.ID)} - {r.Nome} (Estoque: {int(r.Quantidade)})' for r in produtos.itertuples(index=False)])
        pid = int(opt.split(" - ")[0])
        p = produtos[produtos["ID"] == pid].iloc[0]
        st.metric("Preço à vista", f'R$ {p["PrecoVista"]:.2f}')
        st.metric("Preço no cartão", f'R$ {p["PrecoCartao"]:.2f}')
        st.metric("Estoque", int(p["Quantidade"]))

        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão","Fiado"])
        nome_cliente_fiado = None
        data_pagamento_fiado = None
        if forma == "Fiado":
            nome_cliente_fiado = st.text_input("Nome do Cliente (Fiado)")
            data_pagamento_fiado = st.date_input("Data de Pagamento (Fiado)", value=date.today())

        if forma in ("Pix", "Dinheiro", "Fiado"):
            preco_unit = float(p["PrecoVista"])
        else:
            preco_unit = float(p["PrecoCartao"])

        preco_final = preco_unit
        total = preco_final * int(qtd)

        colA, colB = st.columns(2)
        with colA:
            st.metric("Preço unitário aplicado", f"R$ {preco_final:.2f}")
        with colB:
            st.metric("Total", f"R$ {total:.2f}")

        if st.button("Registrar Venda"):
            if int(qtd) > int(p["Quantidade"]):
                st.error("Estoque insuficiente.")
            else:
                nova = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "IDProduto": int(p["ID"]),
                    "NomeProduto": str(p["Nome"]),
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_final),
                    "Total": float(total),
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova])], ignore_index=True)
                salvar_csv(vendas, ARQ_VENDAS)
                produtos.loc[produtos["ID"] == pid, "Quantidade"] = int(p["Quantidade"]) - int(qtd)
                salvar_csv(produtos, ARQ_PRODUTOS)

                if forma == "Fiado" and nome_cliente_fiado and data_pagamento_fiado:
                    if "Status" not in clientes.columns:
                        clientes["Status"] = "Aberto"
                    nova_div = {
                        "ID": prox_id(clientes, "ID"),
                        "Cliente": str(nome_cliente_fiado).strip(),
                        "Produto": str(p["Nome"]),
                        "Valor": float(total),
                        "DataPagamento": str(data_pagamento_fiado),
                        "Status": "Aberto",
                    }
                    clientes = pd.concat([clientes, pd.DataFrame([nova_div])], ignore_index=True)
                    salvar_csv(clientes, ARQ_CLIENTES)

                st.success(f"Venda registrada! Total R$ {total:.2f}")

    st.markdown("---")
    st.subheader("Histórico de Vendas")
    st.dataframe(vendas, use_container_width=True)

    st.markdown("### 🗑️ Excluir Venda")
    if not vendas.empty:
        venda_opts = [
            f'{int(r.IDVenda)} - {r.NomeProduto} - {r.Quantidade} un - R$ {r.Total:.2f} - {r.Data}'
            for r in vendas.itertuples(index=False)
        ]
        venda_sel = st.selectbox("Selecione a venda para excluir", venda_opts, key="sel_excluir_venda")

        if st.button("Excluir venda selecionada"):
            try:
                confirm = st.checkbox("Confirmar exclusão da venda selecionada")
                if confirm:
                    vid = int(venda_sel.split(" - ")[0])
                    venda_excluir = vendas[vendas["IDVenda"] == vid].iloc[0]

                    # Repor estoque do produto
                    pid = int(venda_excluir["IDProduto"])
                    qtd_vendida = int(venda_excluir["Quantidade"])
                    if pid in produtos["ID"].values:
                        produtos.loc[produtos["ID"] == pid, "Quantidade"] += qtd_vendida
                        salvar_csv(produtos, ARQ_PRODUTOS)

                    # Excluir venda
                    vendas = vendas[vendas["IDVenda"] != vid].reset_index(drop=True)
                    salvar_csv(vendas, ARQ_VENDAS)

                    st.warning("Venda excluída e estoque atualizado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")