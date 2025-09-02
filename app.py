import streamlit as st
import pandas as pd
import os
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt


# PDF geração
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage

def gerar_recibo(venda, logo_path="ChatGPT Image 1_09_2025, 21_36_48.png"):
    filename = f"recibo_venda_{venda['IDVenda']}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    try:
        elementos.append(RLImage(logo_path, width=120, height=60))
    except:
        pass
    elementos.append(Paragraph("<b>Doce&Bella Cosmético</b>", styles["Title"]))
    elementos.append(Paragraph("📞 (41) 99168-6525", styles["Normal"]))
    elementos.append(Paragraph("📸 @docebellacosmetico", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    elementos.append(Paragraph(f"Data: {venda['Data']}", styles["Normal"]))
    elementos.append(Paragraph(f"Forma de Pagamento: {venda['FormaPagamento']}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    data = [["Produto", "Qtd", "Preço Unit.", "Total"]]

    if isinstance(venda.get("Itens"), list):
        for item in venda["Itens"]:
            data.append([
                item["NomeProduto"],
                item["Quantidade"],
                f"R$ {item['PrecoUnitario']:.2f}",
                f"R$ {item['Total']:.2f}"
            ])
    else:
        data.append([
            venda["NomeProduto"],
            venda["Quantidade"],
            f"R$ {venda['PrecoUnitario']:.2f}",
            f"R$ {venda['Total']:.2f}"
        ])

    tabela = Table(data, colWidths=[200, 50, 100, 100])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (1,1), (-1,-1), "CENTER")
    ]))
    elementos.append(tabela)

    elementos.append(Spacer(1, 12))

    total_geral = 0.0
    if isinstance(venda.get("Itens"), list):
        total_geral = sum(item["Total"] for item in venda["Itens"])
    else:
        total_geral = venda["Total"]

    elementos.append(Paragraph(f"<b>Valor Total: R$ {total_geral:.2f}</b>", styles["Heading2"]))

    elementos.append(Spacer(1, 24))
    elementos.append(Paragraph("<para align='center'><b>Obrigado pela sua compra, volte sempre!</b></para>", styles["Normal"]))

    elementos.append(Spacer(1, 36))
    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elementos.append(Paragraph(f"<para align='right'><font size=8>Recibo gerado em: {data_geracao}</font></para>", styles["Normal"]))

    doc.build(elementos)
    return filename


# PDF geração
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage

# =============================
# Função para gerar recibo PDF (suporta várias linhas de produtos)
# =============================
def gerar_recibo(venda, logo_path="ChatGPT Image 1_09_2025, 21_36_48.png"):
    filename = f"recibo_venda_{venda['IDVenda']}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Logo e informações da loja
    try:
        elementos.append(RLImage(logo_path, width=120, height=60))
    except:
        pass
    elementos.append(Paragraph("<b>Doce&Bella Cosmético</b>", styles["Title"]))
    elementos.append(Paragraph("📞 (41) 99168-6525", styles["Normal"]))
    elementos.append(Paragraph("📸 @docebellacosmetico", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # Dados da venda
    elementos.append(Paragraph(f"Data: {venda['Data']}", styles["Normal"]))
    elementos.append(Paragraph(f"Forma de Pagamento: {venda['FormaPagamento']}", styles["Normal"]))
    elementos.append(Spacer(1, 12))

    # Tabela de produtos
    data = [["Produto", "Qtd", "Preço Unit.", "Total"]]

    # Se for lista de produtos
    if isinstance(venda.get("Itens"), list):
        for item in venda["Itens"]:
            data.append([
                item["NomeProduto"],
                item["Quantidade"],
                f"R$ {item['PrecoUnitario']:.2f}",
                f"R$ {item['Total']:.2f}"
            ])
    else:
        # Venda simples (um produto)
        data.append([
            venda["NomeProduto"],
            venda["Quantidade"],
            f"R$ {venda['PrecoUnitario']:.2f}",
            f"R$ {venda['Total']:.2f}"
        ])

    tabela = Table(data, colWidths=[200, 50, 100, 100])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (1,1), (-1,-1), "CENTER")
    ]))
    elementos.append(tabela)

    elementos.append(Spacer(1, 12))

    # Total geral
    total_geral = 0.0
    if isinstance(venda.get("Itens"), list):
        total_geral = sum(item["Total"] for item in venda["Itens"])
    else:
        total_geral = venda["Total"]

    elementos.append(Paragraph(f"<b>Valor Total: R$ {total_geral:.2f}</b>", styles["Heading2"]))

    elementos.append(Spacer(1, 24))
    elementos.append(Paragraph("<para align='center'><b>Obrigado pela sua compra, volte sempre!</b></para>", styles["Normal"]))

    elementos.append(Spacer(1, 36))
    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elementos.append(Paragraph(f"<para align='right'><font size=8>Recibo gerado em: {data_geracao}</font></para>", styles["Normal"]))

    doc.build(elementos)
    return filename

# ===================================================
# No bloco de Vendas, se no futuro você permitir
# adicionar vários produtos de uma vez, basta montar
# a lista de itens e passar em venda["Itens"].
# ===================================================

# Exemplo de venda com vários itens:
# nova = {
#     "IDVenda": prox_id(vendas, "IDVenda"),
#     "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
#     "FormaPagamento": forma,
#     "Itens": [
#         {"NomeProduto": "Batom", "Quantidade": 2, "PrecoUnitario": 15.0, "Total": 30.0},
#         {"NomeProduto": "Perfume", "Quantidade": 1, "PrecoUnitario": 50.0, "Total": 50.0},
#     ]
# }
# pdf_file = gerar_recibo(nova)
