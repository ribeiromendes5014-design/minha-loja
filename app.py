
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
    # API alternativa: WebQR (mais estável que ZXing)
    url_webqr = "https://api.qrserver.com/v1/read-qr-code/"
    
    try:
        # A API WebQR espera o arquivo no campo 'file' ou 'f'
        files = {"file": ("barcode.png", image_bytes, "image/png")} 
        
        # Usando um timeout de 30 segundos
        response = requests.post(url_webqr, files=files, timeout=30) 

        if response.status_code != 200:
            st.error(f"❌ Erro na API WebQR. Status HTTP: {response.status_code}")
            return []

        # A resposta é JSON (mais fácil de parsear que HTML)
        data = response.json()
        codigos = []
        
        # Navega na estrutura JSON da resposta
        if data and isinstance(data, list) and data[0].get('symbol'):
            for symbol in data[0]['symbol']:
                if symbol['data'] is not None:
                    codigos.append(symbol['data'])
        
        st.write("Debug API WebQR:", codigos)
        
        if not codigos:
             st.warning("⚠️ API WebQR não retornou nenhum código válido. Tente novamente ou use uma imagem mais clara.")
             
        return codigos

    except requests.exceptions.ConnectionError as ce:
        st.error(f"❌ Erro de Conexão: O WebQR recusou ou falhou na conexão. O servidor pode estar fora do ar. Detalhe: {ce}")
        return []
        
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Erro de Requisição (Timeout/Outro): Falha ao completar a chamada à API WebQR. Detalhe: {e}")
        return []
    
    except Exception as e:
        st.error(f"❌ Erro inesperado ao chamar API de leitura: {e}")
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
# Funções auxiliares (CORRIGIDO: API ZXing com tratamento de erros de conexão)
# =====================================

import requests
from requests.exceptions import ConnectionError, RequestException # Importa exceções de rede

def ler_codigo_barras_api(image_bytes):
    # Endpoint original que você disse que funcionava
    URL_DECODER_ZXING = "https://zxing.org/w/decode"
    
    try:
        # Define o arquivo com o mimetype que a API ZXing espera
        files = {"f": ("barcode.png", image_bytes, "image/png")}
        
        # Faz a requisição com um timeout de 30 segundos
        response = requests.post(URL_DECODER_ZXING, files=files, timeout=30) 

        if response.status_code != 200:
            st.error(f"❌ Erro na API ZXing. Status HTTP: {response.status_code}")
            return []

        # Parse de HTML (lógica original)
        text = response.text
        codigos = []
        if "<pre>" in text:
            partes = text.split("<pre>")
            for p in partes[1:]:
                codigo = p.split("</pre>")[0].strip()
                if codigo and not codigo.startswith("Erro na decodificação"):
                    codigos.append(codigo)

        st.write("Debug API ZXing:", codigos)
        
        if not codigos:
             st.warning("⚠️ API ZXing não retornou nenhum código válido. Tente novamente ou use uma imagem mais clara.")
             
        return codigos

    except ConnectionError as ce:
        # CAPTURA O ERRO 'Connection refused'
        st.error(f"❌ Erro de Conexão (Rede Bloqueada): O servidor {URL_DECODER_ZXING} recusou a conexão. O problema é na rede do seu host.")
        return []
        
    except RequestException as e:
        # CAPTURA OUTROS ERROS (Timeout, etc.)
        st.error(f"❌ Erro de Requisição (Timeout/Outro): Falha ao completar a chamada à API. Detalhe: {e}")
        return []
    
    except Exception as e:
        st.error(f"❌ Erro inesperado: {e}")
        return []

# O resto do seu código permanece como está.




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
# INÍCIO - GARANTIR CARREGAMENTO DO CSV
# =====================================

import pandas as pd

# Exemplo de função para carregar o CSV do GitHub (modifique conforme sua implementação)
def carregar_csv_github(arquivo_csv):
    url = f"https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/{arquivo_csv}"
    return pd.read_csv(url, dtype=str).fillna("")

# Arquivo de produtos
ARQ_PRODUTOS = "produtos.csv"

# Inicializa o DataFrame se ainda não estiver no session_state
if "produtos" not in st.session_state:
    try:
        produtos = carregar_csv_github(ARQ_PRODUTOS)
        st.session_state["produtos"] = produtos
    except Exception as e:
        st.error(f"Erro ao carregar produtos: {e}")
        st.session_state["produtos"] = pd.DataFrame(columns=[
            "ID", "Nome", "Marca", "Categoria", "Quantidade",
            "PrecoCusto", "PrecoVista", "PrecoCartao",
            "Validade", "FotoURL", "CodigoBarras", "PaiID"
        ])

# Pega os produtos carregados do session_state
produtos = st.session_state["produtos"]


# =====================================
# PRODUTOS COM GRADE (PAI/FILHO)
# =====================================
if view == "Produtos":
    show_logo("main")
    st.header("📦 Produtos")

    # Função auxiliar para criar um novo ID sequencial (usada aqui)
    def prox_id(df, coluna_id="ID"):
        if df.empty:
            return "1"
        else:
            try:
                # O pd.to_numeric e .max() garantem a maior segurança para IDs mistos
                return str(pd.to_numeric(df[coluna_id], errors='coerce').fillna(0).astype(int).max() + 1)
            except:
                return str(len(df) + 1)


    # ================================
    # SUBABAS
    # ================================
    tab_cadastro, tab_lista = st.tabs(["📝 Cadastro de Produtos", "📑 Lista & Busca"])

    # ================================
    # SUBABA: CADASTRO
    # ================================
    with tab_cadastro:
        st.subheader("📝 Cadastro de Produtos")

        # --- Cadastro ---
        with st.expander("Cadastrar novo produto", expanded=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                # Produto pai ou simples
                tipo_produto = st.radio("Tipo de produto", ["Produto simples", "Produto com variações (grade)"], key="cad_tipo_produto")

                nome = st.text_input("Nome", key="cad_nome")
                marca = st.text_input("Marca", key="cad_marca")
                categoria = st.text_input("Categoria", key="cad_categoria")

            with c2:
                # Se for produto simples, cadastro direto da quantidade e preços
                if tipo_produto == "Produto simples":
                    qtd = st.number_input("Quantidade", min_value=0, step=1, value=0, key="cad_qtd")
                    preco_custo = st.text_input("Preço de Custo", value="0,00", key="cad_preco_custo")
                    preco_vista = st.text_input("Preço à Vista", value="0,00", key="cad_preco_vista")
                    preco_cartao = 0.0
                    try:
                        preco_cartao = round(float(preco_vista.replace(",", ".").strip()) / FATOR_CARTAO, 2)
                    except Exception:
                        preco_cartao = 0.0
                    st.text_input("Preço no Cartão (auto)", value=str(preco_cartao).replace(".", ","), disabled=True, key="cad_preco_cartao")
                else:
                    st.info("Cadastre as variações abaixo (grade).")

            with c3:
                validade = st.date_input("Validade (opcional)", value=date.today(), key="cad_validade")
                foto_url = st.text_input("URL da Foto (opcional)", key="cad_foto_url")
                foto_arquivo = st.file_uploader("📷 Enviar Foto", type=["png", "jpg", "jpeg"], key="cad_foto")

                if "codigo_barras" not in st.session_state:
                    st.session_state["codigo_barras"] = ""

                # O campo de código de barras principal é mantido apenas para Produto Simples/Pai
                codigo_barras = st.text_input("Código de Barras (Pai/Simples)", value=st.session_state["codigo_barras"], key="cad_cb")

                # --- Escanear com câmera (Produto Simples/Pai) ---
                foto_codigo = st.camera_input("📷 Escanear código de barras / QR Code", key="cad_cam")
                if foto_codigo is not None:
                    imagem_bytes = foto_codigo.getvalue()
                    codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                    if codigos_lidos:
                        st.session_state["codigo_barras"] = codigos_lidos[0]
                        st.success(f"Código lido: {st.session_state['codigo_barras']}")
                        st.experimental_rerun()
                    else:
                        st.error("❌ Não foi possível ler nenhum código.")

                # --- Upload de imagem do código de barras (Produto Simples/Pai) ---
                foto_codigo_upload = st.file_uploader("📤 Upload de imagem do código de barras", type=["png", "jpg", "jpeg"], key="cad_cb_upload")
                if foto_codigo_upload is not None:
                    imagem_bytes = foto_codigo_upload.getvalue()
                    codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                    if codigos_lidos:
                        st.session_state["codigo_barras"] = codigos_lidos[0]
                        st.success(f"Código lido via upload: {st.session_state['codigo_barras']}")
                        st.experimental_rerun()
                    else:
                        st.error("❌ Não foi possível ler nenhum código da imagem enviada.")

            # --- Cadastro da grade (variações) ---
            variações = []
            if tipo_produto == "Produto com variações (grade)":
                st.markdown("#### Cadastro das variações (grade)")
                qtd_variações = st.number_input("Quantas variações deseja cadastrar?", min_value=1, step=1, key="cad_qtd_variações")

                # Inicializa a lista de códigos de barras lidos para a grade na sessão
                if 'cb_grade_lidos' not in st.session_state:
                    st.session_state.cb_grade_lidos = {}
                    
                variações = []
                for i in range(int(qtd_variações)):
                    # Adicionado separador de linha para melhor visualização
                    st.markdown(f"--- **Variação {i+1}** ---")
                    
                    # Colunas para Nome, Qtd, Custo e Vista
                    var_c1, var_c2, var_c3, var_c4 = st.columns(4)
                    
                    var_nome = var_c1.text_input(f"Nome da variação {i+1}", key=f"var_nome_{i}")
                    var_qtd = var_c2.number_input(f"Quantidade variação {i+1}", min_value=0, step=1, value=0, key=f"var_qtd_{i}")
                    var_preco_custo = var_c3.text_input(f"Preço de custo variação {i+1}", value="0,00", key=f"var_pc_{i}")
                    var_preco_vista = var_c4.text_input(f"Preço à vista variação {i+1}", value="0,00", key=f"var_pv_{i}")
                    
                    # --- Leitura/Upload de Código de Barras para a Variação ---
                    # Colunas para Código de Barras (texto), Upload e Câmera
                    var_cb_c1, var_cb_c2, var_cb_c3 = st.columns([2, 1, 1])

                    # 1. Campo de texto do Código de Barras (puxa o valor lido da sessão)
                    with var_cb_c1:
                        valor_cb_inicial = st.session_state.cb_grade_lidos.get(f"var_cb_{i}", "")
                        var_codigo_barras = st.text_input(
                            f"Código de barras variação {i+1}", 
                            value=valor_cb_inicial, 
                            key=f"var_cb_{i}" # Chave principal para o CB da variação
                        )
                        # Nota: o campo acima é o que será salvo.
                    
                    # 2. Upload da foto
                    with var_cb_c2:
                        var_foto_upload = st.file_uploader(
                            "Upload CB", 
                            type=["png", "jpg", "jpeg"], 
                            key=f"var_cb_upload_{i}"
                        )
                    
                    # 3. Câmera
                    with var_cb_c3:
                        var_foto_cam = st.camera_input(
                            "Escanear CB", 
                            key=f"var_cb_cam_{i}"
                        )
                    
                    # Logica de leitura do Código de Barras
                    foto_lida = var_foto_upload or var_foto_cam
                    if foto_lida:
                        # ⚠️ Se for ler o código, usa o buffer do objeto file_uploader/camera_input
                        imagem_bytes = foto_lida.getvalue() 
                        codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                        if codigos_lidos:
                            # Armazena o código lido no estado da sessão (será puxado pelo campo de texto acima)
                            st.session_state.cb_grade_lidos[f"var_cb_{i}"] = codigos_lidos[0]
                            st.success(f"CB Variação {i+1} lido: {codigos_lidos[0]}")
                            st.experimental_rerun()
                        else:
                            st.error(f"❌ Variação {i+1}: Não foi possível ler o código.")

                    # Coleta os dados da variação para salvar
                    variações.append({
                        "Nome": var_nome.strip(),
                        "Quantidade": int(var_qtd),
                        "PrecoCusto": to_float(var_preco_custo),
                        "PrecoVista": to_float(var_preco_vista),
                        "PrecoCartao": round(to_float(var_preco_vista) / FATOR_CARTAO, 2) if to_float(var_preco_vista) > 0 else 0.0,
                        # Usa o valor final do campo de texto (que pode ter sido preenchido pela leitura)
                        "CodigoBarras": var_codigo_barras.strip() 
                    })

            if st.button("💾 Salvar Produto", use_container_width=True, key="cad_salvar"):
                novo_id = prox_id(produtos, "ID")
                
                if tipo_produto == "Produto simples":
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
                        "CodigoBarras": codigo_barras.strip(),
                        "PaiID": None  # Produto simples, sem pai
                    }
                    produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
                else:
                    # Produto pai
                    novo_pai = {
                        "ID": novo_id,
                        "Nome": nome.strip(),
                        "Marca": marca.strip(),
                        "Categoria": categoria.strip(),
                        "Quantidade": 0,  # estoque do pai fica 0, soma nas variações
                        "PrecoCusto": 0.0,
                        "PrecoVista": 0.0,
                        "PrecoCartao": 0.0,
                        "Validade": str(validade),
                        "FotoURL": foto_url.strip(),
                        "CodigoBarras": codigo_barras.strip(),
                        "PaiID": None
                    }
                    produtos = pd.concat([produtos, pd.DataFrame([novo_pai])], ignore_index=True)

                    # Agora cadastra as variações ligadas ao pai pelo ID
                    for var in variações:
                        if var["Nome"] == "":
                            continue  # pula variações sem nome
                        novo_filho = {
                            "ID": prox_id(produtos, "ID"),
                            "Nome": var["Nome"],
                            "Marca": marca.strip(),
                            "Categoria": categoria.strip(),
                            "Quantidade": var["Quantidade"],
                            "PrecoCusto": var["PrecoCusto"],
                            "PrecoVista": var["PrecoVista"],
                            "PrecoCartao": var["PrecoCartao"],
                            "Validade": str(validade),
                            "FotoURL": foto_url.strip(),
                            "CodigoBarras": var["CodigoBarras"],
                            "PaiID": novo_id  # aponta para o produto pai
                        }
                        produtos = pd.concat([produtos, pd.DataFrame([novo_filho])], ignore_index=True)

                st.session_state["produtos"] = produtos
                # Limpa a sessão de códigos de barras lidos da grade
                if 'cb_grade_lidos' in st.session_state:
                    del st.session_state.cb_grade_lidos 
                save_csv_github(produtos, ARQ_PRODUTOS, "Novo produto cadastrado")
                st.success(f"✅ Produto '{nome}' cadastrado com sucesso!")
                st.experimental_rerun()

    # ================================
    # SUBABA: LISTA & BUSCA
    # ================================
    with tab_lista:
        st.subheader("📑 Lista & Busca de Produtos")

        # --- Busca minimalista ---
        with st.expander("🔍 Pesquisar produto", expanded=True):
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

            # ✅ Garantir que PaiID exista mesmo após filtro
            if "PaiID" not in produtos_filtrados.columns:
                produtos_filtrados["PaiID"] = None

        # --- Lista de produtos com agrupamento por Pai e Variações ---
        st.markdown("### Lista de produtos")

        if produtos_filtrados.empty:
            st.info("Nenhum produto encontrado.")
        else:
            # Separar produtos pais e variações (filhos)
            produtos_pai = produtos_filtrados[produtos_filtrados["PaiID"].isnull()]
            produtos_filho = produtos_filtrados[produtos_filtrados["PaiID"].notnull()]

            for _, pai in produtos_pai.iterrows():
                with st.container():
                    c = st.columns([1, 3, 1, 1, 1])
                    # Imagem do produto pai
                    if str(pai["FotoURL"]).strip():
                        try:
                            c[0].image(pai["FotoURL"], width=80)
                        except Exception:
                            c[0].write("Sem imagem")
                    else:
                        c[0].write("—")

                    cb = f' • CB: {pai["CodigoBarras"]}' if str(pai.get("CodigoBarras", "")).strip() else ""
                    c[1].markdown(f"**{pai['Nome']}**  \nMarca: {pai['Marca']}  \nCat: {pai['Categoria']}{cb}")
                    c[2].write(f"Estoque: {pai['Quantidade']}")
                    c[3].write(f"Validade: {pai['Validade']}")
                    col_btn = c[4]

                    try:
                        eid = int(pai["ID"])
                    except Exception:
                        continue

                    acao = col_btn.selectbox(
                        "Ação",
                        ["Nenhuma", "✏️ Editar", "🗑️ Excluir"],
                        key=f"acao_{eid}"
                    )

                    if acao == "✏️ Editar":
                        st.session_state["edit_prod"] = eid

                    if acao == "🗑️ Excluir":
                        if col_btn.button("Confirmar exclusão", key=f"conf_del_{eid}"):
                            # ✅ Garante que a coluna 'PaiID' existe
                            if "PaiID" not in produtos.columns:
                                produtos["PaiID"] = None

                            # Apaga o pai
                            produtos = produtos[produtos["ID"] != str(eid)]

                            # Apaga as variações ligadas ao pai
                            produtos = produtos[produtos["PaiID"] != str(eid)]

                            # Atualiza estado e salva
                            st.session_state["produtos"] = produtos
                            save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")
                            st.warning(f"Produto {pai['Nome']} e suas variações excluídas!")
                            st.experimental_rerun()

                    # Listar variações filhas do produto
                    filhos = produtos_filho[produtos_filho["PaiID"] == str(pai["ID"])]
                    if not filhos.empty:
                        with st.expander(f"Variações de {pai['Nome']}"):
                            for _, var in filhos.iterrows():
                                c_var = st.columns([1, 3, 1, 1, 1])
                                if str(var["FotoURL"]).strip():
                                    try:
                                        c_var[0].image(var["FotoURL"], width=60)
                                    except Exception:
                                        c_var[0].write("Sem imagem")
                                else:
                                    c_var[0].write("—")

                                cb_var = f' • CB: {var["CodigoBarras"]}' if str(var.get("CodigoBarras", "")).strip() else ""
                                c_var[1].markdown(f"**{var['Nome']}**  \nMarca: {var['Marca']}  \nCat: {var['Categoria']}{cb_var}")
                                c_var[2].write(f"Estoque: {var['Quantidade']}")
                                c_var[3].write(f"Validade: {var['Validade']}")
                                col_btn_var = c_var[4]

                                try:
                                    eid_var = int(var["ID"])
                                except Exception:
                                    continue

                                acao_var = col_btn_var.selectbox(
                                    "Ação",
                                    ["Nenhuma", "✏️ Editar", "🗑️ Excluir"],
                                    key=f"acao_{eid_var}"
                                )

                                if acao_var == "✏️ Editar":
                                    st.session_state["edit_prod"] = eid_var

                                if acao_var == "🗑️ Excluir":
                                    if col_btn_var.button("Confirmar exclusão", key=f"conf_del_{eid_var}"):
                                        produtos = produtos[produtos["ID"] != str(eid_var)]
                                        st.session_state["produtos"] = produtos
                                        save_csv_github(produtos, ARQ_PRODUTOS, "Atualizando produtos")
                                        st.warning(f"Variação {var['Nome']} excluída!")
                                        st.experimental_rerun()

            # Editor inline (para pais e filhos)
            if "edit_prod" in st.session_state:
                eid = st.session_state["edit_prod"]
                row = produtos[produtos["ID"] == str(eid)]
                if not row.empty:
                    st.subheader("Editar produto")
                    row = row.iloc[0]
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        novo_nome = st.text_input("Nome", value=row["Nome"], key=f"edit_nome_{eid}")
                        nova_marca = st.text_input("Marca", value=row["Marca"], key=f"edit_marca_{eid}")
                        nova_cat = st.text_input("Categoria", value=row["Categoria"], key=f"edit_cat_{eid}")
                    with c2:
                        nova_qtd = st.number_input("Quantidade", min_value=0, step=1, value=int(row["Quantidade"]), key=f"edit_qtd_{eid}")
                        novo_preco_custo = st.text_input("Preço de Custo", value=str(row["PrecoCusto"]).replace(".", ","), key=f"edit_pc_{eid}")
                        novo_preco_vista = st.text_input("Preço à Vista", value=str(row["PrecoVista"]).replace(".", ","), key=f"edit_pv_{eid}")
                    with c3:
                        try:
                            vdata = datetime.strptime(str(row["Validade"] or date.today()), "%Y-%m-%d").date()
                        except Exception:
                            vdata = date.today()
                        nova_validade = st.date_input("Validade", value=vdata, key=f"edit_val_{eid}")
                        nova_foto = st.text_input("URL da Foto", value=row["FotoURL"], key=f"edit_foto_{eid}")
                        novo_cb = st.text_input("Código de Barras", value=str(row.get("CodigoBarras", "")), key=f"edit_cb_{eid}")

                        foto_codigo_edit = st.camera_input("📷 Atualizar código de barras", key=f"edit_cam_{eid}")
                        if foto_codigo_edit is not None:
                            codigo_lido = ler_codigo_barras_api(foto_codigo_edit.getbuffer())
                            if codigo_lido:
                                novo_cb = codigo_lido
                                st.success(f"Código lido: {novo_cb}")

                    col_save, col_cancel = st.columns([1, 1])
                    with col_save:
                        if st.button("Salvar alterações", key=f"save_{eid}"):
                            produtos.loc[produtos["ID"] == str(eid), [
                                "Nome", "Marca", "Categoria", "Quantidade",
                                "PrecoCusto", "PrecoVista", "PrecoCartao",
                                "Validade", "FotoURL", "CodigoBarras"
                            ]] = [
                                novo_nome.strip(),
                                nova_marca.strip(),
                                nova_cat.strip(),
                                int(nova_qtd),
                                to_float(novo_preco_custo),
                                to_float(novo_preco_vista),
                                round(to_float(novo_preco_vista) / FATOR_CARTAO, 2) if to_float(novo_preco_vista) > 0 else 0.0,
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
                            st.experimental_rerun()










  import streamlit as st
import pandas as pd
import os
from datetime import date, datetime, timedelta
from PIL import Image, ImageEnhance
from io import BytesIO
import requests
from github import Github # Import necessário para save_csv_github (se estiver nos secrets)
from reportlab.lib.pagesizes import A4 # Import necessário para geração de PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer # Import necessário para geração de PDF
from reportlab.lib.styles import getSampleStyleSheet # Import necessário para geração de PDF
from reportlab.lib import colors # Import necessário para geração de PDF
import pytz
from requests.exceptions import ConnectionError, RequestException

# =====================================
# Variáveis e Constantes
# (Adaptadas do seu código para simular o ambiente)
# =====================================
ARQ_PRODUTOS  = "produtos.csv"
ARQ_VENDAS    = "vendas.csv"
ARQ_CLIENTES  = "clientes.csv"
ARQ_CAIXAS = "caixas.csv"
ARQ_PROMOCOES = "promocoes.csv"
FATOR_CARTAO  = 0.8872

TELEGRAM_TOKEN = "8106907671:AAFoh0TfADdyP-NWasS2BQu4BkfG9ez-Smw"
TELEGRAM_CHAT_ID = "-1003030758192"

# =====================================
# Funções Auxiliares (CRÍTICAS PARA A ABA VENDAS)
# =====================================

def to_float(x, default=0.0):
    try:
        return float(str(x).replace(",", ".").strip())
    except Exception:
        return default

def brl(v: float) -> str:
    try:
        s = f"{float(v):,.2f}"
        s = s.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {s}"
    except Exception:
        return "R$ 0,00"

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

def preco_por_forma(preco_vista: float, forma: str) -> float:
    if forma == "Cartão":
        return float(preco_vista) / FATOR_CARTAO
    return float(preco_vista)

def preco_vista_com_promocao(prod_id: str, preco_vista: float, hoje: date, prom_df: pd.DataFrame) -> tuple[float, dict | None]:
    promo = promocao_ativa_para(prod_id, hoje, prom_df)
    preco_aplicado = aplica_promocao_no_preco(preco_vista, promo)
    return preco_aplicado, promo

def ler_codigo_barras_api(image_bytes):
    # Dummy para simular a leitura do código de barras
    st.error("❌ A função real de leitura de código de barras via API não está disponível neste ambiente.")
    return []

def save_csv_github(df: pd.DataFrame, path: str, mensagem: str):
    # Dummy para simular o salvamento no GitHub
    df.to_csv(path, index=False)
    st.info(f"💾 Salvamento simulado de '{path}'.")

def norm_caixas(df: pd.DataFrame) -> pd.DataFrame:
    # Dummy para simular norm_caixas
    cols = ["Data","FaturamentoTotal","Dinheiro","PIX","Cartão","Fiado","Status"]
    if df.empty:
        return pd.DataFrame(columns=cols)
    return df

def norm_clientes(df: pd.DataFrame) -> pd.DataFrame:
    # Dummy para simular norm_clientes
    cols = ["ID","Cliente","Produto","CodigoBarras","Valor","DataPagamento","Status","FormaPagamento"]
    if df.empty:
        return pd.DataFrame(columns=cols)
    return df

def prox_id(df: pd.DataFrame, col: str) -> int:
    if df.empty or col not in df.columns:
        return 1
    try:
        vals = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
        return int(vals.max()) + 1 if len(vals) else 1
    except Exception:
        return 1

def desenha_pedido(forma: str, prom_df: pd.DataFrame) -> pd.DataFrame:
    # Implementação do desenho do pedido (mantida do código original)
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
            nova_qtd = st.number_input("Qtd", min_value=1, value=int(item["Quantidade"]), key=f"q_{idx}")

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

# =====================
# Funções de Telegram
# =====================
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
        r.json()
    except Exception:
        pass # Silenciar erros de Telegram na simulação

def enviar_pdf_telegram(caminho_arquivo, thread_id=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            files = {'document': arquivo_pdf}
            data = {"chat_id": TELEGRAM_CHAT_ID}
            if thread_id is not None:
                data["message_thread_id"] = thread_id
            requests.post(url, data=data, files=files)
    except Exception:
        pass # Silenciar erros de Telegram na simulação

# =====================
# Funções de Caixa (Abertura/Fechamento)
# =====================
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
                st.session_state["valor_inicial_original"] = valor_inicial
                st.session_state["caixa_aberto"] = True
                st.success(
                    f"✅ Caixa aberto com sucesso! Operador: {operador} | Valor inicial: {valor_inicial:.2f}"
                )
                st.rerun()

def gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf):
    # Dummy para simular a geração do PDF
    with open(caminho_pdf, "w") as f:
        f.write("Relatório de Caixa\n")
        f.write(f"Data: {dados_caixa['Data']}\n")
        f.write(f"Faturamento Total: {brl(dados_caixa['FaturamentoTotal'])}\n")
        f.write(f"Dinheiro: {brl(dados_caixa['Dinheiro'])}\n")
        f.write(f"Total de vendas: {len(vendas_dia)}\n")
    

def enviar_relatorio_fechamento_caixa(dados_caixa, vendas_dia, thread_id=3):
    # Simulação do envio do PDF/mensagem para o Telegram
    caminho_pdf = f"caixa_{dados_caixa['Data']}.pdf"
    gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf) # Gera o PDF dummy
    
    # Simula o envio
    msg = f"📊 Relatório de Fechamento de Caixa - {dados_caixa['Data']} - Total: {brl(dados_caixa['FaturamentoTotal'])}"
    enviar_telegram(msg, thread_id=thread_id)
    # enviar_pdf_telegram(caminho_pdf, thread_id=thread_id) # Descomentar se o ambiente permitir

def fechar_caixa():
    if st.session_state.get("caixa_aberto", False):
        operador = st.session_state.get("operador", "—")
        valor_inicial = st.session_state.get("valor_inicial_original", 0.0)
        hoje = date.today()

        vendas_df = st.session_state.get("vendas", pd.DataFrame())
        if vendas_df.empty:
            vendas_dia = pd.DataFrame()
        else:
            vendas_df["Data"] = pd.to_datetime(vendas_df["Data"], errors="coerce").dt.date
            vendas_dia = vendas_df[vendas_df["Data"] == hoje]

        total_dinheiro = vendas_dia[vendas_dia["FormaPagamento"] == "Dinheiro"]["Total"].sum()
        total_pix = vendas_dia[vendas_dia["FormaPagamento"] == "PIX"]["Total"].sum()
        total_cartao_bruto = vendas_dia[vendas_dia["FormaPagamento"] == "Cartão"]["Total"].sum()
        total_fiado = vendas_dia[vendas_dia["FormaPagamento"] == "Fiado"]["Total"].sum()

        valor_final_caixa = valor_inicial + total_dinheiro
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

        caixas = st.session_state.get("caixas", norm_caixas(pd.DataFrame()))
        caixas = pd.concat([caixas, pd.DataFrame([dados_caixa])], ignore_index=True)
        save_csv_github(caixas, ARQ_CAIXAS, f"Fechamento de caixa {hoje.strftime('%Y-%m-%d')}")
        st.session_state["caixas"] = caixas

        st.session_state["dados_fechamento_caixa"] = dados_caixa
        st.session_state["vendas_dia_fechamento"] = vendas_dia
        st.session_state["caixa_aberto"] = False

        st.success(
            f"📦 Caixa fechado! Operador: {operador} | Valor final esperado: {brl(valor_final_caixa)}"
        )
        enviar_relatorio_fechamento_caixa(dados_caixa, vendas_dia, thread_id=3)
        st.rerun()

# =====================
# Função de Finalizar Venda
# =====================
def finalizar_venda(forma, forma1, forma2, valor1, valor2, promocoes,
                    nome_cliente=None, data_pagamento=None, valor_recebido=0.0):
    
    vendas = st.session_state.get("vendas", pd.DataFrame())
    produtos = st.session_state.get("produtos", pd.DataFrame())
    clientes = st.session_state.get("clientes", pd.DataFrame())

    if not st.session_state.get("pedido_atual"):
        st.warning("⚠️ Nenhum item no pedido.")
        return

    # Lógica de determinação do novo IDVenda (mantida)
    if not vendas.empty and "IDVenda" in vendas.columns:
        vendas["IDVenda"] = pd.to_numeric(vendas["IDVenda"], errors="coerce").fillna(0).astype(int)
        novo_id = int(vendas["IDVenda"].max() + 1)
    else:
        novo_id = 1

    df_pedido = pd.DataFrame(st.session_state["pedido_atual"])

    # 🔹 Garante coluna PrecoComDesconto calculada com promoções (mantida)
    precos_corrigidos = []
    promocoes_aplicadas = []
    for _, row in df_pedido.iterrows():
        preco_base = float(row["PrecoVista"])
        preco_desc, promo = preco_vista_com_promocao(
            row["IDProduto"], preco_base, date.today(), promocoes
        )
        precos_corrigidos.append(preco_desc)
        promocoes_aplicadas.append(promo["Desconto"] if promo else None)
        
        # 🔻 Lógica de baixa de estoque 
        prod_id = str(row["IDProduto"])
        qtd_vendida = int(row["Quantidade"])
        mask = produtos["ID"].astype(str) == prod_id
        if mask.any():
             produtos.loc[mask, "Quantidade"] = (
                 produtos.loc[mask, "Quantidade"].astype(int) - qtd_vendida
             ).astype(int)

    df_pedido["PrecoComDesconto"] = precos_corrigidos
    df_pedido["Promocao"] = promocoes_aplicadas

    df_pedido["IDVenda"] = novo_id
    df_pedido["Data"] = date.today().strftime("%Y-%m-%d")
    df_pedido["Cliente"] = nome_cliente if nome_cliente else ""
    df_pedido["DataPagamento"] = str(data_pagamento) if data_pagamento else ""
    df_pedido["ValorRecebido"] = valor_recebido

    total_pedido = df_pedido["PrecoComDesconto"].multiply(df_pedido["Quantidade"]).sum()

    # Lógica de pagamento (mantida)
    if forma == "Misto" and forma1 and forma2:
        soma_valores = valor1 + valor2
        if soma_valores == 0:
            valor1_corrigido = valor2_corrigido = 0
        else:
            # Re-calcula a proporção com o total com desconto
            valor1_corrigido = total_pedido * (valor1 / soma_valores)
            valor2_corrigido = total_pedido * (valor2 / soma_valores)
        
        # Cria as linhas para a forma mista (uma linha por produto/forma)
        df_vendas_misto = pd.DataFrame()
        df_temp = df_pedido.copy()
        df_temp["FormaPagamento"] = forma1
        df_temp["Total"] = valor1_corrigido * df_temp["PrecoComDesconto"] / total_pedido if total_pedido > 0 else 0
        df_vendas_misto = pd.concat([df_vendas_misto, df_temp], ignore_index=True)

        df_temp = df_pedido.copy()
        df_temp["FormaPagamento"] = forma2
        df_temp["Total"] = valor2_corrigido * df_temp["PrecoComDesconto"] / total_pedido if total_pedido > 0 else 0
        df_vendas_misto = pd.concat([df_vendas_misto, df_temp], ignore_index=True)

        vendas = pd.concat([vendas, df_vendas_misto], ignore_index=True)
    else:
        df_pedido["FormaPagamento"] = forma
        df_pedido["Total"] = df_pedido["PrecoComDesconto"].multiply(df_pedido["Quantidade"]) # Total é o total do item
        vendas = pd.concat([vendas, df_pedido], ignore_index=True)

    # Lógica de Fiado (mantida)
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
        st.session_state["clientes"] = clientes

    # Salva o estado atualizado
    save_csv_github(vendas, ARQ_VENDAS, "Nova venda adicionada")
    save_csv_github(produtos, ARQ_PRODUTOS, "Estoque atualizado")
    st.session_state["vendas"] = vendas
    st.session_state["produtos"] = produtos
    st.session_state["pedido_atual"] = []

    # Envio para Telegram (mantido)
    try:
        tz = pytz.timezone("America/Sao_Paulo")
        agora = datetime.now(tz)
        data_str = agora.strftime("%Y-%m-%d")
        hora_str = agora.strftime("%H:%M:%S")

        produtos_txt = ""
        for _, row in df_pedido.iterrows():
            promo_str = ""
            if "Promocao" in row and row["Promocao"]:
                promo_str = f" 🔥 {row['Promocao']:.0f}% OFF"
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
        
        enviar_telegram(msg, thread_id=2)
    except Exception:
        pass # Silenciar erros de Telegram

    st.success(f"✅ Venda {novo_id} finalizada com sucesso!")
    st.rerun()

def gerar_pdf_venda(venda_id: int, vendas: pd.DataFrame, path: str):
    # Dummy para simular a geração do PDF
    with open(path, "w") as f:
        f.write(f"Recibo de Venda ID: {venda_id}\n")
        f.write("...\n")

# =====================================
# Simulação de Session State e Carregamento de Dados
# =====================================
if "caixa_aberto" not in st.session_state:
    st.session_state["caixa_aberto"] = False
if "pedido_atual" not in st.session_state:
    st.session_state["pedido_atual"] = []

# --- Simulação de Produtos e Promoções (carregados na sessão) ---
if "produtos" not in st.session_state:
    st.session_state["produtos"] = pd.DataFrame([{
        "ID": "1", "Nome": "Teclado Sem Fio", "PrecoVista": 100.00, "CodigoBarras": "12345", "Quantidade": 10
    }, {
        "ID": "2", "Nome": "Mousepad Gamer", "PrecoVista": 50.00, "CodigoBarras": "67890", "Quantidade": 5
    }])
if "vendas" not in st.session_state:
    st.session_state["vendas"] = pd.DataFrame(columns=["IDVenda","Data","IDProduto","NomeProduto","CodigoBarras","FormaPagamento","Quantidade","PrecoUnitario","Total"])
if "promocoes" not in st.session_state:
    st.session_state["promocoes"] = pd.DataFrame(columns=["ID","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"])
if "clientes" not in st.session_state:
    st.session_state["clientes"] = pd.DataFrame(columns=["ID","Cliente","Produto","CodigoBarras","Valor","DataPagamento","Status","FormaPagamento"])
if "caixas" not in st.session_state:
    st.session_state["caixas"] = pd.DataFrame(columns=["Data","FaturamentoTotal","Dinheiro","PIX","Cartão","Fiado","Status"])


produtos = st.session_state["produtos"]
vendas = st.session_state["vendas"]
promocoes = st.session_state["promocoes"]
clientes = st.session_state["clientes"]
view = "Vendas" # Força a visualização para a aba Vendas

# =====================================
# INÍCIO DO CÓDIGO DA ABA VENDAS
# (Este é o código que você está procurando)
# =====================================

# 🔹 Resumo do Fechamento de Caixa (se houver)
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

    # O código original chama a geração de PDF aqui, mas foi omitido
    # para simplificar a demonstração do layout.
    
    st.write("---")

# 🔹 Fluxo de Vendas
if view == "Vendas":
    st.header("🛒 Vendas")
    if not st.session_state.get("caixa_aberto", False):
        st.info("⚠️ Para iniciar as vendas, abra o caixa abaixo:")
        abrir_caixa()
    else:
        operador = st.session_state.get("operador", "—")
        valor_inicial = st.session_state.get("valor_inicial", 0.0)
        st.success(f"✅ Caixa aberto! Operador: {operador} | Valor Inicial: {brl(valor_inicial)}")

        # --- Sub-abas ---
        tab1, tab2, tab3 = st.tabs(["Venda Detalhada", "Últimas Vendas", "Recibos de Vendas"])

        # ================= TAB 1 - VENDA DETALHADA =================
        with tab1:
            st.subheader("🛒 Venda Detalhada")
            st.markdown("### 🔍 Pesquisar Produto")
            sub1, sub2, sub3 = st.tabs(["Por Nome", "Por Código de Barras", "Por Foto"])

            # ---------------- PESQUISA POR NOME ----------------
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

            # ---------------- PESQUISA POR CÓDIGO DE BARRAS ----------------
            with sub2:
                codigo = st.text_input("Digite ou escaneie o código de barras", key="codigo_barras_venda")
                df_sel = produtos.copy()
                if codigo:
                    # Busca por ID ou CodigoBarras
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

            # ---------------- PESQUISA POR FOTO ----------------
            with sub3:
                foto = st.camera_input("Tirar foto do produto", key="foto_venda")
                if foto:
                    # Simulação de leitura de código de barras por foto
                    imagem_bytes = foto.getvalue()
                    codigos_lidos = ler_codigo_barras_api(imagem_bytes)
                    if codigos_lidos:
                        codigo_foto = codigos_lidos[0]
                        st.session_state["codigo_barras_venda"] = codigo_foto # Atualiza o campo de texto (se existir)
                        st.info(f"Código lido: {codigo_foto}. Adicione manualmente no campo de código.")
                    else:
                        st.warning("⚠️ Código de barras não detectado ou inválido.")

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

                # ---------------- MISTO ----------------
                if forma == "Misto":
                    st.markdown("#### Configuração do pagamento misto")
                    colm1, colm2 = st.columns(2)
                    with colm1:
                        forma1 = st.selectbox(
                            "Primeira forma",
                            ["Dinheiro", "PIX", "Cartão", "Fiado"],
                            key="misto_forma1"
                        )
                        valor1_input = st.number_input(
                            f"Valor em {forma1}",
                            min_value=0.0,
                            step=1.0,
                            key="misto_valor1"
                        )
                        valor1 = valor1_input
                    with colm2:
                        forma2 = st.selectbox(
                            "Segunda forma",
                            ["Dinheiro", "PIX", "Cartão", "Fiado"],
                            key="misto_forma2"
                        )
                        # O valor 2 é calculado após a exibição do pedido
                        valor2_input = st.number_input(
                            f"Valor em {forma2} (auto)",
                            min_value=0.0,
                            step=1.0,
                            value=0.0,
                            disabled=True,
                            key="misto_valor2"
                        )
                        valor2 = valor2_input # Usado apenas para passagem de parâmetro
                
                # ---------------- DESENHO DO PEDIDO ----------------
                df_pedido = desenha_pedido(forma, promocoes)
                valor_total = float(df_pedido["Total"].sum()) if not df_pedido.empty else 0.0
                
                # Re-cálculo do valor2 (misto) para exibição e uso
                if forma == "Misto" and forma1 and forma2:
                    # Aplica a correção do Cartão no valor TOTAL (não item a item)
                    valor1_ajustado_ao_total = valor1_input
                    if forma1 == "Cartão":
                         valor1_ajustado_ao_total = valor1_input * FATOR_CARTAO # O valor de venda precisa ser ajustado (desconto)

                    valor2_calculado = max(valor_total - valor1_ajustado_ao_total, 0.0)
                    
                    valor2_ajustado_ao_total = valor2_calculado
                    if forma2 == "Cartão":
                        valor2_ajustado_ao_total = valor2_calculado / FATOR_CARTAO # O valor de venda precisa ser ajustado (acréscimo)
                        
                    st.info(f"💳 Pagamento dividido (Total: {brl(valor_total)}): {forma1} = {brl(valor1_input)}, {forma2} = {brl(valor2_calculado)}")
                    
                    # Passa os valores de entrada originais (que serao corrigidos na funcao)
                    valor1 = valor1_input 
                    valor2 = valor2_calculado
                    

                # ---------------- DINHEIRO / FIADO ----------------
                if forma == "Dinheiro":
                    valor_recebido = st.number_input("💵 Valor recebido em dinheiro", min_value=0.0, step=1.0, value=valor_total)
                    troco = max(valor_recebido - valor_total, 0.0)
                elif forma == "Fiado":
                    nome_cliente = st.text_input("👤 Nome do Cliente")
                    data_pagamento = st.date_input("📅 Data prevista de pagamento", value=date.today())

                # ---------------- METRICS RESUMO ----------------
                st.markdown("#### Resumo da Venda")
                colA, colB, colC = st.columns(3)
                colA.metric("Valor Total", brl(valor_total))

                if forma == "Misto":
                    colB.metric(f"{forma1}", brl(valor1_input))
                    colC.metric(f"{forma2}", brl(valor2_calculado))
                elif forma == "Dinheiro":
                    colB.metric("Valor Recebido", brl(valor_recebido))
                    colC.metric("Troco", brl(max(valor_recebido - valor_total, 0.0)))
                elif forma == "Fiado":
                    colB.metric("Cliente", nome_cliente if nome_cliente else "—")
                    colC.metric("Data Pagamento", str(data_pagamento) if data_pagamento else "—")
                else: # PIX, Cartão
                    colB.metric("Pagamento", forma)
                    colC.metric("Status", "Aguardando Confirmação")


                # ================= BOTÕES DE AÇÃO =================
                b1, b2 = st.columns([1, 1])
                with b1:
                    if st.button("✅ Finalizar Venda", use_container_width=True, key="btn_finalizar_venda"):
                        # Chama a função de finalização de venda com todos os parâmetros
                        finalizar_venda(
                            forma, forma1, forma2, valor1, valor2, promocoes,
                            nome_cliente=nome_cliente, data_pagamento=data_pagamento,
                            valor_recebido=valor_recebido
                        )
                with b2:
                    if st.button("🆕 Nova Venda", use_container_width=True, key="btn_nova_venda"):
                        st.session_state["pedido_atual"] = []
                        st.success("Nova venda iniciada!")

                st.markdown("---")
            else:
                st.info("⚠️ Adicione um produto ao pedido para escolher a forma de pagamento.")

            # ================= BOTÃO FECHAR CAIXA =================
            if st.session_state.get("caixa_aberto", False):
                if st.button("📦 Fechar Caixa", use_container_width=True, key="btn_fechar_caixa_detalhada"):
                    fechar_caixa()


        # ================= TAB 2 - ÚLTIMAS VENDAS =================
        with tab2:
            st.subheader("📊 Últimas Vendas")
            if not vendas.empty:
                ult = vendas.sort_values(by=["Data", "IDVenda"], ascending=False).head(100)
                st.dataframe(ult, use_container_width=True, key="df_ultimas_vendas")

                # Simulação da lógica de exclusão de vendas (para referência)
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
                        if id_excluir and id_excluir != 0:
                            st.warning(f"Lógica de exclusão da Venda {id_excluir} acionada (devolve estoque).")
                            # A função de exclusão está completa no seu código, mas foi omitida aqui para foco no layout.
                            st.rerun()

            else:
                st.info("Ainda não há vendas registradas.")

        # ================= TAB 3 - RECIBOS =================
        with tab3:
            st.subheader("📄 Recibos de Vendas")

            if not vendas.empty:
                vendas_com_data = vendas[vendas["Data"].notna()].copy()
                if vendas_com_data.empty:
                    st.info("Nenhuma venda com data válida para gerar recibo.")
                else:
                    datas = sorted(vendas_com_data["Data"].astype(str).unique())
                    data_sel = st.selectbox("Selecione a data da venda", datas, key="recibo_data")
                    vendas_dia = vendas_com_data[vendas_com_data["Data"].astype(str) == data_sel]
                    ids_dia = sorted(vendas_dia["IDVenda"].astype(int).unique().tolist())
                    id_sel = st.selectbox("Selecione o ID da venda", ids_dia, key="recibo_id")

                    if st.button("Gerar Recibo (PDF)", key="btn_recibo"):
                        caminho_pdf = f"recibo_venda_{id_sel}.pdf"
                        gerar_pdf_venda(id_sel, vendas, caminho_pdf) # Gera o PDF dummy

                        with open(caminho_pdf, "rb") as f:
                            st.download_button(
                                label="⬇️ Baixar Recibo",
                                data=f,
                                file_name=caminho_pdf,
                                mime="application/pdf",
                                key="download_recibo"
                            )
                        st.success(f"Recibo da Venda {id_sel} gerado!")
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
      


