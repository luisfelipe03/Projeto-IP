# Função para verificar se já existe um quarto cadastrado com o mesmo número
def verifica_numero_existente_quarto(numero, quartos):
    for quarto in quartos:
        if quarto["numero"] == numero:
            return True
    return False

# Função para cadastrar um novo quarto
def cadastrar_quarto(quartos):
    
    # Verifica o último ID e soma +1 para continuar a sequência dos IDs
    if not quartos:
        id = 1
    else:
        ultimo_dicionario = quartos[-1]
        id = ultimo_dicionario.get("id") + 1

    while True:
        try:
            numero = int(input("Número do quarto: "))
            if verifica_numero_existente_quarto(numero, quartos):
                print('\033[31m' + f"Já existe um quarto cadastrado com esse número: {numero}" + '\033[0;0m')
                continue
            break
        except ValueError:
            print('\033[31m' + "O número do quarto deve ser um número inteiro" + '\033[0;0m')

    # Cria um dicionário para o novo quarto
    quarto = {
        "id": id,
        "numero": numero,
        "reservado": "nao"
    }

    # Adiciona o dicionário à lista de quartos
    quartos.append(quarto)
    print('\033[32m' + "Quarto cadastrado com sucesso!" + '\033[0;0m')


