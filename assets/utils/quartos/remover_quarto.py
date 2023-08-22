def remover_quarto(quartos): 
    while True: 
        print("------QUAL QUARTO VOCÊ DESEJA REMOVER ?------\n")
        for i in quartos:
            print(f"ID = {i['id']}\nNumero do quarto = {i['numero']}\nReservado = {i['reservado']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
        try:
            escolha = int(input("Digite o ID do quarto que você quer remover (ou 0 para voltar ao menu): "))
            
            if escolha == 0:
                break  
              
            quarto_encontrado = None
            for quarto in quartos:
                if quarto['id'] == escolha:
                    quarto_encontrado = quarto
                    break
                        
            if quarto_encontrado:
                quartos.remove(quarto_encontrado)
                print(f"Quarto com ID {escolha} removido com sucesso.")
            else:
                print(f"Nenhum quarto cadastrado com ID {escolha}.")
        except ValueError:
            print("Opção inválida!")
            
