def remover_quarto(quartos):
    while True:
        print("------ QUAL QUARTO VOCÊ DESEJA REMOVER? ------\n")
        
        # Exibe os detalhes de cada quarto na lista de quartos
        for i in quartos:
            print(f"ID = {i['id']}")
            print(f"Número do quarto = {i['numero']}")
            print(f"Reservado = {i['reservado']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
        try:
            escolha = int(input("Digite o ID do quarto que você deseja remover (ou 0 para voltar ao menu): "))
            
            # Se a escolha for 0, sai do loop e retorna ao menu principal
            if escolha == 0:
                break
                
            quarto_encontrado = None
            # Procura o quarto com o ID correspondente à escolha do usuário
            for quarto in quartos:
                if quarto['id'] == escolha:
                    quarto_encontrado = quarto
                    break
                        
            if quarto_encontrado:
                # Remove o quarto encontrado da lista de quartos
                quartos.remove(quarto_encontrado)
                print(f"Quarto com ID {escolha} removido com sucesso.")
            else:
                print(f"\nNenhum quarto cadastrado com ID {escolha}.\n")
        except ValueError:
            print("\nOpção inválida! Por favor, digite um valor numérico.\n")