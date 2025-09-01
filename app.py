# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from datetime import datetime, date
from drive_store import (
    load_csv, save_csv, ensure_file, list_files_in_folder,
    backup_csv, DRIVE_FOLDER_ID
)

st.set_page_config(page_title="Loja Cosméticos - Online", layout="wide")

# ------------ Configurações ------------
PRODUTOS_FILE = "produtos.csv"
VENDAS_FILE    = "vendas.csv"
PROMOS_FILE    = "promocoes.csv"
CARTAO_DIVISOR = 0.8873  # Valor no cartão é PrecoVista / 0.8873

# Garante que os arquivos existam no Drive (com cabeçalho)
ensure_file(PRODUTOS_FILE, [
    "ID","Nome","Marca","Categoria","Quantidade","PrecoCusto",
    "PrecoVista","PrecoCartao","Validade","MinEstoque"
])
ensure_file(VENDAS_FILE, [
    "ID","Data","ProdutoID","ProdutoNome","Quantidade","PrecoUnit","FormaPgto","Total"
])
ensure_file(PROMOS_FILE, ["ProdutoID","ProdutoNome","Descricao","DescontoPct","Validade"])

# Helpers
def _next_id(df: pd.DataFrame) -> int:
    if df.empty: 
        return 1
    try:
        return int(df["ID"].max()) + 1
    except Exception:
        return len(df) + 1

def preco_cartao(preco_vista: float) -> float:
    try:
        return round(float(preco_vista) / CARTAO_DIVISOR, 2)
    except Exception:
        return 0.0

def load_all():
    produtos = load_csv(PRODUTOS_FILE)
    vendas = load_csv(VENDAS_FILE)
    return produtos, vendas

def salvar_produtos(df):
    backup_csv(PRODUTOS_FILE, df)
    save_csv(PRODUTOS_FILE, df)

def salvar_vendas(df):
    backup_csv(VENDAS_FILE, df)
    save_csv(VENDAS_FILE, df)

# ------------ Barra lateral ------------
with st.sidebar:
    st.header("Menu")
    page = st.radio("Ir para:", ["Produtos", "Vendas", "Dashboard"], index=0)

# ------------ Páginas ------------
produtos_df, vendas_df = load_all()

if page == "Produtos":
    st.title("🛍️ Produtos")
if not produtos_df.empty:
    baixo = produtos_df[produtos_df["Quantidade"] <= produtos_df["MinEstoque"]]
    if not baixo.empty:
        st.warning("⚠️ Produtos com estoque baixo: " + ", ".join(baixo["Nome"].astype(str).tolist()))


    with st.expander("Cadastrar novo produto", expanded=True):
        col1, col2 = st.columns([3,1])
        nome = col1.text_input("Nome do Produto")
        min_estoque = col2.number_input("Estoque mínimo (alerta)", min_value=0, value=1, step=1)

        marca = st.text_input("Marca")
        categoria = st.text_input("Categoria")
        validade = st.date_input("Validade", value=date.today())

        quantidade = st.number_input("Quantidade", min_value=0, step=1)
        preco_custo = st.number_input("Preço de Custo", min_value=0.0, step=0.01, format="%.2f")
        preco_vista = st.number_input("Preço à Vista", min_value=0.0, step=0.01, format="%.2f")
        st.caption("Preço no Cartão (automático)")
        preco_cartao_calc = preco_cartao(preco_vista)
        st.metric("Preço no Cartão", f"R$ {preco_cartao_calc:,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))

        if st.button("➕ Adicionar Produto", type="primary", use_container_width=False):
            if not nome.strip():
                st.warning("Informe o nome do produto.")
            else:
                new_id = _next_id(produtos_df)
                novo = {
                    "ID": new_id,
                    "Nome": nome.strip(),
                    "Marca": marca.strip() or None,
                    "Categoria": categoria.strip() or None,
                    "Quantidade": int(quantidade),
                    "PrecoCusto": float(preco_custo),
                    "PrecoVista": float(preco_vista),
                    "PrecoCartao": float(preco_cartao_calc),
                    "Validade": validade.strftime("%Y-%m-%d"),
                    "MinEstoque": int(min_estoque),
                }
                produtos_df = pd.concat([produtos_df, pd.DataFrame([novo])], ignore_index=True)
                salvar_produtos(produtos_df)
                st.success("Produto cadastrado! Atualize/volte a página se a lista não recarregar automaticamente.")
                st.experimental_rerun()

    st.subheader("🔎 Buscar Produtos")
    c1, c2, c3 = st.columns([2,1,1])
    filtro_nome = c1.text_input("Buscar por Nome")
    marcas = sorted([m for m in produtos_df["Marca"].dropna().unique().tolist() if m])
    filtro_marca = c2.selectbox("Filtrar por Marca", options=["(todas)"]+marcas, index=0)
    preco_max = c3.number_input("Preço máximo (à vista)", min_value=0.0, step=0.01, format="%.2f")

    df_view = produtos_df.copy()
    if filtro_nome:
        df_view = df_view[df_view["Nome"].str.contains(filtro_nome, case=False, na=False)]
    if filtro_marca != "(todas)":
        df_view = df_view[df_view["Marca"] == filtro_marca]
    if preco_max > 0:
        df_view = df_view[df_view["PrecoVista"] <= preco_max]

    # Alerta de baixo estoque
    def _alerta(row):
        try:
            return "🔴 Baixo" if int(row["Quantidade"]) <= int(row["MinEstoque"]) else ""
        except Exception:
            return ""
    if not df_view.empty:
        df_view = df_view.assign(Alerta=df_view.apply(_alerta, axis=1))

    st.write("### Lista de Produtos")
    st.dataframe(df_view.sort_values("ID"), use_container_width=True)

    st.write("---")
    st.write("### ✏️ Editar / Excluir")
    if produtos_df.empty:
        st.info("Nenhum produto cadastrado ainda.")
    else:
        options = [f'{int(r["ID"])} - {r["Nome"]}' for _, r in produtos_df.iterrows()]
        sel = st.selectbox("Selecionar produto", options=options)
        sel_id = int(sel.split(" - ")[0])
        registro = produtos_df[produtos_df["ID"] == sel_id].iloc[0]

        en1, en2 = st.columns([3,1])
        enome = en1.text_input("Nome", value=str(registro["Nome"] or ""))
        emin = en2.number_input("Estoque mínimo", min_value=0, value=int(registro.get("MinEstoque",1)), step=1)
        emarca = st.text_input("Marca", value=str(registro.get("Marca") or ""))
        ecategoria = st.text_input("Categoria", value=str(registro.get("Categoria") or ""))
        try:
            v_ini = datetime.strptime(str(registro["Validade"]), "%Y-%m-%d").date()
        except Exception:
            v_ini = date.today()
        evalidade = st.date_input("Validade", value=v_ini)
        equantidade = st.number_input("Quantidade", min_value=0, value=int(registro.get("Quantidade",0)), step=1)
        eprecocusto = st.number_input("Preço de Custo", min_value=0.0, value=float(registro.get("PrecoCusto",0.0)), step=0.01, format="%.2f")
        eprecovista = st.number_input("Preço à Vista", min_value=0.0, value=float(registro.get("PrecoVista",0.0)), step=0.01, format="%.2f")
        eprecocartao = preco_cartao(eprecovista)
        st.caption("Preço no Cartão (automático)")
        st.metric("Preço no Cartão", f"R$ {eprecocartao:,.2f}".replace(',', 'X').replace('.', ',').replace('X','.'))

        cbt1, cbt2 = st.columns(2)
        if cbt1.button("💾 Salvar alterações", type="primary"):
            idx = produtos_df.index[produtos_df["ID"]==sel_id][0]
            produtos_df.loc[idx,"Nome"] = enome.strip()
            produtos_df.loc[idx,"MinEstoque"] = int(emin)
            produtos_df.loc[idx,"Marca"] = emarca.strip() or None
            produtos_df.loc[idx,"Categoria"] = ecategoria.strip() or None
            produtos_df.loc[idx,"Validade"] = evalidade.strftime("%Y-%m-%d")
            produtos_df.loc[idx,"Quantidade"] = int(equantidade)
            produtos_df.loc[idx,"PrecoCusto"] = float(eprecocusto)
            produtos_df.loc[idx,"PrecoVista"] = float(eprecovista)
            produtos_df.loc[idx,"PrecoCartao"] = float(eprecocartao)
            salvar_produtos(produtos_df)
            st.success("Produto atualizado!")
            st.experimental_rerun()
        if cbt2.button("🗑️ Excluir produto"):
            produtos_df = produtos_df[produtos_df["ID"]!=sel_id].reset_index(drop=True)
            salvar_produtos(produtos_df)
            st.warning("Produto excluído.")
            st.experimental_rerun()

elif page == "Vendas":
    st.title("🧾 Vendas")
    if produtos_df.empty:
        st.info("Cadastre produtos antes de lançar vendas.")
    else:
        with st.expander("Lançar venda", expanded=True):
            # seleção de produto
            options = [f'{int(r["ID"])} - {r["Nome"]}' for _, r in produtos_df.iterrows()]
            sel_prod = st.selectbox("Produto", options=options)
            prod_id = int(sel_prod.split(" - ")[0])
            prod_row = produtos_df[produtos_df["ID"]==prod_id].iloc[0]

            qtd_venda = st.number_input("Quantidade", min_value=1, step=1, value=1)
            forma = st.selectbox("Forma de pagamento", ["à vista","cartão"])
            preco_unit = float(prod_row["PrecoVista"] if forma=="à vista" else prod_row["PrecoCartao"])
            st.metric("Preço Unitário", f'R$ {preco_unit:,.2f}'.replace(',', 'X').replace('.', ',').replace('X','.'))
            total = qtd_venda * preco_unit
            st.metric("Total", f'R$ {total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X','.'))

            if st.button("➕ Registrar venda", type="primary"):
                if int(prod_row["Quantidade"]) < qtd_venda:
                    st.error("Estoque insuficiente para esta venda.")
                else:
                    vendas_df = load_csv(VENDAS_FILE)  # recarrega mais recente
                    new_id = _next_id(vendas_df)
                    nova = {
                        "ID": new_id,
                        "Data": datetime.now().strftime("%Y-%m-%d"),
                        "ProdutoID": int(prod_row["ID"]),
                        "ProdutoNome": str(prod_row["Nome"]),
                        "Quantidade": int(qtd_venda),
                        "PrecoUnit": float(preco_unit),
                        "FormaPgto": forma,
                        "Total": float(total),
                    }
                    vendas_df = pd.concat([vendas_df, pd.DataFrame([nova])], ignore_index=True)
                    salvar_vendas(vendas_df)
                    # Atualiza estoque do produto
                    idx = produtos_df.index[produtos_df["ID"]==prod_id][0]
                    produtos_df.loc[idx,"Quantidade"] = int(prod_row["Quantidade"]) - int(qtd_venda)
                    salvar_produtos(produtos_df)
                    st.success("Venda lançada!")
                    st.experimental_rerun()

    st.subheader("🗂️ Histórico de Vendas")
    if vendas_df.empty:
        st.info("Ainda não há vendas.")
    else:
        st.dataframe(vendas_df.sort_values(["Data","ID"], ascending=[False,False]), use_container_width=True)

        st.write("---")
        st.write("### ✏️ Editar / Excluir venda")
        options = [f'{int(r["ID"])} - {r["ProdutoNome"]} ({r["Data"]})' for _, r in vendas_df.iterrows()]
        sel_venda = st.selectbox("Selecionar venda", options=options)
        vid = int(sel_venda.split(" - ")[0])
        vrow = vendas_df[vendas_df["ID"]==vid].iloc[0]

        vdata = st.date_input("Data", value=datetime.strptime(str(vrow["Data"]), "%Y-%m-%d").date())
        vqtd = st.number_input("Quantidade", min_value=1, value=int(vrow["Quantidade"]), step=1)
        vforma = st.selectbox("Forma", ["à vista","cartão"], index=0 if vrow["FormaPgto"]=="à vista" else 1)
        vunit = st.number_input("Preço Unitário", min_value=0.0, value=float(vrow["PrecoUnit"]), step=0.01, format="%.2f")
        vtotal = vqtd * vunit
        st.metric("Total", f'R$ {vtotal:,.2f}'.replace(',', 'X').replace('.', ',').replace('X','.'))

        bc1, bc2 = st.columns(2)
        if bc1.button("💾 Salvar venda", type="primary"):
            idx = vendas_df.index[vendas_df["ID"]==vid][0]
            vendas_df.loc[idx,"Data"] = vdata.strftime("%Y-%m-%d")
            vendas_df.loc[idx,"Quantidade"] = int(vqtd)
            vendas_df.loc[idx,"FormaPgto"] = vforma
            vendas_df.loc[idx,"PrecoUnit"] = float(vunit)
            vendas_df.loc[idx,"Total"] = float(vtotal)
            salvar_vendas(vendas_df)
            st.success("Venda atualizada!")
            st.experimental_rerun()
        if bc2.button("🗑️ Excluir venda"):
            vendas_df = vendas_df[vendas_df["ID"]!=vid].reset_index(drop=True)
            salvar_vendas(vendas_df)
            st.warning("Venda excluída.")
            st.experimental_rerun()

elif page == "Dashboard":
    st.title("📊 Dashboard")
    if vendas_df.empty:
        st.info("Sem dados de vendas.")
    else:
        colf1, colf2 = st.columns(2)
        meses = sorted(pd.to_datetime(vendas_df["Data"]).dt.to_period("M").astype(str).unique().tolist())
        mes_sel = colf1.selectbox("Mês (YYYY-MM)", options=meses, index=len(meses)-1)
        dias_mes = vendas_df[pd.to_datetime(vendas_df["Data"]).dt.to_period("M").astype(str) == mes_sel]["Data"].unique().tolist()
        dia_sel = colf2.selectbox("Filtrar dia (opcional)", options=["(todo o mês)"] + sorted(dias_mes))

        v = vendas_df.copy()
        v["Data"] = pd.to_datetime(v["Data"]).dt.date
        if dia_sel != "(todo o mês)":
            v = v[v["Data"] == pd.to_datetime(dia_sel).date()]
        else:
            ym = mes_sel + "-01"
            m0 = pd.to_datetime(ym).date()
            v = v[[d.year == m0.year and d.month == m0.month for d in v["Data"]]]

        total = v["Total"].sum() if not v.empty else 0.0
        qtd = int(v["ID"].count()) if not v.empty else 0

        m1, m2 = st.columns(2)
        m1.metric("Faturamento", f'R$ {total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X','.'))
        m2.metric("Nº de vendas", f"{qtd}")

        # Gráfico diário
        vg = v.copy()
        vg = vg.groupby("Data", as_index=False)["Total"].sum().sort_values("Data")
        st.line_chart(vg.set_index("Data"))

        # Gráfico por categoria
        if not v.empty:
            prod = load_csv(PRODUTOS_FILE)[["ID","Categoria"]]
            merged = v.merge(prod, left_on="ProdutoID", right_on="ID", how="left")
            cat = merged.groupby("Categoria", as_index=False)["Total"].sum().sort_values("Total", ascending=False)
            st.bar_chart(cat.set_index("Categoria"))
        else:
            st.info("Sem dados para o período.")
