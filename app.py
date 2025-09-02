import streamlit as st
import pandas as pd
from datetime import date
import os
import io
from PIL import Image
import pyzxing

# =====================================
# Configurações básicas
# =====================================
PAGE_ICON = "🛍️"
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"

FATOR_CARTAO  = 0.8872

# =====================================
# Função para ler código de barras em imagem
# =====================================
def ler_codigo_barras_imagem(img_bytes):
    try:
        img_path = "temp_code.jpg"
        with open(img_path, "wb") as f:
            f.write(img_bytes)
        reader = pyzxing.BarCodeReader()
        results = reader.decode(img_path)
        if results and "parsed" in results[0]:
            return results[0]["parsed"]
    except Exception as e:
        st.error(f"Erro ao ler código de barras: {e}")
    return None

# =====================================
# Utilidades de persistência (CSV)
# =====================================
def ensure_csv(path: str, columns: list) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
    for c in columns:
        if c not in df.columns:
            df[c] = ""
    df = df[columns]
    return df

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

# =====================================
# Normalizadores de dados
# =====================================
def norm_produtos() -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

# =====================================
# Menu lateral
# =====================================
if "view" not in st.session_state:
    st.session_state["view"] = "Dashboard"

view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Sair"], index=0)

produtos = norm_produtos()

# =====================================
# PRODUTOS
# =====================================
if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar novo produto"):
        st.subheader("📷 Escanear ou digitar código de barras")
        foto = st.camera_input("Tire uma foto do código de barras")
        codigo_barras = ""
        if foto is not None:
            cod_lido = ler_codigo_barras_imagem(foto.getvalue())
            if cod_lido:
                st.success(f"Código lido: {cod_lido}")
                codigo_barras = cod_lido
        codigo_barras = st.text_input("Código do Produto (ID)", value=codigo_barras)

        c1,c2,c3 = st.columns(3)
        with c1:
            nome = st.text_input("Nome")
            marca = st.text_input("Marca")
            categoria = st.text_input("Categoria")
        with c2:
            qtd = st.number_input("Quantidade", min_value=0, step=1, value=0)
            preco_custo = st.text_input("Preço de Custo", value="0,00")
            preco_vista = st.text_input("Preço à Vista", value="0,00")
        preco_cartao = 0.0
        try:
            preco_cartao = round(float(preco_vista.replace(",", ".").strip()) / FATOR_CARTAO, 2)
        except Exception:
            preco_cartao = 0.0
        st.text_input("Preço no Cartão (auto)", value=str(preco_cartao).replace(".", ","), disabled=True)

        with c3:
            validade = st.date_input("Validade (opcional)", value=date.today())
            foto_url = st.text_input("URL da Foto (opcional)")

        if st.button("Adicionar produto"):
            if not codigo_barras:
                st.error("Escaneie ou insira manualmente o código de barras.")
            else:
                novo = {
                    "ID": codigo_barras.strip(),
                    "Nome": nome.strip(),
                    "Marca": marca.strip(),
                    "Categoria": categoria.strip(),
                    "Quantidade": int(qtd),
                    "PrecoCusto": to_float(preco_custo),
                    "PrecoVista": to_float(preco_vista),
                    "PrecoCartao": round(to_float(preco_vista) / FATOR_CARTAO, 2) if to_float(preco_vista)>0 else 0.0,
                    "Validade": str(validade) if validade else "",
                    "FotoURL": foto_url.strip()
                }
                produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
                st.session_state["produtos"] = produtos
                save_csv(produtos, ARQ_PRODUTOS)
                st.success("Produto cadastrado!")

    st.markdown("### Lista de produtos")
    if produtos.empty:
        st.info("Nenhum produto cadastrado ainda.")
    else:
        st.dataframe(produtos, use_container_width=True)

# =====================================
# VENDAS
# =====================================
if view == "Vendas":
    st.header("🧾 Vendas")
    st.subheader("📷 Escanear ou digitar código de barras")

    foto = st.camera_input("Tire uma foto do código de barras para vender")
    codigo_venda = ""
    if foto is not None:
        cod_lido = ler_codigo_barras_imagem(foto.getvalue())
        if cod_lido:
            st.success(f"Código lido: {cod_lido}")
            codigo_venda = cod_lido

    codigo_venda = st.text_input("Código de Barras do Produto", value=codigo_venda)

    if codigo_venda:
        prod = produtos[produtos["ID"] == codigo_venda]
        if not prod.empty:
            prod = prod.iloc[0]
            st.success(f"Produto encontrado: {prod['Nome']} (Estoque: {prod['Quantidade']})")
            qtd = st.number_input("Quantidade", min_value=1, max_value=int(prod["Quantidade"]), step=1)
            if st.button("Adicionar à venda"):
                st.info(f"{qtd}x {prod['Nome']} adicionado ao pedido.")
        else:
            st.error("Produto não encontrado no cadastro.")
