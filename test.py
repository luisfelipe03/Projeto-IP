clientes = []

def dados():        
    with open("./clientes.csv", "r", encoding="UTF-8") as c:
        linhas = c.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            cliente = {
                "id": int(dados[0]),
                "nome": str(dados[1]),
                "idade": str(dados[2]),
                "CPF": str(dados[3]),
                "RG": str(dados[4])
            }
            clientes.append(cliente)

def verifica_rg_existente_cliente(rg):
    for cliente in clientes:
        if cliente["RG"] == rg:
            return True
    return False

def verifica_cpf_existente_cliente(cpf):
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            return True
    return False

def cadastrar_cliente():
    dados()  # Carregar os clientes existentes

    if not clientes:
        id = 1
    else:
        ultimo_dicionario = clientes[-1]
        id = ultimo_dicionario.get("id") + 1

    nome = input("Nome do cliente: ")
    idade = input("Idade do cliente: ")

    while True:
        cpf = input("CPF do cliente: ")
        if verifica_cpf_existente_cliente(cpf):
            print(f"Já existe cliente cadastrado com CPF: {cpf}")
            continue
        break

    while True:
        rg = input("RG do cliente: ")
        if verifica_rg_existente_cliente(rg):
            print(f"Já existe cliente cadastrado com esse RG: {rg}")
            continue
        break

    cliente = {
        "id": id,
        "nome": nome,
        "idade": idade,
        "CPF": cpf,
        "RG": rg
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

# Chame a função dados() para carregar os clientes existentes
dados()

for i in clientes:
    print(i)

cadastrar_cliente()

for i in clientes:
    print(i)
















































































