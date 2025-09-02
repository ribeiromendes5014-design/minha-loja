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

    # 1) Checagem por secrets (se configurado)
    adm_user = None
    adm_pass = None
    try:
        adm_user = st.secrets.get("admin_user", None)
        adm_pass = st.secrets.get("admin_pass", None)
    except Exception:
        pass
    if adm_user and adm_pass:
        if u_norm == str(adm_user).strip().lower() and p_norm == str(adm_pass).strip():
            return True, "admin"

    # 2) Carrega CSV (ou cria admin/admin se não existir)
    try:
        df = pd.read_csv(ARQ_USUARIOS)
    except Exception:
        df = pd.DataFrame([{"usuario":"admin","senha":"admin","nivel":"admin"}])
        df.to_csv(ARQ_USUARIOS, index=False)

    # 3) Admin hardcoded sempre funciona
    if u_norm == "admin" and p_norm == "admin":
        return True, "admin"

    # 4) Validação linha-a-linha (evita combinar usuário de uma linha com senha de outra)
    if not df.empty and {"usuario","senha"}.issubset(df.columns):
        hit = df[(df["usuario"].astype(str).str.lower() == u_norm) & (df["senha"].astype(str) == p_norm)]
        if not hit.empty:
            nivel = str(hit.iloc[0].get("nivel", "user")) or "user"
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
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID","FotoURL"]
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

# ========= Recarregar dados sempre do GitHub =========
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

# Recarrega sempre que a view mudar (toda interação reroda o app)
recarregar_dados()

# ========= Views =========
produtos  = st.session_state.produtos
vendas    = st.session_state.vendas
clientes  = st.session_state.clientes
promocoes = st.session_state.promocoes

if view == "Dashboard":
    st.header("📊 Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Produtos", len(produtos))
    c2.metric("Vendas", len(vendas))
    c3.metric("Clientes (fiados)", len(clientes))
    total_vendas = float(vendas["Total"].sum()) if not vendas.empty else 0.0
    c4.metric("Faturamento", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

    st.subheader("Últimas vendas")
    if not vendas.empty:
        st.dataframe(vendas.sort_values("Data", ascending=False).head(10), use_container_width=True)
    else:
        st.info("Sem vendas registradas ainda.")

    if not produtos.empty:
        hoje = date.today()
        limite = hoje + timedelta(days=60)
        tmp = produtos.copy()
        tmp["Validade_dt"] = pd.to_datetime(tmp["Validade"], errors="coerce")
        vencendo = tmp[tmp["Validade_dt"].between(hoje, limite)]
        if not vencendo.empty:
            st.warning(f"⚠️ {len(vencendo)} produto(s) vencendo em até 60 dias!")
            st.dataframe(vencendo[["ID","Nome","Validade"]], use_container_width=True)

if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar novo produto"):
        nome = st.text_input("Nome")
        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        qtd = st.number_input("Quantidade", 0, step=1)
        custo = st.number_input("Preço de Custo", 0.0, step=0.01)
        vista = st.number_input("Preço à Vista", 0.0, step=0.01)
        cartao = round(vista / FATOR_CARTAO, 2) if vista else 0.0
        st.text_input("Preço no Cartão (automático)", value=str(cartao), disabled=True)
        validade = st.date_input("Validade", value=date.today())
        foto_file = st.file_uploader("Foto do produto (opcional)", type=["jpg","jpeg","png","webp"])

        if st.button("Salvar Produto"):
            novo = {
                "ID": prox_id(produtos, "ID"),
                "Nome": nome, "Marca": marca, "Categoria": categoria,
                "Quantidade": int(qtd),
                "PrecoCusto": float(custo or 0.0),
                "PrecoVista": float(vista or 0.0),
                "PrecoCartao": float(cartao or 0.0),
                "Validade": str(validade),
                "FotoID": "",
                "FotoURL": ""
            }
            produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)

            if foto_file is not None and nome:
                file_bytes = foto_file.read()
                ok, raw_url, path_saved = upload_foto_produto_github(file_bytes, nome, foto_file.name)
                if ok:
                    produtos.loc[produtos["ID"]==novo["ID"], "FotoURL"] = raw_url
                    produtos.loc[produtos["ID"]==novo["ID"], "FotoID"] = path_saved
                    st.toast("📸 Foto enviada para o GitHub!", icon="✅")
                else:
                    st.warning("Não foi possível enviar a foto para o GitHub.")

            st.session_state.produtos = produtos
            salvar_csv_github(produtos, ARQ_PRODUTOS)
            st.success("Produto cadastrado!")

    st.dataframe(produtos, use_container_width=True)

    with st.expander("Excluir produto"):
        if not produtos.empty:
            id_exc = st.selectbox("ID do produto para excluir", produtos["ID"])
            if st.button("Excluir"):
                produtos = produtos[produtos["ID"]!=id_exc].reset_index(drop=True)
                st.session_state.produtos = produtos
                salvar_csv_github(produtos, ARQ_PRODUTOS)
                st.success("Produto excluído.")

if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.warning("Cadastre produtos antes de registrar vendas.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        qtd = st.number_input("Quantidade", 1, step=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão","Fiado"])
        idp = mapa[prod_sel]
        preco = float(produtos.loc[produtos["ID"]==idp,"PrecoVista"].iloc[0])
        if forma == "Cartão":
            preco = round(preco / FATOR_CARTAO, 2)
        total = preco * qtd
        st.info(f"Preço unitário: R$ {preco:,.2f} | Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

        cliente_nome, data_pag = (st.text_input("Nome do cliente"), st.date_input("Data prevista de pagamento", value=date.today())) if forma=="Fiado" else (None, None)

        if st.button("Registrar venda"):
            venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": idp,
                "NomeProduto": prod_sel.split(" (ID")[0],
                "FormaPagamento": forma,
                "Quantidade": int(qtd),
                "PrecoUnitario": preco,
                "Total": total
            }
            vendas = pd.concat([vendas, pd.DataFrame([venda])], ignore_index=True)
            produtos.loc[produtos["ID"]==idp, "Quantidade"] -= int(qtd)

            if forma == "Fiado" and cliente_nome:
                fiado = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": cliente_nome,
                    "Produto": prod_sel.split(" (ID")[0],
                    "Valor": total,
                    "DataPagamento": str(data_pag),
                    "Status": "Aberto"
                }
                clientes = pd.concat([clientes, pd.DataFrame([fiado])], ignore_index=True)
                st.session_state.clientes = clientes
                salvar_csv_github(clientes, ARQ_CLIENTES)

            st.session_state.vendas = vendas
            st.session_state.produtos = produtos
            salvar_csv_github(vendas, ARQ_VENDAS)
            salvar_csv_github(produtos, ARQ_PRODUTOS)
            st.success("Venda registrada!")

    st.dataframe(vendas, use_container_width=True)

    with st.expander("Excluir venda"):
        if not vendas.empty:
            id_exc = st.selectbox("ID da venda para excluir", vendas["IDVenda"])
            if st.button("Excluir venda"):
                vendas = vendas[vendas["IDVenda"]!=id_exc].reset_index(drop=True)
                st.session_state.vendas = vendas
                salvar_csv_github(vendas, ARQ_VENDAS)
                st.success("Venda excluída.")

if view == "Clientes":
    st.header("👥 Clientes / Fiado")
    with st.expander("Lançar novo fiado"):
        cliente = st.text_input("Cliente")
        produto = st.text_input("Produto")
        valor = st.number_input("Valor", 0.0, step=0.01)
        data_pag = st.date_input("Data prevista de pagamento", value=date.today())
        if st.button("Lançar"):
            novo = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": cliente,
                "Produto": produto,
                "Valor": valor,
                "DataPagamento": str(data_pag),
                "Status": "Aberto"
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.clientes = clientes
            salvar_csv_github(clientes, ARQ_CLIENTES)
            st.success("Fiado lançado!")

    st.dataframe(clientes, use_container_width=True)

    with st.expander("Gerenciar fiados"):
        if not clientes.empty:
            id_sel = st.selectbox("ID do fiado", clientes["ID"])
            if st.button("Marcar como pago"):
                clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
                st.session_state.clientes = clientes
                salvar_csv_github(clientes, ARQ_CLIENTES)
                st.success("Fiado atualizado.")

if view == "Fluxo de Caixa":
    st.header("💰 Fluxo de Caixa")
    if vendas.empty:
        st.info("Nenhuma venda registrada.")
    else:
        total = vendas["Total"].sum()
        st.metric("Faturamento Total", f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
        st.dataframe(vendas, use_container_width=True)

if view == "Promoções":
    st.header("🏷️ Promoções")
    with st.expander("Cadastrar promoção"):
        if not produtos.empty:
            mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
            prod_sel = st.selectbox("Produto", list(mapa.keys()))
            desconto = st.number_input("Desconto (%)", 0.0, 100.0, step=0.1)
            di = st.date_input("Início", value=date.today())
            dfim = st.date_input("Fim", value=date.today()+timedelta(days=7))
            if st.button("Salvar promoção"):
                novo = {
                    "IDPromo": prox_id(promocoes, "IDPromo"),
                    "IDProduto": mapa[prod_sel],
                    "NomeProduto": prod_sel.split(" (ID")[0],
                    "Desconto": desconto,
                    "DataInicio": str(di),
                    "DataFim": str(dfim)
                }
                promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
                st.session_state.promocoes = promocoes
                salvar_csv_github(promocoes, ARQ_PROMOCOES)
                st.success("Promoção cadastrada!")
    st.dataframe(promocoes, use_container_width=True)

if view == "Segurança":
    st.header("🔒 Segurança")
    st.info("Aqui você pode gerenciar usuários (em desenvolvimento).")
