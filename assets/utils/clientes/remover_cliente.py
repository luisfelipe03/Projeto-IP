def remover_cliente(clientes):
    while True:
        print("------QUAL CLIENTE VOCÊ DESEJA REMOVER?------\n")  # Exibe o cabeçalho para remover um cliente
        for i in clientes:
            # Exibe as informações de cada cliente na lista
            print(f"ID = {i['id']}\nNome = {i['nome']}\nRG = {i['rg']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
        try:
            escolha = int(input("Digite o ID do cliente que você deseja remover (ou 0 para voltar ao menu): "))
            
            if escolha == 0:
                break  # Sai do loop caso o usuário escolha 0
            
            cliente_encontrado = None
            for cliente in clientes:
                if cliente['id'] == escolha:
                    cliente_encontrado = cliente  # Armazena o cliente encontrado
                    break  # Sai do loop ao encontrar o cliente desejado
                    
            if cliente_encontrado:
                clientes.remove(cliente_encontrado)  # Remove o cliente encontrado da lista
                print('\033[33m' + f"Cliente com ID {escolha} removido com sucesso." + '\033[0;0m')
            else:
                print(f"Nenhum cliente cadastrado com ID {escolha}.")
        except ValueError:
            print('\033[31m' + "Opção inválida!" + '\033[0;0m')  # Trata exceção se o usuário inserir um valor inválido
