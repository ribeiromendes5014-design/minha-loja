
import streamlit as st
import pandas as pd
from datetime import date
import os

# =====================================
# Configurações básicas
# =====================================
PAGE_ICON = "🛍️"
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide", page_icon=PAGE_ICON)

ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_USUARIOS  = "usuarios.csv"
FATOR_CARTAO  = 0.8872  # preço no cartão = preço à vista / 0,8872

# =====================================
# Utilidades de persistência (CSV)
# =====================================
def ensure_csv(path: str, columns: list) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
    # garante colunas
    for c in columns:
        if c not in df.columns:
            df[c] = ""
    return df[columns]

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

def prox_id(df: pd.DataFrame, col: str) -> int:
    if df.empty or col not in df.columns:
        return 1
    try:
        vals = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        return int(vals.max()) + 1 if len(vals) else 1
    except Exception:
        return 1

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

def norm_vendas() -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes() -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status","FormaPagamento"]
    df = ensure_csv(ARQ_CLIENTES, cols)
    df["Valor"] = df["Valor"].apply(to_float)
    return df

# =====================================
# Formatação BRL
# =====================================
def brl(v: float) -> str:
    try:
        s = f"{float(v):,.2f}"
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {s}"
    except Exception:
        return "R$ 0,00"

# =====================================
# Sessão
# =====================================
def boot_session():
    if "produtos" not in st.session_state:
        st.session_state["produtos"] = norm_produtos()
    if "vendas" not in st.session_state:
        st.session_state["vendas"] = norm_vendas()
    if "clientes" not in st.session_state:
        st.session_state["clientes"] = norm_clientes()
    if "pedido_atual" not in st.session_state:
        st.session_state["pedido_atual"] = []  # itens: IDProduto, NomeProduto, Qtd, PrecoVista
    if "valor_pago" not in st.session_state:
        st.session_state["valor_pago"] = 0.0

boot_session()

produtos = st.session_state["produtos"]
vendas   = st.session_state["vendas"]

# =====================================
# Helpers
# =====================================
def preco_por_forma(preco_vista: float, forma: str) -> float:
    if forma == "Cartão":
        return float(preco_vista) / FATOR_CARTAO
    # Dinheiro, PIX, Fiado usam à vista
    return float(preco_vista)

def desenha_pedido(forma: str) -> pd.DataFrame:
    # Tabela editável com remoção e alteração de quantidade
    pedido_lista = st.session_state["pedido_atual"]
    if not pedido_lista:
        return pd.DataFrame()

    st.write("### Pedido Atual")
    novos_itens = []
    total = 0.0
    for idx, item in enumerate(pedido_lista):
        col1, col2, col3, col4, col5 = st.columns([4,2,2,2,1])
        with col1:
            st.write(f"**{item['NomeProduto']}** (ID {item['IDProduto']})")
        with col2:
            # quantidade editável
            nova_qtd = st.number_input("Qtd", min_value=1, value=int(item["Quantidade"]), key=f"q_{idx}")
        preco_unit = preco_por_forma(item["PrecoVista"], forma)
        with col3:
            st.write("Unit.:", brl(preco_unit))
        subtotal = nova_qtd * preco_unit
        with col4:
            st.write("Subtotal:", brl(subtotal))
        with col5:
            if st.button("🗑️", key=f"rem_{idx}"):
                # remove e rerun
                st.session_state["pedido_atual"].pop(idx)
                st.experimental_rerun()
        novos_itens.append({
            "IDProduto": item["IDProduto"],
            "NomeProduto": item["NomeProduto"],
            "Quantidade": int(nova_qtd),
            "PrecoVista": float(item["PrecoVista"]),
        })
        total += subtotal

    # sobrescreve quantidades editadas
    st.session_state["pedido_atual"] = novos_itens
    df_exib = pd.DataFrame([{
        "IDProduto": it["IDProduto"],
        "Produto": it["NomeProduto"],
        "Quantidade": it["Quantidade"],
        "Preço unit.": preco_por_forma(it["PrecoVista"], forma),
        "Total": it["Quantidade"] * preco_por_forma(it["PrecoVista"], forma),
    } for it in novos_itens])
    return df_exib

# =====================================
# Sidebar
# =====================================
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Promoções"], index=2)

# =====================================
# VENDAS - Layout final com melhorias
# =====================================
if view == "Vendas":
    st.header("🧾 Vendas Detalhadas")

    # -- Forma de pagamento primeiro (impacta preço unitário)
    st.subheader("Forma de Pagamento")
    forma = st.radio("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"], horizontal=True)

    # -- Seleção de produto
    st.subheader("Itens do pedido")
    c1,c2,c3,c4 = st.columns([2,3,2,2])
    with c1:
        codigo = st.text_input("Código do Produto")
    with c2:
        nome_filtro = st.text_input("Pesquisar por nome")

    df_sel = produtos.copy()
    if codigo:
        df_sel = df_sel[df_sel["ID"].astype(str).str.contains(codigo)]
    if nome_filtro:
        df_sel = df_sel[df_sel["Nome"].str.contains(nome_filtro, case=False, na=False)]

    escolha = None
    if not df_sel.empty:
        escolha = st.selectbox("Selecione o produto", df_sel["ID"].astype(str) + " - " + df_sel["Nome"])
    col_qtd, col_preco = st.columns([1,3])
    with col_qtd:
        qtd = st.number_input("Qtd", min_value=1, value=1, step=1)
    with col_preco:
        if escolha is not None:
            pid = escolha.split(" - ")[0].strip()
            rowp = df_sel[df_sel["ID"].astype(str)==pid].iloc[0]
            preco_vista = float(rowp["PrecoVista"])
            preco_unit = preco_por_forma(preco_vista, forma)
            st.write("Preço do item:", brl(preco_unit))

            if st.button("Adicionar ao pedido"):
                st.session_state["pedido_atual"].append({
                    "IDProduto": pid,
                    "NomeProduto": rowp["Nome"],
                    "Quantidade": int(qtd),
                    "PrecoVista": preco_vista,  # guardo o à vista, e calculo por forma depois
                })
                st.success("Item adicionado.")

    # -- Exibe pedido com edição/remoção
    df_pedido = desenha_pedido(forma)
    valor_total = float(df_pedido["Total"].sum()) if not df_pedido.empty else 0.0

    # -- Dinheiro: valor pago e troco
    valor_pago = st.session_state.get("valor_pago", 0.0)
    troco = 0.0
    if forma == "Dinheiro":
        valor_pago = st.number_input("Valor pago", min_value=0.0, value=float(valor_pago), step=1.0)
        st.session_state["valor_pago"] = valor_pago
        troco = max(valor_pago - valor_total, 0.0)

    colA, colB, colC = st.columns(3)
    colA.metric("Valor Total", brl(valor_total))
    colB.metric("Valor Pago", brl(valor_pago if forma == "Dinheiro" else 0.0))
    colC.metric("Troco", brl(troco if forma == "Dinheiro" else 0.0))

    st.markdown("---")
    b1,b2,b3,b4,b5,b6 = st.columns(6)

    if b1.button("✅ Finalizar Venda"):
        if not st.session_state["pedido_atual"]:
            st.warning("Adicione itens ao pedido.")
        else:
            novo_id = prox_id(vendas, "IDVenda")
            for item in st.session_state["pedido_atual"]:
                preco_unit = preco_por_forma(item["PrecoVista"], forma)
                total_item = preco_unit * int(item["Quantidade"])
                nova_linha = {
                    "IDVenda": novo_id,
                    "Data": str(date.today()),
                    "IDProduto": item["IDProduto"],
                    "NomeProduto": item["NomeProduto"],
                    "FormaPagamento": forma,
                    "Quantidade": int(item["Quantidade"]),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total_item),
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_linha])], ignore_index=True)
                # baixa estoque
                mask = produtos["ID"].astype(str) == str(item["IDProduto"])
                if mask.any():
                    produtos.loc[mask, "Quantidade"] = (produtos.loc[mask, "Quantidade"].astype(int) - int(item["Quantidade"])).astype(int)
            save_csv(vendas, ARQ_VENDAS)
            save_csv(produtos, ARQ_PRODUTOS)
            st.session_state["pedido_atual"] = []
            st.session_state["valor_pago"] = 0.0
            st.success(f"Venda {novo_id} finalizada!")

    if b2.button("🆕 Nova Venda"):
        st.session_state["pedido_atual"] = []
        st.session_state["valor_pago"] = 0.0
        st.info("Novo pedido iniciado.")

    if b3.button("↩️ Devolução"):
        st.info("Devolução ainda não implementada.")

    if b4.button("📦 Fechar Caixa"):
        st.info("Caixa fechado (simulação).")

    if b5.button("✏️ Editar Pedido"):
        st.info("Edite as quantidades acima e remova itens com o ícone 🗑️.")

    if b6.button("❌ Sair"):
        st.stop()

    # Histórico com exclusão de venda
    st.markdown("### Últimas vendas")
    if not vendas.empty:
        ult = vendas.sort_values(by=["Data","IDVenda"], ascending=False).head(100)
        st.dataframe(ult, use_container_width=True)
        ids = list(map(int, sorted(vendas["IDVenda"].astype(int).unique(), reverse=True)))
        colx, coly = st.columns([3,1])
        with colx:
            id_excluir = st.selectbox("Selecione a venda para excluir (devolve estoque)", ids if ids else [0])
        with coly:
            if st.button("Excluir venda"):
                if id_excluir in ids:
                    linhas = vendas[vendas["IDVenda"].astype(int)==int(id_excluir)]
                    # devolve estoque
                    for _, r in linhas.iterrows():
                        mask = produtos["ID"].astype(str) == str(r["IDProduto"])
                        if mask.any():
                            produtos.loc[mask, "Quantidade"] = (produtos.loc[mask, "Quantidade"].astype(int) + int(r["Quantidade"])).astype(int)
                    # remove da planilha de vendas
                    vendas = vendas[vendas["IDVenda"].astype(int)!=int(id_excluir)]
                    save_csv(vendas, ARQ_VENDAS)
                    save_csv(produtos, ARQ_PRODUTOS)
                    st.success(f"Venda {id_excluir} excluída e estoque ajustado.")
                else:
                    st.warning("Venda não encontrada.")
    else:
        st.info("Ainda não há vendas registradas.")

