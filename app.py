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
# Função utilitária para ler código de barras via pyzxing
# =====================================
def ler_codigo_barras(imagem_bytes: bytes) -> str | None:
    try:
        reader = BarCodeReader()
        with open("temp_barcode.png", "wb") as f:
            f.write(imagem_bytes)
        res = reader.decode("temp_barcode.png")
        if res and len(res) > 0:
            return res[0]["parsed"]
        return None
    except Exception as e:
        st.error(f"Erro ao ler código de barras: {e}")
        return None

# =====================================
# Utilidades de persistência (CSV)
# =====================================
def ensure_csv(path: str, columns: list, defaults: dict = None) -> pd.DataFrame:
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

# =====================================
# PRODUTOS (com código de barras)
# =====================================
# Cadastro e edição já incluem campo CodigoBarras

# =====================================
# VENDAS (com leitura e salvamento de código de barras)
# =====================================
if view == "Vendas":
    show_logo("main")
    st.header("🧾 Vendas Detalhadas")

    st.subheader("Forma de Pagamento")
    forma = st.radio("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"], horizontal=True)

    st.subheader("Itens do pedido")
    c1,c2,c3 = st.columns([2,3,2])
    with c1:
        codigo = st.text_input("Código do Produto")
        foto_codigo = st.camera_input("📷 Escanear código de barras")
        if foto_codigo is not None:
            codigo_lido = ler_codigo_barras(foto_codigo.getbuffer())
            if codigo_lido:
                codigo = codigo_lido
                st.success(f"Código lido: {codigo}")
    with c2:
        nome_filtro = st.text_input("Pesquisar por nome")

    df_sel = produtos.copy()
    if codigo:
        df_sel = df_sel[(df_sel["ID"].astype(str).str.contains(codigo)) | (df_sel.get("CodigoBarras", "").astype(str).str.contains(codigo))]
    if nome_filtro:
        df_sel = df_sel[df_sel["Nome"].astype(str).str.contains(nome_filtro, case=False, na=False)]

    if not df_sel.empty:
        st.dataframe(df_sel[["ID","Nome","CodigoBarras","Quantidade","PrecoVista"]], use_container_width=True)

        escolha = st.selectbox("Selecione o produto", (df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)).tolist())
        qtd = st.number_input("Qtd", min_value=1, value=1, step=1)

        if escolha and st.button("Adicionar ao pedido"):
            pid = escolha.split(" - ")[0]
            rowp = df_sel[df_sel["ID"].astype(str)==pid].iloc[0]
            st.session_state.setdefault("pedido_atual", []).append({
                "IDProduto": pid,
                "NomeProduto": rowp["Nome"],
                "CodigoBarras": rowp.get("CodigoBarras", ""),
                "Quantidade": int(qtd),
                "PrecoVista": float(rowp["PrecoVista"])
            })
            st.success("Item adicionado.")

    if "pedido_atual" in st.session_state and st.session_state["pedido_atual"]:
        st.write("### Pedido Atual")
        st.dataframe(pd.DataFrame(st.session_state["pedido_atual"]), use_container_width=True)

# =====================================
# CLIENTES (Fiado) vinculado ao código de barras
# =====================================
if view == "Clientes":
    show_logo("main")
    st.header("👥 Clientes (Fiado)")
    if clientes.empty:
        st.info("Nenhum fiado lançado.")
    else:
        st.subheader("Pesquisar registros")
        c1, c2 = st.columns([2,2])
        with c1:
            nome_cliente_filtro = st.text_input("Filtrar por nome do cliente")
        with c2:
            foto_codigo_cliente = st.camera_input("📷 Escanear código de barras para buscar")
            codigo_cliente = None
            if foto_codigo_cliente is not None:
                codigo_cliente = ler_codigo_barras(foto_codigo_cliente.getbuffer())
                if codigo_cliente:
                    st.success(f"Código lido: {codigo_cliente}")

        clientes_filtrados = clientes.copy()
        if nome_cliente_filtro:
            clientes_filtrados = clientes_filtrados[clientes_filtrados["Cliente"].astype(str).str.contains(nome_cliente_filtro, case=False, na=False)]
        if codigo_cliente:
            clientes_filtrados = clientes_filtrados[clientes_filtrados["Produto"].astype(str).str.contains(codigo_cliente, case=False, na=False)]

        if clientes_filtrados.empty:
            st.info("Nenhum registro encontrado com os filtros aplicados.")
        else:
            st.dataframe(clientes_filtrados, use_container_width=True)

        st.markdown("#### Atualizar status")
        ids = clientes_filtrados["ID"].astype(str).tolist()
        sel = st.selectbox("Selecione o registro", ids) if ids else None
        novo_status = st.selectbox("Status", ["Aberto","Pago"])

        forma_pag = None
        if novo_status == "Pago":
            forma_pag = st.selectbox("Forma de pagamento (finalização)", ["Dinheiro","PIX","Cartão"])

        if st.button("Salvar status"):
            if sel is None:
                st.warning("Selecione um registro válido.")
            else:
                idx = clientes["ID"].astype(str)==str(sel)
                clientes.loc[idx, "Status"] = novo_status
                if forma_pag:
                    clientes.loc[idx, "FormaPagamento"] = forma_pag
                st.session_state["clientes"] = clientes
                save_csv(clientes, ARQ_CLIENTES)
                st.success("Status atualizado!")
