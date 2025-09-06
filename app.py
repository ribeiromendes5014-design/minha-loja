import streamlit as st
import pandas as pd
from datetime import datetime, date
import os

ARQ_PRODUTOS = "produtos.csv"
FOTOS_DIR = "foto_produtos"
os.makedirs(FOTOS_DIR, exist_ok=True)
FATOR_CARTAO = 0.8872

# Funções auxiliares
def to_float(x, default=0.0):
    try:
        return float(str(x).replace(",", ".").strip())
    except:
        return default

def save_csv(df, path):
    df.to_csv(path, index=False)

def prox_id(df: pd.DataFrame, col: str) -> int:
    if df.empty or col not in df.columns:
        return 1
    try:
        vals = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        return int(vals.max()) + 1 if len(vals) else 1
    except:
        return 1

# =====================================
# Cadastro de produto (trecho alterado)
# =====================================

if st.button("Adicionar produto"):
    novo_id = prox_id(produtos, "ID")

    # salva a foto se enviada
    caminho_foto = foto_url.strip()
    if foto_arquivo is not None:
        extensao = os.path.splitext(foto_arquivo.name)[1]
        caminho_foto = os.path.join(FOTOS_DIR, f"produto_{novo_id}{extensao}")
        with open(caminho_foto, "wb") as f:
            f.write(foto_arquivo.getbuffer())
        # 🔥 salva caminho relativo no CSV
        caminho_foto = os.path.relpath(caminho_foto, start=".")

    novo = {
        "ID": novo_id,
        "Nome": nome.strip(),
        "Marca": marca.strip(),
        "Categoria": categoria.strip(),
        "Quantidade": int(qtd),
        "PrecoCusto": to_float(preco_custo),
        "PrecoVista": to_float(preco_vista),
        "PrecoCartao": round(to_float(preco_vista) / FATOR_CARTAO, 2) if to_float(preco_vista) > 0 else 0.0,
        "Validade": str(validade) if validade else "",
        "FotoURL": caminho_foto,
        "CodigoBarras": str(codigo_barras).strip()
    }

    produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
    st.session_state["produtos"] = produtos
    save_csv(produtos, ARQ_PRODUTOS)
    st.success("Produto cadastrado!")
