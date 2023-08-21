'''
SISTEMA DE GESTÃO DE HOTEL

Desenvolvedores: Luis Felipe de Oliveira Andrade
                 Phylypy Cabral de Lima Tavares 

Para mais informações sobre o sistema leia o arquivo README.txt
'''
#-----------------------------------------------------MENU--------------------------------------------------------

def menu():
    print("Fazer uma reserva")
    print("Editar reserva")
    print("Cancelar reserva")
    print("Ver todos os quartos reservados")
    print("Cadastrar quarto")
    print("Cadastrar cliente")
    print("Editar quarto")
    print("Editar cliente")
    print("Remover quarto")
    print("Remover cliente")
    print("Buscar quarto por número ou ID")
    print("Buscar cliente por nome ou ID")
    print("Sair")
    return input("Escolha uma opção: ")

#------------------------------------------------CARREGAR DADOS-------------------------------------------------
def carregar_dados():
    clientes = []
    quartos = []
    reservas = []
    
    try:
        #Exportando dados dos clientes
        with open("./assets/clientes.csv", "r", encoding="UTF-8") as c:
            linhas = c.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                cliente = {
                    "id":int(dados[0]),
                    "nome":dados[1],
                    "idade":dados[2],
                    "cpf":dados[3],
                    "rg":dados[4]
                }
                clientes.append(cliente)
            
        #Exportando dados dos quartos        
        with open("./assets/quartos.csv", "r", encoding="UTF-8") as q:
            for i in q:
                id, num, reser = i.strip().split(',')
                quarto = {
                    "id":int(id),
                    "numero":int(num),
                    "reservado": reser
                }
                quartos.append(quarto)
        
        with open("./assets/reservas.csv", "r", encoding="UTF-8") as r:
            for linha in r:
                id_reserva,id_quarto, id_cliente, check_in, check_out = linha.strip().split(',')
                reserva = {
                    "id_reserva":int(id_reserva),
                    "id_quarto":int(id_quarto),
                    "id_cliente":int(id_cliente),
                    "check-in":check_in,
                    "check-out":check_out
                    
                }
                reservas.append(reserva)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
    return quartos, clientes, reservas

#------------------------------------------------SALVAR DADOS-------------------------------------------------
def salvar_dados(quartos, clientes, reservas):
    with open("./assets/clientes.csv", "w", encoding="UTF-8") as arquivo:
        for cliente in clientes:
             arquivo.write(f"{cliente['id']},{cliente['nome']},{cliente['idade']},{cliente['cpf']},{cliente['rg']}\n")
    
    with open("./assets/quartos.csv", "w", encoding="UTF-8") as arquivo:  
        for quarto in quartos:    
            arquivo.write(f"{quarto['id']},{quarto['numero']},{quarto['reservado']}\n")   
            
    with open("./assets/reservas.csv", "w", encoding="UTF-8") as arquivo:
        for reserva in reservas:
            arquivo.write(f"{reserva['id_reserva']},{reserva['id_quarto']},{reserva['id_cliente']},{reserva['check-in']},{reserva['check-out']}\n")  

#-----------------------------------------------FAZER RESERVA------------------------------------------------
def fazer_reserva(quartos, clientes, reservas):
    # Verifica o ultimo ID e soma +1 para continuar a sequencia dos IDs 
    if not reservas:
        id = 1
    else:
        ultimo_dicionario = reservas[-1]
        id = int(ultimo_dicionario.get("id_reserva")) + 1
        
    # Verifica se a quartos cadastrados
    if not quartos:
        return print("Não a quartos cadastrados")  
        
    # Verifica se a clientes cadastrados    
    if not clientes:
        return print("Não a clientes cadastrados")
    
    while True:      
        #Verifica quartos disponiveis 
        quartos_disponivel = []
        print("QUARTOS DISPONIVEIS:\n")
        for quarto in quartos:
            if quarto["reservado"] == 'nao':
                quartos_disponivel.append(quarto['id'])
                print(f"{quarto['id']} - Quarto.{quarto['numero']}")
        escolha_quarto = int(input("Escolha o quarto: "))
            
        if escolha_quarto not in quartos_disponivel:
            print("OPÇÃO INVALIDA")
            continue
        break
    
    while True:        
        #Escolher cliente
        lista_clientes = []
        print('\nA RESERVA É PARA QUAL CLIENTE: \n')
        for cliente in clientes:
            lista_clientes.append(cliente['id'])
            print(f"{cliente['id']} - {cliente['nome']}")
        escolha_cliente = int(input("Escolha o cliente: "))
            
        if escolha_cliente not in lista_clientes:
            print("OPÇÃO INVALIDA")
            continue
        break
          
    while True:  
        #Perguntar ao professor se pode usar regex para verificar formatação da data
        #Escolher Check-IN
        check_in = str(input("INFORME A DATA DE CHECK-IN(dd/mm/aaaa): "))
            
        #Escolher Check-OUT
        check_out = str(input("INFORME A DATA DE CHECK-OUT(dd/mm/aaaa): "))
    
        dia_in, mes_in, ano_in = map(int, check_in.split('/'))
        dia_out, mes_out, ano_out = map(int, check_out.split('/'))

        if (ano_in, mes_in, dia_in) < (ano_out, mes_out, dia_out):
            break
        else:
            print("O CHECK-IN TEM QUE ACONTECER ANTES DO CHECK-OUT")
            continue
        
    #mudando status 'reservado' p/ sim
    for i in quartos:
        if i['id'] == escolha_quarto:
            i['reservado'] = 'sim'
                
    reserva = {
            "id_reserva":id,
            "id_quarto":escolha_quarto,
            "id_cliente":escolha_cliente,
            "check-in":check_in,
            "check-out":check_out
        }
        
    reservas.append(reserva)
    print("Reserva feito com sucesso!")

#-----------------------------------------------CADASTRAR QUARTO------------------------------------------------

# Verifica se já existe quarto cadastrado com o mesmo número
def verifica_numero_existente_quarto(numero, quartos):
    for quarto in quartos:
        if quarto["numero"] == numero:
            return True
    return False

def cadastrar_quarto(quartos):
    
    # Verifica o ultimo ID e soma +1 para continuar a sequencia dos IDs
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

#-----------------------------------------------CADASTRAR CLIENTE------------------------------------------------
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
        "CPF": cpf,
        "RG": rg
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

#-----------------------------------------------REMOVER QUARTO------------------------------------------------
def remover_quarto(quartos): 
    while True: 
        print("------QUAL QUARTO VOCÊ DESEJA REMOVER ?------\n")
        for i in quartos:
            print(f"ID = {i['id']}\nNumero do quarto = {i['numero']}\nReservado = {i['reservado']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
        try:
            escolha = int(input("Digite o ID do quarto que você quer remover (ou 0 para voltar ao menu): "))
            
            if escolha == 0:
                break  
              
            quarto_encontrado = None
            for quarto in quartos:
                if quarto['id'] == escolha:
                    quarto_encontrado = quarto
                    break
                        
            if quarto_encontrado:
                quartos.remove(quarto_encontrado)
                print(f"Quarto com ID {escolha} removido com sucesso.")
            else:
                print(f"Nenhum quarto cadastrado com ID {escolha}.")
        except ValueError:
            print("Opção inválida!")
            
#-----------------------------------------------REMOVER CLIENTE------------------------------------------------
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




quartos, clientes, reservas = carregar_dados()
fazer_reserva(quartos, clientes, reservas)
salvar_dados(quartos, clientes, reservas)
















































#-----------------------------------------------FUNÇÃO PRINCIPAL------------------------------------------------

"""def principal():
    clientes, quartos, reservas = carregar_dados()
    
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=Bates Motel-=-=-=-=-=-=-=-=-=-=-=")
        escolha = menu()
        

        if escolha == 1:
            cadastrar_quarto(quartos)
            return f"{quartos}"
        elif escolha == 2:
            cadastrar_cliente(clientes)
        elif escolha == 10:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    principal()"""





































































