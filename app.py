import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import os
from pyzxing import BarCodeReader

# =====================================
# Configurações básicas
# =====================================
LOGO_URL = os.environ.get("LOGO_URL", "").strip()  # opcional: defina LOGO_URL no ambiente
LOGO_CANDIDATES = ["logo.png", "assets/logo.png", "static/logo.png"]
PAGE_ICON = "🛍️"

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_USUARIOS  = "usuarios.csv"
ARQ_PROMOCOES = "promocoes.csv"

FATOR_CARTAO  = 0.8872  # preco_cartao = preco_vista / FATOR_CARTAO
ESTOQUE_MINIMO_PADRAO = 5

# =====================================
# Leitura de Código de Barras (pyzxing)
# =====================================
def ler_codigo_barras(imagem_bytes: bytes) -> str | None:
    try:
        reader = BarCodeReader()
        with open("temp_barcode.png", "wb") as f:
            f.write(imagem_bytes)
        res = reader.decode("temp_barcode.png")
        if res and len(res) > 0:
            return res[0].get("parsed") or res[0].get("raw", "").strip()
        return None
    except Exception as e:
        st.error(f"Erro ao ler código de barras: {e}")
        return None

# =====================================
# Sessão: login
# =====================================
def do_login():
    st.session_state.setdefault("logado", False)
    if st.session_state.get("logado"):
        return True

    st.title("🔐 Login")
    user = st.text_input("Usuário", key="login_user")
    pwd  = st.text_input("Senha", type="password", key="login_pwd")
    if st.button("Entrar", key="login_btn"):
        if user == "admin" and pwd == "123":
            st.session_state["logado"] = True
            st.rerun() if hasattr(st,'rerun') else st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    st.stop()

do_login()

# =====================================
# PRODUTOS (exemplo corrigido)
# =====================================
st.header("📦 Produtos")
with st.expander("Cadastrar novo produto"):
    c1,c2,c3 = st.columns(3)
    with c1:
        nome = st.text_input("Nome", key="prod_nome")
    with c2:
        qtd = st.number_input("Quantidade", min_value=0, step=1, value=0, key="prod_qtd")
    with c3:
        validade = st.date_input("Validade", value=date.today(), key="prod_validade")
        codigo_barras = st.text_input("Código de Barras", key="cb_novo")
        foto_codigo = st.camera_input("📷 Escanear código de barras", key="cam_novo")
        if foto_codigo is not None:
            codigo_lido = ler_codigo_barras(foto_codigo.getbuffer())
            if codigo_lido:
                codigo_barras = codigo_lido
                st.success(f"Código lido: {codigo_barras}")

# Editor inline corrigido (exemplo)
eid = 1
novo_cb = st.text_input("Código de Barras", value="", key=f"cb_edit_{eid}")
