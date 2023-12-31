'''
SISTEMA DE GESTÃO DE HOTEL

Desenvolvedores: Luis Felipe de Oliveira Andrade
                 Phylypy Cabral de Lima Tavares 

Para mais informações sobre o sistema leia o arquivo README.md
'''

from assets.utils.menu import menu 
from assets.utils.carregar_dados import carregar_dados
from assets.utils.salvar_dados import salvar_dados
from assets.utils.reservas.fazer_reserva import fazer_reserva
from assets.utils.reservas.ver_reservas import ver_reservas
from assets.utils.reservas.editar_reserva import editar_reserva
from assets.utils.reservas.cancelar_reserva import cancelar_reserva
from assets.utils.quartos.cadastrar_quarto import cadastrar_quarto
from assets.utils.clientes.cadastrar_clientes import cadastrar_cliente
from assets.utils.quartos.buscar_quarto import buscar_quarto
from assets.utils.clientes.buscar_cliente import buscar_cliente
from assets.utils.reservas.buscar_reserva import buscar_reserva
from assets.utils.quartos.editar_quarto import editar_quarto
from assets.utils.clientes.editar_cliente import editar_cliente
from assets.utils.quartos.remover_quarto import remover_quarto
from assets.utils.clientes.remover_cliente import remover_cliente


def principal():
    quartos, clientes, reservas = carregar_dados()

    while True:
        print("\n-=-=-=-=-=-=-=-=-=-=-=Bates Motel=-=-=-=-=-=-=-=-=-=-=-=-\n")
        escolha = menu()

        if escolha == '1':
            fazer_reserva(quartos, clientes, reservas)
        elif escolha == '2':
            i = ver_reservas(quartos, clientes, reservas)
            if i == 0:
                print("\nNÃO TEM RESERVAS NO SISTEMA\n")
            id_reserva = int(input("Digite o ID da reserva que deseja editar(Ou digite 0 para voltar ao menu): "))
            editar_reserva(quartos, clientes, reservas, id_reserva)
        elif escolha == '3':
            i = ver_reservas(quartos, clientes, reservas)
            if i == 0:
                print("\nNÃO TEM RESERVAS NO SISTEMA\n")
            id_reserva = int(input("Digite o ID da reserva que deseja cancelar(Ou digite 0 para voltar ao menu): "))
            cancelar_reserva(reservas, quartos, id_reserva)
        elif escolha == '4':
            i = ver_reservas(quartos, clientes, reservas)
            if i == 0:
                print("\nNÃO TEM RESERVAS NO SISTEMA\n")
        elif escolha == "5":
            reservas_encontradas = buscar_reserva(reservas, quartos, clientes)

            if reservas_encontradas:
                print("Detalhes encontrados:")
                for detalhes in reservas_encontradas:
                    print("-=-=-=-=-=-=-=-=-=-==-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=")
                    for key, value in detalhes.items():
                        print(f"{key}: {value}")
            else:
                print("Nenhum detalhe encontrado.")
        elif escolha == '6':
            cadastrar_quarto(quartos)
        elif escolha == '7':
            cadastrar_cliente(clientes)
        elif escolha == '8':
            editar_quarto(quartos)
        elif escolha == '9':
            editar_cliente(clientes)
        elif escolha == '10':
            remover_quarto(quartos)
        elif escolha == '11':
            remover_cliente(clientes)
        elif escolha == '12':
            buscar_quarto(quartos)
        elif escolha == '13':
            buscar_cliente(clientes)
        elif escolha == '0':
            salvar_dados(quartos, clientes, reservas)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()


