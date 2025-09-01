
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
import streamlit as st
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
import pandas as pd
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
import os
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
from datetime import datetime, date, timedelta
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
import matplotlib.pyplot as plt
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# Configurações
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
st.set_page_config(page_title="Sistema Loja - Cosméticos", layout="wide")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
FATOR_CARTAO = 0.8872
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
ARQ_PRODUTOS = "produtos.csv"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
ARQ_VENDAS = "vendas.csv"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
ARQ_PROMOCOES = "promocoes.csv"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
ARQ_CLIENTES = "clientes.csv"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# --- Integração opcional com Google Drive ---
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# IDs dos arquivos no Google Drive (fornecidos pelo usuário)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
DRIVE_IDS = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    "produtos.csv": "1p1UyY7DdkNG1RlEwOKwLaJ9mgwFTpkAC",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    "clientes.csv": "1DO60F8Eu43xurBDhIxvp0ysMac7LSDkE",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    "vendas.csv":   "1EIREc1zPSRY0OS7xz8d5hpOMI2c43mBI",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    "promocoes.csv":"1CqwlBWv43XO0XWsgRvBjfXgurZlqslIk",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
}
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def _drive_file_id(caminho: str):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    base = os.path.basename(caminho)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return DRIVE_IDS.get(base)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def ler_csv_drive(file_id: str):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Lê direto do Google Drive usando o link de exportação
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    import pandas as _pd
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    url = f"https://drive.google.com/uc?id={file_id}"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return _pd.read_csv(url)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def enviar_csv_drive(df: pd.DataFrame, file_id: str):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Envia para o Google Drive se pydrive2 estiver configurado (opcional)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        from pydrive2.auth import GoogleAuth
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        from pydrive2.drive import GoogleDrive
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        import tempfile
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        gauth = GoogleAuth()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Tenta autenticar com Service Account via st.secrets["service_account_json"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            import streamlit as _st
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            sa_json = _st.secrets.get("service_account_json", None)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            sa_json = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if sa_json:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            import json
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            tmpjson = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            tmpjson.write(sa_json.encode("utf-8"))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            tmpjson.flush()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            gauth.settings['service_config'] = {'client_json_file_path': tmpjson.name}
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            gauth.ServiceAccountAuth()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            # Fallback (local): abrirá navegador. Em Streamlit Cloud, ignore silenciosamente.
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                gauth.LocalWebserverAuth()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                return
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        drive = GoogleDrive(gauth)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df.to_csv(tmp.name, index=False)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        gfile = drive.CreateFile({'id': file_id})
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        gfile.SetContentFile(tmp.name)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        gfile.Upload()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Falha silenciosa: mantém gravação local funcionando
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        pass
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# Utilidades
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_produtos(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["ID","Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in ["PrecoCusto","PrecoVista","PrecoCartao"]:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Validade"] = df["Validade"].astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["ID","Cliente","Produto","Valor","DataPagamento"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_vendas(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["IDVenda","Data","IDProduto","NomeProduto","FormaPagamento","Quantidade","PrecoUnitario","Total"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in ["PrecoUnitario","Total"]:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Data"] = df["Data"].astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["ID","Cliente","Produto","Valor","DataPagamento"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_promocoes(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["IDPromo","IDProduto","NomeProduto","Desconto","DataInicio","DataFim"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Desconto"] = pd.to_numeric(df["Desconto"], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["DataInicio"] = pd.to_datetime(df["DataInicio"], errors="coerce").dt.date.astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["DataFim"] = pd.to_datetime(df["DataFim"], errors="coerce").dt.date.astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def garantir_colunas_clientes(df: pd.DataFrame) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    cols = ["ID","Cliente","Produto","Valor","DataPagamento"]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df is None or df.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return pd.DataFrame(columns=cols)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for c in cols:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if c not in df.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df[c] = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0).astype(float)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df["DataPagamento"] = pd.to_datetime(df["DataPagamento"], errors="coerce").dt.date.astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return df[cols].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def carregar_csv(caminho: str, cols_func) -> pd.DataFrame:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df = pd.DataFrame()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    file_id = _drive_file_id(caminho)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if file_id:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df = ler_csv_drive(file_id)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df = pd.DataFrame()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if (df is None or df.empty) and os.path.exists(caminho):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df = pd.read_csv(caminho)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df = pd.DataFrame()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return cols_func(df)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def salvar_csv(df: pd.DataFrame, caminho: str):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Salva localmente
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df.to_csv(caminho, index=False)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # E opcionalmente envia ao Google Drive
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    file_id = _drive_file_id(caminho)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if file_id:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            enviar_csv_drive(df, file_id)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            pass
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def prox_id(df: pd.DataFrame, col: str) -> int:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return (int(df[col].max()) + 1) if not df.empty else 1
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
def preco_com_promocao(pid, preco_normal):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    hoje = date.today()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    promos = promocoes[promocoes["IDProduto"] == pid]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if promos.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        return preco_normal, False, None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    for _, r in promos.iterrows():
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        try:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            di = pd.to_datetime(r["DataInicio"]).date()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            df = pd.to_datetime(r["DataFim"]).date()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        except Exception:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            continue
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if di <= hoje <= df:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            preco_desc = preco_normal * (1 - float(r["Desconto"]) / 100)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            return preco_desc, True, r
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    return preco_normal, False, None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# Carregar dados
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
produtos = carregar_csv(ARQ_PRODUTOS, garantir_colunas_produtos)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
vendas = carregar_csv(ARQ_VENDAS, garantir_colunas_vendas)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
promocoes = carregar_csv(ARQ_PROMOCOES, garantir_colunas_promocoes)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
clientes = carregar_csv(ARQ_CLIENTES, garantir_colunas_clientes)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
st.sidebar.title("📚 Menu")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
view = st.sidebar.radio("Navegar", ["Dashboard","Produtos","Vendas","Fluxo de Caixa","Promoções","Clientes"], index=0)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# DASHBOARD
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
if view == "Dashboard":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("📊 Dashboard Geral")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    col1, col2, col3 = st.columns(3)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col1:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        total_estoque = produtos["Quantidade"].sum()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("📦 Total em Estoque", total_estoque)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col2:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        vendas_hoje = vendas[vendas["Data"].str.startswith(datetime.now().strftime("%Y-%m-%d"))]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        total_hoje = vendas_hoje["Total"].sum()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("🛒 Vendas de Hoje", f"R$ {total_hoje:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col3:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        hoje = date.today()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        prom_ativas = promocoes[
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            (pd.to_datetime(promocoes["DataInicio"]) <= pd.to_datetime(hoje)) &
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            (pd.to_datetime(promocoes["DataFim"]) >= pd.to_datetime(hoje))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        ]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("🏷️ Promoções Ativas", len(prom_ativas))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.markdown("---")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.subheader("Resumo de Vendas por Mês")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if not vendas.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        vendas["DataMes"] = pd.to_datetime(vendas["Data"]).dt.to_period("M").astype(str)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        resumo = vendas.groupby("DataMes")["Total"].sum()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # 🔽 Filtro de meses passados
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        mes_escolhido = st.selectbox("📅 Selecionar mês", resumo.index.tolist())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        total_mes = resumo.loc[mes_escolhido]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("🛒 Vendas no mês selecionado", f"R$ {total_mes:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.bar_chart(resumo)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Sem vendas registradas.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# PRODUTOS
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
if view == "Produtos":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("🛍️ Produtos")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # 🔔 Alerta de estoque baixo
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    baixo_estoque = produtos[produtos["Quantidade"] <= 1]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if not baixo_estoque.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        nomes_alerta = ", ".join([f"{row['Nome']} (Estoque: {row['Quantidade']})" for _, row in baixo_estoque.iterrows()])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.warning(f"⚠️ Produtos com estoque baixo: {nomes_alerta}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Cadastro de produtos
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with st.form("form_produto", clear_on_submit=True):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.subheader("Cadastrar novo produto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        nome = st.text_input("Nome do Produto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        marca = st.text_input("Marca")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        categoria = st.text_input("Categoria")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        validade = st.date_input("Validade", value=date.today())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        quantidade = st.number_input("Quantidade", min_value=0, step=1, value=0)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        preco_custo = st.number_input("Preço de Custo", min_value=0.0, step=0.01, format="%.2f")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        preco_vista = st.number_input("Preço à Vista", min_value=0.0, step=0.01, format="%.2f")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        preco_cartao = preco_vista / FATOR_CARTAO if preco_vista > 0 else 0.0
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("Preço no Cartão (automático)", f"R$ {preco_cartao:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        salvar = st.form_submit_button("➕ Adicionar Produto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if salvar:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if not nome.strip():
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.error("O nome do produto é obrigatório.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                novo = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "ID": prox_id(produtos, "ID"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Nome": nome.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Marca": marca.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Categoria": categoria.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Quantidade": int(quantidade),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "PrecoCusto": float(preco_custo),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "PrecoVista": float(preco_vista),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "PrecoCartao": float(preco_cartao),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Validade": str(validade)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                }
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                produtos = pd.concat([produtos, pd.DataFrame([novo])], ignore_index=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_csv(produtos, ARQ_PRODUTOS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.success(f"Produto '{nome}' adicionado com sucesso!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Filtros de busca
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.markdown("---")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.subheader("🔎 Buscar Produtos")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    col1, col2, col3 = st.columns(3)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col1:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        filtro_nome = st.text_input("Buscar por Nome")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col2:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        filtro_marca = st.selectbox("Filtrar por Marca", [""] + sorted(produtos["Marca"].dropna().unique().tolist()))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with col3:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        max_preco = st.number_input("Preço máximo", min_value=0.0, step=0.01, value=0.0)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    df_filtrado = produtos.copy()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if filtro_nome:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df_filtrado = df_filtrado[df_filtrado["Nome"].str.contains(filtro_nome, case=False, na=False)]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if filtro_marca:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df_filtrado = df_filtrado[df_filtrado["Marca"] == filtro_marca]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if max_preco > 0:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        df_filtrado = df_filtrado[df_filtrado["PrecoVista"] <= max_preco]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.markdown("### 📋 Lista de Produtos")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if df_filtrado.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Nenhum produto encontrado com os filtros.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.dataframe(df_filtrado, use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Edição/Exclusão
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if not produtos.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        opt = st.selectbox("Selecionar produto para editar/excluir", [f'{int(r.ID)} - {r.Nome}' for r in produtos.itertuples(index=False)])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if opt:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            pid = int(opt.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            prod_sel = produtos[produtos["ID"] == pid].iloc[0]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            with st.form("form_editar_produto", clear_on_submit=False):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                nome_e = st.text_input("Nome", value=prod_sel["Nome"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                marca_e = st.text_input("Marca", value=prod_sel["Marca"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                categoria_e = st.text_input("Categoria", value=prod_sel["Categoria"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                validade_e = st.date_input("Validade", value=pd.to_datetime(prod_sel["Validade"]).date())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                quantidade_e = st.number_input("Quantidade", min_value=0, step=1, value=int(prod_sel["Quantidade"]))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                preco_custo_e = st.number_input("Preço de Custo", min_value=0.0, step=0.01, value=float(prod_sel["PrecoCusto"]))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                preco_vista_e = st.number_input("Preço à Vista", min_value=0.0, step=0.01, value=float(prod_sel["PrecoVista"]))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                preco_cartao_e = preco_vista_e / FATOR_CARTAO if preco_vista_e > 0 else 0.0
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.metric("Preço no Cartão (automático)", f"R$ {preco_cartao_e:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_edicao = st.form_submit_button("💾 Salvar alterações")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                excluir_prod = st.form_submit_button("🗑️ Excluir produto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if salvar_edicao:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    produtos.loc[produtos["ID"] == pid, ["Nome","Marca","Categoria","Quantidade","PrecoCusto","PrecoVista","PrecoCartao","Validade"]] = [
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        nome_e.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        marca_e.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        categoria_e.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        int(quantidade_e),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        float(preco_custo_e),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        float(preco_vista_e),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        float(preco_cartao_e),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        str(validade_e),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    ]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(produtos, ARQ_PRODUTOS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.success("Produto atualizado com sucesso!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if excluir_prod:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    produtos = produtos[produtos["ID"] != pid].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(produtos, ARQ_PRODUTOS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.warning("Produto excluído com sucesso!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# VENDAS
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
elif view == "Vendas":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("🧾 Vendas")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if produtos.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Cadastre produtos primeiro.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        opt = st.selectbox("Produto", [f'{int(r.ID)} - {r.Nome} (Estoque: {int(r.Quantidade)})' for r in produtos.itertuples(index=False)])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        pid = int(opt.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        p = produtos[produtos["ID"] == pid].iloc[0]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("Preço à vista", f'R$ {p["PrecoVista"]:.2f}')
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("Preço no cartão", f'R$ {p["PrecoCartao"]:.2f}')
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.metric("Estoque", int(p["Quantidade"]))
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        qtd = st.number_input("Quantidade", min_value=1, step=1, value=1)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        forma = st.selectbox("Forma de pagamento", ["Pix","Dinheiro","Cartão","Fiado"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        preco_unit = float(p["PrecoVista"]) if forma in ("Pix","Dinheiro","Fiado") else float(p["PrecoCartao"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Campos extras para Fiado
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    nome_cliente_fiado = ""
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    data_pagamento_fiado = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if forma == "Fiado":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        nome_cliente_fiado = st.text_input("Nome do Cliente (Fiado)")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        data_pagamento_fiado = st.date_input("Data de Pagamento (Fiado)", value=date.today())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    preco_final, em_promo, promo = preco_com_promocao(pid, preco_unit)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if em_promo:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.markdown(f"<span style='color:red; font-weight:bold'>💥 Promoção: R$ {preco_final:.2f}</span> <del>R$ {preco_unit:.2f}</del>", unsafe_allow_html=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.info(f"Valor unitário selecionado: R$ {preco_final:.2f} ({forma})")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if st.button("Registrar Venda"):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if qtd > int(p["Quantidade"]):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.error("Estoque insuficiente.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                total = float(qtd) * preco_final
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                nova = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "IDVenda": prox_id(vendas, "IDVenda"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "IDProduto": int(p["ID"]),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "NomeProduto": str(p["Nome"]),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "FormaPagamento": forma,
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Quantidade": int(qtd),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "PrecoUnitario": float(preco_final),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    "Total": float(total),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                }
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                vendas = pd.concat([vendas, pd.DataFrame([nova])], ignore_index=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_csv(vendas, ARQ_VENDAS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                produtos.loc[produtos["ID"] == pid, "Quantidade"] = int(p["Quantidade"]) - int(qtd)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_csv(produtos, ARQ_PRODUTOS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                # Se for fiado, registra também em clientes (valor à vista)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if forma == "Fiado":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    valor_fiado = float(total)  # já com promoções aplicadas, sempre baseado no PrecoVista
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    novo_cli = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "ID": prox_id(clientes, "ID"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "Cliente": nome_cliente_fiado.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "Produto": str(p["Nome"]),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "Valor": float(valor_fiado),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "DataPagamento": str(data_pagamento_fiado or date.today()),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "Status": "Aberto",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    }
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    clientes = pd.concat([clientes, pd.DataFrame([novo_cli])], ignore_index=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(clientes, ARQ_CLIENTES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.success(f"Venda registrada! Total R$ {total:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.markdown("---")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.subheader("Histórico de Vendas")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.dataframe(vendas, use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if not vendas.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        sel_v = st.selectbox("Selecionar venda para excluir", [f'{int(r.IDVenda)} - {r.NomeProduto}' for r in vendas.itertuples(index=False)])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if sel_v:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            vid = int(sel_v.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            venda_sel = vendas[vendas["IDVenda"] == vid].iloc[0]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if st.button("🗑️ Excluir venda selecionada"):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                pid = int(venda_sel["IDProduto"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                qtd_vendida = int(venda_sel["Quantidade"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if pid in produtos["ID"].values:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    produtos.loc[produtos["ID"] == pid, "Quantidade"] += qtd_vendida
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(produtos, ARQ_PRODUTOS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                vendas = vendas[vendas["IDVenda"] != vid].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_csv(vendas, ARQ_VENDAS)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.warning("Venda excluída e estoque atualizado.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# FLUXO DE CAIXA (adições de relatórios)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
elif view == "Fluxo de Caixa":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("💵 Fluxo de Caixa")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if vendas.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Sem vendas ainda.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        receita_bruta = float(vendas["Total"].sum())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        vendas["Liquido"] = vendas.apply(
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            lambda r: float(r["Total"]) * (FATOR_CARTAO if str(r["FormaPagamento"]) == "Cartão" else 1.0),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            axis=1
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        )
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        receita_liquida = float(vendas["Liquido"].sum())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        custo_total = 0.0
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        for _, v in vendas.iterrows():
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            pid = int(v["IDProduto"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            prod = produtos[produtos["ID"] == pid]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if not prod.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                custo_total += float(v["Quantidade"]) * float(prod.iloc[0]["PrecoCusto"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        lucro_liquido = receita_liquida - custo_total
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        col1, col2, col3 = st.columns(3)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        col1.metric("Receita Bruta", f"R$ {receita_bruta:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        col2.metric("Receita Líquida (pós taxa)", f"R$ {receita_liquida:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        col3.metric("Lucro Líquido", f"R$ {lucro_liquido:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.markdown("---")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.subheader("📈 Gráficos")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Vendas por forma de pagamento
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        forma_pg = vendas.groupby("FormaPagamento")["Total"].sum()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        fig, ax = plt.subplots()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        ax.pie(forma_pg, labels=forma_pg.index, autopct="%1.1f%%")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        ax.set_title("Distribuição por Forma de Pagamento")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.pyplot(fig)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Exportação CSV
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.download_button("⬇️ Exportar Vendas (CSV)", vendas.to_csv(index=False), "vendas_exportadas.csv", "text/csv")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# PROMOÇÕES (adições de validação)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
# =============================
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
elif view == "Promoções":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("🏷️ Promoções")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if produtos.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Cadastre produtos antes de criar promoções.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        with st.form("form_promo", clear_on_submit=True):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            produto_options = [f"{int(r.ID)} - {r.Nome}" for r in produtos.itertuples(index=False)]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            produto_opt = st.selectbox("Produto", produto_options) if produto_options else None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if produto_opt:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                pid = int(produto_opt.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                nome_prod = produtos.loc[produtos["ID"] == pid, "Nome"].iloc[0]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                pid = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                nome_prod = None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            desconto = st.number_input("Desconto (%)", min_value=1.0, max_value=100.0, step=1.0, value=10.0)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            di = st.date_input("Data início", value=date.today())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            dfim = st.date_input("Data fim", value=date.today())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            salvar = st.form_submit_button("➕ Criar promoção")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if salvar:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if pid is None:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.error("Selecione um produto.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                elif dfim < di:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.error("A data final não pode ser antes da inicial.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                elif not promocoes[(promocoes["IDProduto"] == pid)].empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.warning("Já existe uma promoção cadastrada para este produto.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    nova = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "IDPromo": prox_id(promocoes, "IDPromo"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "IDProduto": pid,
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "NomeProduto": nome_prod,
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "Desconto": float(desconto),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "DataInicio": str(di),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        "DataFim": str(dfim),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    }
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    promocoes = pd.concat([promocoes, pd.DataFrame([nova])], ignore_index=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(promocoes, ARQ_PROMOCOES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.success("Promoção criada com sucesso!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.markdown("### 📋 Promoções cadastradas")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if promocoes.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Nenhuma promoção cadastrada.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.dataframe(promocoes, use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        promo_options = [f"{int(r.IDPromo)} - {r.NomeProduto}" for r in promocoes.itertuples(index=False)]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        promo_opt = st.selectbox("Selecionar promoção para excluir", promo_options) if promo_options else None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if st.button("🗑️ Excluir promoção selecionada") and promo_opt:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            pid_del = int(promo_opt.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            promocoes = promocoes[promocoes["IDPromo"] != pid_del].reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            salvar_csv(promocoes, ARQ_PROMOCOES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.warning("Promoção excluída com sucesso!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
elif view == "Clientes":
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.title("👥 Clientes - Vendas Fiado")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    # Formulário para adicionar fiado manualmente (opcional)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    with st.form("form_clientes_fiado", clear_on_submit=True):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        nome_cliente = st.text_input("Nome do Cliente")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        produto_cli = st.text_input("Produto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        valor_cli = st.number_input("Valor da Dívida (R$)", min_value=0.0, step=0.01, format="%.2f")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        data_pag = st.date_input("Data de Pagamento", value=date.today())
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        salvar_cli = st.form_submit_button("➕ Adicionar Venda Fiado")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if salvar_cli:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            nova = {
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "ID": prox_id(clientes, "ID"),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "Cliente": nome_cliente.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "Produto": produto_cli.strip(),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "Valor": float(valor_cli),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "DataPagamento": str(data_pag),
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                "Status": "Aberto",
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            }
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            clientes = pd.concat([clientes, pd.DataFrame([nova])], ignore_index=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            salvar_csv(clientes, ARQ_CLIENTES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.success("Venda fiado registrada!")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    st.subheader("📋 Dívidas cadastradas")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    if clientes.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.info("Nenhuma venda fiado registrada.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.dataframe(clientes, use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Dívidas em aberto
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if "Status" not in clientes.columns:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            clientes["Status"] = "Aberto"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        abertas = clientes[clientes["Status"] != "Pago"].copy()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.subheader("🔓 Dívidas em Aberto")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if abertas.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.info("Sem dívidas em aberto.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            # Seleção da dívida para agir
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            opts = [f"{idx} - {row.Cliente} - {row.Produto} - R$ {float(row.Valor):.2f} - {row.DataPagamento}"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    for idx, row in abertas.iterrows()]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            escolha = st.selectbox("Selecione uma dívida", opts) if opts else None
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            col_a, col_b = st.columns([1,1])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            with col_a:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                forma_pg_quit = st.selectbox("Forma de Pagamento (quitar)", ["Dinheiro", "Pix", "Cartão"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            with col_b:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                if st.button("💰 Marcar como Pago", use_container_width=True) and escolha:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    idx = int(escolha.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    valor_original = float(abertas.loc[idx, "Valor"])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    if forma_pg_quit in ("Dinheiro", "Pix"):
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        valor_pago = valor_original
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    else:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        # Aplica taxa do cartão (usa FATOR_CARTAO se já definido na venda; senão 1/0.8872 ~ 1.1274)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        fator = 1.0 / FATOR_CARTAO if FATOR_CARTAO not in (0, None) else 1.1275
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                        valor_pago = round(valor_original * fator, 2)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    clientes.loc[idx, "Status"] = "Pago"
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    salvar_csv(clientes, ARQ_CLIENTES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                    st.success(f"Dívida quitada com {forma_pg_quit}. Valor pago: R$ {valor_pago:.2f}")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            if st.button("🗑️ Excluir dívida selecionada", use_container_width=True) and escolha:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                idx = int(escolha.split(" - ")[0])
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                clientes = clientes.drop(index=idx).reset_index(drop=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                salvar_csv(clientes, ARQ_CLIENTES)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
                st.warning("Dívida excluída.")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")

elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        # Alertas
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.markdown("---")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        st.subheader("⏱️ Alertas de Vencimento")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        hoje = date.today()
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        clientes["DataPagamento"] = pd.to_datetime(clientes["DataPagamento"], errors="coerce").dt.date
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        vencidas = clientes[(clientes["Status"] != "Pago") & (clientes["DataPagamento"] < hoje)]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        a_vencer = clientes[(clientes["Status"] != "Pago") & (clientes["DataPagamento"] >= hoje) & (clientes["DataPagamento"] <= hoje + timedelta(days=3))]
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if not a_vencer.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.info("⏳ Dívidas a vencer (próximos 3 dias)")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.dataframe(a_vencer[["Cliente","Produto","Valor","DataPagamento"]], use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
        if not vencidas.empty:
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.error("⚠️ Dívidas vencidas")
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
            st.dataframe(vencidas[["Cliente","Produto","Valor","DataPagamento"]], use_container_width=True)
elif aba == "Promoções":
    st.title("🎯 Promoções")

    if produtos.empty:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("promocoes_form"):
            produto_opt = st.selectbox("Produto", produtos_list)

            if produto_opt:
                pid = int(produto_opt.split(" - ")[0])
                em_promo = promos["ProdutoID"].astype(str).eq(str(pid)).any()
                if em_promo:
                    st.info("Produto já está em promoção.")
                desconto = st.number_input("Desconto (%)", min_value=0.0, max_value=100.0, step=1.0)
                salvar_promo = st.form_submit_button("Salvar Promoção")

                if salvar_promo:
                    nova = {
                        "ID": prox_id(promos, "ID"),
                        "ProdutoID": pid,
                        "Desconto": desconto
                    }
                    promos = pd.concat([promos, pd.DataFrame([nova])], ignore_index=True)
                    salvar_csv(promos, ARQ_PROMOCOES)
                    st.success("Promoção registrada!")

    st.subheader("📋 Promoções Ativas")
    if promos.empty:
        st.info("Nenhuma promoção ativa.")
    else:
        st.dataframe(promos, use_container_width=True)
        if st.button("🗑️ Excluir todas promoções"):
            promos = pd.DataFrame(columns=promos.columns)
            salvar_csv(promos, ARQ_PROMOCOES)
            st.warning("Todas promoções excluídas!")
