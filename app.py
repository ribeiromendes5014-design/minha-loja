
# Arquivo app.py corrigido
# Ajuste principal: no registro de fiado em Clientes, agora salva 'FormaPagamento': 'Fiado'
# Restante do código permanece igual ao original.

# Dentro do trecho onde é criado novo_cli (na aba Vendas, se forma == "Fiado"):

novo_cli = {
    "ID": prox_id(clientes, "ID"),
    "Cliente": nome_cliente.strip(),
    "Produto": f"Pedido {novo_id}",
    "Valor": round(float(total_venda), 2),
    "DataPagamento": str(data_prevista) if data_prevista else "",
    "Status": "Aberto",
    "FormaPagamento": "Fiado"   # <<--- CORRIGIDO
}

# Substitua esse bloco no seu app.py original. 
