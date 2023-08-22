def salvar_dados(quartos, clientes, reservas):
    # Salvando informações dos clientes em um arquivo CSV
    with open("./assets/csv/clientes.csv", "w", encoding="UTF-8") as arquivo:
        for cliente in clientes:
            arquivo.write(f"{cliente['id']},{cliente['nome']},{cliente['idade']},{cliente['cpf']},{cliente['rg']}\n")
    
    # Salvando informações dos quartos em um arquivo CSV
    with open("./assets/csv/quartos.csv", "w", encoding="UTF-8") as arquivo:
        for quarto in quartos:
            arquivo.write(f"{quarto['id']},{quarto['numero']},{quarto['reservado']}\n")
            
    # Salvando informações das reservas em um arquivo CSV
    with open("./assets/csv/reservas.csv", "w", encoding="UTF-8") as arquivo:
        for reserva in reservas:
            arquivo.write(f"{reserva['id_reserva']},{reserva['id_quarto']},{reserva['id_cliente']},{reserva['check-in']},{reserva['check-out']}\n")
