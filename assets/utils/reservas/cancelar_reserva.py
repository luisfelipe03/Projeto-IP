def cancelar_reserva(reservas, quartos, id_reserva):
    
    if id_reserva == 0:
        return print("Voltando para o menu...")
    
    # Verificar se a reserva existe pelo id_reserva fornecido
    reserva_encontrada = None
    for reserva in reservas:
        if reserva["id_reserva"] == id_reserva:
            reserva_encontrada = reserva
            break

    if reserva_encontrada is None:
        return print("\nReserva não encontrada.\n")

    id_quarto_reservado = reserva_encontrada["id_quarto"]

    # Atualizar status do quarto para não reservado
    for quarto in quartos:
        if quarto['id'] == id_quarto_reservado:
            quarto['reservado'] = 'nao'
            break

    # Remover a reserva da lista de reservas
    reservas.remove(reserva_encontrada)

    print('\033[32m' +"\nReserva cancelada com sucesso.\n" + '\033[0;0m')