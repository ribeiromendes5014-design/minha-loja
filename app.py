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

# =============================
# Função para gerar recibo PDF (suporta várias linhas de produtos)
# =============================
def gerar_recibo(venda, logo_path=None):
    filename = f"recibo_venda_{venda['IDVenda']}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Logo (opcional)
    if logo_path and os.path.exists(logo_path):
        try:
            elementos.append(RLImage(logo_path, width=120, height=60))
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    # Informações da loja
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

    itens = venda.get("Itens")
    if isinstance(itens, list) and len(itens) > 0:
        for item in itens:
            data.append([
                item["NomeProduto"],
                item["Quantidade"],
                f"R$ {item['PrecoUnitario']:.2f}",
                f"R$ {item['Total']:.2f}"
            ])
        total_geral = sum(item["Total"] for item in itens)
    else:
        data.append([
            venda["NomeProduto"],
            venda["Quantidade"],
            f"R$ {venda['PrecoUnitario']:.2f}",
            f"R$ {venda['Total']:.2f}"
        ])
        total_geral = venda["Total"]

    tabela = Table(data, colWidths=[200, 50, 100, 100])
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (1,1), (-1,-1), "CENTER")
    ]))
    elementos.append(tabela)

    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph(f"<b>Valor Total: R$ {total_geral:.2f}</b>", styles["Heading2"]))

    # Rodapé
    elementos.append(Spacer(1, 24))
    elementos.append(Paragraph("<para align='center'><b>Obrigado pela sua compra, volte sempre!</b></para>", styles["Normal"]))

    elementos.append(Spacer(1, 36))
    data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elementos.append(Paragraph(f"<para align='right'><font size=8>Recibo gerado em: {data_geracao}</font></para>", styles["Normal"]))

    doc.build(elementos)
    return filename
