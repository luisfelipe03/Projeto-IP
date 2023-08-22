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