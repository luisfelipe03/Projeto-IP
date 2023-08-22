def carregar_dados():
    clientes = []
    quartos = []
    reservas = []
    
    try:
        #Exportando dados dos clientes
        with open("./assets/csv/clientes.csv", "r", encoding="UTF-8") as c:
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
        with open("./assets/csv/quartos.csv", "r", encoding="UTF-8") as q:
            for i in q:
                id, num, reser = i.strip().split(',')
                quarto = {
                    "id":int(id),
                    "numero":int(num),
                    "reservado": reser
                }
                quartos.append(quarto)
        
        with open("./assets/csv/reservas.csv", "r", encoding="UTF-8") as r:
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
    with open("./assets/csv/clientes.csv", "w", encoding="UTF-8") as arquivo:
        for cliente in clientes:
             arquivo.write(f"{cliente['id']},{cliente['nome']},{cliente['idade']},{cliente['cpf']},{cliente['rg']}\n")
    
    with open("./assets/csv/quartos.csv", "w", encoding="UTF-8") as arquivo:  
        for quarto in quartos:    
            arquivo.write(f"{quarto['id']},{quarto['numero']},{quarto['reservado']}\n")   
            
    with open("./assets/csv/reservas.csv", "w", encoding="UTF-8") as arquivo:
        for reserva in reservas:
            arquivo.write(f"{reserva['id_reserva']},{reserva['id_quarto']},{reserva['id_cliente']},{reserva['check-in']},{reserva['check-out']}\n")  

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
            
        if len(quartos_disponivel) == 0:
            return print("NÃO TEM MAIS QUARTOS DISPONIVEIS")
                
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
                
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                
def ver_reservas(quartos, clientes, reservas):
    for r in reservas:
        cliente = ''
        id_cliente = -1
        id_quarto = -1
        num_quarto = -1
        for c in clientes:
            if c['id'] == r['id_cliente']:
                cliente = c['nome']
                id_cliente = c['id']
        
        for q in quartos:
            if q['id'] == r['id_quarto']:
                id_quarto = q['id']
                num_quarto = q['numero']
            
        print(f"ID da reserva - {r['id_reserva']}\nQuarto - ID do quarto = {id_quarto} / Numero do quarto = {num_quarto}\nCliente - ID do cliente = {id_cliente} / Nome do cliente = {cliente}\nCheck-IN - {r['check-in']}\nCheck-OUT - {r['check-out']}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                
def editar_reserva(quartos, clientes, reservas):

    while True:
        id_reservas = []
        cliente = ''
        id_cliente = -1
        id_quarto = -1
        num_quarto = -1
        for r in reservas:
            id_reservas.append(r['id_reserva'])
            for c in clientes:
                if c['id'] == r['id_cliente']:
                    cliente = c['nome']
                    id_cliente = c['id']
            
            for q in quartos:
                if q['id'] == r['id_quarto']:
                    id_quarto = q['id']
                    num_quarto = q['numero']
                
            print(f"ID da reserva - {r['id_reserva']}\nQuarto - ID do quarto = {id_quarto} / Numero do quarto = {num_quarto}\nCliente - ID do cliente = {id_cliente} / Nome do cliente = {cliente}\nCheck-IN - {r['check-in']}\nCheck-OUT - {r['check-out']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        escolha = int(input("Escolha o ID da reserva que você quer editar: "))
        
        if escolha not in id_reservas:
            print("OPÇÃO INVALIDA!")
            continue
        
        for i in reservas:
            if i['id'] == escolha:
                # Modificando o id_quarto da reserva
                while True:
                    try:
                        x = int(input('Digite o ID do quarto(Se o ID for o mesmo digite 0): '))
                        if x == 0:
                            x = id_quarto   
                        break
                    except ValueError:
                        print("ID É DO TIPO NUMERICO!")
                        continue
                # Modificando o id_cliente da reserva
                while True:
                    try:
                        y = int(input('Digite o ID do cliente(Se o ID for o mesmo digite 0): '))
                        if y == 0:
                            y = id_cliente
                        break
                    except ValueError:
                        print("ID É DO TIPO NUMERICO!")
                        continue
        
        
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                 
quartos, clientes, reservas = carregar_dados()
editar_reserva(quartos, clientes, reservas)



#editar reserva
#1. precisamos saber qual reserva o usuario que mudar, escolher pelo id
#2. escolhido a reserva pergunta ao usuario se que manter o mudar o id de quarto e cliente
#3. Se mudar o quarto tem que mudar o status da reserva de 'sim' para 'nao'
#4. 