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

salvar_dados(quartos, clientes, reservas)


"""def principal():
    clientes, quartos, reservas = carregar_dados()
    
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=Bates Motel-=-=-=-=-=-=-=-=-=-=-=")
        escolha = menu()
        

        if escolha == 1:
            cadastrar_quarto(quartos)
            return f"{quartos}"
        elif escolha == 2:
            cadastrar_cliente(clientes)
        elif escolha == 10:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    principal()"""


