
import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
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
ESTOQUE_MINIMO_PADRAO = 5

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
    # Calcula preço de cartão se faltando
    df.loc[df["PrecoCartao"].isna() | (df["PrecoCartao"]==""), "PrecoCartao"] = (df["PrecoVista"].astype(float) / FATOR_CARTAO)
    return df

def norm_vendas() -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes() -> pd.DataFrame:
    # Inclui RefVenda e FormaPagamento para correlacionar exclusões e auditoria
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status","RefVenda","FormaPagamento"]
    df = ensure_csv(ARQ_CLIENTES, cols)
    df["Valor"] = df["Valor"].apply(to_float)
    return df

def norm_usuarios() -> pd.DataFrame:
    cols = ["Usuario","Senha"]
    df = ensure_csv(ARQ_USUARIOS, cols)
    if df.empty:
        df = pd.DataFrame([{"Usuario":"admin","Senha":"123"}])
        save_csv(df, ARQ_USUARIOS)
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
        st.session_state["pedido_atual"] = []  # itens: {IDProduto, NomeProduto, Quantidade, PrecoVista}
    if "valor_pago" not in st.session_state:
        st.session_state["valor_pago"] = 0.0

boot_session()

produtos = st.session_state["produtos"]
vendas   = st.session_state["vendas"]
clientes = st.session_state["clientes"]

# =====================================
# Helpers
# =====================================
def preco_por_forma(preco_vista: float, forma: str) -> float:
    if forma == "Cartão":
        return float(preco_vista) / FATOR_CARTAO
    return float(preco_vista)

def add_item_ao_pedido(pid: str, nome: str, qtd: int, preco_vista: float):
    st.session_state["pedido_atual"].append({
        "IDProduto": str(pid),
        "NomeProduto": nome,
        "Quantidade": int(qtd),
        "PrecoVista": float(preco_vista),
    })

def desenha_pedido(forma: str) -> pd.DataFrame:
    pedido_lista = st.session_state["pedido_atual"]
    if not pedido_lista:
        return pd.DataFrame()

    st.write("### Pedido Atual")
    novos_itens = []
    for idx, item in enumerate(pedido_lista):
        col1, col2, col3, col4, col5 = st.columns([4,2,2,2,1])
        with col1:
            st.write(f"**{item['NomeProduto']}** (ID {item['IDProduto']})")
        with col2:
            nova_qtd = st.number_input("Qtd", min_value=1, value=int(item["Quantidade"]), step=1, key=f"q_{idx}")
        preco_unit = preco_por_forma(item["PrecoVista"], forma)
        with col3:
            st.write("Unit.:", brl(preco_unit))
        with col4:
            st.write("Subtotal:", brl(nova_qtd * preco_unit))
        with col5:
            if st.button("🗑️", key=f"rem_{idx}"):
                # remove item e força rerun seguro (API nova)
                st.session_state["pedido_atual"].pop(idx)
                st.rerun()
        novos_itens.append({
            "IDProduto": item["IDProduto"],
            "NomeProduto": item["NomeProduto"],
            "Quantidade": int(nova_qtd),
            "PrecoVista": float(item["PrecoVista"]),
        })
    st.session_state["pedido_atual"] = novos_itens

    df = pd.DataFrame([{
        "IDProduto": it["IDProduto"],
        "Produto": it["NomeProduto"],
        "Quantidade": it["Quantidade"],
        "Preço unit.": round(preco_por_forma(it["PrecoVista"], forma), 2),
        "Total": round(it["Quantidade"] * preco_por_forma(it["PrecoVista"], forma), 2),
    } for it in novos_itens])
    return df

# =====================================
# Sidebar
# =====================================
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Promoções","Sair"], index=0)

if view == "Sair":
    st.session_state.clear()
    st.success("Sessão encerrada.")
    st.stop()

# =====================================
# DASHBOARD
# =====================================
if view == "Dashboard":
    st.header("📊 Dashboard")
    total_vendas = vendas["Total"].sum() if not vendas.empty else 0.0
    hoje_str = str(date.today())
    vendas_hoje = vendas[vendas["Data"]==hoje_str]["Total"].sum() if not vendas.empty else 0.0
    qntd_vendas = len(vendas) if not vendas.empty else 0
    fiados_abertos = len(clientes[clientes["Status"].str.lower()=="aberto"]) if not clientes.empty else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Faturamento Total", brl(total_vendas))
    with col2: st.metric("Vendas Hoje", brl(vendas_hoje))
    with col3: st.metric("Qtde de Vendas", qntd_vendas)
    with col4: st.metric("Fiados em Aberto", fiados_abertos)

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by=["Data","IDVenda"], ascending=False).head(50), use_container_width=True)

# =====================================
# PRODUTOS
# =====================================
if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar novo produto"):
        c1,c2,c3 = st.columns(3)
        with c1:
            nome = st.text_input("Nome")
            marca = st.text_input("Marca")
            categoria = st.text_input("Categoria")
        with c2:
            qtd = st.number_input("Quantidade", min_value=0, step=1, value=0)
            preco_custo = st.text_input("Preço de Custo", value="0,00")
            preco_vista = st.text_input("Preço à Vista", value="0,00")
        with c3:
            validade = st.date_input("Validade (opcional)", value=date.today())
            foto_url = st.text_input("URL da Foto (opcional)")

        preco_cartao_calc = round(to_float(preco_vista) / FATOR_CARTAO, 2) if to_float(preco_vista) > 0 else 0.0
        st.text_input("Preço no Cartão (auto)", value=str(preco_cartao_calc).replace(".", ","), disabled=True)

        if st.button("Adicionar produto"):
            novo = {
                "ID": prox_id(produtos, "ID"),
                "Nome": nome.strip(),
                "Marca": marca.strip(),
                "Categoria": categoria.strip(),
                "Quantidade": int(qtd),
                "PrecoCusto": to_float(preco_custo),
                "PrecoVista": to_float(preco_vista),
                "PrecoCartao": preco_cartao_calc,
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

    # -- Forma de pagamento primeiro (impacta preço unitário)
    forma = st.radio("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"], horizontal=True)

    # -- Seleção/pesquisa de produto
    st.subheader("Adicionar itens")
    c1,c2 = st.columns([2,3])
    with c1:
        codigo = st.text_input("Código do Produto")
    with c2:
        nome_filtro = st.text_input("Pesquisar por nome")

    df_sel = produtos.copy()
    if not df_sel.empty:
        if codigo:
            df_sel = df_sel[df_sel["ID"].astype(str).str.contains(str(codigo))]
        if nome_filtro:
            df_sel = df_sel[df_sel["Nome"].str.contains(nome_filtro, case=False, na=False)]

    escolha = None
    if not df_sel.empty:
        df_sel["Rotulo"] = df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)
        escolha = st.selectbox("Selecione o produto", df_sel["Rotulo"].tolist())
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
                add_item_ao_pedido(pid, rowp["Nome"], int(qtd), preco_vista)
                st.success("Item adicionado.")

    # -- Exibe pedido com edição/remoção
    df_pedido = desenha_pedido(forma)
    valor_total = float(df_pedido["Total"].sum()) if not df_pedido.empty else 0.0

    # -- Campos extras para FIADO
    cliente_nome = ""
    data_pag = None
    if forma == "Fiado":
        st.markdown("#### Dados do fiado")
        cliente_nome = st.text_input("Nome do cliente")
        data_pag = st.date_input("Data prevista de pagamento", value=date.today()+timedelta(days=7))

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
    b1,b2,b3,b4 = st.columns(4)

    if b1.button("✅ Finalizar Venda"):
        if not st.session_state["pedido_atual"]:
            st.warning("Adicione itens ao pedido.")
        else:
            novo_id = prox_id(vendas, "IDVenda")
            # grava itens e baixa estoque
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

            # Se FIADO: registra também em clientes.csv
            if forma == "Fiado":
                if not cliente_nome.strip():
                    st.error("Informe o nome do cliente para fiado.")
                    st.stop()
                if not data_pag:
                    st.error("Informe a data prevista de pagamento para fiado.")
                    st.stop()
                # um registro por venda (valor total do pedido)
                novo_cli = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome.strip(),
                    "Produto": "Pedido de venda",
                    "Valor": float(valor_total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto",
                    "RefVenda": str(novo_id),
                    "FormaPagamento": "Fiado",
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_cli])], ignore_index=True)
                st.session_state["clientes"] = clientes
                save_csv(clientes, ARQ_CLIENTES)

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

    if b4.button("❌ Limpar Pedido"):
        st.session_state["pedido_atual"] = []
        st.session_state["valor_pago"] = 0.0
        st.info("Pedido limpo.")

    # Histórico com exclusão de venda (devolve estoque) e sem experimental_rerun
    st.markdown("### Últimas vendas")
    if not vendas.empty:
        ult = vendas.sort_values(by=["Data","IDVenda"], ascending=False).head(200)
        st.dataframe(ult, use_container_width=True)
        ids = pd.to_numeric(vendas["IDVenda"], errors="coerce").dropna().astype(int).unique().tolist()
ids = sorted(ids, reverse=True)

        colx, coly = st.columns([3,1])
        with colx:
            id_excluir = st.selectbox("Selecione a venda para excluir (devolve estoque)", ids if ids else [0])
        with coly:
            if st.button("Excluir venda"):
                # devolve estoque antes de excluir
                linhas = vendas[vendas["IDVenda"].astype(int)==int(id_excluir)]
                for _, r in linhas.iterrows():
                    mask = produtos["ID"].astype(str) == str(r["IDProduto"])
                    if mask.any():
                        produtos.loc[mask, "Quantidade"] = (produtos.loc[mask, "Quantidade"].astype(int) + int(r["Quantidade"])).astype(int)
                # remove venda
                vendas = vendas[vendas["IDVenda"].astype(int)!=int(id_excluir)]
                save_csv(vendas, ARQ_VENDAS)
                save_csv(produtos, ARQ_PRODUTOS)
                st.session_state["vendas"] = vendas
                st.success(f"Venda {id_excluir} excluída e estoque ajustado.")
    else:
        st.info("Ainda não há vendas registradas.")

# =====================================
# CLIENTES (Fiado)
# =====================================
if view == "Clientes":
    st.header("👥 Clientes (Fiado)")
    if clientes.empty:
        st.info("Nenhum fiado lançado.")
    else:
        st.dataframe(clientes, use_container_width=True)
        st.markdown("#### Atualizar status de fiado")
        ids = clientes["ID"].astype(str).tolist()
        sel = st.selectbox("Selecione o registro", ids)
        novo_status = st.selectbox("Status", ["Aberto","Pago"])
        if st.button("Salvar status"):
            clientes.loc[clientes["ID"].astype(str)==str(sel), "Status"] = novo_status
            st.session_state["clientes"] = clientes
            save_csv(clientes, ARQ_CLIENTES)
            st.success("Status atualizado!")

# =====================================
# PROMOÇÕES (simples)
# =====================================
if view == "Promoções":
    st.header("🏷️ Promoções")
    promocoes_file = "promocoes.csv"
    try:
        promocoes = pd.read_csv(promocoes_file, dtype=str)
    except Exception:
        promocoes = pd.DataFrame(columns=["ID","Descricao","Desconto"])
        promocoes.to_csv(promocoes_file, index=False)

    with st.expander("Cadastrar promoção"):
        desc = st.text_input("Descrição")
        desconto = st.text_input("Desconto (%)", value="0")
        if st.button("Adicionar promoção"):
            novo = {"ID": str(prox_id(promocoes, "ID")), "Descricao": desc, "Desconto": desconto}
            promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
            promocoes.to_csv(promocoes_file, index=False)
            st.success("Promoção cadastrada!")

    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        st.dataframe(promocoes, use_container_width=True)
        del_id = st.selectbox("Selecione ID para excluir", promocoes["ID"].astype(str).tolist())
        if st.button("Excluir promoção"):
            promocoes = promocoes[promocoes["ID"].astype(str)!=del_id]
            promocoes.to_csv(promocoes_file, index=False)
            st.warning(f"Promoção {del_id} excluída!")
