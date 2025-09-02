
import streamlit as st
import pandas as pd
import io, os, re, base64, requests
from datetime import datetime, date, timedelta

# ====================== Configurações ======================
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")

# ======== Arquivos CSV no repositório ========
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"

# Pasta para fotos dentro do repositório
FOTOS_DIR = "fotos_produtos"

# Fator de ajuste para preço no cartão (preço no cartão = preço_vista / FATOR_CARTAO)
FATOR_CARTAO   = 0.8872

# ====================== Utilitários GitHub ======================
def _gh_conf():
    try:
        gh = st.secrets["github"]
        token = gh.get("token")
        repo  = gh.get("repo")
        user  = gh.get("user")
        email = gh.get("email")
        branch = gh.get("branch", "main")
        if not all([token, repo, user, email]):
            return None
        return {"token":token, "repo":repo, "user":user, "email":email, "branch":branch}
    except Exception:
        return None

def _gh_headers(token:str):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

def _gh_file_sha(repo:str, path:str, branch:str, token:str):
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    r = requests.get(url, headers=_gh_headers(token))
    if r.status_code == 200:
        try:
            return r.json().get("sha")
        except Exception:
            return None
    return None

def github_put_file(path:str, content_bytes:bytes, message:str):
    conf = _gh_conf()
    if not conf:
        st.warning("⚠️ st.secrets['github'] não configurado. Salvando apenas em memória.")
        return False
    token, repo, branch = conf["token"], conf["repo"], conf["branch"]
    sha = _gh_file_sha(repo, path, branch, token)
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    b64 = base64.b64encode(content_bytes).decode("utf-8")
    data = {"message": message, "content": b64, "branch": branch,
            "committer": {"name": conf["user"], "email": conf["email"]}}
    if sha:
        data["sha"] = sha
    r = requests.put(url, headers=_gh_headers(token), json=data)
    return (r.status_code in (200, 201))

def github_get_file(path:str):
    conf = _gh_conf()
    if not conf:
        return None
    url = f"https://raw.githubusercontent.com/{conf['repo']}/{conf['branch']}/{path}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.content
    return None

def salvar_csv_github(df: pd.DataFrame, filename: str):
    if df is None:
        return False
    buf = io.StringIO()
    df.to_csv(buf, index=False, encoding="utf-8-sig")
    content = buf.getvalue().encode("utf-8-sig")
    ok = github_put_file(filename, content, f"Atualiza {filename} via app")
    return ok

def download_csv_from_github(filename: str, ensure_cols):
    content = github_get_file(filename)
    if content is None:
        return ensure_cols(pd.DataFrame())
    try:
        df = pd.read_csv(io.BytesIO(content))
    except Exception:
        df = pd.DataFrame()
    return ensure_cols(df)

def _sanitize_filename(name:str, default_ext:str) -> str:
    base = re.sub(r"[^A-Za-z0-9 _.-]", "", str(name)).strip()
    base = re.sub(r"\s+", "_", base)
    if not base:
        base = "arquivo"
    if "." not in base:
        base = f"{base}.{default_ext.lower()}"
    return base

def upload_foto_produto_github(file_bytes:bytes, nome_produto:str, original_name:str):
    ext = original_name.split(".")[-1] if "." in original_name else "jpg"
    filename = _sanitize_filename(nome_produto, ext)
    path = f"{FOTOS_DIR}/{filename}"
    ok = github_put_file(path, file_bytes, f"Foto do produto {nome_produto}")
    conf = _gh_conf()
    raw_url = f"https://raw.githubusercontent.com/{conf['repo']}/{conf['branch']}/{path}" if conf else path
    return ok, raw_url, path

# ====================== Garantia de colunas ======================
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","FotoPath"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c not in ["Quantidade","PrecoCusto","PrecoVista","PrecoCartao"] else 0
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
    return df[cols]

def garantir_colunas_vendas(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c not in ["Quantidade","PrecoUnitario","Total"] else 0
    df["Quantidade"]    = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
    df["PrecoUnitario"] = pd.to_numeric(df["PrecoUnitario"], errors="coerce").fillna(0.0).astype(float)
    df["Total"]         = pd.to_numeric(df["Total"], errors="coerce").fillna(0.0).astype(float)
    return df[cols]

def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c != "Valor" else 0.0
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
    if "Status" in df.columns:
        df["Status"] = df["Status"].replace("", "Aberto")
    return df[cols]

def garantir_colunas_promocoes(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    df = df.copy() if df is not None else pd.DataFrame()
    for c in cols:
        if c not in df.columns:
            df[c] = "" if c != "Desconto" else 0.0
    df["Desconto"] = pd.to_numeric(df["Desconto"], errors="coerce").fillna(0.0).astype(float)
    return df[cols]

def prox_id(df: pd.DataFrame, col: str) -> int:
    return (int(pd.to_numeric(df[col], errors="coerce").fillna(0).max()) + 1) if not df.empty else 1

# ====================== Usuários / Login ======================
def carregar_usuarios_local():
    if os.path.exists(ARQ_USUARIOS):
        try:
            return pd.read_csv(ARQ_USUARIOS)
        except Exception:
            pass
    base = pd.DataFrame([{ "usuario":"admin", "senha":"admin", "nivel":"admin" }])
    base.to_csv(ARQ_USUARIOS, index=False)
    return base

def salvar_usuarios_local(df):
    df.to_csv(ARQ_USUARIOS, index=False)

def _load_usuarios_df():
    try:
        df = carregar_usuarios_local()
        for col in ["usuario","senha","nivel"]:
            if col not in df.columns:
                df[col] = ""
        df["usuario"] = df["usuario"].astype(str).str.strip().str.lower()
        df["senha"]   = df["senha"].astype(str).str.strip()
        df["nivel"]   = df["nivel"].astype(str).str.strip().str.lower().replace("", "user")
        return df[["usuario","senha","nivel"]]
    except Exception:
        return pd.DataFrame(columns=["usuario","senha","nivel"])

def autenticar(u, p):
    u_norm = str(u).strip().lower()
    p_norm = str(p).strip()
    df = _load_usuarios_df()
    su = None; sp = None
    try:
        su = st.secrets.get("admin_user", None)
        sp = st.secrets.get("admin_pass", None)
    except Exception:
        pass
    if su and sp and u_norm == str(su).strip().lower() and p_norm == str(sp).strip():
        return True, "admin"
    if u_norm == "admin" and p_norm == "admin":
        return True, "admin"
    if not df.empty:
        hit = df[(df["usuario"] == u_norm) & (df["senha"] == p_norm)]
        if not hit.empty:
            return True, str(hit.iloc[0]["nivel"] or "user")
    return False, ""

def _logo_path_or_url():
    try:
        url = st.secrets.get("brand_logo_url", None)
    except Exception:
        url = None
    local = None
    for fname in ["logo.png", "logo.jpg", "logo.jpeg"]:
        if os.path.exists(fname):
            local = fname
            break
    return url or local

def show_logo_places():
    logo = _logo_path_or_url()
    with st.sidebar:
        if logo:
            st.image(logo, use_column_width=True)
        if st.button("🔄 Sincronizar agora"):
            try:
                salvar_csv_github(st.session_state.produtos, ARQ_PRODUTOS)
                salvar_csv_github(st.session_state.vendas, ARQ_VENDAS)
                salvar_csv_github(st.session_state.clientes, ARQ_CLIENTES)
                salvar_csv_github(st.session_state.promocoes, ARQ_PROMOCOES)
                st.success("✅ Dados enviados ao GitHub!")
            except Exception as e:
                st.error(f"Erro ao sincronizar: {e}")

# ====================== Estado de sessão/login ======================
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.nivel   = ""

if not st.session_state.logado:
    logo = _logo_path_or_url()
    if logo:
        st.image(logo, width=140)
    st.title("🔐 Login")
    _ = carregar_usuarios_local()
    u = st.text_input("Usuário")
    p = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        ok, nivel = autenticar(u, p)
        if ok:
            st.session_state.logado = True
            st.session_state.usuario = u.strip()
            st.session_state.nivel   = nivel
            st.success(f"Bem-vindo, {st.session_state.usuario}!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")
    st.stop()

# ====================== Carregamento inicial dos CSVs ======================
if "produtos" not in st.session_state:
    st.session_state.produtos  = download_csv_from_github(ARQ_PRODUTOS, garantir_colunas_produtos)
if "vendas" not in st.session_state:
    st.session_state.vendas    = download_csv_from_github(ARQ_VENDAS, garantir_colunas_vendas)
if "clientes" not in st.session_state:
    st.session_state.clientes  = download_csv_from_github(ARQ_CLIENTES, garantir_colunas_clientes)
if "promocoes" not in st.session_state:
    st.session_state.promocoes = download_csv_from_github(ARQ_PROMOCOES, garantir_colunas_promocoes)

produtos  = st.session_state.produtos
vendas    = st.session_state.vendas
clientes  = st.session_state.clientes
promocoes = st.session_state.promocoes

# ====================== Sidebar ======================
show_logo_places()
st.sidebar.title("📚 Menu")
opcoes = ["Dashboard","Produtos","Vendas","Clientes","Fluxo de Caixa","Promoções","Segurança"]
view = st.sidebar.radio("Navegar", opcoes, index=0)

st.sidebar.markdown("---")
st.sidebar.write(f"👤 Usuário: **{st.session_state.usuario}** ({st.session_state.nivel})")
if st.sidebar.button("🚪 Sair"):
    st.session_state.clear()
    st.rerun()

# ====================== Views ======================
# ----- Dashboard -----
if view == "Dashboard":
    st.title("📊 Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    total_vendas = vendas["Total"].sum() if not vendas.empty else 0.0
    hoje = str(date.today())
    vendas_hoje = vendas[vendas["Data"] == hoje]["Total"].sum() if not vendas.empty else 0.0
    qntd_vendas = len(vendas) if not vendas.empty else 0
    em_aberto = len(clientes[clientes["Status"].astype(str).str.lower()=="aberto"]) if not clientes.empty else 0
    with col1:
        st.metric("Faturamento Total", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    with col2:
        st.metric("Vendas Hoje", f"R$ {vendas_hoje:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    with col3:
        st.metric("Qtde de Vendas", qntd_vendas)
    with col4:
        st.metric("Fiados em Aberto", em_aberto)
    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False).tail(50), use_container_width=True)

# ----- Produtos -----
if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar produto"):
        nome = st.text_input("Nome")
        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        quantidade = st.number_input("Quantidade", 0, step=1)
        preco_custo = st.number_input("Preço de custo", 0.0, step=0.01)
        preco_vista = st.number_input("Preço à vista", 0.0, step=0.01)
        preco_cartao = round(preco_vista / FATOR_CARTAO, 2) if preco_vista else 0.0
        validade = st.date_input("Validade", value=date.today())
        foto = st.file_uploader("Foto do produto", type=["png","jpg","jpeg"])
        if st.button("Salvar produto"):
            foto_url = ""; foto_path=""
            if foto is not None:
                ok, url, path = upload_foto_produto_github(foto.read(), nome, foto.name)
                if ok:
                    foto_url, foto_path = url, path
                else:
                    st.warning("Não foi possível enviar a foto ao GitHub.")
            novo = {
                "ID": prox_id(produtos, "ID"),
                "Nome": nome, "Marca": marca, "Categoria": categoria,
                "Quantidade": int(quantidade),
                "PrecoCusto": float(preco_custo),
                "PrecoVista": float(preco_vista),
                "PrecoCartao": float(preco_cartao),
                "Validade": str(validade),
                "FotoURL": foto_url, "FotoPath": foto_path
            }
            produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.produtos = produtos
            salvar_csv_github(produtos, ARQ_PRODUTOS)
            st.success("Produto cadastrado!")
    st.markdown("### Lista de produtos")
    st.dataframe(produtos, use_container_width=True)

# ----- Vendas -----
if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        df_sel = produtos.copy()
        df_sel["Rotulo"] = df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)
        escolha = st.selectbox("Produto", df_sel["Rotulo"].tolist())
        pid = int(escolha.split(" - ")[0])
        rowp = df_sel[df_sel["ID"]==pid].iloc[0]
        qtd = st.number_input("Quantidade", 1, step=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])
        if st.button("Registrar venda"):
            nome_prod = rowp["Nome"]
            preco_unit = float(rowp["PrecoVista"])
            total = preco_unit * qtd
            if forma == "Cartão":
                preco_unit = round(preco_unit / FATOR_CARTAO, 2)
                total = round(preco_unit * qtd, 2)
            if forma != "Fiado":
                nova_venda = {
                    "IDVenda": prox_id(vendas, "IDVenda"),
                    "Data": str(date.today()),
                    "IDProduto": pid,
                    "NomeProduto": nome_prod,
                    "FormaPagamento": forma,
                    "Quantidade": int(qtd),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total)
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
                st.session_state.vendas = vendas
                # baixa estoque
                produtos.loc[produtos["ID"]==pid, "Quantidade"] = int(rowp["Quantidade"]) - int(qtd)
                st.session_state.produtos = produtos
                salvar_csv_github(vendas, ARQ_VENDAS)
                salvar_csv_github(produtos, ARQ_PRODUTOS)
                st.success("Venda registrada!")
            else:
                # Fiado -> registrar em clientes (Status=Aberto)
                novo = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": st.text_input("Nome do cliente (fiado)", key="fiado_nome") or "Cliente",
                    "Produto": nome_prod,
                    "Valor": float(total),
                    "DataPagamento": str(date.today() + timedelta(days=7)),
                    "Status": "Aberto"
                }
                if st.button("Confirmar fiado"):
                    clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
                    st.session_state.clientes = clientes
                    salvar_csv_github(clientes, ARQ_CLIENTES)
                    st.success("Fiado lançado para o cliente.")

    st.markdown("### Últimas vendas")
    st.dataframe(vendas.sort_values(by="Data", ascending=False), use_container_width=True)

# ----- Clientes (Fiado) -----
if view == "Clientes":
    st.header("👥 Clientes / Fiado")

    with st.expander("Lançar novo fiado"):
        cliente = st.text_input("Cliente")
        produto_f = st.text_input("Produto")
        valor = st.number_input("Valor", 0.0, step=0.01)
        data_pag = st.date_input("Data prevista de pagamento", value=date.today())
        if st.button("Lançar"):
            novo = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": cliente, "Produto": produto_f,
                "Valor": float(valor), "DataPagamento": str(data_pag), "Status": "Aberto"
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.clientes = clientes
            salvar_csv_github(clientes, ARQ_CLIENTES)
            st.success("Lançamento criado e salvo.")

    st.subheader("Contas")
    st.dataframe(clientes, use_container_width=True)

    with st.expander("Baixar/Pagar conta"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None
        forma_pg = None
        if id_sel is not None:
            forma_pg = st.selectbox("Forma de pagamento", ["Dinheiro", "PIX", "Cartão"])
        if st.button("Marcar como Pago") and id_sel is not None:
            row = clientes.loc[clientes["ID"]==id_sel].iloc[0]
            valor_pago = float(row["Valor"])
            if forma_pg == "Cartão":
                valor_pago = round(valor_pago / FATOR_CARTAO, 2)

            # Atualiza status no clientes.csv
            clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
            st.session_state.clientes = clientes
            salvar_csv_github(clientes, ARQ_CLIENTES)

            # Lança em vendas.csv
            nova_venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": "",
                "NomeProduto": row["Produto"],
                "FormaPagamento": forma_pg,
                "Quantidade": 1,
                "PrecoUnitario": float(valor_pago),
                "Total": float(valor_pago)
            }
            vendas = pd.concat([vendas, pd.DataFrame([nova_venda])], ignore_index=True)
            st.session_state.vendas = vendas
            salvar_csv_github(vendas, ARQ_VENDAS)

            st.success(f"Lançamento pago via {forma_pg} e registrado em vendas.")

    with st.expander("Excluir dívida"):
        ids2 = clientes["ID"].tolist() if not clientes.empty else []
        id_exc = st.selectbox("ID da dívida para excluir", ids2) if ids2 else None
        if st.button("Excluir dívida") and id_exc is not None:
            prod = clientes.loc[clientes["ID"]==id_exc, "Produto"].iloc[0]
            val  = clientes.loc[clientes["ID"]==id_exc, "Valor"].iloc[0]

            # remove de clientes
            clientes = clientes[clientes["ID"] != id_exc].reset_index(drop=True)
            st.session_state.clientes = clientes
            salvar_csv_github(clientes, ARQ_CLIENTES)

            # remove também de vendas (se houver correspondência simples)
            vendas = vendas[~((vendas["NomeProduto"]==prod) & (vendas["Total"]==val))].reset_index(drop=True)
            st.session_state.vendas = vendas
            salvar_csv_github(vendas, ARQ_VENDAS)

            st.success("Dívida excluída de clientes e vendas.")

# ----- Fluxo de Caixa -----
if view == "Fluxo de Caixa":
    st.header("💰 Fluxo de Caixa")
    if vendas.empty:
        st.info("Sem vendas registradas.")
    else:
        vendas["Data"] = vendas["Data"].astype(str)
        df = vendas.groupby(["Data","FormaPagamento"], as_index=False)["Total"].sum()
        st.dataframe(df, use_container_width=True)
        dia = st.date_input("Filtrar por dia", value=date.today())
        d_str = str(dia)
        filtro = vendas[vendas["Data"]==d_str]
        st.markdown(f"### Total do dia {d_str}")
        st.write(f"R$ {filtro['Total'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
        st.dataframe(filtro, use_container_width=True)

# ----- Promoções -----
if view == "Promoções":
    st.header("🏷️ Promoções")
    if produtos.empty:
        st.info("Cadastre produtos primeiro.")
    else:
        dfp = produtos.copy()
        dfp["Rotulo"] = dfp["ID"].astype(str) + " - " + dfp["Nome"].astype(str)
        escolha = st.selectbox("Produto", dfp["Rotulo"].tolist())
        pid = int(escolha.split(" - ")[0])
        nomep = dfp[dfp["ID"]==pid]["Nome"].iloc[0]
        desconto = st.slider("Desconto (%)", 0, 90, 10, step=1)
        di = st.date_input("Início", value=date.today())
        df = st.date_input("Fim", value=date.today() + timedelta(days=7))
        if st.button("Criar/Atualizar promoção"):
            novo = {
                "IDPromo": prox_id(promocoes, "IDPromo"),
                "IDProduto": pid,
                "NomeProduto": nomep,
                "Desconto": float(desconto),
                "DataInicio": str(di),
                "DataFim": str(df)
            }
            promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.promocoes = promocoes
            salvar_csv_github(promocoes, ARQ_PROMOCOES)
            st.success("Promoção salva.")
    st.dataframe(promocoes, use_container_width=True)

# ----- Segurança -----
if view == "Segurança":
    st.header("🔒 Segurança / Usuários")
    usuarios = _load_usuarios_df()
    st.write("Usuários locais (arquivo usuarios.csv)")
    st.dataframe(usuarios, use_container_width=True)
    with st.expander("Adicionar usuário"):
        u = st.text_input("Usuário (minúsculas)")
        s = st.text_input("Senha", type="password")
        nivel = st.selectbox("Nível", ["user","admin"])
        if st.button("Salvar usuário"):
            usuarios = pd.concat([usuarios, pd.DataFrame([{"usuario":u.strip().lower(),"senha":s,"nivel":nivel}])], ignore_index=True)
            salvar_usuarios_local(usuarios)
            st.success("Usuário adicionado.")
