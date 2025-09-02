import streamlit as st
import pandas as pd
import io, os
from datetime import date, timedelta
import requests, base64, re

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")
FOLDER_FOTOS = "1Zhb6lZVOUST2WR08C9SYIYAS1q0BwF6k"
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"
FATOR_CARTAO   = 0.8872

# ====================== GitHub (CSVs e fotos) ======================
def _gh_conf():
    try:
        gh = st.secrets["github"]
        token = gh.get("token")
        repo  = gh.get("repo")
        user  = gh.get("user")
        email = gh.get("email")
        if not all([token, repo, user, email]):
            return None
        return {"token":token, "repo":repo, "user":user, "email":email, "branch":"main"}
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
        return False
    token, repo, branch = conf["token"], conf["repo"], conf["branch"]
    sha = _gh_file_sha(repo, path, branch, token)
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    b64 = base64.b64encode(content_bytes).decode("utf-8")
    data = {"message": message, "content": b64, "branch": branch}
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
    return github_put_file(filename, content, f"Atualiza {filename} via app")

def download_csv_from_github(filename, ensure_cols):
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
        base = "produto"
    if "." not in base:
        base = f"{base}.{default_ext.lower()}"
    return base

def upload_foto_produto_github(file_bytes:bytes, nome_produto:str, original_name:str):
    ext = "jpg"
    if "." in original_name:
        ext = original_name.split(".")[-1]
    filename = _sanitize_filename(nome_produto, ext)
    path = f"fotos_produtos/{filename}"
    ok = github_put_file(path, file_bytes, f"Foto do produto {nome_produto}")
    conf = _gh_conf()
    raw_url = f"https://raw.githubusercontent.com/{conf['repo']}/{conf['branch']}/{path}" if conf else path
    return ok, raw_url, path

# ========= Helpers =========
def _logo_path_or_url():
    try:
        url = st.secrets.get("brand_logo_url", None)
    except Exception:
        url = None
    for fname in ["logo.png", "logo.jpg", "logo.jpeg"]:
        if os.path.exists(fname):
            return fname
    return url

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

# ========= Sessão =========
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.nivel   = ""

# ========= Login =========
def autenticar(u, p):
    u_norm, p_norm = str(u).strip().lower(), str(p).strip()
    try:
        df = pd.read_csv(ARQ_USUARIOS)
    except Exception:
        df = pd.DataFrame([{"usuario":"admin","senha":"admin","nivel":"admin"}])
        df.to_csv(ARQ_USUARIOS, index=False)
    if (u_norm == "admin" and p_norm == "admin") or \       (u_norm in df["usuario"].str.lower().tolist() and p_norm in df["senha"].tolist()):
        nivel = "admin" if u_norm == "admin" else df.loc[df["usuario"].str.lower()==u_norm,"nivel"].iloc[0]
        return True, nivel
    return False, ""

if not st.session_state.logado:
    logo = _logo_path_or_url()
    if logo:
        st.image(logo, width=140)
    st.title("🔐 Login")
    u = st.text_input("Usuário")
    p = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        ok, nivel = autenticar(u, p)
        if ok:
            st.session_state.logado, st.session_state.usuario, st.session_state.nivel = True, u, nivel
            st.success(f"Bem-vindo, {u}!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")
    st.stop()

# ========= Dados =========
def garantir_colunas_produtos(df):
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID","FotoURL"]
    for c in cols:
        if c not in df:
            df[c] = 0 if c in ["Quantidade","PrecoCusto","PrecoVista","PrecoCartao"] else ""
    return df[cols]

def garantir_colunas_vendas(df):
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    for c in cols:
        if c not in df:
            df[c] = 0 if c in ["Quantidade","PrecoUnitario","Total"] else ""
    return df[cols]

def garantir_colunas_clientes(df):
    cols = ["ID","Cliente","Produto","Valor","DataPagamento","Status"]
    for c in cols:
        if c not in df:
            df[c] = 0.0 if c=="Valor" else ""
    return df[cols]

def garantir_colunas_promocoes(df):
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    for c in cols:
        if c not in df:
            df[c] = 0.0 if c=="Desconto" else ""
    return df[cols]

def prox_id(df, col):
    return int(pd.to_numeric(df[col], errors="coerce").max() + 1) if not df.empty else 1

def recarregar_dados():
    st.session_state.produtos  = download_csv_from_github(ARQ_PRODUTOS, garantir_colunas_produtos)
    st.session_state.vendas    = download_csv_from_github(ARQ_VENDAS, garantir_colunas_vendas)
    st.session_state.clientes  = download_csv_from_github(ARQ_CLIENTES, garantir_colunas_clientes)
    st.session_state.promocoes = download_csv_from_github(ARQ_PROMOCOES, garantir_colunas_promocoes)

recarregar_dados()

# ========= Menu =========
show_logo_places()
st.sidebar.title("📚 Menu")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Clientes","Fluxo de Caixa","Promoções","Segurança"], index=0)
st.sidebar.markdown("---")
st.sidebar.write(f"👤 Usuário: **{st.session_state.usuario}** ({st.session_state.nivel})")
if st.sidebar.button("🚪 Sair"):
    st.session_state.clear()
    st.rerun()

# ========= Views =========
# (restante do código continua igual ao fornecido na resposta anterior)
