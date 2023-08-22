def menu():
    """
    Exibe o menu de opções para a gestão de reservas e informações do hotel.
    Retorna a opção escolhida pelo usuário.
    """
    print("1. Fazer uma reserva")
    print("2. Editar reserva")
    print("3. Cancelar reserva")
    print("4. Ver todos os quartos reservados")
    print("5. Cadastrar quarto")
    print("6. Cadastrar cliente")
    print("7. Editar quarto")
    print("8. Editar cliente")
    print("9. Remover quarto")
    print("10. Remover cliente")
    print("11. Buscar quarto por número ou ID")
    print("12. Buscar cliente por nome ou ID")
    print("0. Sair")
    return input("Escolha uma opção: ")