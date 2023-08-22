def carregar_dados():
    clientes = []   # Lista para armazenar dados dos clientes
    quartos = []    # Lista para armazenar dados dos quartos
    reservas = []   # Lista para armazenar dados das reservas
    
    try:
        # Exportando dados dos clientes
        with open("./assets/csv/clientes.csv", "r", encoding="UTF-8") as c:
            linhas = c.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                # Criando um dicionário para armazenar os dados de um cliente
                cliente = {
                    "id": int(dados[0]),
                    "nome": dados[1],
                    "idade": dados[2],
                    "cpf": dados[3],
                    "rg": dados[4]
                }
                clientes.append(cliente) # Adicionando o cliente à lista de clientes
            
        # Exportando dados dos quartos        
        with open("./assets/csv/quartos.csv", "r", encoding="UTF-8") as q:
            for i in q:
                id, num, reser = i.strip().split(',')
                # Criando um dicionário para armazenar os dados de um quarto
                quarto = {
                    "id": int(id),
                    "numero": int(num),
                    "reservado": reser
                }
                quartos.append(quarto) # Adicionando o quarto à lista de quartos
        
        # Exportando dados das reservas
        with open("./assets/csv/reservas.csv", "r", encoding="UTF-8") as r:
            for linha in r:
                id_reserva, id_quarto, id_cliente, check_in, check_out = linha.strip().split(',')
                # Criando um dicionário para armazenar os dados de uma reserva
                reserva = {
                    "id_reserva": int(id_reserva),
                    "id_quarto": int(id_quarto),
                    "id_cliente": int(id_cliente),
                    "check-in": check_in,
                    "check-out": check_out
                }
                reservas.append(reserva) # Adicionando a reserva à lista de reservas
    except FileNotFoundError:
        print("Arquivo não encontrado")
        
    return quartos, clientes, reservas # Retornando as listas de quartos, clientes e reservas
