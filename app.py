
import streamlit as st
import pandas as pd
import os
from datetime import date, datetime, timedelta
from PIL import Image, ImageEnhance
from io import BytesIO
import requests  


# =====================================
# Funções auxiliares
# =====================================

def ler_codigo_barras_api(image_bytes):
    try:
        files = {"f": ("barcode.png", image_bytes, "image/png")}
        response = requests.post("https://zxing.org/w/decode", files=files)

        if response.status_code != 200:
            st.error(f"Erro na API ZXing: {response.status_code}")
            return []

        # A resposta é HTML, então fazemos um parse simples
        text = response.text
        codigos = []

        # Os códigos geralmente aparecem entre <pre>...</pre>
        if "<pre>" in text:
            partes = text.split("<pre>")
            for p in partes[1:]:
                codigo = p.split("</pre>")[0].strip()
                codigos.append(codigo)

        st.write("Debug API ZXing:", codigos)
        return codigos

    except Exception as e:
        st.error(f"Erro ao chamar API ZXing: {e}")
        return []




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
ARQ_CAIXAS = "caixas.csv"
ARQ_PRECIFICACAO = "precificacao.csv"


FATOR_CARTAO  = 0.8872  # preco_cartao = preco_vista / FATOR_CARTAO
ESTOQUE_MINIMO_PADRAO = 5

# Pasta para salvar as fotos dos produtos
FOTOS_DIR = "foto_produtos"
os.makedirs(FOTOS_DIR, exist_ok=True)

# =====================================
# Salvar CSV no GitHub (genérico)
# =====================================
def save_csv_github(df: pd.DataFrame, path="produtos.csv", mensagem="Atualizando CSV"):
    """Salva DataFrame CSV localmente e no GitHub."""
    # Sempre salva local
    df.to_csv(path, index=False)

    try:
        gh = st.secrets["github"]
        token = gh["token"]
        repo_name = gh["repo"]

        g = Github(token)
        repo = g.get_repo(repo_name)
        branch = repo.default_branch  # ✅ agora usa branch padrão automaticamente

        content = df.to_csv(index=False)

        try:
            contents = repo.get_contents(path, ref=branch)
            repo.update_file(contents.path, mensagem, content, contents.sha, branch=branch)
            st.info(f"✅ CSV atualizado no GitHub ({path}, branch {branch})")
        except Exception:
            repo.create_file(path, mensagem, content, branch=branch)
            st.info(f"✅ CSV criado no GitHub ({path}, branch {branch})")

    except Exception as e:
        st.error(f"❌ Erro ao salvar no GitHub: {e}")


# =====================================
# FUNÇÃO PDF - RELATÓRIO PRODUTOS MAIS VENDIDOS
# =====================================
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gerar_pdf_produtos_vendidos(df, caminho_pdf, data_inicio, data_fim):
    doc = SimpleDocTemplate(caminho_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Cabeçalho
    titulo = f"Relatório de Produtos Mais Vendidos ({data_inicio} a {data_fim})"
    elementos.append(Paragraph(titulo, styles["Title"]))
    elementos.append(Spacer(1, 20))

    # Montar tabela
    data = [["ID Produto", "Nome Produto", "Quantidade Vendida"]]
    for _, row in df.iterrows():
        data.append([str(row["IDProduto"]), str(row["NomeProduto"]), int(row["Quantidade"])])

    tabela = Table(data, colWidths=[80, 300, 120])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ]))

    elementos.append(tabela)
    doc.build(elementos)



# =====================================
# Relatório PDF de Caixa
# =====================================
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gerar_pdf_caixa(dados_caixa: dict, vendas_dia: pd.DataFrame, path: str):
    """Gera um relatório PDF de fechamento de caixa incluindo produtos vendidos"""
    doc = SimpleDocTemplate(path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # --- Cabeçalho
    story.append(Paragraph("Relatório de Fechamento de Caixa", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Data: {dados_caixa['Data']}", styles["Heading2"]))
    story.append(Spacer(1, 12))

    # --- Resumo Financeiro
    tabela = [
        ["Faturamento Total", f"R$ {dados_caixa['FaturamentoTotal']:.2f}"],
        ["Dinheiro", f"R$ {dados_caixa['Dinheiro']:.2f}"],
        ["PIX", f"R$ {dados_caixa['PIX']:.2f}"],
        ["Cartão", f"R$ {dados_caixa['Cartão']:.2f}"],
        ["Fiado", f"R$ {dados_caixa['Fiado']:.2f}"],
        ["Status", dados_caixa['Status']],
    ]
    t = Table(tabela, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))

    # --- Produtos vendidos no dia
    if vendas_dia is not None and not vendas_dia.empty:
        story.append(Paragraph("Produtos Vendidos", styles["Heading2"]))
        story.append(Spacer(1, 10))

        tabela_prod = [["Produto", "Qtd", "Preço Unit.", "Total"]]
        for _, row in vendas_dia.iterrows():
            tabela_prod.append([
                row["NomeProduto"],
                str(int(row["Quantidade"])),
                f"R$ {row['PrecoUnitario']:.2f}",
                f"R$ {row['Total']:.2f}"
            ])

        tp = Table(tabela_prod, hAlign="LEFT", colWidths=[200, 50, 80, 80])
        tp.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        story.append(tp)

    doc.build(story)


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus import Image as RLImage  # <- renomeado para não conflitar com Pillow
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from datetime import datetime

def gerar_pdf_venda(venda_id: int, vendas: pd.DataFrame, path: str):
    """Gera um PDF estilo cupom com fundo amarelo claro"""
    # 📐 Tamanho tipo recibo (80mm x 200mm)
    page_size = (80*mm, 200*mm)

    # Função para desenhar o fundo antes do conteúdo
    def draw_background(canvas, doc):
        canvas.setFillColor(HexColor("#FFF9C4"))  # amarelo claro
        canvas.rect(0, 0, page_size[0], page_size[1], fill=True, stroke=False)

    doc = SimpleDocTemplate(path, pagesize=page_size,
                            rightMargin=10, leftMargin=10,
                            topMargin=10, bottomMargin=10)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="NormalCenter", fontSize=9, alignment=1))
    styles.add(ParagraphStyle(name="BoldCenter", fontSize=10, alignment=1, spaceAfter=6))
    styles.add(ParagraphStyle(name="BoldLeft", fontSize=10, alignment=0, spaceAfter=6))
    styles.add(ParagraphStyle(name="Total", fontSize=12, alignment=1, spaceBefore=6, spaceAfter=6, leading=14))

    story = []

    # --- Logo fixa ---
    try:
        story.append(RLImage("logo_docebella.png", width=55*mm, height=25*mm))
    except Exception:
        story.append(Paragraph("Doce&Bella Cosmético", styles["BoldCenter"]))

    story.append(Spacer(1, 6))
    story.append(Paragraph("📞 (41) 99168-6525", styles["NormalCenter"]))
    story.append(Paragraph("📷 @docebellacosmetico", styles["NormalCenter"]))
    story.append(Spacer(1, 10))

    # --- Seleciona venda ---
    venda_sel = vendas[vendas["IDVenda"].astype(int) == int(venda_id)]
    if venda_sel.empty:
        story.append(Paragraph("Venda não encontrada.", styles["NormalCenter"]))
        doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)
        return

    venda_info = venda_sel.iloc[0]
    story.append(Paragraph(f"<b>Data:</b> {venda_info['Data']}", styles["BoldLeft"]))
    story.append(Paragraph(f"<b>Forma de Pagamento:</b> {venda_info['FormaPagamento']}", styles["BoldLeft"]))
    story.append(Spacer(1, 10))

    # --- Produtos ---
    tabela = [["Produto", "Qtd", "Preço Unit.", "Total"]]
    for _, row in venda_sel.iterrows():
        tabela.append([
            str(row["NomeProduto"]),
            str(int(row["Quantidade"])),
            f"R$ {float(row['PrecoUnitario']):.2f}",
            f"R$ {float(row['Total']):.2f}",
        ])

    t = Table(tabela, colWidths=[80*mm*0.4, 80*mm*0.15, 80*mm*0.2, 80*mm*0.25])
    t.setStyle(TableStyle([
        ("LINEABOVE", (0, 0), (-1, 0), 0.5, colors.black),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.black),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
    ]))
    story.append(t)

    # --- Total ---
    valor_total = venda_sel["Total"].sum()
    story.append(Spacer(1, 6))
    story.append(Table(
        [["", f"Valor Total: R$ {valor_total:.2f}"]],
        colWidths=[80*mm*0.4, 80*mm*0.6],
        style=[
            ("LINEABOVE", (0, 0), (-1, 0), 0.5, colors.black),
            ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.black),
            ("FONTNAME", (1, 0), (1, 0), "Helvetica-Bold"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
        ]
    ))
    story.append(Spacer(1, 10))

    # --- Mensagem final ---
    story.append(Paragraph("Obrigado pela sua compra,<br/>volte sempre!", styles["NormalCenter"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), styles["NormalCenter"]))

    # gera PDF com fundo amarelo
    doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)




# =====================================
# Leitura de Código de Barras (API ZXing)
# =====================================
import requests

def ler_codigo_barras_api(image_bytes):
    try:
        files = {"f": ("barcode.png", image_bytes, "image/png")}
        response = requests.post("https://zxing.org/w/decode", files=files)

        if response.status_code != 200:
            st.error(f"Erro na API ZXing: {response.status_code}")
            return []

        text = response.text
        codigos = []
        if "<pre>" in text:
            partes = text.split("<pre>")
            for p in partes[1:]:
                codigo = p.split("</pre>")[0].strip()
                codigos.append(codigo)

        st.write("Debug API ZXing:", codigos)
        return codigos

    except Exception as e:
        st.error(f"Erro ao chamar API ZXing: {e}")
        return []



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
    # Ordenar colunas
    df = df[columns]
    return df

def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

# =====================================
# Salvar no GitHub
# =====================================
def save_csv_github(df: pd.DataFrame, path: str, mensagem: str):
    try:
        gh = st.secrets["github"]
        token = gh["token"]
        repo_name = gh["repo"]

        g = Github(token)
        repo = g.get_repo(repo_name)
        branch = repo.default_branch

        # Ler arquivo atual (se existir)
        try:
            contents = repo.get_contents(path, ref=branch)
            sha = contents.sha
        except Exception:
            sha = None

        from io import StringIO
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        repo.update_file(
            path,
            mensagem,
            csv_buffer.getvalue(),
            sha if sha else None,
            branch=branch,
        )
    except Exception as e:
        st.error(f"❌ Erro ao salvar no GitHub: {e}")

# =====================================
# Carregar do GitHub (usando token/secret - privado)
# =====================================
def load_csv_github(path: str) -> pd.DataFrame | None:
    """Carrega CSV do GitHub (se existir)."""
    try:
        gh = st.secrets["github"]
        token = gh["token"]
        repo_name = gh["repo"]

        g = Github(token)
        repo = g.get_repo(repo_name)
        branch = repo.default_branch

        contents = repo.get_contents(path, ref=branch)
        import io
        return pd.read_csv(io.StringIO(contents.decoded_content.decode()), dtype=str)
    except Exception:
        return None


# =====================================
# Carregar CSV direto de URL (raw GitHub - público)
# =====================================
def load_csv_from_url(url: str) -> pd.DataFrame:
    """Carrega CSV diretamente de uma URL raw do GitHub."""
    try:
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"❌ Erro ao carregar CSV do GitHub (URL): {e}")
        return pd.DataFrame()

        

# =====================================
# Usuários e Login
# =====================================
def norm_usuarios(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["Usuario","Senha"]

    # tenta carregar do GitHub primeiro
    df = load_csv_github(ARQ_USUARIOS)
    if df is None:
        df = ensure_csv(ARQ_USUARIOS, cols)

    # Se vazio, cria admin padrão
    if df.empty:
        df = pd.DataFrame([{"Usuario":"admin","Senha":"123"}])
        save_csv_github(df, ARQ_USUARIOS, "Criando admin inicial")

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
    save_csv_github(df, ARQ_USUARIOS, "Resetando admin")
    return True

def do_login(usuarios: pd.DataFrame) -> bool:
    st.subheader("Login")

    user = st.text_input("Usuário")
    pwd = st.text_input("Senha", type="password")

    manter = st.checkbox("Manter conectado", value=False)

    if st.button("Entrar"):
        if ((usuarios["Usuario"] == user) & (usuarios["Senha"] == pwd)).any():
            st.session_state["logado"] = True
            st.session_state["usuario"] = user
            st.session_state["manter"] = manter   # <<< salva preferencia
            st.success(f"Bem-vindo, {user}!")
            return True
        else:
            st.error("Usuário ou senha inválidos.")
            return False

    # Se já está logado e marcou "manter conectado", mantém ativo
    if st.session_state.get("logado", False) and st.session_state.get("manter", False):
        return True

    return False

# =====================================
# Salvar CSV no GitHub (somente produtos)
# =====================================
from github import Github

def save_csv_github(df: pd.DataFrame, path="produtos.csv", mensagem="Atualizando produtos"):
    """Salva DataFrame CSV no GitHub e também localmente (backup)."""
    # Sempre salva local
    df.to_csv(path, index=False)

    try:
        gh = st.secrets["github"]
        token = gh["token"]
        repo_name = gh["repo"]

        g = Github(token)
        repo = g.get_repo(repo_name)
        content = df.to_csv(index=False)

        try:
            contents = repo.get_contents(path, ref="main")
            repo.update_file(contents.path, mensagem, content, contents.sha, branch="main")
        except Exception:
            repo.create_file(path, mensagem, content, branch="main")

    except Exception as e:
        st.error(f"❌ Erro ao salvar no GitHub: {e}")





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
# Normalizadores de dados (com CodigoBarras nas tabelas)
# =====================================
def norm_produtos(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","CodigoBarras"]
    df = ensure_csv(ARQ_PRODUTOS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_vendas(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["IDVenda","Data","IDProduto","NomeProduto","CodigoBarras","FormaPagamento","Quantidade","PrecoUnitario","Total"]
    df = ensure_csv(ARQ_VENDAS, cols)
    df["Quantidade"] = df["Quantidade"].apply(to_int)
    for c in ["PrecoUnitario","Total"]:
        df[c] = df[c].apply(to_float)
    return df

def norm_clientes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","Cliente","Produto","CodigoBarras","Valor","DataPagamento","Status","FormaPagamento"]
    df = ensure_csv(ARQ_CLIENTES, cols)
    df["Valor"] = df["Valor"].apply(to_float)
    return df



def norm_caixas(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["Data","FaturamentoTotal","Dinheiro","PIX","Cartão","Fiado","Status"]

    # tenta carregar do GitHub primeiro
    df = load_csv_github(ARQ_CAIXAS)
    if df is None:
        df = ensure_csv(ARQ_CAIXAS, cols)

    for c in ["FaturamentoTotal","Dinheiro","PIX","Cartão","Fiado"]:
        df[c] = df[c].apply(to_float)
    return df
    
def norm_usuarios(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["Usuario","Senha"]
    df = ensure_csv(ARQ_USUARIOS, cols)
    # Se vazio, cria admin padrão
    if df.empty:
        df = pd.DataFrame([{"Usuario":"admin","Senha":"123"}])
        save_csv(df, ARQ_USUARIOS)
    return df

# ---- PROMOÇÕES ----
def norm_promocoes(_: pd.DataFrame) -> pd.DataFrame:
    cols = ["ID","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
    df = ensure_csv(ARQ_PROMOCOES, cols)
    # Tipos
    df["IDProduto"] = df["IDProduto"].astype(str)
    df["Desconto"] = df["Desconto"].apply(to_float)
    # Datas como string YYYY-MM-DD
    df["DataInicio"] = df["DataInicio"].astype(str)
    df["DataFim"] = df["DataFim"].astype(str)
    return df

def parse_date_yyyy_mm_dd(s: str):
    try:
        return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()
    except Exception:
        return None

def promocao_ativa_para(prod_id: str, hoje: date, prom_df: pd.DataFrame):
    """Retorna a promoção ativa (dict) para um produto na data 'hoje' ou None."""
    if prom_df is None or prom_df.empty:
        return None
    z = prom_df[prom_df["IDProduto"].astype(str) == str(prod_id)].copy()
    if z.empty:
        return None
    z["di"] = z["DataInicio"].apply(parse_date_yyyy_mm_dd)
    z["df"] = z["DataFim"].apply(parse_date_yyyy_mm_dd)
    z = z[(z["di"].notna()) & (z["df"].notna())]
    z = z[(z["di"] <= hoje) & (hoje <= z["df"])]
    if z.empty:
        return None
    # Se houver várias promoções, pega a de maior desconto
    z = z.sort_values(by="Desconto", ascending=False).iloc[0]
    return {
        "ID": z["ID"],
        "IDProduto": z["IDProduto"],
        "NomeProduto": z["NomeProduto"],
        "Desconto": float(z["Desconto"]),
        "DataInicio": str(z["DataInicio"]),
        "DataFim": str(z["DataFim"]),
    }

def aplica_promocao_no_preco(preco_vista: float, promo: dict | None) -> float:
    if not promo:
        return float(preco_vista)
    desc = float(promo.get("Desconto", 0.0))
    desc = max(0.0, min(desc, 100.0))
    return round(float(preco_vista) * (1.0 - desc/100.0), 2)

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


def do_login():
    if "logado" not in st.session_state:
        st.session_state["logado"] = False
        st.session_state["usuario_logado"] = None

    # 🔹 Se já estiver logado, não mostra tela de login de novo
    if st.session_state["logado"]:
        return True

    usuarios = norm_usuarios(pd.DataFrame())
    if "Manter" not in usuarios.columns:
        usuarios["Manter"] = False

    # 🔹 Tenta login automático
    manter_auto = usuarios[usuarios["Manter"] == True]
    if not manter_auto.empty:
        user = manter_auto.iloc[0]["Usuario"]
        st.session_state["logado"] = True
        st.session_state["usuario_logado"] = user
        return True

    # --- Tela de login normal ---
    show_logo("main")
    st.title("🔐 Login")

    user = st.text_input("Usuário")
    pwd  = st.text_input("Senha", type="password")
    manter = st.checkbox("Manter conectado")

    _, c2, _ = st.columns([1, 2, 1])
    with c2:
        if st.button("Entrar", use_container_width=True):
            cred_ok = (
                not usuarios[(usuarios["Usuario"] == user) & (usuarios["Senha"] == pwd)].empty
            ) or (user == "admin" and pwd == "123")

            if cred_ok:
                if user == "admin" and pwd == "123":
                    reset_admin_user()

                st.session_state["logado"] = True
                st.session_state["usuario_logado"] = user

                usuarios["Manter"] = False
                usuarios.loc[usuarios["Usuario"] == user, "Manter"] = manter
                save_csv_github(usuarios, ARQ_USUARIOS, "Atualizando preferências de login")

                st.rerun() if hasattr(st, "rerun") else st.experimental_rerun()
            else:
                st.error("Usuário ou senha inválidos.")

    return False







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
    if "promocoes" not in st.session_state:
        st.session_state["promocoes"] = norm_promocoes(pd.DataFrame())
    if "estoque_minimo" not in st.session_state:
        st.session_state["estoque_minimo"] = ESTOQUE_MINIMO_PADRAO
    if "pedido_atual" not in st.session_state:
        st.session_state["pedido_atual"] = []  # itens: IDProduto, NomeProduto, Quantidade, PrecoVista, CodigoBarras
    if "valor_pago" not in st.session_state:
        st.session_state["valor_pago"] = 0.0

# =====================================
# Helpers de Vendas
# =====================================
def preco_por_forma(preco_vista: float, forma: str) -> float:
    if forma == "Cartão":
        return float(preco_vista) / FATOR_CARTAO
    # Dinheiro, PIX, Fiado usam à vista
    return float(preco_vista)

def preco_vista_com_promocao(prod_id: str, preco_vista: float, hoje: date, prom_df: pd.DataFrame) -> tuple[float, dict | None]:
    promo = promocao_ativa_para(prod_id, hoje, prom_df)
    preco_aplicado = aplica_promocao_no_preco(preco_vista, promo)
    return preco_aplicado, promo

def desenha_pedido(forma: str, prom_df: pd.DataFrame) -> pd.DataFrame:
    # Tabela editável com remoção e alteração de quantidade
    pedido_lista = st.session_state.get("pedido_atual", [])
    if not pedido_lista:
        return pd.DataFrame()

    st.write("### Pedido Atual")
    novos_itens = []
    total = 0.0
    for idx, item in enumerate(pedido_lista):
        col1, col2, col3, col4, col5 = st.columns([4,2,2,2,1])
        with col1:
            extra_cb = f" • CB: {item.get('CodigoBarras','')}" if item.get("CodigoBarras") else ""
            st.write(f"**{item['NomeProduto']}** (ID {item['IDProduto']}){extra_cb}")
        with col2:
            # quantidade editável
            nova_qtd = st.number_input("Qtd", min_value=1, value=int(item["Quantidade"]), key=f"q_{idx}")

        # preço com promoção (se existir) e depois com forma de pagamento
        preco_vista_base = float(item["PrecoVista"])
        preco_vista_aplicado, promo = preco_vista_com_promocao(item["IDProduto"], preco_vista_base, date.today(), prom_df)
        preco_unit = preco_por_forma(preco_vista_aplicado, forma)

        with col3:
            st.write("Unit.:", brl(preco_unit))
            if promo:
                st.caption(f"🏷️ Promo: -{promo['Desconto']:.0f}% até {promo['DataFim']}")
        subtotal = float(nova_qtd) * float(preco_unit)
        with col4:
            st.write("Subtotal:", brl(subtotal))
        with col5:
            if st.button("🗑️", key=f"rem_{idx}"):
                # remove e rerun
                st.session_state["pedido_atual"].pop(idx)
                st.rerun() if hasattr(st, 'rerun') else st.experimental_rerun()
        novos_itens.append({
            "IDProduto": item["IDProduto"],
            "NomeProduto": item["NomeProduto"],
            "CodigoBarras": item.get("CodigoBarras",""),
            "Quantidade": int(nova_qtd),
            "PrecoVista": float(item["PrecoVista"]),
        })
        total += subtotal

    # sobrescreve quantidades editadas
    st.session_state["pedido_atual"] = novos_itens
    df_exib = pd.DataFrame([{
        "IDProduto": it["IDProduto"],
        "Produto": it["NomeProduto"],
        "CodigoBarras": it.get("CodigoBarras",""),
        "Quantidade": it["Quantidade"],
        "Preço unit.": preco_por_forma(preco_vista_com_promocao(it["IDProduto"], it["PrecoVista"], date.today(), prom_df)[0], forma),
        "Total": it["Quantidade"] * preco_por_forma(preco_vista_com_promocao(it["IDProduto"], it["PrecoVista"], date.today(), prom_df)[0], forma),
    } for it in novos_itens])
    return df_exib

# =====================================
# Guardas
# =====================================
if not do_login():
    st.stop()   # 🔒 mostra só tela de login e interrompe aqui

# =====================================
# Se logou, continua
# =====================================
boot_session()

# Carrega dados atuais
produtos  = norm_produtos(pd.DataFrame())
vendas    = norm_vendas(pd.DataFrame())
clientes  = norm_clientes(pd.DataFrame())
promocoes = norm_promocoes(pd.DataFrame())

st.session_state["produtos"]  = produtos
st.session_state["vendas"]    = vendas
st.session_state["clientes"]  = clientes
st.session_state["promocoes"] = promocoes

# =====================================
# Sidebar
# =====================================
show_logo("sidebar")
st.sidebar.title("📚 Menu")
view = st.sidebar.radio(
    "Navegar",
    ["Dashboard", "Produtos", "Vendas", "Clientes", "Promoções", "precificação", "Papelaria", "Sair"],
    index=0
)
st.sidebar.markdown("---")
st.sidebar.number_input(
    "🔔 Estoque mínimo (alerta)",
    min_value=0,
    step=1,
    value=st.session_state.get("estoque_minimo", 0),
    key="estoque_minimo"
)

if view == "Sair":
    # 🔹 Limpa sessão e também zera o "Manter"
    usuarios = norm_usuarios(pd.DataFrame())
    if "Manter" in usuarios.columns and st.session_state.get("usuario_logado"):
        usuarios.loc[usuarios["Usuario"] == st.session_state["usuario_logado"], "Manter"] = False
        save_csv_github(usuarios, ARQ_USUARIOS, "Logout do usuário")

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

    # 🔹 Sub-abas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Faturamento", "Alertas", "Promoções Ativas",
        "Relatório de Caixa", "Produtos Mais Vendidos"
    ])

    # ================= TAB 1 - FATURAMENTO =================
    with tab1:
        col1, col2, col3, col4 = st.columns(4)
        total_vendas = vendas["Total"].sum() if not vendas.empty else 0.0
        hoje_str = str(date.today())
        vendas_hoje = vendas[vendas["Data"] == hoje_str]["Total"].sum() if not vendas.empty else 0.0
        qntd_vendas = len(vendas) if not vendas.empty else 0
        fiados_abertos = len(clientes[clientes["Status"].astype(str).str.lower() == "aberto"]) if not clientes.empty else 0
        with col1: st.metric("Faturamento Total", brl(total_vendas))
        with col2: st.metric("Vendas Hoje", brl(vendas_hoje))
        with col3: st.metric("Qtde de Vendas", qntd_vendas)
        with col4: st.metric("Fiados em Aberto", fiados_abertos)

    # ================= TAB 2 - ALERTAS =================
    with tab2:
        st.subheader("⚠️ Alertas")
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
                st.dataframe(validade_proxima[["ID", "Nome", "Quantidade", "Validade"]], use_container_width=True)
            if not estoque_baixo.empty:
                st.error(f"Produtos com estoque baixo (≤ {estoque_min}):")
                st.dataframe(estoque_baixo[["ID", "Nome", "Quantidade"]], use_container_width=True)

    # ================= TAB 3 - PROMOÇÕES ATIVAS =================
    with tab3:
        st.subheader("🏷️ Promoções Ativas")
        hoje = date.today()
        if promocoes.empty:
            st.info("Nenhuma promoção ativa no momento.")
        else:
            # filtra ativas
            p = promocoes.copy()
            p["di"] = p["DataInicio"].apply(parse_date_yyyy_mm_dd)
            p["df"] = p["DataFim"].apply(parse_date_yyyy_mm_dd)
            p = p[(p["di"].notna()) & (p["df"].notna())]
            p = p[(p["di"] <= hoje) & (hoje <= p["df"])]
            if p.empty:
                st.info("Nenhuma promoção ativa hoje.")
            else:
                # mostrar em linhas de 3 cards
                cards = p[["NomeProduto", "Desconto", "DataFim"]].values.tolist()
                step = 3
                for i in range(0, len(cards), step):
                    cols = st.columns(step)
                    for j, (nome, desc, datafim) in enumerate(cards[i:i + step]):
                        with cols[j]:
                            st.markdown(f"""
                            <div style="border:1px solid #e5e7eb; border-radius:16px; padding:16px; box-shadow:0 1px 6px rgba(0,0,0,0.06)">
                                <div style="font-size:18px; font-weight:700;">{nome}</div>
                                <div style="font-size:32px; font-weight:800; margin:8px 0;">🔥 {float(desc):.0f}% OFF</div>
                                <div style="color:#6b7280;">Válido até {str(datafim)}</div>
                            </div>
                            """, unsafe_allow_html=True)

    # ================= TAB 4 - RELATÓRIO DE CAIXA =================
    with tab4:
        st.subheader("📦 Relatórios de Caixa")
        caixas = norm_caixas(pd.DataFrame())
        if caixas.empty:
            st.info("Nenhum fechamento de caixa registrado ainda.")
        else:
            st.subheader("🔍 Filtro de Caixa por Data")
            datas_disp = sorted(caixas["Data"].unique(), reverse=True)
            data_sel = st.selectbox("Selecione a data do caixa", ["Todas"] + datas_disp)

            caixas_filtrados = caixas.copy()
            if data_sel != "Todas":
                caixas_filtrados = caixas_filtrados[caixas_filtrados["Data"] == data_sel]

            st.dataframe(caixas_filtrados.sort_values("Data", ascending=False), use_container_width=True)

            if data_sel != "Todas":
                vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
                vendas_dia = vendas[vendas["Data"].dt.strftime("%Y-%m-%d") == data_sel]

                st.subheader(f"🛒 Produtos vendidos em {data_sel}")
                if vendas_dia.empty:
                    st.info("Nenhum produto vendido nesse dia.")
                else:
                    st.dataframe(
                        vendas_dia[["IDProduto", "NomeProduto", "Quantidade", "PrecoUnitario", "Total"]],
                        use_container_width=True
                    )
            else:
                vendas_dia = pd.DataFrame()

            st.subheader("🗑️ Excluir Relatório de Caixa")
            if not caixas_filtrados.empty:
                ids = caixas_filtrados["Data"].tolist()
                del_data = st.selectbox("Selecione a data do relatório para excluir", ids)
                if st.button("Excluir Relatório de Caixa"):
                    caixas = caixas[caixas["Data"] != del_data]
                    st.session_state["caixas"] = caixas
                    save_csv_github(caixas, ARQ_CAIXAS, f"Excluindo relatório de caixa {del_data}")
                    st.warning(f"Relatório de caixa de {del_data} excluído!")
                    st.rerun()

            if data_sel != "Todas" and not caixas_filtrados.empty:
                caixa_sel = caixas_filtrados.iloc[0].to_dict()
                if st.button("📄 Gerar PDF do Caixa Selecionado"):
                    caminho_pdf = f"caixa_{caixa_sel['Data']}.pdf"
                    gerar_pdf_caixa(caixa_sel, vendas_dia, caminho_pdf)
                    with open(caminho_pdf, "rb") as f:
                        st.download_button(
                            label=f"⬇️ Baixar Relatório de Caixa ({caixa_sel['Data']})",
                            data=f,
                            file_name=caminho_pdf,
                            mime="application/pdf"
                        )
                    st.rerun()

    # ================= TAB 5 - RELATÓRIO DE PRODUTOS MAIS VENDIDOS =================
    with tab5:
        st.subheader("📊 Produtos Mais Vendidos")
        if vendas.empty:
            st.info("Nenhuma venda registrada ainda.")
        else:
            col1, col2 = st.columns(2)
            with col1:
                data_inicio = st.date_input("Data de início", value=date.today().replace(day=1))
            with col2:
                data_fim = st.date_input("Data de fim", value=date.today())

            vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
            filtro = (vendas["Data"] >= pd.to_datetime(data_inicio)) & (vendas["Data"] <= pd.to_datetime(data_fim))
            vendas_filtradas = vendas[filtro]

            if vendas_filtradas.empty:
                st.warning("Nenhum produto vendido neste período.")
            else:
                ranking = (
                    vendas_filtradas.groupby(["IDProduto", "NomeProduto"])["Quantidade"]
                    .sum()
                    .reset_index()
                    .sort_values("Quantidade", ascending=False)
                )

                st.dataframe(ranking, use_container_width=True)

                if st.button("📄 Gerar PDF do Relatório"):
                    caminho_pdf = f"relatorio_produtos_{data_inicio}_a_{data_fim}.pdf"
                    gerar_pdf_produtos_vendidos(ranking, caminho_pdf, data_inicio, data_fim)
                    with open(caminho_pdf, "rb") as f:
                        st.download_button(
                            label=f"⬇️ Baixar Relatório de Produtos ({data_inicio} a {data_fim})",
                            data=f,
                            file_name=caminho_pdf,
                            mime="application/pdf"
                        )



    
# =====================================
# PRODUTOS
# =====================================
if view == "Produtos":
    show_logo("main")
    st.header("📦 Produtos")

    # --- Cadastro ---
    with st.expander("Cadastrar novo produto"):
        c1, c2, c3 = st.columns(3)
        with c1:
            nome = st.text_input("Nome", key="cad_nome")
            marca = st.text_input("Marca", key="cad_marca")
            categoria = st.text_input("Categoria", key="cad_categoria")

        with c2:
            qtd = st.number_input("Quantidade", min_value=0, step=1, value=0, key="cad_qtd")
            preco_custo = st.text_input("Preço de Custo", value="0,00", key="cad_preco_custo")
            preco_vista = st.text_input("Preço à Vista", value="0,00", key="cad_preco_vista")
            preco_cartao = 0.0
            try:
                preco_cartao = round(float(preco_vista.replace(",", ".").strip()) / FATOR_CARTAO, 2)
            except Exception:
                preco_cartao = 0.0
            st.text_input("Preço no Cartão (auto)", value=str(preco_cartao).replace(".", ","), disabled=True, key="cad_preco_cartao")

        with c3:
            validade = st.date_input("Validade (opcional)", value=date.today(), key="cad_validade")
            foto_url = st.text_input("URL da Foto (opcional)", key="cad_foto_url")
            foto_arquivo = st.file_uploader("📷 Enviar Foto", type=["png", "jpg", "jpeg"], key="cad_foto")

            if "codigo_barras" not in st.session_state:
                st.session_state["codigo_barras"] = ""

            codigo_barras = st.text_input("Código de Barras", value=st.session_state["codigo_barras"], key="cad_cb")

            # --- Escanear com câmera ---
            foto_codigo = st.camera_input("📷 Escanear código de barras / QR Code", key="cad_cam")
            if foto_codigo is not None:
                imagem_bytes = foto_codigo.getvalue()
                codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                if codigos_lidos:
                    st.session_state["codigo_barras"] = codigos_lidos[0]
                    st.success(f"Código lido: {st.session_state['codigo_barras']}")
                    st.rerun()
                else:
                    st.error("❌ Não foi possível ler nenhum código.")

            # --- Upload de imagem do código de barras ---
            foto_codigo_upload = st.file_uploader("📤 Upload de imagem do código de barras", type=["png", "jpg", "jpeg"], key="cad_cb_upload")
            if foto_codigo_upload is not None:
                imagem_bytes = foto_codigo_upload.getvalue()
                codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                if codigos_lidos:
                    st.session_state["codigo_barras"] = codigos_lidos[0]
                    st.success(f"Código lido via upload: {st.session_state['codigo_barras']}")
                    st.rerun()
                else:
                    st.error("❌ Não foi possível ler nenhum código da imagem enviada.")

        if st.button("💾 Salvar Produto", use_container_width=True, key="cad_salvar"):
            novo_id = prox_id(produtos, "ID")
            novo = {
                "ID": novo_id,
                "Nome": nome.strip(),
                "Marca": marca.strip(),
                "Categoria": categoria.strip(),
                "Quantidade": int(qtd),
                "PrecoCusto": to_float(preco_custo),
                "PrecoVista": to_float(preco_vista),
                "PrecoCartao": round(to_float(preco_vista) / FATOR_CARTAO, 2) if to_float(preco_vista) > 0 else 0.0,
                "Validade": str(validade),
                "FotoURL": foto_url.strip(),
                "CodigoBarras": codigo_barras.strip()
            }
            produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
            st.session_state["produtos"] = produtos
            save_csv_github(produtos, ARQ_PRODUTOS, "Novo produto cadastrado")
            st.success(f"✅ Produto '{nome}' cadastrado com sucesso!")
            st.rerun()


    # --- Busca minimalista ---
    with st.expander("🔍 Pesquisar produto"):
        criterio = st.selectbox(
            "Pesquisar por:",
            ["Nome", "Marca", "Código de Barras", "Valor"]
        )
        termo = st.text_input("Digite para buscar:")

        if termo:
            if criterio == "Nome":
                produtos_filtrados = produtos[produtos["Nome"].astype(str).str.contains(termo, case=False, na=False)]
            elif criterio == "Marca":
                produtos_filtrados = produtos[produtos["Marca"].astype(str).str.contains(termo, case=False, na=False)]
            elif criterio == "Código de Barras":
                produtos_filtrados = produtos[produtos["CodigoBarras"].astype(str).str.contains(termo, case=False, na=False)]
            elif criterio == "Valor":
                try:
                    valor = float(termo.replace(",", "."))
                    produtos_filtrados = produtos[produtos["PrecoVista"].astype(float) == valor]
                except:
                    st.warning("Digite um número válido para buscar por valor.")
                    produtos_filtrados = produtos.copy()
        else:
            produtos_filtrados = produtos.copy()

    # --- Lista de produtos ---
    st.markdown("### Lista de produtos")
    if produtos_filtrados.empty:
        st.info("Nenhum produto encontrado.")
    else:
        for _, row in produtos_filtrados.iterrows():
            with st.container():
                c = st.columns([1,2,2,2,2])
                if str(row["FotoURL"]).strip():
                    try:
                        c[0].image(row["FotoURL"], width=80)
                    except Exception:
                        c[0].write("Sem imagem")
                else:
                    c[0].write("—")
                cb = f' • CB: {row["CodigoBarras"]}' if str(row.get("CodigoBarras","")).strip() else ""
                c[1].markdown(f"**{row['Nome']}**  \nMarca: {row['Marca']}  \nCat: {row['Categoria']}{cb}")
                c[2].write(f"Estoque: {row['Quantidade']}")
                c[3].write(f"Validade: {row['Validade']}")
                col_btn = c[4]
                try:
                    eid = int(row["ID"])
                except Exception:
                    continue

                # 🔽 Novo seletor de ação
                acao = col_btn.selectbox(
                    "Ação",
                    ["Nenhuma", "✏️ Editar", "🗑️ Excluir"],
                    key=f"acao_{eid}"
                )

                if acao == "✏️ Editar":
                    st.session_state["edit_prod"] = eid  # só marca, sem rerun

                if acao == "🗑️ Excluir":
                    if col_btn.button("Confirmar exclusão", key=f"conf_del_{eid}"):
                        produtos = produtos[produtos["ID"] != str(eid)]
                        st.session_state["produtos"] = produtos
                        save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")
                        st.warning(f"Produto {row['Nome']} excluído!")
                        st.rerun()

        # Editor inline
        if "edit_prod" in st.session_state:
            eid = st.session_state["edit_prod"]
            row = produtos[produtos["ID"]==str(eid)]
            if not row.empty:
                st.subheader("Editar produto")
                row = row.iloc[0]
                c1,c2,c3 = st.columns(3)
                with c1:
                    novo_nome = st.text_input("Nome", value=row["Nome"], key=f"edit_nome_{eid}")
                    nova_marca = st.text_input("Marca", value=row["Marca"], key=f"edit_marca_{eid}")
                    nova_cat = st.text_input("Categoria", value=row["Categoria"], key=f"edit_cat_{eid}")
                with c2:
                    nova_qtd = st.number_input("Quantidade", min_value=0, step=1, value=int(row["Quantidade"]), key=f"edit_qtd_{eid}")
                    novo_preco_custo = st.text_input("Preço de Custo", value=str(row["PrecoCusto"]).replace(".",","), key=f"edit_pc_{eid}")
                    novo_preco_vista = st.text_input("Preço à Vista", value=str(row["PrecoVista"]).replace(".",","), key=f"edit_pv_{eid}")
                with c3:
                    try:
                        vdata = datetime.strptime(str(row["Validade"] or date.today()), "%Y-%m-%d").date()
                    except Exception:
                        vdata = date.today()
                    nova_validade = st.date_input("Validade", value=vdata, key=f"edit_val_{eid}")
                    nova_foto = st.text_input("URL da Foto", value=row["FotoURL"], key=f"edit_foto_{eid}")
                    novo_cb = st.text_input("Código de Barras", value=str(row.get("CodigoBarras","")), key=f"edit_cb_{eid}")
                    foto_codigo_edit = st.camera_input("📷 Atualizar código de barras", key=f"edit_cam_{eid}")
                    if foto_codigo_edit is not None:
                        codigo_lido = ler_codigo_barras_api(foto_codigo_edit.getbuffer())
                        if codigo_lido:
                            novo_cb = codigo_lido
                            st.success(f"Código lido: {novo_cb}")

                col_save, col_cancel = st.columns([1,1])
                with col_save:
                    if st.button("Salvar alterações", key=f"save_{eid}"):
                        produtos.loc[produtos["ID"]==str(eid), [
                            "Nome","Marca","Categoria","Quantidade",
                            "PrecoCusto","PrecoVista","PrecoCartao",
                            "Validade","FotoURL","CodigoBarras"
                        ]] = [
                            novo_nome.strip(),
                            nova_marca.strip(),
                            nova_cat.strip(),
                            int(nova_qtd),
                            to_float(novo_preco_custo),
                            to_float(novo_preco_vista),
                            round(to_float(novo_preco_vista) / FATOR_CARTAO, 2) if to_float(novo_preco_vista)>0 else 0.0,
                            str(nova_validade),
                            nova_foto.strip(),
                            str(novo_cb).strip()
                        ]
                        st.session_state["produtos"] = produtos
                        save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")
                        del st.session_state["edit_prod"]
                        st.success("Produto atualizado!")
                        st.rerun()

                with col_cancel:
                    if st.button("Cancelar edição", key=f"cancel_{eid}"):
                        del st.session_state["edit_prod"]
                        st.info("Edição cancelada.")
                        st.rerun()








  # ========================================================
# 1. IMPORTS E FUNÇÕES GLOBAIS (SEMPRE NO TOPO)
# ========================================================

import streamlit as st
import pandas as pd
from datetime import date
import requests





# =====================
# 🔧 Configurações
# =====================
import requests
import pytz
from datetime import datetime

TELEGRAM_TOKEN = "8366173640:AAHECvJBn_1jN_OsX8BXBGuMw9XE_angTKc"
TELEGRAM_CHAT_ID = "1003030758192"

# =====================
# 📤 Função para enviar mensagem
# =====================
def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    try:
        r = requests.post(url, json=data)
        resp = r.json()
        print("DEBUG TELEGRAM:", resp)
        if not resp.get("ok"):
            print(f"Erro Telegram: {resp}")
    except Exception as e:
        print(f"Erro ao enviar Telegram: {e}")




def abrir_caixa():
    with st.form("abrir_caixa_form"):
        st.subheader("🟢 Abrir Caixa")
        operador = st.text_input("👤 Nome do Operador", key="input_operador")
        valor_inicial = st.number_input(
            "💵 Valor Inicial do Caixa",
            min_value=0.0,
            step=1.0,
            key="input_valor_inicial"
        )
        submitted = st.form_submit_button("🚀 Abrir Caixa")
        if submitted:
            if not operador:
                st.warning("⚠️ Informe o nome do operador para abrir o caixa.")
            else:
                st.session_state["operador"] = operador
                st.session_state["valor_inicial"] = valor_inicial
                st.session_state["valor_inicial_original"] = valor_inicial  # salva o valor original
                st.session_state["caixa_aberto"] = True
                st.success(
                    f"✅ Caixa aberto com sucesso! Operador: {operador} | Valor inicial: {valor_inicial:.2f}"
                )
                st.rerun()


def fechar_caixa():
    if st.session_state.get("caixa_aberto", False):
        operador = st.session_state.get("operador", "—")
        valor_inicial = st.session_state.get(
            "valor_inicial_original",
            st.session_state.get("valor_inicial", 0.0)
        )
        hoje = date.today()

        # Converte a coluna Data para datetime.date
        vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce").dt.date
        vendas_dia = vendas[vendas["Data"] == hoje]

        total_dinheiro = vendas_dia[vendas_dia["FormaPagamento"] == "Dinheiro"]["Total"].sum()
        total_pix = vendas_dia[vendas_dia["FormaPagamento"] == "PIX"]["Total"].sum()
        total_cartao_bruto = vendas_dia[vendas_dia["FormaPagamento"] == "Cartão"]["Total"].sum()
        total_fiado = vendas_dia[vendas_dia["FormaPagamento"] == "Fiado"]["Total"].sum()

        # Apenas o dinheiro entra no valor final do caixa
        valor_final_caixa = valor_inicial + total_dinheiro
        # Faturamento total do dia inclui todas as formas
        faturamento_total_caixa = total_dinheiro + total_pix + total_cartao_bruto + total_fiado

        dados_caixa = {
            "Data": hoje.strftime("%Y-%m-%d"),
            "Operador": operador,
            "ValorInicial": valor_inicial,
            "Dinheiro": total_dinheiro,
            "PIX": total_pix,
            "Cartão": total_cartao_bruto,
            "Fiado": total_fiado,
            "FaturamentoTotal": faturamento_total_caixa,
            "ValorFinalCaixa": valor_final_caixa,
            "Status": "Fechado"
        }

        caixas = norm_caixas(pd.DataFrame())
        caixas = pd.concat([caixas, pd.DataFrame([dados_caixa])], ignore_index=True)
        save_csv_github(caixas, ARQ_CAIXAS, f"Fechamento de caixa {hoje.strftime('%Y-%m-%d')}")

        st.session_state["dados_fechamento_caixa"] = dados_caixa
        st.session_state["vendas_dia_fechamento"] = vendas_dia
        st.session_state["caixa_aberto"] = False

        st.success(
            f"📦 Caixa fechado! Operador: {operador} | Valor final esperado: {brl(valor_final_caixa)}"
        )
        st.rerun()


# =====================
# 🔧 Configurações (supondo que já esteja no seu código)
# =====================
TELEGRAM_TOKEN = "8366173640:AAHECvJBn_1jN_OsX8BXBGuMw9XE_angTKc"  # Seu token do bot aqui
TELEGRAM_CHAT_ID = "-1003030758192"  # ID do grupo onde estão os tópicos

# =====================
# 📤 Função para enviar mensagem no Telegram (ajustada para tópicos)
# =====================
def enviar_telegram(mensagem, thread_id=None):
    import requests

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    if thread_id is not None:
        data["message_thread_id"] = thread_id  # Define o tópico para enviar

    try:
        r = requests.post(url, json=data)
        resp = r.json()
        print("DEBUG TELEGRAM:", resp)
        if not resp.get("ok"):
            print(f"Erro Telegram: {resp}")
    except Exception as e:
        print(f"Erro ao enviar Telegram: {e}")

# =====================
# Sua função finalizar_venda ajustada
# =====================
def finalizar_venda(forma, forma1, forma2, valor1, valor2, promocoes,
                    nome_cliente=None, data_pagamento=None, valor_recebido=0.0):
    global vendas, produtos, clientes

    if not st.session_state.get("pedido_atual"):
        st.warning("⚠️ Nenhum item no pedido.")
        return

    if not vendas.empty and "IDVenda" in vendas.columns:
        vendas["IDVenda"] = pd.to_numeric(vendas["IDVenda"], errors="coerce").fillna(0).astype(int)
        novo_id = int(vendas["IDVenda"].max() + 1)
    else:
        novo_id = 1

    df_pedido = pd.DataFrame(st.session_state["pedido_atual"])

    # 🔹 Garante coluna PrecoComDesconto calculada com promoções
    if "PrecoComDesconto" not in df_pedido.columns:
        precos_corrigidos = []
        promocoes_aplicadas = []
        for _, row in df_pedido.iterrows():
            preco_base = float(row["PrecoVista"])
            preco_desc, promo = preco_vista_com_promocao(
                row["IDProduto"], preco_base, date.today(), promocoes
            )
            precos_corrigidos.append(preco_desc)
            promocoes_aplicadas.append(promo["Desconto"] if promo else None)
        df_pedido["PrecoComDesconto"] = precos_corrigidos
        df_pedido["Promocao"] = promocoes_aplicadas

    df_pedido["IDVenda"] = novo_id
    df_pedido["Data"] = date.today()
    df_pedido["Cliente"] = nome_cliente if nome_cliente else ""
    df_pedido["DataPagamento"] = str(data_pagamento) if data_pagamento else ""
    df_pedido["ValorRecebido"] = valor_recebido

    # Usa PrecoComDesconto para calcular o total com promoção
    total_pedido = df_pedido["PrecoComDesconto"].multiply(df_pedido["Quantidade"]).sum()

    if forma == "Misto" and forma1 and forma2:
        # Corrige valor1 e valor2 proporcionalmente para o total com desconto
        soma_valores = valor1 + valor2
        if soma_valores == 0:
            valor1_corrigido = valor2_corrigido = 0
        else:
            valor1_corrigido = total_pedido * (valor1 / soma_valores)
            valor2_corrigido = total_pedido * (valor2 / soma_valores)

        df_vendas_misto = pd.DataFrame()

        df_temp = df_pedido.copy()
        df_temp["FormaPagamento"] = forma1
        df_temp["Total"] = valor1_corrigido
        df_vendas_misto = pd.concat([df_vendas_misto, df_temp], ignore_index=True)

        df_temp = df_pedido.copy()
        df_temp["FormaPagamento"] = forma2
        df_temp["Total"] = valor2_corrigido
        df_vendas_misto = pd.concat([df_vendas_misto, df_temp], ignore_index=True)

        vendas = pd.concat([vendas, df_vendas_misto], ignore_index=True)
    else:
        df_pedido["FormaPagamento"] = forma
        df_pedido["Total"] = total_pedido
        vendas = pd.concat([vendas, df_pedido], ignore_index=True)

    if forma == "Fiado" and nome_cliente:
        novos_registros = []
        for _, row in df_pedido.iterrows():
            novo_cliente = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": nome_cliente,
                "Produto": row["NomeProduto"],
                "CodigoBarras": row.get("CodigoBarras", ""),
                "Valor": float(row["PrecoComDesconto"]) * int(row["Quantidade"]),
                "DataPagamento": str(data_pagamento) if data_pagamento else "",
                "Status": "Aberto",
                "FormaPagamento": "Fiado",
            }
            novos_registros.append(novo_cliente)

        clientes = pd.concat([clientes, pd.DataFrame(novos_registros)], ignore_index=True)
        save_csv_github(clientes, ARQ_CLIENTES, "Novo fiado adicionado")

    save_csv_github(vendas, ARQ_VENDAS, "Nova venda adicionada")
    st.session_state["pedido_atual"] = []

    try:
        import pytz
        from datetime import datetime

        tz = pytz.timezone("America/Sao_Paulo")
        agora = datetime.now(tz)
        data_str = agora.strftime("%Y-%m-%d")
        hora_str = agora.strftime("%H:%M:%S")

        produtos_txt = ""
        for _, row in df_pedido.iterrows():
            promo_str = ""
            if "Promocao" in row and row["Promocao"]:
                promo_str = f" 🔥 {row['Promocao']}% OFF"
            produtos_txt += f"• <b>{row['NomeProduto']}</b> x{row['Quantidade']}{promo_str}\n"

        msg = (
            f"🛒 <b>Nova Venda Realizada!</b>\n\n"
            f"📅 <b>Data:</b> {data_str}\n"
            f"⏰ <b>Hora:</b> {hora_str}\n"
            f"🆔 <b>Venda:</b> {novo_id}\n"
            f"💰 <b>Total:</b> {brl(total_pedido)}\n\n"
            f"📦 <b>Produtos:</b>\n{produtos_txt}"
        )

        if forma == "Misto" and forma1 and forma2:
            msg += f"\n💳 <b>Pagamento Misto:</b>\n - {forma1}: {brl(valor1_corrigido)}\n - {forma2}: {brl(valor2_corrigido)}"
        else:
            msg += f"\n💳 <b>Pagamento:</b> {forma}"

        if forma == "Fiado" and nome_cliente:
            data_pag = data_pagamento if data_pagamento else "Não informada"
            msg += f"\n\n👤 <b>Cliente Fiado:</b> {nome_cliente}\n📅 <b>Data Pagamento:</b> {data_pag}"

        # Aqui alterei para enviar no tópico Vendas (thread_id=2)
        enviar_telegram(msg, thread_id=2)

    except Exception as e:
        st.error(f"Erro ao enviar Telegram: {e}")

    st.success(f"✅ Venda {novo_id} finalizada com sucesso!")
    st.rerun()


# =====================
# 🔧 relatório caixa (supondo que já esteja no seu código)
# =====================
TELEGRAM_TOKEN = "8106907671:AAFoh0TfADdyP-NWasS2BQu4BkfG9ez-Smw"  # Seu token do bot aqui
TELEGRAM_CHAT_ID = "-1003030758192"  # ID do grupo onde estão os tópicos

import requests

# Função para enviar mensagens no Telegram (já existente)
def enviar_telegram(mensagem, thread_id=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem,
        "parse_mode": "HTML"
    }
    if thread_id is not None:
        data["message_thread_id"] = thread_id

    try:
        r = requests.post(url, json=data)
        resp = r.json()
        print("DEBUG TELEGRAM mensagem:", resp)
        if not resp.get("ok"):
            print(f"Erro Telegram: {resp}")
    except Exception as e:
        print(f"Erro ao enviar Telegram: {e}")

# Nova função para enviar PDF no Telegram
def enviar_pdf_telegram(caminho_arquivo, thread_id=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            files = {'document': arquivo_pdf}
            data = {
                "chat_id": TELEGRAM_CHAT_ID,
            }
            if thread_id is not None:
                data["message_thread_id"] = thread_id
            
            r = requests.post(url, data=data, files=files)
            resp = r.json()
            print("DEBUG TELEGRAM PDF:", resp)
            if not resp.get("ok"):
                print(f"Erro Telegram no envio do PDF: {resp}")
    except Exception as e:
        print(f"Erro ao enviar PDF no Telegram: {e}")

# Função para formatar valores em reais (já existente)
def brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Ajuste na função para gerar PDF incluindo operador e valor inicial do caixa
def gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm

    c = canvas.Canvas(caminho_pdf, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(2*cm, height - 2*cm, "Relatório de Fechamento de Caixa")

    c.setFont("Helvetica", 12)
    c.drawString(2*cm, height - 3*cm, f"Data: {dados_caixa['Data']}")
    c.drawString(2*cm, height - 4*cm, f"Operador: {dados_caixa.get('Operador', 'N/A')}")
    c.drawString(2*cm, height - 5*cm, f"Valor Inicial do Caixa: {brl(dados_caixa['ValorInicial'])}")

    y = height - 6*cm

    c.drawString(2*cm, y, f"Dinheiro recebido hoje: {brl(dados_caixa['Dinheiro'])}")
    y -= 1*cm
    c.drawString(2*cm, y, f"PIX recebido: {brl(dados_caixa['PIX'])}")
    y -= 1*cm
    c.drawString(2*cm, y, f"Cartão (valor bruto da venda): {brl(dados_caixa['Cartão'])}")
    y -= 1*cm
    c.drawString(2*cm, y, f"Fiado (não entra no caixa): {brl(dados_caixa['Fiado'])}")
    y -= 1*cm

    faturamento_total_caixa = dados_caixa['Dinheiro'] + dados_caixa['PIX'] + dados_caixa['Cartão'] + dados_caixa['Fiado']
    valor_final_caixa = dados_caixa['ValorInicial'] + dados_caixa['Dinheiro']

    c.drawString(2*cm, y, f"Faturamento Total do Dia: {brl(faturamento_total_caixa)}")
    y -= 1*cm
    c.drawString(2*cm, y, f"Valor Final esperado no Caixa: {brl(valor_final_caixa)}")
    y -= 2*cm

    c.drawString(2*cm, y, f"Total de vendas no dia: {len(vendas_dia)}")

    c.save()

# Função para enviar relatório de fechamento de caixa pelo Telegram (mensagem + PDF)
def enviar_relatorio_fechamento_caixa(dados_caixa, vendas_dia, thread_id=3):
    try:
        import pytz
        from datetime import datetime

        tz = pytz.timezone("America/Sao_Paulo")
        agora = datetime.now(tz)
        data_str = agora.strftime("%d/%m/%Y")
        hora_str = agora.strftime("%H:%M:%S")

        valor_inicial = dados_caixa['ValorInicial']
        total_dinheiro = dados_caixa['Dinheiro']
        total_pix = dados_caixa['PIX']
        total_cartao_bruto = dados_caixa['Cartão']
        total_fiado = dados_caixa['Fiado']
        operador = dados_caixa.get('Operador', 'N/A')

        faturamento_total_caixa = total_dinheiro + total_pix + total_cartao_bruto + total_fiado
        valor_final_caixa = valor_inicial + total_dinheiro

        msg = (
            f"📊 <b>Relatório de Fechamento de Caixa</b>\n"
            f"📅 Data: {data_str}\n"
            f"⏰ Hora: {hora_str}\n"
            f"👤 Operador: {operador}\n\n"
            f"💵 Valor Inicial do Caixa: {brl(valor_inicial)}\n"
            f"💵 Dinheiro recebido hoje: {brl(total_dinheiro)}\n"
            f"⚡ PIX recebido: {brl(total_pix)}\n"
            f"💳 Cartão (valor bruto da venda): {brl(total_cartao_bruto)}\n"
            f"📒 Fiado (não entra no caixa): {brl(total_fiado)}\n"
            f"📦 Faturamento Total do Dia: {brl(faturamento_total_caixa)}\n"
            f"💰 Valor Final esperado no Caixa: {brl(valor_final_caixa)}\n\n"
            f"🛒 Total de vendas no dia: {len(vendas_dia)}"
        )

        # Envia a mensagem primeiro
        enviar_telegram(msg, thread_id=thread_id)

        # Gera o PDF no caminho especificado
        caminho_pdf = f"caixa_{dados_caixa['Data']}.pdf"
        gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf)

        # Envia o PDF no mesmo tópico/thread
        enviar_pdf_telegram(caminho_pdf, thread_id=thread_id)

    except Exception as e:
        print(f"Erro ao enviar relatório de fechamento: {e}")

# ===========================
# Trecho do seu código principal que mostra o resumo do fechamento de caixa
# ===========================

if "dados_fechamento_caixa" in st.session_state:
    st.subheader("📊 Resumo do Último Fechamento de Caixa")
    dados_caixa = st.session_state.pop("dados_fechamento_caixa")
    vendas_dia = st.session_state.pop("vendas_dia_fechamento")

    valor_inicial = dados_caixa['ValorInicial']
    total_dinheiro = dados_caixa['Dinheiro']
    total_pix = dados_caixa['PIX']
    total_cartao_bruto = dados_caixa['Cartão']
    total_fiado = dados_caixa['Fiado']
    operador = dados_caixa.get('Operador', 'N/A')

    faturamento_total_caixa = total_dinheiro + total_pix + total_cartao_bruto + total_fiado
    valor_final_caixa = valor_inicial + total_dinheiro

    st.write(f"👤 Operador do Caixa: {operador}")
    st.write(f"💵 Valor Inicial do Caixa: {brl(valor_inicial)}")
    st.write(f"💵 Dinheiro recebido hoje: {brl(total_dinheiro)}")
    st.write(f"⚡ PIX recebido: {brl(total_pix)}")
    st.write(f"💳 Cartão (valor bruto da venda): {brl(total_cartao_bruto)}")
    st.write(f"📒 Fiado (não entra no caixa): {brl(total_fiado)}")
    st.write(f"📦 Faturamento Total do Dia: {brl(faturamento_total_caixa)}")
    st.write(f"💰 Valor Final esperado no Caixa: {brl(valor_final_caixa)}")

    caminho_pdf = f"caixa_{dados_caixa['Data']}.pdf"
    gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf)
    with open(caminho_pdf, "rb") as f:
        st.download_button(
            label=f"⬇️ Baixar Relatório de Caixa ({dados_caixa['Data']})",
            data=f,
            file_name=caminho_pdf,
            mime="application/pdf",
            key="download_caixa"
        )

    # Enviar relatório para o Telegram no tópico com thread_id=3 (altere se necessário)
    enviar_relatorio_fechamento_caixa(dados_caixa, vendas_dia, thread_id=3)

    st.write("---")


# 🔹 Fluxo de Vendas
if view == "Vendas":
    if not st.session_state.get("caixa_aberto", False):
        st.info("⚠️ Para iniciar as vendas, abra o caixa abaixo:")
        abrir_caixa()
    else:
        operador = st.session_state.get("operador", "—")
        valor_inicial = st.session_state.get("valor_inicial", 0.0)
        st.success(f"✅ Caixa aberto! Operador: {operador} | Valor Inicial: {valor_inicial:.2f}")

        tab1, tab2, tab3 = st.tabs(["Venda Detalhada", "Últimas Vendas", "Recibos de Vendas"])

        # ================= TAB 1 - VENDA DETALHADA =================
        with tab1:
            st.subheader("🛒 Venda Detalhada")
            st.markdown("### 🔍 Pesquisar Produto")
            sub1, sub2, sub3 = st.tabs(["Por Nome", "Por Código de Barras", "Por Foto"])

            with sub1:
                nome_filtro = st.text_input("Digite o nome do produto", key="nome_filtro_venda")
                df_sel = produtos.copy()
                if nome_filtro:
                    df_sel = df_sel[df_sel["Nome"].astype(str).str.contains(nome_filtro, case=False, na=False)]
                if not df_sel.empty:
                    escolha = st.selectbox(
                        "Selecione o produto",
                        (df_sel["ID"].astype(str) + " - " + df_sel["Nome"]).tolist(),
                        key="select_nome_venda"
                    )
                    qtd_nome = st.number_input("Quantidade", min_value=1, value=1, step=1, key="qtd_nome_venda")
                    if st.button("Adicionar ao pedido (nome)", key="btn_add_nome_venda"):
                        pid = escolha.split(" - ")[0].strip()
                        rowp = df_sel[df_sel["ID"].astype(str) == pid].iloc[0]
                        st.session_state["pedido_atual"].append({
                            "IDProduto": pid,
                            "NomeProduto": rowp["Nome"],
                            "CodigoBarras": str(rowp.get("CodigoBarras", "")),
                            "Quantidade": int(qtd_nome),
                            "PrecoVista": float(rowp["PrecoVista"]),
                        })
                        st.success("Item adicionado ao pedido.")
                        st.rerun()

            with sub2:
                codigo = st.text_input("Digite ou escaneie o código de barras", key="codigo_barras_venda")
                df_sel = produtos.copy()
                if codigo:
                    df_sel = df_sel[(df_sel["ID"].astype(str).str.contains(codigo)) |
                                    (df_sel["CodigoBarras"].astype(str).str.contains(codigo))]
                if not df_sel.empty:
                    escolha = st.selectbox(
                        "Selecione o produto",
                        (df_sel["ID"].astype(str) + " - " + df_sel["Nome"]).tolist(),
                        key="select_codigo_venda"
                    )
                    qtd_codigo = st.number_input("Quantidade", min_value=1, value=1, step=1, key="qtd_codigo_venda")
                    if st.button("Adicionar ao pedido (código)", key="btn_add_codigo_venda"):
                        pid = escolha.split(" - ")[0].strip()
                        rowp = df_sel[df_sel["ID"].astype(str) == pid].iloc[0]
                        st.session_state["pedido_atual"].append({
                            "IDProduto": pid,
                            "NomeProduto": rowp["Nome"],
                            "CodigoBarras": str(rowp.get("CodigoBarras", "")),
                            "Quantidade": int(qtd_codigo),
                            "PrecoVista": float(rowp["PrecoVista"]),
                        })
                        st.success("Item adicionado ao pedido.")
                        st.rerun()

            with sub3:
                foto = st.camera_input("Tirar foto do produto", key="foto_venda")
                if foto:
                    st.info("🚧 Pesquisa por foto em desenvolvimento (placeholder).")

            st.markdown("---")

            # ================= MOSTRAR PAGAMENTO SOMENTE SE HOUVER ITENS =================
            if st.session_state.get("pedido_atual"):
                st.markdown("### Forma de Pagamento")
                forma = st.radio(
                    "Selecione a forma de pagamento",
                    ["Dinheiro", "PIX", "Cartão", "Fiado", "Misto"],
                    horizontal=True,
                    key="radio_forma_pagamento_venda"
                )

                forma1 = forma2 = None
                valor1 = valor2 = 0.0
                valor_recebido = 0.0
                nome_cliente = None
                data_pagamento = None

                if forma == "Misto":
                    st.markdown("#### Configuração do pagamento misto")
                    colm1, colm2 = st.columns(2)
                    with colm1:
                        forma1 = st.selectbox(
                            "Primeira forma",
                            ["Dinheiro", "PIX", "Cartão", "Fiado"],
                            key="misto_forma1"
                        )
                        valor1 = st.number_input(
                            f"Valor em {forma1}",
                            min_value=0.0,
                            step=1.0,
                            key="misto_valor1"
                        )
                    with colm2:
                        forma2 = st.selectbox(
                            "Segunda forma",
                            ["Dinheiro", "PIX", "Cartão", "Fiado"],
                            key="misto_forma2"
                        )

                df_pedido = desenha_pedido(forma, promocoes)
                valor_total = float(df_pedido["Total"].sum()) if not df_pedido.empty else 0.0

                if forma == "Misto" and forma1 and forma2:
                    if forma1 == "Cartão":
                        valor1 = valor1 / 0.8872 if valor1 > 0 else 0.0
                    if forma2 == "Cartão":
                        valor2 = max((valor_total - valor1) / 0.8872, 0.0)
                    else:
                        valor2 = max(valor_total - valor1, 0.0)
                    st.info(f"💳 Pagamento dividido: {forma1} = {brl(valor1)}, {forma2} = {brl(valor2)}")

                if forma == "Dinheiro":
                    valor_recebido = st.number_input("💵 Valor recebido em dinheiro", min_value=0.0, step=1.0)
                    troco = max(valor_recebido - valor_total, 0.0)
                    st.info(f"Troco: {brl(troco)}")
                elif forma == "Fiado":
                    nome_cliente = st.text_input("👤 Nome do Cliente")
                    data_pagamento = st.date_input("📅 Data prevista de pagamento", value=date.today())

                colA, colB, colC = st.columns(3)
                colA.metric("Valor Total", brl(valor_total))

                if forma == "Misto":
                    colB.metric(f"{forma1}", brl(valor1))
                    colC.metric(f"{forma2}", brl(valor2))
                elif forma == "Dinheiro":
                    colB.metric("Valor Recebido", brl(valor_recebido))
                    colC.metric("Troco", brl(max(valor_recebido - valor_total, 0.0)))
                elif forma == "Fiado":
                    colB.metric("Cliente", nome_cliente if nome_cliente else "—")
                    colC.metric("Data Pagamento", str(data_pagamento) if data_pagamento else "—")

                # ================= BOTÕES DE AÇÃO =================
                b1, b2 = st.columns([1, 1])
                with b1:
                    if st.button("✅ Finalizar Venda", key="btn_finalizar_venda"):
                        finalizar_venda(
                            forma, forma1, forma2, valor1, valor2, promocoes,
                            nome_cliente=nome_cliente, data_pagamento=data_pagamento,
                            valor_recebido=valor_recebido
                        )
                with b2:
                    if st.button("🆕 Nova Venda", key="btn_nova_venda"):
                        st.session_state["pedido_atual"] = []
                        st.success("Nova venda iniciada!")

                st.markdown("---")
            else:
                st.info("⚠️ Adicione um produto ao pedido para escolher a forma de pagamento.")

            # ================= BOTÃO FECHAR CAIXA =================
            if st.session_state.get("caixa_aberto", False):
                if st.button("📦 Fechar Caixa", key="btn_fechar_caixa"):
                    fechar_caixa()


        # ================= TAB 2 - ÚLTIMAS VENDAS =================
        with tab2:
            st.subheader("📊 Últimas Vendas")
            if not vendas.empty:
                ult = vendas.sort_values(by=["Data", "IDVenda"], ascending=False).head(100)

                colunas = [
                    "IDVenda", "Data", "NomeProduto", "Quantidade", "PrecoUnitario",
                    "Total", "FormaPagamento", "ValorPago1", "ValorPago2"
                ]
                colunas = [c for c in colunas if c in ult.columns]

                st.dataframe(ult[colunas], use_container_width=True, key="df_ultimas_vendas")

                ids = sorted(vendas["IDVenda"].astype(int).unique().tolist(), reverse=True)

                colx, coly = st.columns([3, 1])
                with colx:
                    id_excluir = st.selectbox(
                        "Selecione a venda para excluir (devolve estoque)",
                        ids if ids else [0],
                        key="select_excluir_venda"
                    )
                with coly:
                    if st.button("Excluir venda", key="btn_excluir_venda"):
                        try:
                            id_excluir_int = int(id_excluir)
                        except:
                            id_excluir_int = None

                        if id_excluir_int and id_excluir_int in ids:
                            linhas = vendas[vendas["IDVenda"].astype(int) == id_excluir_int]

                            for _, r in linhas.iterrows():
                                mask = produtos["ID"].astype(str) == str(r["IDProduto"])
                                if mask.any():
                                    produtos.loc[mask, "Quantidade"] = (
                                        produtos.loc[mask, "Quantidade"].astype(int) + int(r["Quantidade"])
                                    ).astype(int)

                            vendas = vendas[vendas["IDVenda"].astype(int) != id_excluir_int]

                            save_csv_github(vendas, ARQ_VENDAS, "Atualizando vendas")
                            save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")

                            st.session_state["vendas"] = vendas
                            st.session_state["produtos"] = produtos

                            st.success(f"Venda {id_excluir_int} excluída e estoque ajustado.")
                            st.rerun()
                        else:
                            st.warning("Venda não encontrada.")
            else:
                st.info("Ainda não há vendas registradas.")


        # ================= TAB 3 - RECIBOS =================
        with tab3:
            import os
            from PIL import Image, UnidentifiedImageError

            st.subheader("📄 Recibos de Vendas")

            if not vendas.empty:
                datas = sorted(vendas["Data"].unique())
                data_sel = st.selectbox("Selecione a data da venda", datas, key="recibo_data")
                vendas_dia = vendas[vendas["Data"] == data_sel]
                ids_dia = sorted(vendas_dia["IDVenda"].unique().tolist())
                id_sel = st.selectbox("Selecione o ID da venda", ids_dia, key="recibo_id")

                if st.button("Gerar Recibo (PDF)", key="btn_recibo"):
                    caminho_pdf = f"recibo_venda_{id_sel}.pdf"
                    gerar_pdf_venda(id_sel, vendas, caminho_pdf)

                    with open(caminho_pdf, "rb") as f:
                        st.download_button(
                            label="⬇️ Baixar Recibo",
                            data=f,
                            file_name=caminho_pdf,
                            mime="application/pdf",
                            key="download_recibo"
                        )

                    logo_candidates = [
                        "logo_docebella.png",
                        "assets/logo_docebella.png",
                        "static/logo_docebella.png",
                        "images/logo_docebella.png",
                    ]
                    logo_path = next((p for p in logo_candidates if os.path.exists(p)), None)

                    if logo_path:
                        try:
                            img = Image.open(logo_path)
                            st.image(img, width=200, caption="Doce Bella")
                        except (UnidentifiedImageError, OSError) as e:
                            st.warning(f"⚠️ Não foi possível abrir a imagem do logo em '{logo_path}': {e}")
                    else:
                        st.warning("⚠️ Arquivo 'logo_docebella.png' não foi encontrado. Coloque o arquivo na pasta do app ou em assets/static/images.")

            else:
                st.info("Nenhuma venda para gerar recibo.")









    # =====================================
# PROMOÇÕES
# =====================================
if view == "Promoções":
    show_logo("main")
    st.header("🏷️ Promoções")
    promocoes = norm_promocoes(pd.DataFrame())

    # --- CADASTRAR ---
    with st.expander("➕ Cadastrar promoção", expanded=False):
        if produtos.empty:
            st.info("Cadastre produtos primeiro para criar promoções.")
        else:
            opcoes_prod = (produtos["ID"].astype(str) + " - " + produtos["Nome"]).tolist()
            sel_prod = st.selectbox("Produto", opcoes_prod, key="promo_cad_produto")
            pid = sel_prod.split(" - ")[0].strip()
            pnome = sel_prod.split(" - ", 1)[1].strip()

            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                desconto_str = st.text_input("Desconto (%)", value="0", key="promo_cad_desc")
            with col2:
                data_ini = st.date_input("Início", value=date.today(), key="promo_cad_inicio")
            with col3:
                data_fim = st.date_input("Término", value=date.today() + timedelta(days=7), key="promo_cad_fim")

            if st.button("Adicionar promoção", key="promo_btn_add"):
                desconto = to_float(desconto_str, 0.0)
                if desconto < 0 or desconto > 100:
                    st.error("O desconto deve estar entre 0 e 100%.")
                elif data_fim < data_ini:
                    st.error("A data de término deve ser maior ou igual à data de início.")
                else:
                    novo = {
                        "ID": prox_id(promocoes, "ID"),
                        "IDProduto": str(pid),
                        "NomeProduto": pnome,
                        "Desconto": float(desconto),
                        "DataInicio": str(data_ini),
                        "DataFim": str(data_fim),
                    }
                    promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)
                    save_csv_github(promocoes, ARQ_PROMOCOES, "Atualizando promoções")
                    st.session_state["promocoes"] = promocoes
                    st.success("Promoção cadastrada!")
                    st.rerun()  # 🔑 atualização imediata

    # --- PRODUTOS PARADOS ---
    st.subheader("📦 Produtos parados sem vendas")
    dias_sem_venda = st.number_input(
        "Considerar parados após quantos dias?",
        min_value=1, max_value=365, value=30, key="promo_dias_sem_venda"
    )

    if not vendas.empty:
        vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
        ultima_venda = vendas.groupby("IDProduto")["Data"].max().reset_index()
        ultima_venda.columns = ["IDProduto", "UltimaVenda"]
    else:
        ultima_venda = pd.DataFrame(columns=["IDProduto", "UltimaVenda"])

    produtos_parados = produtos.merge(ultima_venda, left_on="ID", right_on="IDProduto", how="left")
    produtos_parados["UltimaVenda"].fillna(pd.Timestamp("1900-01-01"), inplace=True)

    limite = datetime.now() - timedelta(days=int(dias_sem_venda))
    produtos_parados = produtos_parados[produtos_parados["UltimaVenda"] < limite]

    if produtos_parados.empty:
        st.info("Nenhum produto parado encontrado nesse período.")
    else:
        st.dataframe(produtos_parados[["ID", "Nome", "Quantidade", "UltimaVenda"]])

        desconto_auto = st.number_input(
            "Desconto automático (%)", min_value=1, max_value=100, value=20, key="promo_desc_auto"
        )
        dias_validade = st.number_input(
            "Duração da promoção (dias)", min_value=1, max_value=90, value=7, key="promo_dias_validade_auto"
        )

        if st.button("🔥 Criar promoção automática para produtos parados", key="promo_btn_auto"):
            for _, row in produtos_parados.iterrows():
                novo = {
                    "ID": prox_id(promocoes, "ID"),
                    "IDProduto": str(row["ID"]),
                    "NomeProduto": row["Nome"],
                    "Desconto": float(desconto_auto),
                    "DataInicio": str(date.today()),
                    "DataFim": str(date.today() + timedelta(days=int(dias_validade))),
                }
                promocoes = pd.concat([promocoes, pd.DataFrame([novo])], ignore_index=True)

            save_csv_github(promocoes, ARQ_PROMOCOES, "Criando promoções automáticas de produtos parados")
            st.session_state["promocoes"] = promocoes
            st.success(f"Promoções criadas para {len(produtos_parados)} produtos parados!")
            st.rerun()  # 🔑 atualização imediata

    # --- LISTA DE PROMOÇÕES ---
    st.markdown("### Lista de promoções")
    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        st.dataframe(promocoes, use_container_width=True)

        # --- EDITAR ---
        with st.expander("✏️ Editar promoção", expanded=False):
            ids = promocoes["ID"].astype(str).tolist()
            sel = st.selectbox("Selecione a promoção", ids, key="promo_edit_id") if ids else None
            if sel:
                linha = promocoes[promocoes["ID"].astype(str) == sel]
                if not linha.empty:
                    ln = linha.iloc[0]
                    opcoes_prod = (produtos["ID"].astype(str) + " - " + produtos["Nome"]).tolist()
                    pre_opcao = (
                        f"{ln['IDProduto']} - {ln['NomeProduto']}"
                        if f"{ln['IDProduto']} - {ln['NomeProduto']}" in opcoes_prod
                        else opcoes_prod[0]
                    )
                    sel_prod_edit = st.selectbox(
                        "Produto (editar)", opcoes_prod,
                        index=opcoes_prod.index(pre_opcao),
                        key=f"promo_edit_prod_{sel}"
                    )
                    pid_e = sel_prod_edit.split(" - ")[0].strip()
                    pnome_e = sel_prod_edit.split(" - ", 1)[1].strip()

                    col1, col2, col3 = st.columns([1, 1, 1])
                    with col1:
                        desc_e = st.text_input("Desconto (%)", value=str(ln["Desconto"]), key=f"promo_edit_desc_{sel}")
                    with col2:
                        try:
                            di = parse_date_yyyy_mm_dd(ln["DataInicio"]) or date.today()
                        except Exception:
                            di = date.today()
                        data_ini_e = st.date_input("Início", value=di, key=f"promo_edit_inicio_{sel}")
                    with col3:
                        try:
                            df = parse_date_yyyy_mm_dd(ln["DataFim"]) or (date.today() + timedelta(days=7))
                        except Exception:
                            df = date.today() + timedelta(days=7)
                        data_fim_e = st.date_input("Término", value=df, key=f"promo_edit_fim_{sel}")

                    if st.button("Salvar edição", key=f"promo_btn_edit_{sel}"):
                        dnum = to_float(desc_e, 0.0)
                        if dnum < 0 or dnum > 100:
                            st.error("O desconto deve estar entre 0 e 100%.")
                        elif data_fim_e < data_ini_e:
                            st.error("A data de término deve ser maior ou igual à data de início.")
                        else:
                            idx = promocoes["ID"].astype(str) == sel
                            promocoes.loc[idx, ["IDProduto", "NomeProduto", "Desconto", "DataInicio", "DataFim"]] = [
                                str(pid_e), pnome_e, float(dnum), str(data_ini_e), str(data_fim_e)
                            ]
                            save_csv_github(promocoes, ARQ_PROMOCOES, "Atualizando promoções")
                            st.session_state["promocoes"] = promocoes
                            st.success("Promoção atualizada!")
                            st.rerun()  # 🔑 atualização imediata

        # --- EXCLUIR ---
        with st.expander("🗑️ Excluir promoção", expanded=False):
            del_id = st.selectbox(
                "Selecione ID para excluir", promocoes["ID"].astype(str).tolist(), key="promo_del_id"
            )
            if st.button("Excluir promoção", key="promo_btn_del"):
                promocoes = promocoes[promocoes["ID"].astype(str) != del_id]
                save_csv_github(promocoes, ARQ_PROMOCOES, "Atualizando promoções")
                st.session_state["promocoes"] = promocoes
                st.warning(f"Promoção {del_id} excluída!")
                st.rerun()  # 🔑 atualização imediata


         # =====================================
# CLIENTES
# =====================================
if view == "Clientes":
    show_logo("main")
    st.header("👥 Clientes")

    clientes = norm_clientes(clientes) if "clientes" in st.session_state else clientes

    # --- CADASTRAR ---
    with st.expander("➕ Cadastrar cliente", expanded=False):
        col1, col2 = st.columns([2, 1])
        with col1:
            nome_cliente = st.text_input("Nome do cliente", key="cli_nome")
        with col2:
            telefone = st.text_input("Telefone", key="cli_tel")

        col3, col4 = st.columns([1, 1])
        with col3:
            data_prev = st.date_input("Data prevista pagamento", value=date.today() + timedelta(days=7), key="cli_data")
        with col4:
            status = st.selectbox("Status", ["Aberto", "Pago"], key="cli_status")

        if st.button("Adicionar cliente", key="cli_add_btn"):
            novo = {
                "ID": prox_id(clientes, "ID"),
                "Cliente": nome_cliente.strip(),
                "Telefone": telefone.strip(),
                "Produto": "",
                "Valor": 0.0,
                "Data": str(date.today()),
                "DataPrevista": str(data_prev),
                "Status": status,
                "CodigoBarras": "",
                "FormaPagamento": ""
            }
            clientes = pd.concat([clientes, pd.DataFrame([novo])], ignore_index=True)
            st.session_state["clientes"] = clientes
            save_csv_github(clientes, ARQ_CLIENTES, "Novo cliente cadastrado")
            st.success("Cliente adicionado com sucesso!")
            st.rerun()

    # --- LISTA DE CLIENTES ---
    st.subheader("📋 Lista de clientes")
    if clientes.empty:
        st.info("Nenhum cliente cadastrado ainda.")
    else:
        st.dataframe(clientes, use_container_width=True)

    # --- EDITAR ---
    with st.expander("✏️ Editar cliente", expanded=False):
        ids = clientes["ID"].astype(str).tolist()
        sel = st.selectbox("Selecione o cliente", ids, key="cli_edit_sel") if ids else None
        if sel:
            linha = clientes[clientes["ID"].astype(str) == sel]
            if not linha.empty:
                ln = linha.iloc[0]
                nome_e = st.text_input("Nome", value=ln["Cliente"], key=f"cli_nome_{sel}")
                tel_e = st.text_input("Telefone", value=ln.get("Telefone", ""), key=f"cli_tel_{sel}")
                status_e = st.selectbox("Status", ["Aberto", "Pago"], index=(0 if ln["Status"] == "Aberto" else 1), key=f"cli_status_{sel}")
                data_prev_e = st.date_input("Data prevista", value=pd.to_datetime(ln.get("DataPrevista", date.today())), key=f"cli_data_{sel}")

                if st.button("Salvar edição", key=f"cli_btn_edit_{sel}"):
                    idx = clientes["ID"].astype(str) == sel
                    clientes.loc[idx, ["Cliente", "Telefone", "Status", "DataPrevista"]] = [
                        nome_e.strip(), tel_e.strip(), status_e, str(data_prev_e)
                    ]
                    save_csv_github(clientes, ARQ_CLIENTES, "Atualizando cliente")
                    st.session_state["clientes"] = clientes
                    st.success("Cliente atualizado!")
                    st.rerun()

    # --- EXCLUIR ---
    with st.expander("🗑️ Excluir cliente", expanded=False):
        del_id = st.selectbox("Selecione ID para excluir", clientes["ID"].astype(str).tolist(), key="cli_del_sel")
        if st.button("Excluir cliente", key="cli_btn_del"):
            clientes = clientes[clientes["ID"].astype(str) != del_id]
            save_csv_github(clientes, ARQ_CLIENTES, "Excluindo cliente")
            st.session_state["clientes"] = clientes
            st.warning(f"Cliente {del_id} excluído!")
            st.rerun()









# =====================================
# PRECIFICAÇÃO
# =====================================
import streamlit as st
import pandas as pd
import pdfplumber
import re
import datetime

# ===============================
# Função para baixar CSV
# ===============================
def baixar_csv(df, filename="dados.csv"):
    """
    Gera um botão de download para baixar o DataFrame como CSV.
    """
    if df is not None and not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label=f"📥 Baixar {filename}",
            data=csv,
            file_name=filename,
            mime="text/csv",
        )
    else:
        st.warning("⚠️ Nenhum dado disponível para exportar.")

# ===============================
# Função para carregar CSV do GitHub
# ===============================
def load_csv_github(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"❌ Erro ao carregar CSV do GitHub: {e}")
        return pd.DataFrame()

# segurança: define view padrão
view = st.session_state.get("view", "precificação")

if view == "precificação":
    st.title("💄 Precificador de Produtos")

    url_precificacao = "https://raw.githubusercontent.com/ribeiromendes5014-design/minha-loja/main/precificacao.csv"

    # ===============================
    # Funções de processamento e exibição
    # ===============================
    def extrair_produtos_pdf(pdf_file):
        produtos = []
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                texto = page.extract_text()
                if not texto:
                    continue
                linhas = texto.split("\n")
                buffer_nome = []
                for linha in linhas:
                    linha = linha.strip()
                    match = re.search(r"R\$?\s*([\d,.]+)\s+(\d+)\s+\w*\s*R\$?\s*([\d,.]+)", linha)
                    if match:
                        preco_unit = float(match.group(1).replace(",", "."))
                        qtd = int(match.group(2))
                        subtotal = float(match.group(3).replace(",", "."))
                        nome = " ".join(buffer_nome).strip()
                        buffer_nome = []
                        produtos.append({
                            "Produto": nome,
                            "Qtd": qtd,
                            "Custo Unitário": preco_unit,
                            "Subtotal": subtotal
                        })
                    else:
                        if not re.search(r"R\$|\d", linha):
                            buffer_nome.append(linha)
        return produtos

    def processar_dataframe(df, frete, custos_extras, modo_margem, margem_fixa_sidebar=30.0):
        df_processado = df.copy()
        total_itens = df_processado["Qtd"].sum()
        rateio_unit = (frete + custos_extras) / total_itens if total_itens > 0 else 0
        df_processado["Custo c/ Rateio"] = (
            df_processado["Custo Unitário"] 
            + rateio_unit 
            + df_processado.get("Custos Extras Produto", 0)
        ).round(2)

        if modo_margem == "Margem fixa":
            df_processado["Margem (%)"] = margem_fixa_sidebar

        df_processado["Preço à Vista"] = (
            df_processado["Custo c/ Rateio"] * (1 + df_processado["Margem (%)"] / 100)
        ).round(2)
        df_processado["Preço no Cartão"] = (
            df_processado["Preço à Vista"] / 0.8872
        ).round(2)

        return df_processado

    def exibir_resultados(df):
        if not df.empty:
            custo_total = (df["Custo c/ Rateio"] * df["Qtd"]).sum()
            faturamento_vista = (df["Preço à Vista"] * df["Qtd"]).sum()
            lucro_total = faturamento_vista - custo_total

            col1, col2, col3 = st.columns(3)
            col1.metric("Custo Total", f"R$ {custo_total:,.2f}")
            col2.metric("Faturamento Previsto", f"R$ {faturamento_vista:,.2f}")
            col3.metric("Lucro Estimado", f"R$ {lucro_total:,.2f}")

            st.dataframe(
                df[["Produto", "Qtd", "Custo c/ Rateio", "Margem (%)", "Preço à Vista", "Preço no Cartão"]],
                use_container_width=True
            )

            nome_arquivo = f"precificacao_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            baixar_csv(df, nome_arquivo)

    # ===============================
    # Estado da sessão
    # ===============================
    if "produtos_manuais" not in st.session_state:
        st.session_state.produtos_manuais = pd.DataFrame(
            columns=["Produto", "Qtd", "Custo Unitário", "Custos Extras Produto", "Margem (%)"]
        )
    if "rateio_manual" not in st.session_state:
        st.session_state["rateio_manual"] = 0.0

    # ===============================
    # Variáveis fixas
    # ===============================
    frete_total = 0.0
    custos_extras = 0.0
    modo_margem_global = "Margem fixa"
    margem_fixa_sidebar = 30.0

    # ===============================
    # URL do CSV do GitHub
    # ===============================
    ARQ_CAIXAS = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/precificacao.csv"

    tab_pdf, tab_manual, tab_github = st.tabs([
        "📄 Precificador PDF",
        "✍️ Precificador Manual",
        "📥 Carregar CSV do GitHub"
    ])

    # === Tab PDF ===
    with tab_pdf:
        st.markdown("---")
        pdf_file = st.file_uploader("📤 Selecione o PDF da nota fiscal ou lista de compras", type=["pdf"])
        if pdf_file:
            try:
                produtos_pdf = extrair_produtos_pdf(pdf_file)
                if not produtos_pdf:
                    st.warning("⚠️ Nenhum produto encontrado no PDF.")
                else:
                    df_pdf = pd.DataFrame(produtos_pdf)
                    df_pdf["Custos Extras Produto"] = 0.0
                    st.session_state.df_produtos_geral = processar_dataframe(
                        df_pdf, frete_total, custos_extras, modo_margem_global, margem_fixa_sidebar
                    )
                    st.success("✅ Produtos precificados com sucesso!")
                    exibir_resultados(st.session_state.df_produtos_geral)
            except Exception as e:
                st.error(f"❌ Erro ao processar o PDF: {e}")
        else:
            st.info("📄 Faça upload de um arquivo PDF para começar.")
            if st.button("📥 Carregar CSV de exemplo"):
                df_exemplo = load_csv_github(ARQ_CAIXAS)
                if not df_exemplo.empty:
                    df_exemplo["Custos Extras Produto"] = 0.0
                    st.session_state.df_produtos_geral = processar_dataframe(
                        df_exemplo, frete_total, custos_extras, modo_margem_global, margem_fixa_sidebar
                    )
                    exibir_resultados(st.session_state.df_produtos_geral)

    # === Tab Manual ===
    with tab_manual:
        st.markdown("---")
        aba_prec_manual, aba_rateio = st.tabs(["✍️ Novo Produto Manual", "🔢 Rateio Manual"])

        with aba_rateio:
            st.subheader("🔢 Cálculo de Rateio Unitário (Frete + Custos Extras)")
            col_r1, col_r2, col_r3 = st.columns(3)
            with col_r1:
                frete_manual = st.number_input("🚚 Frete Total (R$)", min_value=0.0, step=0.01, key="frete_manual")
            with col_r2:
                extras_manual = st.number_input("🛠 Custos Extras (R$)", min_value=0.0, step=0.01, key="extras_manual")
            with col_r3:
                qtd_total_manual = st.number_input("📦 Quantidade Total de Produtos", min_value=1, step=1, key="qtd_total_manual")

            rateio_calculado = (frete_manual + extras_manual) / qtd_total_manual
            st.session_state["rateio_manual"] = round(rateio_calculado, 4)
            st.markdown(f"💰 **Rateio Unitário Calculado:** R$ {rateio_calculado:,.4f}")

        with aba_prec_manual:
            st.subheader("Adicionar novo produto")

            col1, col2 = st.columns(2)
            with col1:
                produto = st.text_input("📝 Nome do Produto")
                quantidade = st.number_input("📦 Quantidade", min_value=1, step=1)
                valor_pago = st.number_input("💰 Valor Pago (R$)", min_value=0.0, step=0.01)
            with col2:
                valor_default_rateio = st.session_state.get("rateio_manual", 0.0)
                custo_extra_produto = st.number_input(
                    "💰 Custos extras do Produto (R$)", min_value=0.0, step=0.01, value=valor_default_rateio
                )
                preco_final_sugerido = st.number_input(
                    "💸 Valor Final Sugerido (Preço à Vista) (R$)", min_value=0.0, step=0.01
                )

                margem_manual = 0.0
                if preco_final_sugerido > 0:
                    custo_total_unitario = valor_pago + custo_extra_produto
                    margem_calculada = max(
                        0.0, (preco_final_sugerido / custo_total_unitario - 1) * 100
                    ) if custo_total_unitario > 0 else 0.0
                    margem_manual = round(margem_calculada, 2)
                    st.info(f"🧮 Margem calculada automaticamente: {margem_manual:.2f}%")
                else:
                    margem_manual = st.number_input("🧮 Margem de Lucro (%)", min_value=0.0, value=30.0)

            custo_total_unitario = valor_pago + custo_extra_produto
            preco_a_vista_calc = custo_total_unitario * (1 + margem_manual / 100)
            preco_no_cartao_calc = preco_a_vista_calc / 0.8872

            st.markdown(f"**Preço à Vista Calculado:** R$ {preco_a_vista_calc:,.2f}")
            st.markdown(f"**Preço no Cartão Calculado:** R$ {preco_no_cartao_calc:,.2f}")

            with st.form("form_submit"):
                adicionar_produto = st.form_submit_button("➕ Adicionar Produto")
                if adicionar_produto:
                    if produto and quantidade > 0 and valor_pago >= 0:
                        novo_produto = pd.DataFrame([{
                            "Produto": produto,
                            "Qtd": quantidade,
                            "Custo Unitário": valor_pago,
                            "Custos Extras Produto": custo_extra_produto,
                            "Margem (%)": margem_manual
                        }])
                        st.session_state.produtos_manuais = pd.concat(
                            [st.session_state.produtos_manuais, novo_produto], ignore_index=True
                        )
                        st.success("✅ Produto adicionado!")
                    else:
                        st.warning("⚠️ Preencha todos os campos obrigatórios.")

            if not st.session_state.produtos_manuais.empty:
                df_manual = st.session_state.produtos_manuais.copy()
                df_editavel = st.data_editor(df_manual, use_container_width=True, num_rows="dynamic")
                st.session_state.produtos_manuais = df_editavel.copy()
                st.session_state.df_produtos_geral = processar_dataframe(
                    st.session_state.produtos_manuais,
                    frete_total,
                    custos_extras,
                    modo_margem_global,
                    margem_fixa_sidebar
                )
                exibir_resultados(st.session_state.df_produtos_geral)

    # === Tab GitHub ===
    with tab_github:
        st.markdown("---")
        st.header("📥 Carregar CSV de Precificação do GitHub")
        if st.button("🔄 Carregar CSV do GitHub"):
            df_exemplo = load_csv_github(ARQ_CAIXAS)
            if not df_exemplo.empty:
                df_exemplo["Custos Extras Produto"] = 0.0
                df_processado = processar_dataframe(
                    df_exemplo, frete_total, custos_extras, modo_margem_global, margem_fixa_sidebar
                )
                st.success("✅ CSV carregado e processado com sucesso!")
                exibir_resultados(df_processado)
            else:
                st.warning("⚠️ Não foi possível carregar o CSV do GitHub.")









  



import streamlit as st
import pandas as pd
import requests
from io import StringIO


# Inicializando as abas
aba_campos, aba_insumos, aba_produtos = st.tabs(["Campos (Colunas)", "Insumos", "Produtos"])

# ==============================
# Aba Campos (gerencia colunas extras)
# ==============================
with aba_campos:
    st.header("Campos / Colunas Personalizadas")

    with st.form("form_add_campo"):
        st.subheader("Adicionar novo campo")
        nome_campo = st.text_input("Nome do Campo (será o nome da coluna)")
        aplicacao = st.selectbox("Aplicação", ["Insumos", "Produtos", "Ambos"])
        tipo = st.selectbox("Tipo", ["Texto", "Número", "Seleção"])
        opcoes = st.text_input("Opções (se 'Seleção', separe por vírgula)")
        adicionar = st.form_submit_button("Adicionar Campo")

        if adicionar:
            if not nome_campo.strip():
                st.warning("Informe um nome de campo válido.")
            else:
                ja_existe = (
                    (st.session_state.campos["Campo"].astype(str).str.lower() == nome_campo.strip().lower())
                    & (st.session_state.campos["Aplicação"] == aplicacao)
                ).any()
                if ja_existe:
                    st.warning("Já existe um campo com esse nome para essa aplicação.")
                else:
                    nova_linha = {"Campo": nome_campo.strip(), "Aplicação": aplicacao, "Tipo": tipo, "Opções": opcoes}
                    st.session_state.campos = pd.concat(
                        [st.session_state.campos, pd.DataFrame([nova_linha])],
                        ignore_index=True
                    )
                    if aplicacao in ("Insumos", "Ambos"):
                        if nome_campo not in st.session_state.insumos.columns:
                            st.session_state.insumos[nome_campo] = ""
                    if aplicacao in ("Produtos", "Ambos"):
                        if nome_campo not in st.session_state.produtos.columns:
                            st.session_state.produtos[nome_campo] = ""
                    st.success(f"Campo '{nome_campo}' adicionado para {aplicacao}!")
                    st.rerun()

    st.markdown("### Campos cadastrados")
    if st.session_state.campos.empty:
        st.info("Nenhum campo extra cadastrado ainda.")
    else:
        st.dataframe(st.session_state.campos, use_container_width=True)

    # Editar/Excluir Campo
    if not st.session_state.campos.empty:
        st.divider()
        st.subheader("Editar ou Excluir campo")

        rotulos = [
            f"{row.Campo}  ·  ({row.Aplicação})"
            for _, row in st.session_state.campos.iterrows()
        ]
        escolha = st.selectbox("Escolha um campo", [""] + rotulos)

        if escolha:
            idx = rotulos.index(escolha)
            campo_atual = st.session_state.campos.iloc[idx]

            acao_campo = st.radio(
                "Ação",
                ["Nenhuma", "Editar", "Excluir"],
                horizontal=True,
                key=f"acao_campo_{idx}"
            )

            if acao_campo == "Excluir":
                if st.button("Confirmar Exclusão", key=f"excluir_campo_{idx}"):
                    nome = campo_atual["Campo"]
                    aplic = campo_atual["Aplicação"]

                    st.session_state.campos = st.session_state.campos.drop(st.session_state.campos.index[idx]).reset_index(drop=True)

                    if aplic in ("Insumos", "Ambos"):
                        if nome in st.session_state.insumos.columns:
                            st.session_state.insumos = st.session_state.insumos.drop(columns=[nome])
                    if aplic in ("Produtos", "Ambos"):
                        if nome in st.session_state.produtos.columns:
                            st.session_state.produtos = st.session_state.produtos.drop(columns=[nome])

                    st.success(f"Campo '{nome}' removido de {aplic}!")
                    st.rerun()

            if acao_campo == "Editar":
                with st.form(f"form_edit_campo_{idx}"):
                    novo_nome = st.text_input("Nome do Campo", value=str(campo_atual["Campo"]))
                    nova_aplic = st.selectbox("Aplicação", ["Insumos", "Produtos", "Ambos"], index=["Insumos", "Produtos", "Ambos"].index(campo_atual["Aplicação"]))
                    novo_tipo = st.selectbox("Tipo", ["Texto", "Número", "Seleção"], index=["Texto", "Número", "Seleção"].index(campo_atual["Tipo"]))
                    novas_opcoes = st.text_input("Opções (se 'Seleção')", value=str(campo_atual["Opções"]) if pd.notna(campo_atual["Opções"]) else "")

                    salvar = st.form_submit_button("Salvar Alterações")

                    if salvar:
                        nome_antigo = campo_atual["Campo"]
                        aplic_antiga = campo_atual["Aplicação"]

                        st.session_state.campos.loc[st.session_state.campos.index[idx], ["Campo", "Aplicação", "Tipo", "Opções"]] = [
                            novo_nome, nova_aplic, novo_tipo, novas_opcoes
                        ]

                        renomeou = (str(novo_nome).strip() != str(nome_antigo).strip())
                        if renomeou:
                            if aplic_antiga in ("Insumos", "Ambos") and nome_antigo in st.session_state.insumos.columns:
                                st.session_state.insumos = st.session_state.insumos.rename(columns={nome_antigo: novo_nome})
                            if aplic_antiga in ("Produtos", "Ambos") and nome_antigo in st.session_state.produtos.columns:
                                st.session_state.produtos = st.session_state.produtos.rename(columns={nome_antigo: novo_nome})

                        if nova_aplic in ("Insumos", "Ambos"):
                            if novo_nome not in st.session_state.insumos.columns:
                                st.session_state.insumos[novo_nome] = ""
                        if nova_aplic in ("Produtos", "Ambos"):
                            if novo_nome not in st.session_state.produtos.columns:
                                st.session_state.produtos[novo_nome] = ""

                        st.success("Campo atualizado!")
                        st.rerun()

        st.divider()
        # Função para baixar CSV
        baixar_csv(st.session_state.campos, "campos_papelaria.csv")

# Definir PRODUTOS_BASE_COLS
PRODUTOS_BASE_COLS = ["Produto", "Custo Total", "Preço à Vista", "Preço no Cartão", "Margem (%)"]

# Inicializando produtos, caso não tenha sido feito ainda
if 'produtos' not in st.session_state:
    st.session_state.produtos = pd.DataFrame(columns=PRODUTOS_BASE_COLS)

# Inicializando produtos, caso não tenha sido feito ainda
if 'produtos' not in st.session_state:
    st.session_state.produtos = pd.DataFrame(columns=PRODUTOS_BASE_COLS)

# =====================================
# Aba Produtos
# =====================================
with aba_produtos:
    st.header("Montar Produto")

    # Verifica se há insumos cadastrados
    if st.session_state.insumos.empty:
        st.warning("Cadastre insumos primeiro na aba 'Insumos'.")
    else:
        with st.form("form_montar_produto"):
            st.subheader("Novo Produto")

            nome_produto = st.text_input("Nome do Produto")

            st.markdown("### Insumos utilizados")
            insumos_disponiveis = st.session_state.insumos["Nome"].dropna().unique().tolist()
            insumos_selecionados = st.multiselect(
                "Selecione os insumos utilizados",
                options=insumos_disponiveis,
            )

            insumos_utilizados = []
            custo_total_insumos = 0.0

            for i, insumo in enumerate(insumos_selecionados):
                col1, col2 = st.columns([3, 2])
                with col1:
                    st.markdown(f"**{insumo}**")
                with col2:
                    qtd = st.number_input(f"Quantidade de '{insumo}'", min_value=0.0, step=1.0, key=f"qtd_insumo_{i}")

                preco_unitario = st.session_state.insumos.loc[
                    st.session_state.insumos["Nome"] == insumo, "Preço Unitário (R$)"
                ].values[0]

                subtotal = qtd * preco_unitario
                custo_total_insumos += subtotal

                insumos_utilizados.append({
                    "nome": insumo,
                    "quantidade": qtd,
                    "preco_unitario": preco_unitario,
                    "subtotal": subtotal
                })

            st.markdown("### Mão de obra")
            tempo_horas = st.number_input("Tempo de produção (horas)", min_value=0.0, value=1.0, step=0.5)
            valor_hora = st.number_input("Valor da hora (R$)", min_value=0.0, value=20.0, step=1.0)
            custo_mao_obra = tempo_horas * valor_hora

            # Cálculo total
            custo_total = custo_total_insumos + custo_mao_obra
            st.markdown(f"**Custo Total: R$ {custo_total:.2f}**")

            margem = st.number_input("Margem de Lucro (%)", min_value=0.0, value=50.0, step=1.0)
            preco_venda = custo_total * (1 + margem / 100)
            preco_cartao = preco_venda * 1.05  # 5% taxa de cartão

            st.markdown(f"**Preço à Vista sugerido: R$ {preco_venda:.2f}**")
            st.markdown(f"**Preço no Cartão sugerido (5%): R$ {preco_cartao:.2f}**")

            salvar = st.form_submit_button("Salvar Produto")

            if salvar:
                if not nome_produto.strip():
                    st.warning("Informe um nome para o produto.")
                elif not insumos_utilizados:
                    st.warning("Selecione ao menos um insumo.")
                else:
                    novo_produto = {
                        "Produto": nome_produto.strip(),
                        "Custo Total": round(custo_total, 2),
                        "Preço à Vista": round(preco_venda, 2),
                        "Preço no Cartão": round(preco_cartao, 2),
                        "Margem (%)": margem,
                    }

                    # Adicionando as colunas base, se não existirem
                    for col in PRODUTOS_BASE_COLS:
                        if col not in st.session_state.produtos.columns:
                            st.session_state.produtos[col] = ""

                    # Adicionando o novo produto
                    st.session_state.produtos = pd.concat([
                        st.session_state.produtos,
                        pd.DataFrame([novo_produto])
                    ], ignore_index=True)

                    st.success(f"Produto '{nome_produto}' salvo com sucesso!")
                    st.rerun()

    # =====================================
    # Exibição e edição/exclusão de produtos
    # =====================================
    st.markdown("### Produtos cadastrados")
    
    # Verificando se a coluna 'Produto' existe
    if 'Produto' in st.session_state.produtos.columns:
        st.dataframe(
            st.session_state.produtos.reindex(columns=PRODUTOS_BASE_COLS + [c for c in st.session_state.produtos.columns if c not in PRODUTOS_BASE_COLS]),
            use_container_width=True
        )

        produto_selecionado = st.selectbox(
            "Selecione um produto",
            [""] + st.session_state.produtos["Produto"].astype(str).fillna("").tolist()
        )
    else:
        produto_selecionado = None
        st.warning("Nenhum produto cadastrado ainda.")

    if produto_selecionado:
        acao_produto = st.radio(
            f"Ação para '{produto_selecionado}'",
            ["Nenhuma", "Editar", "Excluir"],
            horizontal=True,
            key=f"acao_produto_{produto_selecionado}"
        )

        idxs_prod = st.session_state.produtos.index[st.session_state.produtos["Produto"] == produto_selecionado].tolist()
        idx_prod = idxs_prod[0] if idxs_prod else None

        if acao_produto == "Excluir" and idx_prod is not None:
            if st.button("Confirmar Exclusão", key=f"excluir_produto_{idx_prod}"):
                st.session_state.produtos = st.session_state.produtos.drop(index=idx_prod).reset_index(drop=True)
                st.success(f"Produto '{produto_selecionado}' removido!")
                st.rerun()

        if acao_produto == "Editar" and idx_prod is not None:
            atual_produto = st.session_state.produtos.loc[idx_prod]
            with st.form(f"form_edit_produto_{idx_prod}"):
                novo_nome_produto = st.text_input("Nome do Produto", value=str(atual_produto.get("Produto", "")))
                novo_custo = st.number_input("Custo Total", min_value=0.0, format="%.2f", value=float(atual_produto.get("Custo Total", 0.0)))
                nova_margem = st.number_input("Margem de Lucro (%)", min_value=0.0, format="%.2f", value=float(atual_produto.get("Margem (%)", 0.0)))

                novo_preco_venda = novo_custo * (1 + nova_margem / 100)
                novo_preco_cartao = novo_preco_venda * 1.05

                st.markdown(f"**Preço à Vista sugerido: R$ {novo_preco_venda:.2f}**")
                st.markdown(f"**Preço no Cartão sugerido (5%): R$ {novo_preco_cartao:.2f}**")

                salvou_prod = st.form_submit_button("Salvar Alterações", key=f"salvar_produto_{idx_prod}")
                if salvou_prod:
                    st.session_state.produtos.loc[idx_prod, "Produto"] = novo_nome_produto
                    st.session_state.produtos.loc[idx_prod, "Custo Total"] = round(novo_custo, 2)
                    st.session_state.produtos.loc[idx_prod, "Margem (%)"] = nova_margem
                    st.session_state.produtos.loc[idx_prod, "Preço à Vista"] = round(novo_preco_venda, 2)
                    st.session_state.produtos.loc[idx_prod, "Preço no Cartão"] = round(novo_preco_cartao, 2)
                    st.success("Produto atualizado!")
                    st.rerun()

    # Adiciona o botão de download do CSV
    baixar_csv(st.session_state.produtos, "produtos_papelaria.csv")

    
    
   # =====================================
# Função auxiliar para garantir colunas
# =====================================
def garantir_colunas_extras(df, tipo="Insumos"):
    """
    Garante que o DataFrame tenha as colunas base + extras necessárias.
    Se não existirem, cria com valores padrão.
    """
    if df is None or df.empty:
        df = pd.DataFrame()

    if tipo == "Insumos":
        colunas_necessarias = ["Nome", "Categoria", "Unidade", "Preço Unitário (R$)"]
    elif tipo == "Produtos":
        colunas_necessarias = ["Produto", "Qtd", "Custo Unitário", "Custos Extras Produto", "Margem (%)"]
    else:
        colunas_necessarias = []

    for col in colunas_necessarias:
        if col not in df.columns:
            if col in ["Nome", "Categoria", "Unidade", "Produto"]:
                df[col] = ""
            elif col in ["Qtd"]:
                df[col] = 0
            else:
                df[col] = 0.0

    return df


# =====================================
# Aba Insumos
# =====================================
with aba_insumos:
    st.header("Insumos")

    # Garante colunas extras atuais
    st.session_state.insumos = garantir_colunas_extras(st.session_state.insumos, "Insumos")

    with st.form("form_add_insumo"):
        st.subheader("Adicionar novo insumo")

        nome_insumo = st.text_input("Nome do Insumo")
        categoria_insumo = st.text_input("Categoria")
        unidade_insumo = st.text_input("Unidade de Medida (ex: un, kg, m)")
        preco_insumo = st.number_input("Preço Unitário (R$)", min_value=0.0, format="%.2f")

        # Campos extras
        extras_insumos = col_defs_para("Insumos")
        valores_extras = {}
        if not extras_insumos.empty:
            st.markdown("**Campos extras**")
            for i, row in extras_insumos.reset_index(drop=True).iterrows():
                key = f"novo_insumo_extra_{row['Campo']}"
                valores_extras[row["Campo"]] = render_input_por_tipo(
                    label=row["Campo"],
                    tipo=row["Tipo"],
                    opcoes=row["Opções"],
                    valor_padrao=None,
                    key=key
                )

        adicionou = st.form_submit_button("Adicionar Insumo")
        if adicionou:
            if not nome_insumo.strip():
                st.warning("Informe o Nome do Insumo.")
            else:
                novo = {
                    "Nome": nome_insumo.strip(),
                    "Categoria": categoria_insumo.strip(),
                    "Unidade": unidade_insumo.strip(),
                    "Preço Unitário (R$)": float(preco_insumo),
                }
                # Adiciona extras
                for k, v in valores_extras.items():
                    novo[k] = v
                # Garante todas as colunas
                todas_cols = list(dict.fromkeys(INSUMOS_BASE_COLS + extras_insumos["Campo"].tolist()))
                st.session_state.insumos = st.session_state.insumos.reindex(
                    columns=list(set(st.session_state.insumos.columns) | set(todas_cols))
                )
                st.session_state.insumos = pd.concat(
                    [st.session_state.insumos, pd.DataFrame([novo])], ignore_index=True
                )
                st.success(f"Insumo '{nome_insumo}' adicionado!")
                st.rerun()

    st.markdown("### Insumos cadastrados")
    # Exibe reordenando: base + extras
    ordem_cols = INSUMOS_BASE_COLS + [c for c in st.session_state.insumos.columns if c not in INSUMOS_BASE_COLS]
    st.dataframe(st.session_state.insumos.reindex(columns=ordem_cols), use_container_width=True)

    # Seleção para editar/excluir
    if not st.session_state.insumos.empty:
        insumo_selecionado = st.selectbox(
            "Selecione um insumo",
            [""] + st.session_state.insumos["Nome"].astype(str).fillna("").tolist()
        )
    else:
        insumo_selecionado = None

    if insumo_selecionado:
        acao_insumo = st.radio(
            f"Ação para '{insumo_selecionado}'",
            ["Nenhuma", "Editar", "Excluir"],
            horizontal=True,
            key=f"acao_insumo_{insumo_selecionado}"
        )

        # Localiza primeira ocorrência (simples)
        idxs = st.session_state.insumos.index[st.session_state.insumos["Nome"] == insumo_selecionado].tolist()
        idx = idxs[0] if idxs else None

        if acao_insumo == "Excluir" and idx is not None:
            if st.button("Confirmar Exclusão", key=f"excluir_insumo_{idx}"):
                st.session_state.insumos = st.session_state.insumos.drop(index=idx).reset_index(drop=True)
                st.success(f"Insumo '{insumo_selecionado}' removido!")
                st.rerun()

        if acao_insumo == "Editar" and idx is not None:
            atual = st.session_state.insumos.loc[idx]
            with st.form(f"form_edit_insumo_{idx}"):
                novo_nome = st.text_input("Nome do Insumo", value=str(atual.get("Nome","")))
                nova_categoria = st.text_input("Categoria", value=str(atual.get("Categoria","")))
                nova_unidade = st.text_input("Unidade de Medida (ex: un, kg, m)", value=str(atual.get("Unidade","")))
                novo_preco = st.number_input(
                    "Preço Unitário (R$)", min_value=0.0, format="%.2f",
                    value=float(atual.get("Preço Unitário (R$)", 0.0))
                )

                # Edita extras
                valores_extras_edit = {}
                extras_insumos = col_defs_para("Insumos")
                if not extras_insumos.empty:
                    st.markdown("**Campos extras**")
                    for i, row in extras_insumos.reset_index(drop=True).iterrows():
                        campo = row["Campo"]
                        key = f"edit_insumo_extra_{idx}_{campo}"
                        valores_extras_edit[campo] = render_input_por_tipo(
                            label=campo,
                            tipo=row["Tipo"],
                            opcoes=row["Opções"],
                            valor_padrao=atual.get(campo, ""),
                            key=key
                        )

                salvou = st.form_submit_button("Salvar Alterações", key=f"salvar_insumo_{idx}")
                if salvou:
                    st.session_state.insumos.loc[idx, "Nome"] = novo_nome
                    st.session_state.insumos.loc[idx, "Categoria"] = nova_categoria
                    st.session_state.insumos.loc[idx, "Unidade"] = nova_unidade
                    st.session_state.insumos.loc[idx, "Preço Unitário (R$)"] = float(novo_preco)
                    for k, v in valores_extras_edit.items():
                        st.session_state.insumos.loc[idx, k] = v
                    st.success("Insumo atualizado!")
                    st.rerun()

    baixar_csv(st.session_state.insumos, "insumos_papelaria.csv")









        


# =====================================
# Views principais
# =====================================

if view == "Dashboard":
    st.write("🏠 Dashboard em construção...")

elif view == "Produtos":
    st.write("📦 Produtos em construção...")

elif view == "precificação":
    # Aqui você cola o código da aba Precificação que já implementou
    st.write("⚙️ Precificação em construção...")

elif view == "Papelaria":
    papelaria_aba()

elif view == "Vendas":
    st.write("🛒 Vendas em construção...")

elif view == "Clientes":
    st.write("👥 Clientes em construção...")

elif view == "Promoções":
    st.write("🏷️ Promoções em construção...")
      


