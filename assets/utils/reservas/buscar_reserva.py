def buscar_reserva(reservas, quartos, clientes):
    print("Escolha a opção de busca:")
    print("1 - Buscar por ID da reserva")
    print("2 - Buscar por ID do quarto")
    
    opcao = input("Opção: ")

    if opcao == "1":
        opcao_busca = "id_reserva"
        valor_busca = int(input("Digite o ID da reserva: "))
    elif opcao == "2":
        opcao_busca = "id_quarto"
        valor_busca = int(input("Digite o ID do quarto: "))
    else:
        print('\033[31m' + "Opção inválida." + '\033[0;0m')
        return []

    detalhes_encontrados = []

    for r in reservas:
        cliente_nome = ""
        numero_quarto = ""

        # Encontrar o cliente correspondente à reserva
        for c in clientes:
            if c['id'] == r['id_cliente']:
                cliente_nome = c['nome']

        # Encontrar o quarto correspondente à reserva
        for q in quartos:
            if q['id'] == r['id_quarto']:
                numero_quarto = q['numero']

        if opcao_busca == "id_reserva" and r['id_reserva'] == valor_busca:
            detalhes_encontrados.append({
                "ID da Reserva": r['id_reserva'],
                "Nome do Cliente": cliente_nome,
                "Número do Quarto": numero_quarto,
                "Check-In": r['check-in'],
                "Check-Out": r['check-out']
            })

        if opcao_busca == "id_quarto" and r['id_quarto'] == valor_busca:
            detalhes_encontrados.append({
                "ID da Reserva": r['id_reserva'],
                "Nome do Cliente": cliente_nome,
                "Número do Quarto": numero_quarto,
                "Check-In": r['check-in'],
                "Check-Out": r['check-out']
            })

    return detalhes_encontrados


