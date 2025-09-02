
import streamlit as st
import pandas as pd
import io, os, re, base64, requests
from datetime import datetime, date, timedelta

# ====================== Configurações ======================
st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")

# CSVs no GitHub
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"

# Pasta para fotos dentro do repositório
FOTOS_DIR = "fotos_produtos"

# Fator de ajuste para preço no cartão
FATOR_CARTAO   = 0.8872

# ====================== Integração com GitHub ======================
def _gh_conf():
    """
    Espera em st.secrets["github"] os campos:
      - token: token de acesso pessoal
      - repo: "usuario/repo"
      - user: nome do autor dos commits
      - email: email do autor dos commits
      - branch: (opcional) nome do branch, padrão 'main'
    """
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
    """
    Cria/atualiza um arquivo binário no repositório.
    """
    conf = _gh_conf()
    if not conf:
        st.warning("Configuração do GitHub ausente em st.secrets['github']. Alterações não serão persistidas.")
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
    """
    Lê um arquivo bruto do branch configurado.
    """
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
    """
    Baixa um CSV do GitHub. Se não existir, retorna DataFrame vazio com colunas garantidas.
    """
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
    ext = "jpg"
    if "." in original_name:
        ext = original_name.split(".")[-1]
    filename = _sanitize_filename(nome_produto, ext)
    path = f"{FOTOS_DIR}/{filename}"
    ok = github_put_file(path, file_bytes, f"Foto do produto {nome_produto}")
    conf = _gh_conf()
    raw_url = f"https://raw.githubusercontent.com/{conf['repo']}/{conf['branch']}/{path}" if conf else path
    return ok, raw_url, path

# ====================== Helpers de LOGO ======================
def _logo_path_or_url():
    # 1) st.secrets["brand_logo_url"]
    try:
        url = st.secrets.get("brand_logo_url", None)
    except Exception:
        url = None
    # 2) arquivo local
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

# ====================== Usuários / Login ======================
def carregar_usuarios_local():
    if os.path.exists(ARQ_USUARIOS):
        try:
            return pd.read_csv(ARQ_USUARIOS)
        except Exception:
            pass
    base = pd.DataFrame([{"usuario":"admin","senha":"admin","nivel":"admin"}])
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

    # 1) credenciais via secrets (se configuradas)
    su = None; sp = None
    try:
        su = st.secrets.get("admin_user", None)
        sp = st.secrets.get("admin_pass", None)
    except Exception:
        pass
    if su and sp and u_norm == str(su).strip().lower() and p_norm == str(sp).strip():
        return True, "admin"

    # 2) default admin/admin
    if u_norm == "admin" and p_norm == "admin":
        return True, "admin"

    # 3) checar no CSV local
    if not df.empty:
        hit = df[(df["usuario"] == u_norm) & (df["senha"] == p_norm)]
        if not hit.empty:
            return True, str(hit.iloc[0]["nivel"] or "user")

    return False, ""

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

# ====================== Estado de sessão ======================
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.nivel   = ""

# ====================== Tela de Login ======================
if not st.session_state.logado:
    logo = _logo_path_or_url()
    if logo:
        st.image(logo, width=140)
    st.title("🔐 Login")
    _ = carregar_usuarios_local()  # garante ARQ_USUARIOS local
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
if view == "Dashboard":
    # Recarrega do GitHub para garantir dados mais recentes
    produtos  = download_csv_from_github(ARQ_PRODUTOS, garantir_colunas_produtos)
    vendas    = download_csv_from_github(ARQ_VENDAS, garantir_colunas_vendas)
    clientes  = download_csv_from_github(ARQ_CLIENTES, garantir_colunas_clientes)
    promocoes = download_csv_from_github(ARQ_PROMOCOES, garantir_colunas_promocoes)
    st.session_state.produtos, st.session_state.vendas = produtos, vendas
    st.session_state.clientes, st.session_state.promocoes = clientes, promocoes

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Produtos", len(produtos))
    c2.metric("Vendas", len(vendas))
    c3.metric("Clientes (fiados)", len(clientes))
    total_vendas = float(vendas["Total"].sum()) if not vendas.empty else 0.0
    c4.metric("Faturamento", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

    st.subheader("Últimas vendas")
    # Alerta de produtos próximos do vencimento (60 dias)
    if not produtos.empty:
        hoje = date.today()
        limite = hoje + timedelta(days=60)
        produtos_tmp = produtos.copy()
        produtos_tmp["Validade_dt"] = pd.to_datetime(produtos_tmp["Validade"], errors="coerce")
        vencendo = produtos_tmp[produtos_tmp["Validade_dt"].between(pd.to_datetime(hoje), pd.to_datetime(limite))]
        if not vencendo.empty:
            st.warning(f"⚠️ {len(vencendo)} produto(s) vencendo em até 60 dias!")
            st.dataframe(vencendo[["ID","Nome","Validade"]], use_container_width=True)

    if vendas.empty:
        st.info("Sem vendas registradas ainda.")
    else:
        st.dataframe(vendas.sort_values("Data", ascending=False).head(10), use_container_width=True)

if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar novo produto"):
        c1, c2 = st.columns([2,1])
        with c1:
            nome = st.text_input("Nome")
            marca = st.text_input("Marca")
            categoria = st.text_input("Categoria")
            qtd = st.number_input("Quantidade", 0, step=1, value=0)
            custo = st.number_input("Preço de Custo", 0.0, step=0.01, value=0.0)
            vista = st.number_input("Preço à Vista", 0.0, step=0.01, value=0.0)
            cartao = round(vista / FATOR_CARTAO, 2) if FATOR_CARTAO else vista
            st.text_input("Preço no Cartão (automático)", value=str(cartao), disabled=True)
            validade = st.date_input("Validade", value=date.today())
        with c2:
            foto = st.file_uploader("Foto do produto (opcional)", type=["png","jpg","jpeg","webp"])

        if st.button("Salvar Produto"):
            foto_url, foto_path = "", ""
            if foto is not None:
                ok, url, path = upload_foto_produto_github(foto.read(), nome or foto.name, foto.name)
                if ok:
                    foto_url, foto_path = url, path
                else:
                    st.warning("Não foi possível enviar a foto ao GitHub.")
            novo = {
                "ID": prox_id(produtos, "ID"),
                "Nome": nome, "Marca": marca, "Categoria": categoria,
                "Quantidade": int(qtd),
                "PrecoCusto": float(custo),
                "PrecoVista": float(vista),
                "PrecoCartao": float(cartao),
                "Validade": str(validade),
                "FotoURL": foto_url,
                "FotoPath": foto_path
            }
            produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.produtos = produtos
            if salvar_csv_github(produtos, ARQ_PRODUTOS):
                st.success("Produto cadastrado e salvo no GitHub!")
            else:
                st.success("Produto cadastrado (não persistido por falta de configuração do GitHub).")

    st.subheader("Lista de produtos")
    st.dataframe(produtos, use_container_width=True)

    with st.expander("Excluir produto"):
        ids = produtos["ID"].tolist() if not produtos.empty else []
        id_exc = st.selectbox("ID do produto para excluir", ids) if ids else None
        if st.button("Excluir") and id_exc is not None:
            produtos = produtos[produtos["ID"] != id_exc].reset_index(drop=True)
            st.session_state.produtos = produtos
            if salvar_csv_github(produtos, ARQ_PRODUTOS):
                st.success("Produto excluído e salvo no GitHub.")
            else:
                st.success("Produto excluído (não persistido por falta de configuração do GitHub).")

if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.warning("Cadastre produtos antes de registrar vendas.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        qtd_v = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])
        idp = mapa[prod_sel]
        preco = float(produtos.loc[produtos["ID"]==idp, "PrecoVista"].iloc[0])
        if forma == "Cartão":
            preco = round(preco / FATOR_CARTAO, 2) if FATOR_CARTAO else preco
        total = preco * qtd_v
        st.info(f"Preço unitário: R$ {preco:,.2f} | Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

        cliente_nome, data_pag = None, None
        if forma == "Fiado":
            cliente_nome = st.text_input("Nome do cliente")
            data_pag = st.date_input("Data prevista de pagamento", value=date.today())

        if st.button("Registrar venda"):
            venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": idp,
                "NomeProduto": prod_sel.split(" (ID")[0],
                "FormaPagamento": forma,
                "Quantidade": int(qtd_v),
                "PrecoUnitario": float(preco),
                "Total": float(total)
            }
            vendas = pd.concat([vendas, pd.DataFrame([venda])], ignore_index=True)
            st.session_state.vendas = vendas

            # baixa do estoque
            produtos.loc[produtos["ID"]==idp, "Quantidade"] = produtos.loc[produtos["ID"]==idp, "Quantidade"].astype(int) - int(qtd_v)
            st.session_state.produtos = produtos

            # se fiado, lança nos clientes
            if forma == "Fiado" and (cliente_nome or "").strip():
                novo_fiado = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome.strip(),
                    "Produto": prod_sel.split(" (ID")[0],
                    "Valor": float(total),
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_fiado])], ignore_index=True)
                st.session_state.clientes = clientes
                salvar_csv_github(clientes, ARQ_CLIENTES)

            ok_v = salvar_csv_github(vendas, ARQ_VENDAS)
            ok_p = salvar_csv_github(produtos, ARQ_PRODUTOS)
            if ok_v and ok_p:
                st.success("Venda registrada e salva no GitHub!")
            else:
                st.success("Venda registrada (não persistida por falta de configuração do GitHub).")

    st.subheader("Histórico de vendas")
    st.dataframe(vendas.sort_values("Data", ascending=False), use_container_width=True)

    with st.expander("Excluir venda"):
        ids = vendas["IDVenda"].tolist() if not vendas.empty else []
        id_exc = st.selectbox("ID da venda para excluir", ids) if ids else None
        if st.button("Excluir venda") and id_exc is not None:
            vendas = vendas[vendas["IDVenda"] != id_exc].reset_index(drop=True)
            st.session_state.vendas = vendas
            if salvar_csv_github(vendas, ARQ_VENDAS):
                st.success("Venda excluída e salva no GitHub.")
            else:
                st.success("Venda excluída (não persistida por falta de configuração do GitHub).")

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
            if salvar_csv_github(clientes, ARQ_CLIENTES):
                st.success("Lançamento criado e salvo no GitHub.")
            else:
                st.success("Lançamento criado (não persistido por falta de configuração do GitHub).")

    st.subheader("Contas em aberto")
    st.dataframe(clientes, use_container_width=True)

    with st.expander("Baixar/Pagar conta"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None
        if st.button("Marcar como Pago") and id_sel is not None:
            clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
            st.session_state.clientes = clientes
            if salvar_csv_github(clientes, ARQ_CLIENTES):
                st.success("Lançamento atualizado e salvo no GitHub.")
            else:
                st.success("Lançamento atualizado (não persistido por falta de configuração do GitHub).")

if view == "Fluxo de Caixa":
    # recarrega do GitHub para consolidar
    vendas_cx   = download_csv_from_github(ARQ_VENDAS, garantir_colunas_vendas)
    clientes_cx = download_csv_from_github(ARQ_CLIENTES, garantir_colunas_clientes)
    st.header("💰 Fluxo de Caixa")
    total_vendas = float(vendas_cx["Total"].sum()) if not vendas_cx.empty else 0.0
    recebimentos = float(clientes_cx[clientes_cx["Status"]=="Pago"]["Valor"].sum()) if not clientes_cx.empty else 0.0
    aberto = float(clientes_cx[clientes_cx["Status"]!="Pago"]["Valor"].sum()) if not clientes_cx.empty else 0.0
    c1,c2,c3 = st.columns(3)
    c1.metric("Vendas", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    c2.metric("Recebido (fiado)", f"R$ {recebimentos:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
    c3.metric("Em aberto", f"R$ {aberto:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

if view == "Promoções":
    st.header("🏷️ Promoções")
    if produtos.empty:
        st.info("Cadastre produtos para criar promoções.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        desc = st.number_input("Desconto (%)", 0.0, 100.0, step=0.5, value=10.0)
        di = st.date_input("Início", value=date.today())
        dfim = st.date_input("Fim", value=date.today())
        if st.button("Criar promoção"):
            novo = {
                "IDPromo": prox_id(promocoes, "IDPromo"),
                "IDProduto": mapa[prod_sel],
                "NomeProduto": prod_sel.split(" (ID")[0],
                "Desconto": float(desc),
                "DataInicio": str(di),
                "DataFim": str(dfim)
            }
            promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.promocoes = promocoes
            if salvar_csv_github(promocoes, ARQ_PROMOCOES):
                st.success("Promoção criada e salva no GitHub!")
            else:
                st.success("Promoção criada (não persistida por falta de configuração do GitHub).")

    st.subheader("Promoções vigentes")
    st.dataframe(promocoes, use_container_width=True)

if view == "Segurança":
    st.header("🔒 Segurança / Usuários (local)")
    usuarios = carregar_usuarios_local()
    st.dataframe(usuarios, use_container_width=True)
    with st.expander("Adicionar usuário"):
        u_novo = st.text_input("Novo usuário")
        s_novo = st.text_input("Senha", type="password")
        nivel = st.selectbox("Nível", ["admin","user"])
        if st.button("Salvar usuário"):
            novo = pd.DataFrame([{"usuario":u_novo,"senha":s_novo,"nivel":nivel}])
            usuarios = pd.concat([usuarios, novo], ignore_index=True)
            salvar_usuarios_local(usuarios)
            st.success("Usuário criado.")
