# Função para buscar um quarto pelo ID
def buscar_quarto_id(quartos, quarto_id):
    for q in quartos:
        if q['id'] == quarto_id:
            return q
    return None

# Função para buscar um quarto pelo número
def buscar_quarto_numero(quartos, quarto_num):
    for q in quartos:
        if q['numero'] == quarto_num:
            return q
    return None

# Função principal para buscar um quarto
def buscar_quarto(quartos):
    while True:
        try:
            escolha_busca = int(input("Digite (1) para buscar pelo ID do quarto\nOu digite (2) para buscar pelo número do quarto: "))
        
            break
        except ValueError:
            # Mensagem de erro em caso de entrada inválida
            print('\033[31m' + "OPÇÃO INVÁLIDA!" + '\033[0;0m')
            continue
        
    if escolha_busca == 1:
        try:
            quarto_id = int(input("Digite o ID do quarto: "))
            qua = buscar_quarto_id(quartos, quarto_id)
            if qua != None:
                # Mostra as informações do quarto encontrado
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print(f"ID - {qua['id']}\nNúmero - {qua['numero']}\nReservado - {qua['reservado']}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
            else:
                # Mensagem de quarto não encontrado
                print(f"Quarto com ID = {quarto_id} não encontrado")
        except ValueError:
            # Mensagem de erro em caso de entrada inválida
            print('\033[31m' + "OPÇÃO INVÁLIDA!" + '\033[0;0m')
    
    if escolha_busca == 2:
        try:
            quarto_num = int(input("Digite o número do quarto: "))
            quar = buscar_quarto_numero(quartos, quarto_num)
            if quar != None:
                # Mostra as informações do quarto encontrado
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print(f"ID - {quar['id']}\nNúmero - {quar['numero']}\nReservado - {quar['reservado']}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
            else:
                # Mensagem de quarto não encontrado
                print(f"Quarto com número = {quarto_num} não encontrado!")
        except ValueError:
            # Mensagem de erro em caso de entrada inválida
            print('\033[31m' + "OPÇÃO INVÁLIDA!" + '\033[0;0m')


