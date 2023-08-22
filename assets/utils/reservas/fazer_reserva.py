def fazer_reserva(quartos, clientes, reservas):
    # Verifica o último ID e soma +1 para continuar a sequência dos IDs 
    if not reservas:
        id = 1
    else:
        ultimo_dicionario = reservas[-1]
        id = int(ultimo_dicionario.get("id_reserva")) + 1
        
    # Verifica se há quartos cadastrados, se não houver a função é cancelada
    if not quartos:
        return print("\nNão há quartos cadastrados\n")  
        
    # Verifica se há clientes cadastrados, se não houver a função é cancelada  
    if not clientes:
        return print("\nNão há clientes cadastrados\n")
    
    while True:      
        # Verifica quartos disponíveis 
        quartos_disponiveis = []
        print("QUARTOS DISPONÍVEIS:\n")
        for quarto in quartos:
            if quarto["reservado"] == 'nao':
                quartos_disponiveis.append(quarto['id'])
                print(f"{quarto['id']} - Quarto {quarto['numero']}")
            
        #Verifica se há quartos disponiveis, se não houver a função é cancelada
        if len(quartos_disponiveis) == 0:
            return print("\nNÃO HÁ MAIS QUARTOS DISPONÍVEIS\n")
        
        try:      
            escolha_quarto = int(input("Escolha o quarto: "))
        except ValueError:
            print('\033[31m' + 'OPÇÃO INVÁLIDA!' + '\033[0;0m\n')
            continue
          
        #Verifica se a escolha_quarto é valida   
        if escolha_quarto not in quartos_disponiveis:
            print('\033[31m' + 'OPÇÃO INVÁLIDA!' + '\033[0;0m\n')
            continue
        break
    
    while True:        
        # Escolher cliente
        lista_clientes = []
        print('\nA RESERVA É PARA QUAL CLIENTE: \n')
        for cliente in clientes:
            lista_clientes.append(cliente['id'])
            print(f"{cliente['id']} - {cliente['nome']}")
            
        try:
            escolha_cliente = int(input("Escolha o cliente: "))
        except ValueError:
            print('OPÇÃO INVÁLIDA!\n')
            continue
            
        #Verifica se escolha_cliente é valida
        if escolha_cliente not in lista_clientes:
            print("OPÇÃO INVÁLIDA\n")
            continue
        break
        
    while True:  
        # Perguntar ao professor se pode usar regex para verificar formatação da data
        # Escolher Check-IN
        check_in = str(input("INFORME A DATA DE CHECK-IN (dd/mm/aaaa): "))
            
        # Escolher Check-OUT
        check_out = str(input("INFORME A DATA DE CHECK-OUT (dd/mm/aaaa): "))
        try:
            dia_in, mes_in, ano_in = map(int, check_in.split('/'))
            dia_out, mes_out, ano_out = map(int, check_out.split('/'))
        except ValueError:
            print("\nPreencha os campos de Check-IN e Check-OUT corretamente!\n")
            continue

        #Verificação para que o check-out não seja antes do check-in
        #Exemplo: check-in = 05/09/2023 / check-out = 01/09/2023
        if (ano_in, mes_in, dia_in) < (ano_out, mes_out, dia_out):
            break
        else:
            print("\nO CHECK-IN TEM QUE ACONTECER ANTES DO CHECK-OUT\n")
            continue
        
    # Mudando status 'reservado' para 'sim'
    for i in quartos:
        if i['id'] == escolha_quarto:
            i['reservado'] = 'sim'
       
    #Criando o dicionario para armazenas os dados da reserva          
    reserva = {
        "id_reserva": id,
        "id_quarto": escolha_quarto,
        "id_cliente": escolha_cliente,
        "check-in": check_in,
        "check-out": check_out
    }
       
    #Adicionado reserva a lista de reservas    
    reservas.append(reserva)
    print("\nReserva feita com sucesso!\n")
