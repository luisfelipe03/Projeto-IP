def editar_reserva(quartos, clientes, reservas, id_reserva):
    reserva_encontrada = None
    while True:
        
        if id_reserva == 0:
            return print('Voltando para o menu...')
            
        # Verificar se a reserva existe pelo id_reserva fornecido
        for reserva in reservas:
            if reserva["id_reserva"] == id_reserva:
                reserva_encontrada = reserva
                break
        
        if reserva_encontrada is None:
            return print("\nReserva não encontrada.\n")
        
        # Informações da reserva encontrada
        id_quarto_antigo = reserva_encontrada["id_quarto"]
        id_cliente_antigo = reserva_encontrada["id_cliente"]
        check_in_antigo = reserva_encontrada["check-in"]
        check_out_antigo = reserva_encontrada["check-out"]
            
        while True:
            # Escolher novo quarto ou manter o antigo
            quartos_disponiveis = [quarto['id'] for quarto in quartos if quarto["reservado"] == 'nao' or quarto["id"] == id_quarto_antigo]
            print("QUARTOS DISPONÍVEIS:\n")
            for quarto in quartos:
                if quarto['id'] == id_quarto_antigo:
                    print(f"{quarto['id']} - Quarto {quarto['numero']} (atual)")
                elif quarto['id'] in quartos_disponiveis:
                    print(f"{quarto['id']} - Quarto {quarto['numero']}")
            escolha_quarto = int(input("Escolha o novo quarto ou mantenha o antigo: "))

            if escolha_quarto in quartos_disponiveis or escolha_quarto == id_quarto_antigo:
                break
            else:
                print("Opção inválida.\n")

        while True:
            # Escolher novo cliente ou manter o antigo
            lista_clientes = [cliente['id'] for cliente in clientes]
            print('\nA RESERVA AGORA É PARA QUAL CLIENTE:\n')
            for cliente in clientes:
                if cliente['id'] == id_cliente_antigo:
                    print(f"{cliente['id']} - {cliente['nome']} (atual)")
                elif cliente['id'] != id_cliente_antigo:
                    print(f"{cliente['id']} - {cliente['nome']}")
            escolha_cliente = int(input("Escolha o novo cliente ou mantenha o antigo: "))

            if escolha_cliente in lista_clientes or escolha_cliente == id_cliente_antigo:
                break
            else:
                print("Opção inválida.\n")

        while True:
            # Escolher novo Check-IN ou manter o antigo
            novo_check_in = str(input(f"INFORME A NOVA DATA DE CHECK-IN (dd/mm/aaaa) ou mantenha a anterior ({check_in_antigo}): "))

            # Escolher novo Check-OUT ou manter o antigo
            novo_check_out = str(input(f"INFORME A NOVA DATA DE CHECK-OUT (dd/mm/aaaa) ou mantenha a anterior ({check_out_antigo}): "))
            try:
                dia_in, mes_in, ano_in = map(int, novo_check_in.split('/'))
                dia_out, mes_out, ano_out = map(int, novo_check_out.split('/'))
            except ValueError:
                print("\nPreencha os campos de datas corretamente!\n")
                continue

            if (ano_in, mes_in, dia_in) < (ano_out, mes_out, dia_out):
                break
            else:
                print("\nO CHECK-IN TEM QUE ACONTECER ANTES DO CHECK-OUT\n")
                continue

        # Atualizando status do quarto anterior para não reservado
        for quarto in quartos:
            if quarto['id'] == id_quarto_antigo:
                quarto['reservado'] = 'nao'
                break

        # Atualizando informações da reserva
        reserva_encontrada["id_quarto"] = escolha_quarto
        reserva_encontrada["id_cliente"] = escolha_cliente
        reserva_encontrada["check-in"] = novo_check_in
        reserva_encontrada["check-out"] = novo_check_out

        # Atualizando status do novo quarto para reservado
        for quarto in quartos:
            if quarto['id'] == escolha_quarto:
                quarto['reservado'] = 'sim'
                break

        print("\nReserva atualizada com sucesso!\n")
        break


