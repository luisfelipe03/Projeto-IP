def buscar_cliente_id(clientes, id_cliente):
    # Percorre a lista de clientes
    for c in clientes:
        # Verifica se o ID do cliente atual corresponde ao ID procurado
        if c['id'] == id_cliente:
            return c  # Retorna o cliente encontrado
    
    return None  # Retorna None caso nenhum cliente com o ID seja encontrado

def buscar_cliente_nome(clientes, nome_cliente):
    lista_nomes = []
    
    # Percorre a lista de clientes
    for c in clientes:
        # Verifica se o nome do cliente atual contém o nome procurado (não é uma correspondência exata)
        if nome_cliente.lower() in c['nome'].lower():
            lista_nomes.append(c)  # Adiciona o cliente à lista de nomes encontrados
            
    if len(lista_nomes) != 0:
        return lista_nomes  # Retorna a lista de clientes com o nome encontrado
    else:
        return None  # Retorna None caso nenhum cliente com o nome seja encontrado

def buscar_cliente(clientes):
    while True:
        try:    
            # Solicita ao usuário que escolha o tipo de busca (ID ou nome)
            escolha_busca = int(input("Digite (1) para buscar pelo ID do cliente\nOu digite (2) para buscar pelo nome do cliente: "))
            break
        except ValueError:
            # Mensagem de erro em caso de entrada inválida
            print("OPÇÃO INVÁLIDA!")
            continue
    
    if escolha_busca == 1: 
        # Busca por ID
        id_cliente = int(input("Digite o ID do cliente: "))
        cli = buscar_cliente_id(clientes, id_cliente)
        if cli != None:
            # Exibe os detalhes do cliente encontrado
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f"ID - {cli['id']}\nNome - {cli['nome']}\nIdade - {cli['idade']}\nCPF - {cli['cpf']}\nRG - {cli['rg']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        else:
            # Mensagem se o cliente não for encontrado pelo ID
            print(f"Cliente com ID = {id_cliente} não encontrado")
    elif escolha_busca == 2:
        # Busca por nome
        ordem = 1
        nome_cliente = str(input("Digite o nome do cliente: "))
        n_cli = buscar_cliente_nome(clientes, nome_cliente)
        if n_cli != None and len(n_cli) != 0 :
            if len(n_cli) > 1:
                # Se mais de um cliente com o nome for encontrado, lista todos
                print("Clientes encontrados com o nome:")
                for i in n_cli:
                    print(f"{ordem} - Nome: {i['nome']} / RG - {i['rg']}")
                    ordem += 1
            else:
                # Exibe os detalhes de um cliente encontrado pelo nome
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print(f"ID - {n_cli[0]['id']}\nNome - {n_cli[0]['nome']}\nIdade - {n_cli[0]['idade']}\nCPF - {n_cli[0]['cpf']}\nRG - {n_cli[0]['rg']}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        else:
            # Mensagem se nenhum cliente for encontrado pelo nome
            print(f"Cliente com nome = {nome_cliente} não encontrado")


