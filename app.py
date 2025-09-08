
# =====================================
# VENDAS (com sub-abas: Venda Detalhada, Últimas, Recibos)
# =====================================
if view == "Vendas":
    show_logo("main")
    st.header("🧾 Vendas")

    # 🔹 Configuração WhatsApp
    import requests
    from datetime import datetime, date
    import pytz

    WHATSAPP_TOKEN = "SEU_TOKEN_AQUI"  # coloque aqui o token válido da API do WhatsApp Cloud
    WHATSAPP_PHONE_ID = "823826790806739"
    WHATSAPP_API_URL = f"https://graph.facebook.com/v20.0/{WHATSAPP_PHONE_ID}/messages"
    NUMERO_DESTINO = "5541987876191"

    def enviar_whatsapp(destinatario, mensagem):
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": destinatario,
            "type": "text",
            "text": {"body": mensagem}
        }
        try:
            r = requests.post(WHATSAPP_API_URL, headers=headers, json=data)
            resp = r.json()
            print("DEBUG WHATSAPP:", resp)
            if "messages" not in resp:
                st.error(f"Erro WhatsApp: {resp}")
        except Exception as e:
            st.error(f"Erro ao enviar WhatsApp: {e}")

    # ========================================================
    # ABERTURA DE CAIXA
    # ========================================================
    def abrir_caixa():
        with st.form("abrir_caixa_form"):
            st.subheader("🟢 Abrir Caixa")

            operador = st.text_input("👤 Nome do Operador", key="input_operador")
            valor_inicial = st.number_input("💵 Valor Inicial do Caixa", min_value=0.0, step=1.0, key="input_valor_inicial")

            submitted = st.form_submit_button("🚀 Abrir Caixa")
            if submitted:
                if not operador:
                    st.warning("⚠️ Informe o nome do operador para abrir o caixa.")
                else:
                    st.session_state["operador"] = operador
                    st.session_state["valor_inicial"] = valor_inicial
                    st.session_state["caixa_aberto"] = True
                    st.success(f"✅ Caixa aberto com sucesso! Operador: {operador} | Valor inicial: {valor_inicial:.2f}")
                    st.rerun()

    # ========================================================
    # FECHAMENTO DE CAIXA (alterado)
    # ========================================================
    def fechar_caixa():
        if "caixa_aberto" in st.session_state and st.session_state["caixa_aberto"]:
            operador = st.session_state.get("operador", "—")
            valor_inicial = st.session_state.get("valor_inicial", 0.0)
            hoje = str(date.today())

            # 🔹 Filtrar vendas do dia
            vendas["Data"] = pd.to_datetime(vendas["Data"], errors="coerce")
            vendas_dia = vendas[vendas["Data"].dt.strftime("%Y-%m-%d") == hoje]

            # 🔹 Calcular totais por forma de pagamento
            total_dinheiro = vendas_dia[vendas_dia["FormaPagamento"] == "Dinheiro"]["Total"].sum()
            total_pix = vendas_dia[vendas_dia["FormaPagamento"] == "PIX"]["Total"].sum()
            total_cartao = vendas_dia[vendas_dia["FormaPagamento"] == "Cartão"]["Total"].sum()
            total_fiado = vendas_dia[vendas_dia["FormaPagamento"] == "Fiado"]["Total"].sum()
            total_misto = vendas_dia[vendas_dia["FormaPagamento"] == "Misto"]["Total"].sum()
            faturamento_total = total_dinheiro + total_pix + total_cartao + total_fiado + total_misto

            # 🔹 Perguntar valor final do caixa (dinheiro físico contado)
            valor_final = st.number_input(
                "💵 Informe o valor final do caixa (dinheiro físico contado)",
                min_value=0.0,
                step=1.0,
                key="valor_final_caixa"
            )

            if st.button("✅ Confirmar Fechamento de Caixa", key="btn_confirmar_fechamento"):
                # 🔹 Montar dados do caixa
                dados_caixa = {
                    "Data": hoje,
                    "Operador": operador,
                    "ValorInicial": valor_inicial,
                    "ValorFinal": valor_final,
                    "FaturamentoTotal": faturamento_total,
                    "Dinheiro": total_dinheiro,
                    "PIX": total_pix,
                    "Cartão": total_cartao,
                    "Fiado": total_fiado,
                    "Misto": total_misto,
                    "Status": "Fechado"
                }

                # 🔹 Atualizar CSV de caixas
                caixas = norm_caixas(pd.DataFrame())
                caixas = pd.concat([caixas, pd.DataFrame([dados_caixa])], ignore_index=True)
                save_csv_github(caixas, ARQ_CAIXAS, f"Fechamento de caixa {hoje}")

                # 🔹 Exibir relatório resumido
                st.subheader("📊 Relatório de Fechamento")
                resumo = pd.DataFrame([
                    ["Dinheiro", total_dinheiro],
                    ["PIX", total_pix],
                    ["Cartão", total_cartao],
                    ["Fiado", total_fiado],
                    ["Misto", total_misto],
                    ["TOTAL", faturamento_total],
                    ["Valor Final (informado)", valor_final],
                    ["Diferença (Dinheiro vs Informado)", valor_final - total_dinheiro]
                ], columns=["Categoria", "Valor"])
                resumo["Valor"] = resumo["Valor"].apply(brl)
                st.dataframe(resumo, use_container_width=True)

                # 🔹 Gerar PDF
                caminho_pdf = f"caixa_{hoje}.pdf"
                gerar_pdf_caixa(dados_caixa, vendas_dia, caminho_pdf)
                with open(caminho_pdf, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Baixar Relatório de Caixa ({hoje})",
                        data=f,
                        file_name=caminho_pdf,
                        mime="application/pdf",
                        key="download_caixa"
                    )

                # 🔹 Fechar caixa na sessão
                st.session_state["caixa_aberto"] = False
                st.success(f"📦 Caixa fechado! Operador: {operador}")
                st.rerun()
