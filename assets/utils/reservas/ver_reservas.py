def ver_reservas(quartos, clientes, reservas):
    for r in reservas:
        cliente = ''
        id_cliente = -1
        id_quarto = -1
        num_quarto = -1
        
        # Encontrar o cliente correspondente à reserva
        for c in clientes:
            if c['id'] == r['id_cliente']:
                cliente = c['nome']
                id_cliente = c['id']
        
        # Encontrar o quarto correspondente à reserva
        for q in quartos:
            if q['id'] == r['id_quarto']:
                id_quarto = q['id']
                num_quarto = q['numero']
            
        # Imprimir os detalhes da reserva
        print(f"\nID da reserva - {r['id_reserva']}")
        print(f"Quarto - ID do quarto = {id_quarto} / Número do quarto = {num_quarto}")
        print(f"Cliente - ID do cliente = {id_cliente} / Nome do cliente = {cliente}")
        print(f"Check-IN - {r['check-in']}")
        print(f"Check-OUT - {r['check-out']}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

