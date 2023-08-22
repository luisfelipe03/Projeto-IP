# Verifica se já existe quarto cadastrado com o mesmo número
def verifica_numero_existente_quarto(numero, quartos):
    for quarto in quartos:
        if quarto["numero"] == numero:
            return True
    return False

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
                print(f"Já existe quarto cadastrado com esse número: {numero}")
                continue
            break
        except ValueError:
            print("Número do quarto deve ser um número inteiro")

    quarto = {
        "id": id,
        "numero": numero,
        "reservado": "não"
    }

    quartos.append(quarto)
    print("Quarto cadastrado com sucesso!")
