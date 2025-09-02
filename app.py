
import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import os

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
FATOR_CARTAO  = 0.8872  # preco_cartao = preco_vista / FATOR_CARTAO
ESTOQUE_MINIMO_PADRAO = 5

# =====================================
# Utilidades de persistência (CSV)
# =====================================
def ensure_csv(path: str, columns: list, defaults: dict = None) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        df = pd.DataFrame(columns=columns)
        df.to_csv(path, index=False)
    # Garantir colunas
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
def norm_produtos(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_vendas(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    df = ensure_csv(ARQ_CLIENTES, cols)
    df["Valor"] = df["Valor"].apply(to_float)
    return df

def norm_usuarios(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["Usuario","Senha"]
    df = ensure_csv(ARQ_USUARIOS, cols)
    # Se vazio, cria admin padrão
    if df.empty:
        df = pd.DataFrame([{"Usuario":"admin","Senha":"123"}])
        save_csv(df, ARQ_USUARIOS)
    return df

def reset_admin_user():
    """Cria/atualiza o usuário admin com senha 123 para recuperar acesso."""
    df = norm_usuarios(pd.DataFrame())
    if "Usuario" not in df.columns:
        df = pd.DataFrame(columns=["Usuario","Senha"])
    if (df["Usuario"] == "admin").any():
        df.loc[df["Usuario"]=="admin", "Senha"] = "123"
    else:
        df.loc[len(df)] = {"Usuario":"admin","Senha":"123"}
    save_csv(df, ARQ_USUARIOS)
    return True

# =====================================
# Formatação BRL
# =====================================
def brl(v: float) -> str:
    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

# =====================================
# Logo helpers
# =====================================
def get_logo_source():
    # URL de ambiente tem prioridade
    if LOGO_URL:
        return LOGO_URL
    for p in LOGO_CANDIDATES:
        if os.path.exists(p):
            return p
    return None

def show_logo(where="main"):
    src = get_logo_source()
    if not src:
        return
    if where == "sidebar":
        st.sidebar.image(src, use_column_width=True)
    else:
        st.image(src, width=180)

# =====================================
# Sessão: login simples (com recuperação e "manter conectado")
# =====================================
def do_login():
    st.session_state.setdefault("logado", False)
    st.session_state.setdefault("usuario_logado", None)
    if st.session_state.get("logado"):
        return True

    # Logo no topo da tela de login
    show_logo("main")
    st.title("🔐 Login")

    user = st.text_input("Usuário")
    pwd  = st.text_input("Senha", type="password")
    manter = st.checkbox("Manter conectado", value=False)
    rec  = st.checkbox("⚙️ Recuperar acesso (recriar admin/123)", value=False)

    _, c2, _ = st.columns([1,2,1])
    with c2:
        if st.button("Entrar", use_container_width=True):
            if rec:
                reset_admin_user()
                st.info("Usuário admin/123 recriado. Tente entrar novamente.")

            usuarios = norm_usuarios(pd.DataFrame())
            # Aceita admin/123 como fallback mesmo se não estiver no CSV
            cred_ok = (not usuarios[(usuarios["Usuario"]==user) & (usuarios["Senha"]==pwd)].empty) or (user=="admin" and pwd=="123")
            if cred_ok:
                # Garante que admin/123 esteja no CSV se foi usado como fallback
                if user == "admin" and pwd == "123":
                    reset_admin_user()
                st.session_state["logado"] = True
                st.session_state["usuario_logado"] = user if manter else None
                st.experimental_rerun()
            else:
                st.error("Usuário ou senha inválidos.")
    st.stop()

# =====================================
# Carregar dados na sessão
# =====================================
def boot_session():
    if "produtos" not in st.session_state:
        st.session_state["produtos"] = norm_produtos(pd.DataFrame())
    if "vendas" not in st.session_state:
        st.session_state["vendas"] = norm_vendas(pd.DataFrame())
    if "clientes" not in st.session_state:
        st.session_state["clientes"] = norm_clientes(pd.DataFrame())
    if "estoque_minimo" not in st.session_state:
        st.session_state["estoque_minimo"] = ESTOQUE_MINIMO_PADRAO

# =====================================
# Guardas
# =====================================
do_login()
boot_session()

produtos = norm_produtos(pd.DataFrame())
vendas   = norm_vendas(pd.DataFrame())
clientes = norm_clientes(pd.DataFrame())
st.session_state["produtos"] = produtos
st.session_state["vendas"] = vendas
st.session_state["clientes"] = clientes

# =====================================
# Sidebar
# =====================================
show_logo("sidebar")
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Promoções","Sair"], index=0)
st.sidebar.markdown("---")
st.sidebar.number_input("🔔 Estoque mínimo (alerta)", min_value=0, step=1, value=st.session_state["estoque_minimo"], key="estoque_minimo")

if view == "Sair":
    st.session_state.clear()
    st.success("Sessão encerrada.")
    st.stop()

# =====================================
# DASHBOARD
# =====================================
if view == "Dashboard":
    st.columns([1,3])[0].markdown("")
    show_logo("main")
    st.title("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    total_vendas = vendas["Total"].sum() if not vendas.empty else 0.0
    hoje_str = str(date.today())
    vendas_hoje = vendas[vendas["Data"]==hoje_str]["Total"].sum() if not vendas.empty else 0.0
    qntd_vendas = len(vendas) if not vendas.empty else 0
    fiados_abertos = len(clientes[clientes["Status"].str.lower()=="aberto"]) if not clientes.empty else 0
    with col1: st.metric("Faturamento Total", brl(total_vendas))
    with col2: st.metric("Vendas Hoje", brl(vendas_hoje))
    with col3: st.metric("Qtde de Vendas", qntd_vendas)
    with col4: st.metric("Fiados em Aberto", fiados_abertos)

    st.markdown("### ⚠️ Alertas")
    hoje = date.today()
    estoque_min = st.session_state["estoque_minimo"]

    def parse_data(v):
        try:
            return datetime.strptime(str(v)[:10], "%Y-%m-%d").date()
        except Exception:
            return None

    produtos["ValidadeDate"] = produtos["Validade"].apply(parse_data)
    validade_proxima = produtos.dropna(subset=["ValidadeDate"])
    validade_proxima = validade_proxima[validade_proxima["ValidadeDate"] <= (hoje + timedelta(days=60))]

    estoque_baixo = produtos[produtos["Quantidade"] <= estoque_min]

    if validade_proxima.empty and estoque_baixo.empty:
        st.success("Nenhum alerta no momento!")
    else:
        if not validade_proxima.empty:
            st.warning("Produtos com validade próxima (≤ 60 dias):")
            st.dataframe(validade_proxima[["ID","Nome","Quantidade","Validade"]], use_container_width=True)
        if not estoque_baixo.empty:
            st.error(f"Produtos com estoque baixo (≤ {estoque_min}):")
            st.dataframe(estoque_baixo[["ID","Nome","Quantidade"]], use_container_width=True)

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False).head(50), use_container_width=True)

# =====================================
# PRODUTOS
# =====================================
if view == "Produtos":
    show_logo("main")
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
        preco_cartao = 0.0
        try:
            preco_cartao = round(float(preco_vista.replace(",", ".").strip()) / 0.8872, 2)
        except Exception:
            preco_cartao = 0.0
        st.text_input("Preço no Cartão (auto)", value=str(preco_cartao).replace(".", ","), disabled=True)

        with c3:
            validade = st.date_input("Validade (opcional)", value=date.today())
            foto_url = st.text_input("URL da Foto (opcional)")

        if st.button("Adicionar produto"):
            novo = {
                "ID": prox_id(produtos, "ID"),
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
        for _, row in produtos.iterrows():
            with st.container():
                c = st.columns([1,2,2,2,2])
                if str(row["FotoURL"]).strip():
                    try:
                        c[0].image(row["FotoURL"], width=80)
                    except Exception:
                        c[0].write("Sem imagem")
                else:
                    c[0].write("—")
                c[1].markdown(f"**{row['Nome']}**  \nMarca: {row['Marca']}  \nCat: {row['Categoria']}")
                c[2].write(f"Estoque: {row['Quantidade']}")
                c[3].write(f"Validade: {row['Validade']}")
                col_btn = c[4]
                eid = int(row["ID"])
                if col_btn.button("✏️ Editar", key=f"edit_{eid}"):
                    st.session_state["edit_prod"] = eid
                if col_btn.button("🗑️ Excluir", key=f"del_{eid}"):
                    produtos = produtos[produtos["ID"] != str(eid)]
                    st.session_state["produtos"] = produtos
                    save_csv(produtos, ARQ_PRODUTOS)
                    st.warning(f"Produto {row['Nome']} excluído!")

        # Editor inline
        if "edit_prod" in st.session_state:
            eid = st.session_state["edit_prod"]
            row = produtos[produtos["ID"]==str(eid)]
            if not row.empty:
                st.subheader("Editar produto")
                row = row.iloc[0]
                c1,c2,c3 = st.columns(3)
                with c1:
                    novo_nome = st.text_input("Nome", value=row["Nome"])
                    nova_marca = st.text_input("Marca", value=row["Marca"])
                    nova_cat = st.text_input("Categoria", value=row["Categoria"])
                with c2:
                    nova_qtd = st.number_input("Quantidade", min_value=0, step=1, value=int(row["Quantidade"]))
                    novo_preco_custo = st.text_input("Preço de Custo", value=str(row["PrecoCusto"]).replace(".",","))
                    novo_preco_vista = st.text_input("Preço à Vista", value=str(row["PrecoVista"]).replace(".",","))
                with c3:
                    try:
                        vdata = datetime.strptime(str(row["Validade"] or date.today()), "%Y-%m-%d").date()
                    except Exception:
                        vdata = date.today()
                    nova_validade = st.date_input("Validade", value=vdata)
                    nova_foto = st.text_input("URL da Foto", value=row["FotoURL"])

                if st.button("Salvar alterações"):
                    produtos.loc[produtos["ID"]==str(eid), ["Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL"]] = [
                        novo_nome.strip(),
                        nova_marca.strip(),
                        nova_cat.strip(),
                        int(nova_qtd),
                        to_float(novo_preco_custo),
                        to_float(novo_preco_vista),
                        round(to_float(novo_preco_vista) / FATOR_CARTAO, 2) if to_float(novo_preco_vista)>0 else 0.0,
                        str(nova_validade),
                        nova_foto.strip()
                    ]
                    st.session_state["produtos"] = produtos
                    save_csv(produtos, ARQ_PRODUTOS)
                    del st.session_state["edit_prod"]
                    st.success("Produto atualizado!")

# =====================================
# VENDAS
# =====================================
# =====================================
# VENDAS
# =====================================
# Tópicos implementados nesta aba:
# 1. Seleção do produto
#    - Lista suspensa com os produtos cadastrados (ID + Nome).
# 2. Quantidade
#    - Campo numérico para escolher a quantidade.
# 3. Forma de pagamento
#    - Opções: Dinheiro, PIX, Cartão, Fiado.
#    - Se escolher Cartão, o preço unitário é recalculado.
#    - Se escolher Fiado, aparecem campos extras: Nome do cliente, Data prevista de pagamento.
# 4. Total do pedido
#    - Mostra o valor calculado automaticamente.
# 5. Registro de venda
#    - Botão Registrar venda para Dinheiro, PIX e Cartão.
#    - Botão Confirmar fiado para vendas a prazo.
#    - O estoque é atualizado automaticamente após cada venda.
# 6. Últimas vendas
#    - Tabela exibindo as vendas registradas, ordenadas por data.
# 7. Excluir venda
#    - Seletor de ID de venda.
#    - Botão Excluir venda que remove do CSV e atualiza a sessão.
if view == "Vendas":
    show_logo("main")
    st.header("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        df_sel = produtos.copy()
        df_sel["Rotulo"] = df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)
        escolha = st.selectbox("Produto", df_sel["Rotulo"].tolist())
        pid = escolha.split(" - ")[0].strip()
        rowp = df_sel[df_sel["ID"].astype(str) == pid]
        if rowp.empty:
            st.error("Produto não encontrado. Atualize a lista de produtos.")
            st.stop()
        rowp = rowp.iloc[0]
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])

        preco_unit = float(rowp["PrecoVista"])
        if forma == "Cartão":
            preco_unit = round(preco_unit / FATOR_CARTAO, 2)
        total = round(preco_unit * int(qtd), 2)

        st.info(f"💰 Total do pedido: {brl(total)}")

        if forma != "Fiado":
            if st.button("Registrar venda"):
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": str(pid),
                    "NomeProduto": rowp["Nome"],
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                # baixa no estoque
                produtos.loc[produtos["ID"]==str(pid), "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                st.session_state["vendas"] = vendas
                st.session_state["produtos"] = produtos
                save_csv(vendas, ARQ_VENDAS)
                save_csv(produtos, ARQ_PRODUTOS)
                st.success("Venda registrada!")
        else:
            st.markdown("#### Vender fiado")
            cliente_nome = st.text_input("Nome do cliente")
            data_pag = st.date_input("Data prevista de pagamento", value=date.today()+timedelta(days=7))
            if st.button("Confirmar fiado"):
                # registra também em vendas para manter histórico
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": str(pid),
                    "NomeProduto": rowp["Nome"],
                    "FormaPagamento": "Fiado",
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                save_csv(vendas, ARQ_VENDAS)

                novo_cli = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome.strip(),
                    "Produto": rowp["Nome"],
                    "Valor": float(total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_cli])], ignore_index=True)
                save_csv(clientes, ARQ_CLIENTES)

                # baixa no estoque também quando fiado
                produtos.loc[produtos["ID"]==str(pid), "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                save_csv(produtos, ARQ_PRODUTOS)

                st.session_state["vendas"] = vendas
                st.session_state["clientes"] = clientes
                st.session_state["produtos"] = produtos
                st.success("Fiado lançado para o cliente.")

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False), use_container_width=True)

    st.subheader("Excluir venda")
    if vendas.empty:
        st.info("Não há vendas para excluir.")
    else:
        id_list = vendas["IDVenda"].astype(str).tolist()
        sel = st.selectbox("Selecione a venda (ID)", id_list)
        if st.button("Excluir venda"):
            venda_sel = vendas[vendas["IDVenda"].astype(str)==str(sel)]
            if not venda_sel.empty:
                venda_sel = venda_sel.iloc[0]
                pid_sel = str(venda_sel["IDProduto"])
                qtd_sel = int(venda_sel["Quantidade"])
                # devolve estoque, se o produto ainda existir
                if pid_sel in produtos["ID"].astype(str).values:
                    produtos.loc[produtos["ID"]==pid_sel, "Quantidade"] = produtos.loc[produtos["ID"]==pid_sel, "Quantidade"].astype(int) + qtd_sel
                    save_csv(produtos, ARQ_PRODUTOS)
                # remove a venda
                vendas = vendas[vendas["IDVenda"].astype(str) != str(sel)]
                st.session_state["vendas"] = vendas
                save_csv(vendas, ARQ_VENDAS)
                st.warning(f"Venda {sel} excluída e estoque atualizado!")


# =====================================
# CLIENTES (Fiado)
# =====================================
if view == "Clientes":
    show_logo("main")
    st.header("👥 Clientes (Fiado)")
    if clientes.empty:
        st.info("Nenhum fiado lançado.")
    else:
        st.dataframe(clientes, use_container_width=True)

        st.markdown("#### Atualizar status")
        ids = clientes["ID"].astype(str).tolist()
        sel = st.selectbox("Selecione o registro", ids)
        novo_status = st.selectbox("Status", ["Aberto","Pago"])

        forma_pag = None
        if novo_status == "Pago":
            forma_pag = st.selectbox("Forma de pagamento (finalização)", ["Dinheiro","PIX","Cartão"])

        if st.button("Salvar status"):
            clientes.loc[clientes["ID"].astype(str)==str(sel), "Status"] = novo_status
            if forma_pag:
                clientes.loc[clientes["ID"].astype(str)==str(sel), "FormaPagamento"] = forma_pag
            st.session_state["clientes"] = clientes
            save_csv(clientes, ARQ_CLIENTES)
            st.success("Status atualizado!")

        st.markdown("#### Excluir registro de fiado")
        if st.button("Excluir registro selecionado"):
            clientes = clientes[clientes["ID"].astype(str)!=str(sel)]
            st.session_state["clientes"] = clientes
            save_csv(clientes, ARQ_CLIENTES)
            st.warning(f"Registro {sel} excluído!")


# =====================================
# PROMOÇÕES
# =====================================
if view == "Promoções":
    st.header("🏷️ Promoções")
    promocoes_file = "promocoes.csv"
    try:
        promocoes = pd.read_csv(promocoes_file)
    except Exception:
        promocoes = pd.DataFrame(columns=["ID","Descricao","Desconto"])
    with st.expander("Cadastrar promoção"):
        desc = st.text_input("Descrição")
        desconto = st.text_input("Desconto (%)", value="0")
        if st.button("Adicionar promoção"):
            novo = {"ID": len(promocoes)+1, "Descricao": desc, "Desconto": desconto}
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
