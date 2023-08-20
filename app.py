# Função para ler os dados do arquivo CSV e carregar em listas
def carregar_dados():
    quartos = []
    clientes = []
    #ignore
    try:
        with open("hotel_data.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(',')
                if dados[0] == 'quarto':
                    quarto = {
                        'id': dados[0],
                        'numero': dados[1],
                        'ocupado': dados[2] == 'True',
                        'checkin': dados[3],
                        'checkout': dados[4]
                    }
                    quartos.append(quarto)
                elif dados[0] == 'cliente':
                    cliente = {
                        'id': dados[0],
                        'nome': dados[1],
                        'idade': dados[2],
                        'cpf': dados[3],
                        'rg': dados[4]
                    }
                    clientes.append(cliente)

    except FileNotFoundError:
        pass

    return quartos, clientes

# Função para salvar os dados no arquivo CSV
def salvar_dados(quartos, clientes):
    with open("hotel_data.csv", "w") as arquivo:
        arquivo.write("tipo,id,numero,ocupado,checkin,checkout,nome,idade,cpf,rg\n")

        for quarto in quartos:
            arquivo.write(f"{quarto['id']},{quarto['numero']},{quarto['ocupado']},{quarto['checkin']},{quarto['checkout']}\n")

        for cliente in clientes:
            arquivo.write(f"{cliente['id']},{cliente['nome']},{cliente['idade']},{cliente['cpf']},{cliente['rg']}\n")

def mostrar_menu():
    print("1. Cadastrar quarto")
    print("2. Cadastrar cliente")
    print("3. Editar quarto")
    print("4. Editar cliente")
    print("5. Remover quarto")
    print("6. Remover cliente")
    print("7. Buscar quarto por número ou ID")
    print("8. Buscar cliente por nome ou ID")
    print("9. Sair")
    return input("Escolha uma opção: ")

def cadastrar_quarto(rooms):
    room_id = input("ID do quarto: ")
    room_number = input("Número do quarto: ")
    occupied = False
    checkin = ""
    checkout = ""

    room = {
        'type': 'room',
        'id': room_id,
        'number': room_number,
        'occupied': occupied,
        'checkin': checkin,
        'checkout': checkout
    }

    rooms.append(room)
    print("Quarto cadastrado com sucesso!")

# Função para cadastrar um novo cliente
def cadastrar_cliente(customers):
    customer_id = input("ID do cliente: ")
    name = input("Nome do cliente: ")
    age = input("Idade do cliente: ")
    cpf = input("CPF do cliente: ")
    rg = input("RG do cliente: ")

    customer = {
        'type': 'customer',
        'id': customer_id,
        'name': name,
        'age': age,
        'cpf': cpf,
        'rg': rg
    }

    customers.append(customer)
    print("Cliente cadastrado com sucesso!")
    
def buscar_quarto(quartos):
    termo = input("Digite o número ou ID do quarto a ser buscado: ")
    
    for quarto in quartos:
        if termo == quarto['numero'] or termo == quarto['id']:
            print("Quarto encontrado:")
            print(f"ID: {quarto['id']}")
            print(f"Número: {quarto['numero']}")
            print(f"Ocupado: {'Sim' if quarto['ocupado'] else 'Não'}")
            print(f"Check-in: {quarto['checkin']}")
            print(f"Check-out: {quarto['checkout']}")
            return
    print("Nenhum quarto encontrado com esse número ou ID.")

# Função para buscar cliente por nome ou ID
def buscar_cliente(clientes):
    termo = input("Digite o nome ou ID do cliente a ser buscado: ")
    
    for cliente in clientes:
        if termo == cliente['nome'] or termo == cliente['id']:
            print("Cliente encontrado:")
            print(f"ID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"RG: {cliente['rg']}")
            return
    print("Nenhum cliente encontrado com esse nome ou ID.")

# Função para editar quarto por número ou ID
def editar_quarto(quartos):
    termo = input("Digite o número ou ID do quarto a ser editado: ")
    
    for quarto in quartos:
        if termo == quarto['numero'] or termo == quarto['id']:
            print("Quarto encontrado:")
            print(f"ID: {quarto['id']}")
            print(f"Número: {quarto['numero']}")
            quarto['ocupado'] = input("Ocupado (Sim/Não): ").lower() == 'sim'
            quarto['checkin'] = input("Check-in: ")
            quarto['checkout'] = input("Check-out: ")
            print("Quarto editado com sucesso.")
            return
    print("Nenhum quarto encontrado com esse número ou ID.")

# Função para editar cliente por nome ou ID
def editar_cliente(clientes):
    termo = input("Digite o nome ou ID do cliente a ser editado: ")
    
    for cliente in clientes:
        if termo == cliente['nome'] or termo == cliente['id']:
            print("Cliente encontrado:")
            print(f"ID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            cliente['idade'] = input("Idade: ")
            cliente['cpf'] = input("CPF: ")
            cliente['rg'] = input("RG: ")
            print("Cliente editado com sucesso.")
            return
    print("Nenhum cliente encontrado com esse nome ou ID.")

# Função para remover quarto por número ou ID
def remover_quarto(quartos):
    termo = input("Digite o número ou ID do quarto a ser removido: ")
    
    for quarto in quartos:
        if termo == quarto['numero'] or termo == quarto['id']:
            quartos.remove(quarto)
            print("Quarto removido com sucesso.")
            return
    print("Nenhum quarto encontrado com esse número ou ID.")

# Função para remover cliente por nome ou ID
def remover_cliente(clientes):
    termo = input("Digite o nome ou ID do cliente a ser removido: ")
    
    for cliente in clientes:
        if termo == cliente['nome'] or termo == cliente['id']:
            clientes.remove(cliente)
            print("Cliente removido com sucesso.")
            return
    print("Nenhum cliente encontrado com esse nome ou ID.")

# Função principal
def principal():
    quartos, clientes = carregar_dados()

    while True:
        escolha = mostrar_menu()

        if escolha == '1':
            cadastrar_quarto(quartos)
        elif escolha == '2':
            cadastrar_cliente(clientes)
        elif escolha == '3':
            editar_quarto(quartos)
        elif escolha == '4':
            editar_cliente(clientes)
        elif escolha == '5':
            remover_quarto(quartos)
        elif escolha == '6':
            remover_cliente(clientes)
        elif escolha == '7':
            buscar_quarto(quartos)
        elif escolha == '8':
            buscar_cliente(clientes)
        elif escolha == '9':
            salvar_dados(quartos, clientes)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()
