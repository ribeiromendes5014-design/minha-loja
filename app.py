
import streamlit as st
import pandas as pd
import io, os
from datetime import datetime, date

st.set_page_config(page_title="Minha Loja - Cosméticos", layout="wide")
FOLDER_FOTOS = "1Eokm87paPB7Ber4hwCqPuMkgFKHePmQq"
ARQ_PRODUTOS   = "produtos.csv"
ARQ_VENDAS     = "vendas.csv"
ARQ_CLIENTES   = "clientes.csv"
ARQ_PROMOCOES  = "promocoes.csv"
ARQ_USUARIOS   = "usuarios.csv"
FATOR_CARTAO   = 0.8872

GOOGLE_OK = True
try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
    from google.oauth2 import service_account
except Exception:
    GOOGLE_OK = False

def get_drive_service():
    if not GOOGLE_OK:
        raise RuntimeError("Bibliotecas do Google não disponíveis no ambiente.")
    creds = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)

def _drive_find_file(service, filename):
    results = service.files().list(
        q=f"name='{filename}' and '{FOLDER_FOTOS}' in parents",
        fields="files(id, name)", pageSize=1
    ).execute()
    items = results.get("files", [])
    return items[0]["id"] if items else None

def download_csv_from_drive(filename, ensure_cols):
    # Baixa CSV do Drive. Se não existir, devolve DF vazio com colunas garantidas.
    # NÃO grava nada no Drive aqui, só leitura.
    if not GOOGLE_OK:
        return ensure_cols(pd.DataFrame())
    try:
        service = get_drive_service()
        file_id = _drive_find_file(service, filename)
        if not file_id:
            return ensure_cols(pd.DataFrame())
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        fh.seek(0)
        try:
            df = pd.read_csv(fh)
        except Exception:
            df = pd.DataFrame()
        return ensure_cols(df)
    except Exception:
        return ensure_cols(pd.DataFrame())

def upload_csv_to_drive(df, filename):
    # Substitui o CSV no Drive apenas se houver dados ou ao menos as colunas corretas.
    if not GOOGLE_OK:
        return
    try:
        if df is None or (df.empty and len(df.columns) == 0):
            return
        service = get_drive_service()
        file_id = _drive_find_file(service, filename)
        if file_id:
            service.files().delete(fileId=file_id).execute()
        tmp = f"_tmp_{filename}"
        df.to_csv(tmp, index=False)
        media = MediaFileUpload(tmp, mimetype="text/csv")
        metadata = {"name": filename, "parents": [FOLDER_FOTOS]}
        service.files().create(body=metadata, media_body=media, fields="id").execute()
        os.remove(tmp)
    except Exception as e:
        st.warning(f"Não foi possível enviar {filename} ao Drive: {e}")

def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoID"]
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

if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.nivel   = ""

if not st.session_state.logado:
    st.title("🔐 Login")
    usuarios_df = carregar_usuarios_local()
    u = st.text_input("Usuário")
    p = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        row = usuarios_df[(usuarios_df["usuario"]==u) & (usuarios_df["senha"]==p)]
        if not row.empty:
            st.session_state.logado = True
            st.session_state.usuario = u
            st.session_state.nivel   = row.iloc[0]["nivel"]
            st.success(f"Bem-vindo, {u}!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos")
    st.stop()

if "produtos" not in st.session_state:
    st.session_state.produtos  = download_csv_from_drive(ARQ_PRODUTOS, garantir_colunas_produtos)
if "vendas" not in st.session_state:
    st.session_state.vendas    = download_csv_from_drive(ARQ_VENDAS, garantir_colunas_vendas)
if "clientes" not in st.session_state:
    st.session_state.clientes  = download_csv_from_drive(ARQ_CLIENTES, garantir_colunas_clientes)
if "promocoes" not in st.session_state:
    st.session_state.promocoes = download_csv_from_drive(ARQ_PROMOCOES, garantir_colunas_promocoes)

produtos  = st.session_state.produtos
vendas    = st.session_state.vendas
clientes  = st.session_state.clientes
promocoes = st.session_state.promocoes

st.sidebar.title("📚 Menu")
opcoes = ["Dashboard","Produtos","Vendas","Clientes","Fluxo de Caixa","Promoções","Segurança"]
view = st.sidebar.radio("Navegar", opcoes, index=0)

st.sidebar.markdown("---")
st.sidebar.write(f"👤 Usuário: **{st.session_state.usuario}** ({st.session_state.nivel})")
if st.sidebar.button("🚪 Sair"):
    st.session_state.clear()
    st.experimental_rerun()

if view == "Dashboard":
    produtos  = download_csv_from_drive(ARQ_PRODUTOS, garantir_colunas_produtos)
    vendas    = download_csv_from_drive(ARQ_VENDAS, garantir_colunas_vendas)
    clientes  = download_csv_from_drive(ARQ_CLIENTES, garantir_colunas_clientes)
    promocoes = download_csv_from_drive(ARQ_PROMOCOES, garantir_colunas_promocoes)
    st.session_state.produtos, st.session_state.vendas = produtos, vendas
    st.session_state.clientes, st.session_state.promocoes = clientes, promocoes

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Produtos", len(produtos))
    c2.metric("Vendas", len(vendas))
    c3.metric("Clientes (fiados)", len(clientes))
    total_vendas = float(vendas["Total"].sum()) if not vendas.empty else 0.0
    c4.metric("Faturamento", f"R$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))

    st.subheader("Últimas vendas")
    if vendas.empty:
        st.info("Sem vendas registradas ainda.")
    else:
        st.dataframe(vendas.sort_values("Data", ascending=False).head(10), use_container_width=True)

if view == "Produtos":
    st.header("📦 Produtos")
    with st.expander("Cadastrar novo produto"):
        nome = st.text_input("Nome")
        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        qtd = st.number_input("Quantidade", 0, step=1)
        custo = st.number_input("Preço de Custo", 0.0, step=0.01)
        vista = st.number_input("Preço à Vista", 0.0, step=0.01)
        cartao = st.number_input("Preço no Cartão", 0.0, step=0.01)
        validade = st.date_input("Validade", value=date.today())
        if st.button("Salvar Produto"):
            novo = {
                "ID": prox_id(produtos, "ID"),
                "Nome": nome, "Marca": marca, "Categoria": categoria,
                "Quantidade": int(qtd),
                "PrecoCusto": float(custo),
                "PrecoVista": float(vista),
                "PrecoCartao": float(cartao),
                "Validade": str(validade),
                "FotoID": ""
            }
            produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.produtos = produtos
            upload_csv_to_drive(produtos, ARQ_PRODUTOS)
            st.success("Produto cadastrado!")

    st.subheader("Lista de produtos")
    st.dataframe(produtos, use_container_width=True)

    with st.expander("Excluir produto"):
        ids = produtos["ID"].tolist() if not produtos.empty else []
        id_exc = st.selectbox("ID do produto para excluir", ids) if ids else None
        if st.button("Excluir") and id_exc is not None:
            produtos = produtos[produtos["ID"] != id_exc].reset_index(drop=True)
            st.session_state.produtos = produtos
            upload_csv_to_drive(produtos, ARQ_PRODUTOS)
            st.success("Produto excluído.")

if view == "Vendas":
    st.header("🧾 Vendas")
    if produtos.empty:
        st.warning("Cadastre produtos antes de registrar vendas.")
    else:
        mapa = {f"{row.Nome} (ID {row.ID})": row.ID for _, row in produtos.iterrows()}
        prod_sel = st.selectbox("Produto", list(mapa.keys()))
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
        forma = st.selectbox("Forma de pagamento", ["Dinheiro","PIX","Cartão"])
        idp = mapa[prod_sel]
        preco = float(produtos.loc[produtos["ID"]==idp, "PrecoVista"].iloc[0])
        if forma == "Cartão":
            preco = round(preco / FATOR_CARTAO, 2)
        total = preco * qtd
        st.info(f"Preço unitário: R$ {preco:,.2f} | Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X","."))
        if st.button("Registrar venda"):
            venda = {
                "IDVenda": prox_id(vendas, "IDVenda"),
                "Data": str(date.today()),
                "IDProduto": idp,
                "NomeProduto": prod_sel.split(" (ID")[0],
                "FormaPagamento": forma,
                "Quantidade": int(qtd),
                "PrecoUnitario": float(preco),
                "Total": float(total)
            }
            vendas = pd.concat([vendas, pd.DataFrame([venda])], ignore_index=True)
            st.session_state.vendas = vendas
            produtos.loc[produtos["ID"]==idp, "Quantidade"] = produtos.loc[produtos["ID"]==idp, "Quantidade"].astype(int) - int(qtd)
            st.session_state.produtos = produtos
            upload_csv_to_drive(vendas, ARQ_VENDAS)
            upload_csv_to_drive(produtos, ARQ_PRODUTOS)
            st.success("Venda registrada!")

    st.subheader("Histórico de vendas")
    st.dataframe(vendas.sort_values("Data", ascending=False), use_container_width=True)

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
                "Cliente": cliente, "Produto": produto,
                "Valor": float(valor), "DataPagamento": str(data_pag), "Status": "Aberto"
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.clientes = clientes
            upload_csv_to_drive(clientes, ARQ_CLIENTES)
            st.success("Lançamento criado.")

    st.subheader("Contas em aberto")
    st.dataframe(clientes, use_container_width=True)

    with st.expander("Baixar/Pagar conta"):
        ids = clientes["ID"].tolist() if not clientes.empty else []
        id_sel = st.selectbox("ID do lançamento", ids) if ids else None
        if st.button("Marcar como Pago") and id_sel is not None:
            clientes.loc[clientes["ID"]==id_sel, "Status"] = "Pago"
            st.session_state.clientes = clientes
            upload_csv_to_drive(clientes, ARQ_CLIENTES)
            st.success("Lançamento atualizado.")

if view == "Fluxo de Caixa":
    vendas   = download_csv_from_drive(ARQ_VENDAS, garantir_colunas_vendas)
    clientes = download_csv_from_drive(ARQ_CLIENTES, garantir_colunas_clientes)
    st.header("💰 Fluxo de Caixa")
    total_vendas = float(vendas["Total"].sum()) if not vendas.empty else 0.0
    recebimentos = float(clientes[clientes["Status"]=="Pago"]["Valor"].sum()) if not clientes.empty else 0.0
    aberto = float(clientes[clientes["Status"]!="Pago"]["Valor"].sum()) if not clientes.empty else 0.0
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
        df = st.date_input("Fim", value=date.today())
        if st.button("Criar promoção"):
            novo = {
                "IDPromo": prox_id(promocoes, "IDPromo"),
                "IDProduto": mapa[prod_sel],
                "NomeProduto": prod_sel.split(" (ID")[0],
                "Desconto": float(desc),
                "DataInicio": str(di),
                "DataFim": str(df)
            }
            promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state.promocoes = promocoes
            upload_csv_to_drive(promocoes, ARQ_PROMOCOES)
            st.success("Promoção criada!")

    st.subheader("Promoções vigentes")
    st.dataframe(promocoes, use_container_width=True)

if view == "Segurança":
    st.header("🔒 Segurança / Usuários (local)")
    usuarios = carregar_usuarios_local()
    st.dataframe(usuarios, use_container_width=True)
    with st.expander("Adicionar usuário"):
        u = st.text_input("Novo usuário")
        s = st.text_input("Senha", type="password")
        nivel = st.selectbox("Nível", ["admin","user"])
        if st.button("Salvar usuário"):
            novo = pd.DataFrame([{"usuario":u,"senha":s,"nivel":nivel}])
            usuarios = pd.concat([usuarios, novo], ignore_index=True)
            salvar_usuarios_local(usuarios)
            st.success("Usuário criado.")
