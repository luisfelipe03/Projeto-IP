clientes = []

def dados():
    with open("./Projeto-IP/clientes.csv", "r", encoding="UTF-8") as c:
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

def remover_cliente():
    while True:    
        print("------QUAL CLIENTE VOCÊS DESEJA REMOVER ?------\n")
        for i in clientes:
                print(f"ID = {i['id']}\nNome = {i['nome']}\nRG = {i['RG']}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
        try:
            escolha = int(input("Digite o ID do cliente que você quer remover: "))
            for i in clientes:
                if i['id'] != escolha:
                    continue
                else:    
                    print(f"NÃO TEM CLIENTE CADASTRADO COM ID: {escolha}")
                    continue
        except ValueError:
            print("OPÇÃO INVALIDA!")
            continue
    print(escolha)
        
dados()

remover_cliente()