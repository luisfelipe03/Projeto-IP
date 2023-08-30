from assets.utils.quartos.cadastrar_quarto import verifica_numero_existente_quarto

def editar_quarto(quartos):
    #Verde
    numero = int(input("Digite o número do quarto que você deseja editar: "))
    
    quarto_encontrado = None
    for quarto in quartos:
        if quarto["numero"] == numero:
            quarto_encontrado = quarto
            break
    
    if quarto_encontrado is None:
        #Vermelho
        print('\033[31m' + f"Não foi encontrado nenhum quarto com o número {numero}" + '\033[0;0m')
        return
    
    if quarto_encontrado['reservado'] == "sim":
        #Vermelho
        return print('\033[31m' + "NÃO É POSSIVEL EDITAR QUARTO QUE ESTÁ RESERVADO" + '\033[0;0m')
    
    print(f"Editando quarto número {numero}:")
    while True:
        try:
            novo_numero = int(input("Novo número do quarto: "))
            if verifica_numero_existente_quarto(novo_numero, quartos):
                #Vermelho
                print('\033[31m' + f"Já existe um quarto cadastrado com esse número: {novo_numero}" + '\033[0;0m')
                continue
            break
        except ValueError:
            #Vermelho
            print("O número do quarto deve ser um número inteiro")
    
    quarto_encontrado["numero"] = novo_numero
    #Verde
    print("Quarto editado com sucesso!")
