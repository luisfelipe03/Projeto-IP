def remover_cliente(clientes): 
    while True: 
        print("------QUAL CLIENTE VOCÊ DESEJA REMOVER ?------\n")
        for i in clientes:
            print(f"ID = {i['id']}\nNome = {i['nome']}\nRG = {i['rg']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
        try:
            escolha = int(input("Digite o ID do cliente que você quer remover (ou 0 para voltar ao menu): "))
            
            if escolha == 0:
                break  
              
            cliente_encontrado = None
            for cliente in clientes:
                if cliente['id'] == escolha:
                    cliente_encontrado = cliente
                    break
                        
            if cliente_encontrado:
                clientes.remove(cliente_encontrado)
                print(f"Cliente com ID {escolha} removido com sucesso.")
            else:
                print(f"Nenhum cliente cadastrado com ID {escolha}.")
        except ValueError:
            print("Opção inválida!")

