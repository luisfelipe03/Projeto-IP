def carregar_dados():
    clientes = []
    quartos = []
    reservas = []
    
    try:
        #Exportando dados dos clientes
        with open("./Projeto-IP/assets/clientes.csv", "r", encoding="UTF-8") as c:
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
        with open("./Projeto-IP/assets/quartos.csv", "r", encoding="UTF-8") as q:
            for i in q:
                id, num, reser = i.strip().split(',')
                quarto = {
                    "id":int(id),
                    "numero":int(num),
                    "reservado": reser
                }
                quartos.append(quarto)
        
        with open("./Projeto-IP/assets/reservas.csv", "r", encoding="UTF-8") as r:
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
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                
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
            
    #Perguntar ao professor se pode usar regex para verificar formatação da data
    #Escolher Check-IN
    check_in = str(input("INFORME A DATA DE CHECK-IN(dd/mm/aaaa): "))
        
    #Escolher Check-OUT
    check_out = str(input("INFORME A DATA DE CHECK-OUT(dd/mm/aaaa): "))
        
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
        
        
                
                
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                
                
quartos, clientes, reservas = carregar_dados()

    
    