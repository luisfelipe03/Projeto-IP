def ver_reservas(quartos, clientes, reservas):
    for r in reservas:
        cliente = ''
        id_cliente = -1
        id_quarto = -1
        num_quarto = -1
        for c in clientes:
            if c['id'] == r['id_cliente']:
                cliente = c['nome']
                id_cliente = c['id']
        
        for q in quartos:
            if q['id'] == r['id_quarto']:
                id_quarto = q['id']
                num_quarto = q['numero']
            
        print(f"ID da reserva - {r['id_reserva']}\nQuarto - ID do quarto = {id_quarto} / Número do quarto = {num_quarto}\nCliente - ID do cliente = {id_cliente} / Nome do cliente = {cliente}\nCheck-IN - {r['check-in']}\nCheck-OUT - {r['check-out']}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
