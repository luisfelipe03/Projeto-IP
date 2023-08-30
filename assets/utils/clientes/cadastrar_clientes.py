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
    nome = input("Nome do cliente(Ou digite 0 para voltar ao menu): ")
    
    if '0' == nome: 
        return print("Voltando ao menu...")
    
    #Verde
    idade = input("Idade do cliente: ")
    
    while True:
        rg = input("RG do cliente: ")
        if verifica_rg_existente_cliente(rg, clientes):
            #Vermelho
            print('\033[31m' + f"Já existe cliente cadastrado com esse RG: {rg}" + '\033[0;0m')
        else:
            break

    while True:
        cpf = input("CPF do cliente: ")
        if verifica_cpf_existente_cliente(cpf, clientes):
            #Vermelho
            print('\033[31m' + f"Já existe cliente cadastrado com CPF: {cpf}" + '\033[0;0m')
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
    print('\033[32m' + "Cliente cadastrado com sucesso!" + '\033[0;0m')