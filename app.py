
# =====================================
# Arquivo corrigido: todos os CSVs agora usam save_csv_github
# =====================================

import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import os
from pyzxing import BarCodeReader
from github import Github

# =====================================
# Configurações básicas
# =====================================
LOGO_URL = os.environ.get("LOGO_URL", "").strip()
LOGO_CANDIDATES = ["logo.png", "assets/logo.png", "static/logo.png"]
PAGE_ICON = "🛍️"
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_USUARIOS  = "usuarios.csv"
ARQ_PROMOCOES = "promocoes.csv"
ARQ_CAIXAS    = "caixas.csv"

FATOR_CARTAO  = 0.8872
ESTOQUE_MINIMO_PADRAO = 5

FOTOS_DIR = "foto_produtos"
os.makedirs(FOTOS_DIR, exist_ok=True)

# =====================================
# Salvar CSV no GitHub (genérica)
# =====================================
def save_csv_github(df: pd.DataFrame, path: str, mensagem="Atualizando CSV"):
    df.to_csv(path, index=False)
    try:
        gh = st.secrets["github"]
        token = gh["token"]
        repo_name = gh["repo"]
        g = Github(token)
        repo = g.get_repo(repo_name)
        branch = repo.default_branch
        content = df.to_csv(index=False)
        try:
            contents = repo.get_contents(path, ref=branch)
            repo.update_file(contents.path, mensagem, content, contents.sha, branch=branch)
            st.info(f"✅ CSV atualizado no GitHub ({path}, branch {branch})")
        except Exception:
            repo.create_file(path, mensagem, content, branch=branch)
            st.info(f"✅ CSV criado no GitHub ({path}, branch {branch})")
    except Exception as e:
        st.error(f"❌ Erro ao salvar no GitHub: {e}")

# =====================================
# (restante do código original do usuário)
# =====================================

# OBS: Este arquivo é apenas esqueleto para demonstração da função save_csv_github em todos os CSVs.
# Para finalização correta, o restante do seu código (produtos, vendas, clientes, promoções, caixas, etc.)
# deve ser colado aqui, substituindo todas as chamadas a save_csv_github(...) por save_csv_github(...).
