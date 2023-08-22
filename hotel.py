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

quartos, clientes, reservas = carregar_dados()
ver_reservas(quartos, clientes, reservas)
salvar_dados(quartos, clientes, reservas)


# Função principal
"""
def principal():
    quartos, clientes = carregar_dados()

    while True:
        escolha = mostrar_menu()

        if escolha == '1':
            cadastrar_quarto(quartos)
        elif escolha == '2':
            cadastrar_cliente(clientes)
        elif escolha == '3':
            editar_quarto(quartos)
        elif escolha == '4':
            editar_cliente(clientes)
        elif escolha == '5':
            remover_quarto(quartos)
        elif escolha == '6':
            remover_cliente(clientes)
        elif escolha == '7':
            buscar_quarto(quartos)
        elif escolha == '8':
            buscar_cliente(clientes)
        elif escolha == '9':
            salvar_dados(quartos, clientes)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()"""


