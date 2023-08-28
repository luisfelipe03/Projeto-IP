def verifica_rg_existente_cliente(rg, clientes):
    for cliente in clientes:
        if cliente["rg"] == rg:
            return True
    return False

def verifica_cpf_existente_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return True
    return False

def cadastrar_cliente(clientes):
    #Verde
    nome = input("Nome do cliente: ")
    #Verde
    idade = input("Idade do cliente: ")
    
    while True:
        rg = input("RG do cliente: ")
        if verifica_rg_existente_cliente(rg, clientes):
            #Vermelho
            print(f"Já existe cliente cadastrado com esse RG: {rg}")
        else:
            break

    while True:
        cpf = input("CPF do cliente: ")
        if verifica_cpf_existente_cliente(cpf, clientes):
            #Vermelho
            print(f"Já existe cliente cadastrado com CPF: {cpf}")
        else:
            break
        
    if not clientes:
        id = 1
    else:
        ultimo_dicionario = clientes[-1]
        id = ultimo_dicionario.get("id") + 1

    cliente = {
        "id": id,
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "rg": rg
    }

    clientes.append(cliente)
    #Verde
    print("Cliente cadastrado com sucesso!")