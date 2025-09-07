
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
# Relatório PDF de Caixa
# =====================================
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def gerar_pdf_caixa(dados_caixa: dict, vendas_dia: pd.DataFrame, path: str):
    """Gera um relatório PDF de fechamento de caixa incluindo produtos vendidos"""
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors

    doc = SimpleDocTemplate(path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []


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
        story.append(RLImage("logo.png", width=55*mm, height=25*mm))
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
# Carregar do GitHub
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

    if st.button("Entrar"):
        if ((usuarios["Usuario"] == user) & (usuarios["Senha"] == pwd)).any():
            st.session_state["logado"] = True
            st.session_state["usuario"] = user
            st.success(f"Bem-vindo, {user}!")
            return True
        else:
            st.error("Usuário ou senha inválidos.")
            return False

    return st.session_state.get("logado", False)

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
                st.rerun() if hasattr(st, 'rerun') else st.experimental_rerun()
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
do_login()
boot_session()

# Carrega dados atuais
produtos = norm_produtos(pd.DataFrame())
vendas   = norm_vendas(pd.DataFrame())
clientes = norm_clientes(pd.DataFrame())
promocoes = norm_promocoes(pd.DataFrame())

st.session_state["produtos"] = produtos
st.session_state["vendas"] = vendas
st.session_state["clientes"] = clientes
st.session_state["promocoes"] = promocoes

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
    fiados_abertos = len(clientes[clientes["Status"].astype(str).str.lower()=="aberto"]) if not clientes.empty else 0
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

    # ---- PROMOÇÕES ATIVAS EM CARDS ----
    st.markdown("### 🏷️ Promoções Ativas")
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
            cards = p[["NomeProduto","Desconto","DataFim"]].values.tolist()
            step = 3
            for i in range(0, len(cards), step):
                cols = st.columns(step)
                for j, (nome, desc, datafim) in enumerate(cards[i:i+step]):
                    with cols[j]:
                        st.markdown(f"""
                        <div style="border:1px solid #e5e7eb; border-radius:16px; padding:16px; box-shadow:0 1px 6px rgba(0,0,0,0.06)">
                            <div style="font-size:18px; font-weight:700;">{nome}</div>
                            <div style="font-size:32px; font-weight:800; margin:8px 0;">🔥 {float(desc):.0f}% OFF</div>
                            <div style="color:#6b7280;">Válido até {str(datafim)}</div>
                        </div>
                        """, unsafe_allow_html=True)

                # --- RELATÓRIOS DE CAIXA ---
    st.markdown("### 📦 Relatórios de Caixa")
    caixas = norm_caixas(pd.DataFrame())
    if caixas.empty:
        st.info("Nenhum fechamento de caixa registrado ainda.")
    else:
        # --- FILTRO POR DATA ---
        st.subheader("🔍 Filtro de Caixa por Data")
        datas_disp = sorted(caixas["Data"].unique(), reverse=True)
        data_sel = st.selectbox("Selecione a data do caixa", ["Todas"] + datas_disp)

        caixas_filtrados = caixas.copy()
        if data_sel != "Todas":
            caixas_filtrados = caixas_filtrados[caixas_filtrados["Data"] == data_sel]

        st.dataframe(caixas_filtrados.sort_values("Data", ascending=False), use_container_width=True)

        # --- PRODUTOS DO DIA ---
        if data_sel != "Todas":
            vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
            vendas_dia = vendas[vendas["Data"].dt.strftime("%Y-%m-%d") == data_sel]

            st.subheader(f"🛒 Produtos vendidos em {data_sel}")
            if vendas_dia.empty:
                st.info("Nenhum produto vendido nesse dia.")
            else:
                st.dataframe(
                    vendas_dia[["IDProduto","NomeProduto","Quantidade","PrecoUnitario","Total"]],
                    use_container_width=True
                )
        else:
            vendas_dia = pd.DataFrame()  # vazio para não dar erro no PDF

        # --- EXCLUSÃO DE RELATÓRIO ---
        st.subheader("🗑️ Excluir Relatório de Caixa")
        if not caixas_filtrados.empty:
            ids = caixas_filtrados["Data"].tolist()
            del_data = st.selectbox("Selecione a data do relatório para excluir", ids)
            if st.button("Excluir Relatório de Caixa"):
                caixas = caixas[caixas["Data"] != del_data]
                st.session_state["caixas"] = caixas
                save_csv_github(caixas, ARQ_CAIXAS, f"Excluindo relatório de caixa {del_data}")
                st.warning(f"Relatório de caixa de {del_data} excluído!")

        # --- GERAR PDF ---
        if data_sel != "Todas" and not caixas_filtrados.empty:
            caixa_sel = caixas_filtrados.iloc[0].to_dict()
            if st.button("📄 Gerar PDF do Caixa Selecionado"):
                caminho_pdf = f"caixa_{caixa_sel['Data']}.pdf"
                gerar_pdf_caixa(caixa_sel, vendas_dia, caminho_pdf)  # <-- agora leva vendas do dia também
                with open(caminho_pdf, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Baixar Relatório de Caixa ({caixa_sel['Data']})",
                        data=f,
                        file_name=caminho_pdf,
                        mime="application/pdf"
                    )
# --- RECIBOS DE VENDAS ---
st.markdown("### 🧾 Recibos de Vendas")
if not vendas.empty:
    # selecionar a data
    datas_vendas = sorted(vendas["Data"].unique(), reverse=True)
    data_venda = st.selectbox("Selecione a data da venda", datas_vendas, key="sel_data_venda")

    vendas_dia = vendas[vendas["Data"] == data_venda]
    if not vendas_dia.empty:
        # selecionar o ID da venda dentro da data
        ids_vendas = vendas_dia["IDVenda"].astype(int).unique().tolist()
        id_sel = st.selectbox("Selecione o ID da venda", ids_vendas, key="sel_id_venda")

        if st.button("📄 Gerar Recibo (PDF)", key="btn_pdf_venda"):
            caminho_pdf = f"venda_{id_sel}.pdf"
            gerar_pdf_venda(id_sel, vendas, caminho_pdf)
            with open(caminho_pdf, "rb") as f:
                st.download_button(
                    label=f"⬇️ Baixar Recibo da Venda {id_sel}",
                    data=f,
                    file_name=caminho_pdf,
                    mime="application/pdf"
                )
else:
    st.info("Nenhuma venda registrada ainda.")


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

            foto_codigo = st.camera_input("📷 Escanear código de barras / QR Code", key="cad_cam")
            if foto_codigo is not None:
                imagem_bytes = foto_codigo.getvalue()
                codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                if codigos_lidos:
                    st.session_state["codigo_barras"] = codigos_lidos[0]
                    st.success(f"Código lido: {st.session_state['codigo_barras']}")
                    st.rerun() if hasattr(st, "rerun") else st.experimental_rerun()
                else:
                    st.error("❌ Não foi possível ler nenhum código.")

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


    

    # --- Lista de produtos (fora do expander) ---
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
                cb = f' • CB: {row["CodigoBarras"]}' if str(row.get("CodigoBarras","")).strip() else ""
                c[1].markdown(f"**{row['Nome']}**  \nMarca: {row['Marca']}  \nCat: {row['Categoria']}{cb}")
                c[2].write(f"Estoque: {row['Quantidade']}")
                c[3].write(f"Validade: {row['Validade']}")
                col_btn = c[4]
                try:
                    eid = int(row["ID"])
                except Exception:
                    continue
                if col_btn.button("✏️ Editar", key=f"edit_{eid}"):
                    st.session_state["edit_prod"] = eid
                if col_btn.button("🗑️ Excluir", key=f"del_{eid}"):
                    produtos = produtos[produtos["ID"] != str(eid)]
                    st.session_state["produtos"] = produtos
                    save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")
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
                    novo_cb = st.text_input("Código de Barras", value=str(row.get("CodigoBarras","")), key=f"edit_cb_{eid}")
                    foto_codigo_edit = st.camera_input("📷 Atualizar código de barras", key=f"edit_cam_{eid}")
                    if foto_codigo_edit is not None:
                        codigo_lido = ler_codigo_barras_api(foto_codigo_venda.getbuffer())
                        if codigo_lido:
                            novo_cb = codigo_lido
                            st.success(f"Código lido: {novo_cb}")

                if st.button("Salvar alterações"):
                    produtos.loc[produtos["ID"]==str(eid), ["Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade","FotoURL","CodigoBarras"]] = [
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


# =====================================
# VENDAS (Layout completo com promoções + leitura/salvamento de CB)
# =====================================
if view == "Vendas":
    show_logo("main")
    st.header("🧾 Vendas Detalhadas")

    # -- Forma de pagamento
    st.subheader("Forma de Pagamento")
    forma = st.radio("Forma de pagamento", ["Dinheiro", "PIX", "Cartão", "Fiado"], horizontal=True)

    # -- Seleção de produto
    st.subheader("Itens do pedido")
    c1, c2, c3, c4 = st.columns([2, 3, 2, 2])
    with c1:
        # Campo sincronizado com session_state
        if "codigo_venda" not in st.session_state:
            st.session_state["codigo_venda"] = ""

        codigo = st.text_input("Código / Código de Barras", value=st.session_state["codigo_venda"], key="venda_codigo")

        foto_codigo = st.camera_input("📷 Escanear código de barras (Venda)", key="venda_cam")
        if foto_codigo is not None:
            imagem_bytes = foto_codigo.getvalue()
            codigos_lidos = ler_codigo_barras_api(imagem_bytes)

            if codigos_lidos:
                st.session_state["codigo_venda"] = codigos_lidos[0]
                st.success(f"Código lido: {st.session_state['codigo_venda']}")
                st.rerun() if hasattr(st, "rerun") else st.experimental_rerun()
            else:
                st.error("❌ Não foi possível ler nenhum código.")

    with c2:
        nome_filtro = st.text_input("Pesquisar por nome")

    df_sel = produtos.copy()
    if codigo:
        df_sel = df_sel[
            (df_sel["ID"].astype(str).str.contains(codigo)) |
            (df_sel["CodigoBarras"].astype(str).str.contains(codigo))
        ]
    if nome_filtro:
        df_sel = df_sel[df_sel["Nome"].astype(str).str.contains(nome_filtro, case=False, na=False)]

    escolha = None
    if not df_sel.empty:
        st.dataframe(df_sel[["ID", "Nome", "CodigoBarras", "Quantidade", "PrecoVista"]], use_container_width=True)
        escolha = st.selectbox("Selecione o produto", (df_sel["ID"].astype(str) + " - " + df_sel["Nome"].astype(str)).tolist())

    col_qtd, col_preco = st.columns([1, 3])
    with col_qtd:
        qtd = st.number_input("Qtd", min_value=1, value=1, step=1)
    with col_preco:
        if escolha is not None:
            pid = escolha.split(" - ")[0].strip()
            rowp = df_sel[df_sel["ID"].astype(str) == pid]
            if not rowp.empty:
                rowp = rowp.iloc[0]
                preco_vista = float(rowp["PrecoVista"])

                # Aplica promoção
                preco_vista_aplicado, promo = preco_vista_com_promocao(pid, preco_vista, date.today(), promocoes)
                preco_unit = preco_por_forma(preco_vista_aplicado, forma)

                if promo:
                    st.info(f"🏷️ Promoção ativa: -{promo['Desconto']:.0f}% até {promo['DataFim']}. "
                            f"Preço à vista de {brl(preco_vista)} por {brl(preco_vista_aplicado)}.")
                st.write("Preço do item:", brl(preco_unit))

                if st.button("Adicionar ao pedido"):
                    st.session_state["pedido_atual"].append({
                        "IDProduto": pid,
                        "NomeProduto": rowp["Nome"],
                        "CodigoBarras": str(rowp.get("CodigoBarras", "")).strip(),
                        "Quantidade": int(qtd),
                        "PrecoVista": preco_vista,
                    })
                    st.success("Item adicionado.")

    # -- Exibe pedido
    df_pedido = desenha_pedido(forma, promocoes)
    valor_total = float(df_pedido["Total"].sum()) if not df_pedido.empty else 0.0

    # -- Fiado
    nome_cliente, data_prevista = "", None
    if forma == "Fiado":
        st.markdown("#### Dados do fiado")
        nome_cliente = st.text_input("Nome do cliente")
        data_prevista = st.date_input("Data prevista de pagamento", value=date.today() + timedelta(days=7))

    # -- Dinheiro
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
    b1, b2, b3, b4, b5, b6 = st.columns(6)

    # --- FINALIZAR VENDA ---
with b1:
    if st.button("✅ Finalizar Venda"):
        if not st.session_state["pedido_atual"]:
            st.warning("Adicione itens ao pedido.")
        else:
            novo_id = prox_id(vendas, "IDVenda")
            total_venda = 0.0
            codigos_fiado = []

            for item in st.session_state["pedido_atual"]:
                preco_vista_aplicado, _promo = preco_vista_com_promocao(
                    item["IDProduto"], float(item["PrecoVista"]), date.today(), promocoes
                )
                preco_unit = preco_por_forma(preco_vista_aplicado, forma)
                total_item = preco_unit * int(item["Quantidade"])
                total_venda += total_item

                nova_linha = {
                    "IDVenda": novo_id,
                    "Data": str(date.today()),
                    "IDProduto": item["IDProduto"],
                    "NomeProduto": item["NomeProduto"],
                    "CodigoBarras": str(item.get("CodigoBarras", "")).strip(),
                    "FormaPagamento": forma,
                    "Quantidade": int(item["Quantidade"]),
                    "PrecoUnitario": float(preco_unit),
                    "Total": float(total_item),
                }
                vendas = pd.concat([vendas, pd.DataFrame([nova_linha])], ignore_index=True)

                # baixa estoque
                mask = produtos["ID"].astype(str) == str(item["IDProduto"])
                if mask.any():
                    produtos.loc[mask, "Quantidade"] = (
                        produtos.loc[mask, "Quantidade"].astype(int) - int(item["Quantidade"])
                    ).astype(int)

                if str(item.get("CodigoBarras", "")).strip():
                    codigos_fiado.append(str(item.get("CodigoBarras")).strip())

            save_csv_github(vendas, ARQ_VENDAS, "Atualizando vendas")
            save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")

            # Fiado → registra também em clientes
            if forma == "Fiado":
                codigos_join = ";".join(sorted(set([c for c in codigos_fiado if c])))
                novo_cli = {
                    "ID": prox_id(clientes, "ID"),
                    "Cliente": nome_cliente.strip(),
                    "Produto": f"Pedido {novo_id}",
                    "CodigoBarras": codigos_join,
                    "Valor": round(float(total_venda), 2),
                    "DataPagamento": str(data_prevista) if data_prevista else "",
                    "Status": "Aberto",
                    "FormaPagamento": ""
                }
                clientes = pd.concat([clientes, pd.DataFrame([novo_cli])], ignore_index=True)
                save_csv_github(clientes, ARQ_CLIENTES, "Atualizando clientes")
                st.session_state["clientes"] = clientes

            # limpa carrinho
            st.session_state["pedido_atual"] = []
            st.session_state["valor_pago"] = 0.0
            st.session_state["vendas"] = vendas
            st.session_state["produtos"] = produtos

            st.success(f"✅ Venda {novo_id} finalizada!")

            # --- RECIBO PDF ---
            caminho_pdf = f"recibo_venda_{novo_id}.pdf"
            gerar_pdf_venda(novo_id, vendas, caminho_pdf)

            with open(caminho_pdf, "rb") as f:
                pdf_bytes = f.read()
                st.download_button(
                    label="⬇️ Baixar Recibo da Venda",
                    data=pdf_bytes,
                    file_name=caminho_pdf,
                    mime="application/pdf"
                )


    # --- NOVA VENDA ---
    with b2:
        if st.button("🆕 Nova Venda"):
            st.session_state["pedido_atual"] = []
            st.session_state["valor_pago"] = 0.0
            st.session_state["codigo_venda"] = ""       # ✅ limpa código de barras
            st.session_state["codigo_lido_venda"] = False  # ✅ limpa flag da câmera
            st.info("Novo pedido iniciado.")

    # --- FECHAR CAIXA ---
    with b4:
        if st.button("📦 Fechar Caixa"):
            hoje = str(date.today())
            vendas_dia = vendas[vendas["Data"] == hoje]
            # (sua lógica de fechamento de caixa continua aqui...)
            pass

    # --- HISTÓRICO DE VENDAS ---
st.markdown("### Últimas vendas")
if not vendas.empty:
    ult = vendas.sort_values(by=["Data","IDVenda"], ascending=False).head(100)

    # Mostra apenas colunas úteis no histórico
    colunas = ["IDVenda", "Data", "NomeProduto", "Quantidade", "PrecoUnitario", "Total", "FormaPagamento"]
    colunas = [c for c in colunas if c in ult.columns]  # garante que só usa colunas existentes
    st.dataframe(ult[colunas], use_container_width=True)

    # Conversão robusta para IDs de venda
    ids_series = pd.to_numeric(vendas["IDVenda"], errors="coerce").dropna().astype(int)
    ids = sorted(ids_series.unique().tolist(), reverse=True)

    colx, coly = st.columns([3,1])
    with colx:
        id_excluir = st.selectbox("Selecione a venda para excluir (devolve estoque)", ids if ids else [0])

    with coly:
        if st.button("Excluir venda"):
            if id_excluir in ids:
                linhas = vendas[pd.to_numeric(vendas["IDVenda"], errors="coerce").astype(int)==int(id_excluir)]
                # devolve estoque
                for _, r in linhas.iterrows():
                    mask = produtos["ID"].astype(str) == str(r["IDProduto"])
                    if mask.any():
                        produtos.loc[mask, "Quantidade"] = (
                            produtos.loc[mask, "Quantidade"].astype(int) + int(r["Quantidade"])
                        ).astype(int)

                # remove da planilha
                vendas = vendas[pd.to_numeric(vendas["IDVenda"], errors="coerce").astype(int)!=int(id_excluir)]
                save_csv_github(vendas, ARQ_VENDAS, "Atualizando vendas")
                save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")

                st.session_state["vendas"] = vendas
                st.session_state["produtos"] = produtos
                st.success(f"Venda {id_excluir} excluída e estoque ajustado.")
            else:
                st.warning("Venda não encontrada.")
else:
    st.info("Ainda não há vendas registradas.")




# =====================================
# CLIENTES (Fiado) com busca por CB
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
            codigo_barras_filtro = st.text_input("Filtrar por código de barras")
        with c2:
            foto_codigo_cliente = st.camera_input("📷 Escanear código de barras para buscar")
            if foto_codigo_cliente is not None:
                codigo_cliente_lido = ler_codigo_barras(foto_codigo_cliente.getbuffer())
                if codigo_cliente_lido:
                    codigo_barras_filtro = codigo_cliente_lido
                    st.success(f"Código lido: {codigo_barras_filtro}")

        clientes_filtrados = clientes.copy()
        if nome_cliente_filtro:
            clientes_filtrados = clientes_filtrados[clientes_filtrados["Cliente"].astype(str).str.contains(nome_cliente_filtro, case=False, na=False)]
        if codigo_barras_filtro:
            clientes_filtrados = clientes_filtrados[clientes_filtrados["CodigoBarras"].astype(str).str.contains(str(codigo_barras_filtro), case=False, na=False)]

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

                # Aplica alterações de acordo com forma de pagamento escolhida ao marcar "Pago"
                if forma_pag:
                    clientes.loc[idx, "FormaPagamento"] = forma_pag

                    if forma_pag == "Cartão":
                        # Recalcula valor do cliente com taxa de cartão
                        valor_vista = clientes.loc[idx, "Valor"].astype(float)
                        novo_valor = (valor_vista / FATOR_CARTAO).round(2)
                        clientes.loc[idx, "Valor"] = novo_valor

                        # Atualiza também possíveis vendas fiado relacionadas (heurística)
                        produto_nome = clientes.loc[idx, "Produto"].values[0]
                        valor_original = float(valor_vista.iloc[0]) if hasattr(valor_vista, "iloc") else float(valor_vista)
                        venda_idx = (
                            (vendas["NomeProduto"] == produto_nome) &
                            (vendas["FormaPagamento"] == "Fiado") &
                            (vendas["Total"].astype(float) == valor_original)
                        )
                        if venda_idx.any():
                            vendas.loc[venda_idx, "FormaPagamento"] = "Cartão"
                            vendas.loc[venda_idx, "PrecoUnitario"] = (vendas.loc[venda_idx, "PrecoUnitario"].astype(float) / FATOR_CARTAO).round(2)
                            vendas.loc[venda_idx, "Total"] = (vendas.loc[venda_idx, "Total"].astype(float) / FATOR_CARTAO).round(2)
                            save_csv(vendas, ARQ_VENDAS)

                        # Aviso visual do novo valor
                        try:
                            val_num = float(novo_valor.iloc[0])
                        except Exception:
                            val_num = float(novo_valor)
                        st.info(f"Valor atualizado para pagamento no cartão: {brl(val_num)}")

                st.session_state["clientes"] = clientes
                save_csv_github(clientes, ARQ_CLIENTES, "Atualizando clientes")
                st.success("Status atualizado!")

        st.markdown("#### Excluir registro de fiado")
        if st.button("Excluir registro selecionado"):
            if sel is None:
                st.warning("Selecione um registro válido.")
            else:
                clientes = clientes[clientes["ID"].astype(str)!=str(sel)]
                st.session_state["clientes"] = clientes
                save_csv_github(clientes, ARQ_CLIENTES, "Atualizando clientes")
                st.warning(f"Registro {sel} excluído!")

# =====================================
# PROMOÇÕES
# =====================================
if view == "Promoções":
    show_logo("main")
    st.header("🏷️ Promoções")
    promocoes = norm_promocoes(pd.DataFrame())

    # --- CADASTRAR ---
    with st.expander("Cadastrar promoção", expanded=True):
        # Seleção de produto (ID + Nome)
        if produtos.empty:
            st.info("Cadastre produtos primeiro para criar promoções.")
        else:
            opcoes_prod = (produtos["ID"].astype(str) + " - " + produtos["Nome"].astype(str)).tolist()
            sel_prod = st.selectbox("Produto", opcoes_prod)
            pid = sel_prod.split(" - ")[0].strip()
            pnome = sel_prod.split(" - ", 1)[1].strip()

            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                desconto_str = st.text_input("Desconto (%)", value="0")
            with col2:
                data_ini = st.date_input("Início", value=date.today(), key="cad_inicio")
            with col3:
                data_fim = st.date_input("Término", value=date.today() + timedelta(days=7), key="cad_fim")

            if st.button("Adicionar promoção"):
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
    # --- PRODUTOS PARADOS ---
    st.subheader("📦 Produtos parados sem vendas")
    dias_sem_venda = st.number_input("Considerar parados após quantos dias?", min_value=1, max_value=365, value=30)

    # calcular última venda de cada produto
    if not vendas.empty:
        vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
        ultima_venda = vendas.groupby("IDProduto")["Data"].max().reset_index()
        ultima_venda.columns = ["IDProduto", "UltimaVenda"]
    else:
        ultima_venda = pd.DataFrame(columns=["IDProduto","UltimaVenda"])

    produtos_parados = produtos.merge(ultima_venda, left_on="ID", right_on="IDProduto", how="left")
    produtos_parados["UltimaVenda"].fillna(pd.Timestamp("1900-01-01"), inplace=True)

    limite = datetime.now() - timedelta(days=int(dias_sem_venda))
    produtos_parados = produtos_parados[produtos_parados["UltimaVenda"] < limite]

    if produtos_parados.empty:
        st.info("Nenhum produto parado encontrado nesse período.")
    else:
        st.dataframe(produtos_parados[["ID","Nome","Quantidade","UltimaVenda"]])

        desconto_auto = st.number_input("Desconto automático (%)", min_value=1, max_value=100, value=20)
        dias_validade = st.number_input("Duração da promoção (dias)", min_value=1, max_value=90, value=7)

        if st.button("🔥 Criar promoção automática para produtos parados"):
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

    
    st.markdown("### Lista de promoções")
    if promocoes.empty:
        st.info("Nenhuma promoção cadastrada.")
    else:
        # Mostrar tabela
        st.dataframe(promocoes, use_container_width=True)

        # --- EDITAR ---
        st.subheader("Editar promoção")
        ids = promocoes["ID"].astype(str).tolist()
        sel = st.selectbox("Selecione a promoção", ids) if ids else None
        if sel:
            linha = promocoes[promocoes["ID"].astype(str)==sel]
            if not linha.empty:
                ln = linha.iloc[0]
                # Pre-select produto
                opcoes_prod = (produtos["ID"].astype(str) + " - " + produtos["Nome"].astype(str)).tolist()
                pre_opcao = f"{ln['IDProduto']} - {ln['NomeProduto']}" if f"{ln['IDProduto']} - {ln['NomeProduto']}" in opcoes_prod else opcoes_prod[0]
                sel_prod_edit = st.selectbox("Produto (editar)", opcoes_prod, index=opcoes_prod.index(pre_opcao))
                pid_e = sel_prod_edit.split(" - ")[0].strip()
                pnome_e = sel_prod_edit.split(" - ", 1)[1].strip()

                col1, col2, col3 = st.columns([1,1,1])
                with col1:
                    desc_e = st.text_input("Desconto (%)", value=str(ln["Desconto"]))
                with col2:
                    try:
                        di = parse_date_yyyy_mm_dd(ln["DataInicio"]) or date.today()
                    except Exception:
                        di = date.today()
                    data_ini_e = st.date_input("Início", value=di, key=f"edit_inicio_{sel}")
                with col3:
                    try:
                        df = parse_date_yyyy_mm_dd(ln["DataFim"]) or (date.today()+timedelta(days=7))
                    except Exception:
                        df = date.today()+timedelta(days=7)
                    data_fim_e = st.date_input("Término", value=df, key=f"edit_fim_{sel}")

                if st.button("Salvar edição"):
                    dnum = to_float(desc_e, 0.0)
                    if dnum < 0 or dnum > 100:
                        st.error("O desconto deve estar entre 0 e 100%.")
                    elif data_fim_e < data_ini_e:
                        st.error("A data de término deve ser maior ou igual à data de início.")
                    else:
                        idx = promocoes["ID"].astype(str)==sel
                        promocoes.loc[idx, ["IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]] = [
                            str(pid_e), pnome_e, float(dnum), str(data_ini_e), str(data_fim_e)
                        ]
                        save_csv_github(promocoes, ARQ_PROMOCOES, "Atualizando promoções")
                        st.session_state["promocoes"] = promocoes
                        st.success("Promoção atualizada!")

        # --- EXCLUIR ---
        st.subheader("Excluir promoção")
        del_id = st.selectbox("Selecione ID para excluir", promocoes["ID"].astype(str).tolist())
        if st.button("Excluir promoção"):
            promocoes = promocoes[promocoes["ID"].astype(str)!=del_id]
            save_csv_github(promocoes, ARQ_PROMOCOES, "Atualizando promoções")
            st.session_state["promocoes"] = promocoes
            st.warning(f"Promoção {del_id} excluída!")
