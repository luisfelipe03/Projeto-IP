"""def verifica_rg_existente_cliente(rg, clientes):
    for cliente in clientes:
        if cliente["rg"] == rg:
            return True
    return False

def verifica_cpf_existente_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return True
    return False"""

def cadastrar_cliente(clientes):

    nome = input("Nome do cliente: ")
    idade = input("Idade do cliente: ")
    cpf = str(input("CPF do cliente: "))
    rg = str(input("RG do cliente: "))
    
    """while True:
        rg = input("RG do cliente: ")
        if verifica_rg_existente_cliente(rg):
            print(f"Já existe cliente cadastrado com esse RG: {rg}")
            continue
        break

    while True:
        cpf = input("CPF do cliente: ")
        if verifica_cpf_existente_cliente(cpf):
            print(f"Já existe cliente cadastrado com CPF: {cpf}")
            continue
        break"""
        
    # Verifica o ultimo ID e soma +1 para continuar a sequencia dos IDs
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
    print("Cliente cadastrado com sucesso!")