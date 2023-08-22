def cancelar_reserva(quartos, clientes, reservas):
    while True:
        for r in reservas:
            cliente = ''
            id_cliente = -1
            id_quarto = -1
            num_quarto = -1
            lista_id_reservas = []
            lista_id_reservas.append(r['id_reserva'])
            
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
        
        try:
            escolha = int(input("Digite o ID da reserva que você deseja cancelar (ou 0 para voltar ao menu): "))
        except ValueError:
            print("\nOpção inválida!\n")
            continue
        
        if escolha == 0:
            break
        
        if escolha not in lista_id_reservas:
            print(f"\nNenhum reserva cadastrado com ID {escolha}.\n")
            continue
        
        reserva_encontrada = None
        for reserva in reservas:
                if reserva['id_reserva'] == escolha:
                    reserva_encontrada = reserva  # Armazena a reserva encontrado
                    break  # Sai do loop ao encontrar a reserva desejado
        
        if reserva_encontrada:
                reservas.remove(reserva_encontrada)  # Remove a reserva encontrado da lista
                print(f"Reserva com ID {escolha} cancelada com sucesso.")
        
            
            
        
            