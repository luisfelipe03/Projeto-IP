from assets.utils.quartos.cadastrar_quarto import verifica_numero_existente_quarto

def editar_quarto(quartos):
    numero = int(input("Digite o número do quarto que você deseja editar: "))
    
    quarto_encontrado = None
    for quarto in quartos:
        if quarto["numero"] == numero:
            quarto_encontrado = quarto
            break
    
    if quarto_encontrado is None:
        print(f"Não foi encontrado nenhum quarto com o número {numero}")
        return
    
    if quarto_encontrado['reservado'] == "sim":
        return print("NÃO É POSSIVEL EDITAR QUARTO QUE ESTÁ RESERVADO")
    
    print(f"Editando quarto número {numero}:")
    while True:
        try:
            novo_numero = int(input("Novo número do quarto: "))
            if verifica_numero_existente_quarto(novo_numero, quartos):
                print(f"Já existe um quarto cadastrado com esse número: {novo_numero}")
                continue
            break
        except ValueError:
            print("O número do quarto deve ser um número inteiro")
    
    quarto_encontrado["numero"] = novo_numero
    print("Quarto editado com sucesso!")
