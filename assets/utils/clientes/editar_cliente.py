from assets.utils.clientes.cadastrar_clientes import verifica_cpf_existente_cliente, verifica_rg_existente_cliente

def editar_cliente(clientes):
    for cliente in clientes:
        #Azul os 3 primeiros prints
        print(f"ID - {cliente['id']}")
        print(f"Nome - {cliente['nome']}")
        print(f"RG - {cliente['rg']}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    #Verde até o parênteses e dentro do parêntese azul para destacar a opção de voltar ao menu 
    id_busca = int(input("Digite o ID do cliente que deseja editar(Ou digite 0 para voltar ao menu): "))

    if id_busca == 0:
        #Verde
        return print("Voltando ao menu...")
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_busca:
            cliente_encontrado = cliente
            break
    
    while True:
        if cliente_encontrado:
            print("Cliente encontrado. Preencha os novos dados:")
            cliente_encontrado["nome"] = input("Nome do cliente: ")
            cliente_encontrado["idade"] = input("Idade do cliente: ")
            
            while True:
                novo_rg = input("Novo RG do cliente: ")
                if not verifica_rg_existente_cliente(novo_rg, clientes):
                    cliente_encontrado["rg"] = novo_rg
                    break
                else:
                    print(f"Já existe cliente cadastrado com esse RG: {novo_rg}")
                    continue

            while True:
                novo_cpf = input("Novo CPF do cliente: ")
                if not verifica_cpf_existente_cliente(novo_cpf, clientes):
                    cliente_encontrado["cpf"] = novo_cpf
                    break
                else:
                    print(f"Já existe cliente cadastrado com CPF: {novo_cpf}")
                    continue
            
            print("Cliente editado com sucesso!")
            break
        else:
            print(f"Cliente com ID {id_busca} não encontrado.")
            continue