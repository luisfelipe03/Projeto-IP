'''
SISTEMA DE GESTÃO DE HOTEL

Desenvolvedores: Luis Felipe de Oliveira Andrade
                 Phylypy Cabral de Lima Tavares 

Para mais informações sobre o sistema leia o arquivo README.txt
'''

from assets.utils.menu import menu 
from assets.utils.carregar_dados import carregar_dados
from assets.utils.salvar_dados import salvar_dados
from assets.utils.reservas.fazer_reserva import fazer_reserva
from assets.utils.reservas.ver_reservas import ver_reservas
from assets.utils.quartos.cadastrar_quarto import cadastrar_quarto
from assets.utils.clientes.cadastrar_clientes import cadastrar_cliente
from assets.utils.quartos.remover_quarto import remover_quarto
from assets.utils.clientes.remover_cliente import remover_cliente
from assets.utils.reservas.cancelar_reserva import cancelar_reserva

"""quartos, clientes, reservas = carregar_dados()
cancelar_reserva(quartos, clientes, reservas)
salvar_dados(quartos, clientes, reservas)"""


# Função principal

def principal():
    quartos, clientes, reservas = carregar_dados()

    while True:
        print("\n-=-=-=-=-=-=-=-=-=-=-=Bates Motel=-=-=-=-=-=-=-=-=-=-=-=\n")
        escolha = menu()

        if escolha == '1':
            fazer_reserva(quartos, clientes, reservas)
        elif escolha == '2':
            #editar_reserva()
            print("\nEM DESENVOLVIMENTO...\n")
        elif escolha == '3':
            cancelar_reserva(reservas)
        elif escolha == '4':
            ver_reservas(quartos, clientes, reservas)
        elif escolha == '5':
            cadastrar_quarto(quartos)
        elif escolha == '6':
            cadastrar_cliente(clientes)
        elif escolha == '7':
            #editar_quarto(quartos)
            print("\nEM DESENVOLVIMENTO...\n")
        elif escolha == '8':
            #editar_cliente(clientes)
            print("\nEM DESENVOLVIMENTO...\n")
        elif escolha == '9':
            remover_quarto(quartos)
        elif escolha == '10':
            remover_cliente(clientes)
        elif escolha == '11':
            #buscar_quarto(quartos)
            print("\nEM DESENVOLVIMENTO...\n")
        elif escolha == '12':
            #buscar_cliente(clientes)
            print("\nEM DESENVOLVIMENTO...\n")
        elif escolha == '0':
            salvar_dados(quartos, clientes, reservas)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()


