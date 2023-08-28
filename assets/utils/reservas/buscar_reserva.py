def buscar_reserva(quartos, clientes, reservas):
    while True:    
        try:
            escolha_busca = int(input("Digite (1) para buscar a reserva pelo número do quarto,\nOu digite (2) para buscar pelo nome do cliente: "))
            break
        except ValueError:
            #Vermelho
            print("OPÇÃO INVÁLIDA!")
            continue
        
    if escolha_busca == 1:
        escolha_quarto = int(input("Digite o ID do quarto: "))
        