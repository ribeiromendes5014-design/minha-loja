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
# Utilidades de persistência (CSV)
# =====================================
# (... restante do código igual ...)

# =====================================
# VENDAS (trecho corrigido)
# =====================================
if view == "Vendas":
    show_logo("main")
    st.header("🧾 Vendas Detalhadas")

    # (... código anterior ...)

    # -- Dinheiro: valor pago e troco
    valor_pago = st.session_state.get("valor_pago", 0.0)
    troco = 0.0
    if forma == "Dinheiro":
        valor_pago = st.number_input("Valor pago", min_value=0.0, value=float(valor_pago), step=1.0)
        st.session_state["valor_pago"] = valor_pago
        troco = max(valor_pago - valor_total, 0.0)

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("Valor Total", brl(valor_total))
    with colB:
        st.metric("Valor Pago", brl(valor_pago if forma == "Dinheiro" else 0.0))
    with colC:
        st.metric("Troco", brl(troco if forma == "Dinheiro" else 0.0))

    st.markdown("---")
    b1, b2, b3, b4, b5 = st.columns(5)

    if b1.button("✅ Finalizar Venda"):
        # ... código de finalizar venda ...
        pass

    if b2.button("🆕 Nova Venda"):
        st.session_state["pedido_atual"] = []
        st.session_state["valor_pago"] = 0.0
        st.info("Novo pedido iniciado.")

    if b3.button("📦 Fechar Caixa"):
        hoje = str(date.today())
        vendas_dia = vendas[vendas["Data"] == hoje]

        if vendas_dia.empty:
            st.warning("Nenhuma venda registrada hoje.")
        else:
            total = vendas_dia["Total"].sum()
            dinheiro = vendas_dia[vendas_dia["FormaPagamento"]=="Dinheiro"]["Total"].sum()
            pix = vendas_dia[vendas_dia["FormaPagamento"]=="PIX"]["Total"].sum()
            cartao = vendas_dia[vendas_dia["FormaPagamento"]=="Cartão"]["Total"].sum()
            fiado = vendas_dia[vendas_dia["FormaPagamento"]=="Fiado"]["Total"].sum()

            caixas = norm_caixas(pd.DataFrame())
            caixas = caixas[caixas["Data"] != hoje]
            novo = {
                "Data": hoje,
                "FaturamentoTotal": total,
                "Dinheiro": dinheiro,
                "PIX": pix,
                "Cartão": cartao,
                "Fiado": fiado,
                "Status": "Fechado"
            }
            caixas = pd.concat([caixas, pd.DataFrame([novo])], ignore_index=True)
            save_csv(caixas, "caixas.csv")
            st.session_state["caixas"] = caixas
            st.success(f"Caixa do dia {hoje} fechado!")
            st.info("Caixa fechado (simulação).")

    if b4.button("✏️ Editar Pedido"):
        st.info("Edite as quantidades acima e remova itens com o ícone 🗑️.")

    if b5.button("❌ Sair"):
        st.stop()

    # (... resto do código continua igual ...)
