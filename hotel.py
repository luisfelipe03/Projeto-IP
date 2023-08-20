#------------------------------------------------CARREGAR DADOS-------------------------------------------------
def carregar_dados():
    clientes = []
    quartos = []
    reservas = []
    
    try:
        #Exportando dados dos clientes
        with open("./clientes.csv", "r", encoding="UTF-8") as c:
            linhas = c.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                cliente = {
                    "id":int(dados[0]),
                    "nome":dados[1],
                    "idade":dados[2],
                    "CPF":dados[3],
                    "RG":dados[4]
                }
                clientes.append(cliente)
            
        #Exportando dados dos quartos        
        with open("./quartos.csv", "r", encoding="UTF-8") as q:
            for i in q:
                id, num, reser = i.strip().split(',')
                quarto = {
                    "id":int(id),
                    "numero":int(num),
                    "reservado": bool(reser)
                }
                quartos.append(quarto)
        
        with open("./reservas.csv", "r", encoding="UTF-8") as r:
            for linha in r:
                id_quarto, id_cliente, check_in, check_out = linha.strip().split(',')
                reserva = {
                    "id_quarto":int(id_quarto),
                    "id_cliente":int(id_cliente),
                    "check-in":check_in,
                    "check-out":check_out
                    
                }
                reservas.append(reserva)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    return quartos, clientes, reservas
            
#-----------------------------------------------------MENU--------------------------------------------------------

def menu():
    print("1. Cadastrar quarto")
    print("2. Cadastrar cliente")
    print("3. Editar quarto")
    print("4. Editar cliente")
    print("5. Remover quarto")
    print("6. Remover cliente")
    print("7. Buscar quarto por número ou ID")
    print("8. Buscar cliente por nome ou ID")
    print("9. Ver todos os quartos reservados")
    print("10. Sair")
    return input("Escolha uma opção: ")

#-----------------------------------------------CADASTRAR QUARTO------------------------------------------------

def verifica_numero_existente_quarto(numero, quartos):
    for quarto in quartos:
        if quarto["numero"] == numero:
            return True
    return False

def cadastrar_quarto(quartos):
    
    if not quartos:
        id = 1
    else:
        ultimo_dicionario = quartos[-1]
        id = ultimo_dicionario.get("id") + 1

    while True:
        try:
            numero = int(input("Número do quarto: "))
            if verifica_numero_existente_quarto(numero, quartos):
                print(f"Já existe quarto cadastrado com esse número: {numero}")
                continue
            break
        except ValueError:
            print("Número do quarto deve ser um número inteiro")

    quarto = {
        "id": id,
        "numero": numero,
        "reservado": False
    }

    quartos.append(quarto)
    print("Quarto cadastrado com sucesso!")






























































#-----------------------------------------------FUNÇÃO PRINCIPAL------------------------------------------------

def principal():
    clientes, quartos, reservas = carregar_dados()
    
    while True:
        escolha = menu()

        if escolha == 1:
            cadastrar_quarto(quartos)
            return f"{quartos}"
        elif escolha == 10:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    principal()





































































