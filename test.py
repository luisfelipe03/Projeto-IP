from assets.utils.carregar_dados import carregar_dados
from assets.utils.salvar_dados import salvar_dados
from assets.utils.reservas.fazer_reserva import fazer_reserva
from assets.utils.reservas.ver_reservas import ver_reservas
           
def editar_reserva(quartos, clientes, reservas):

    while True:
        id_reservas = []
        cliente = ''
        id_cliente = -1
        id_quarto = -1
        num_quarto = -1
        for r in reservas:
            id_reservas.append(r['id_reserva'])
            for c in clientes:
                if c['id'] == r['id_cliente']:
                    cliente = c['nome']
                    id_cliente = c['id']
            
            for q in quartos:
                if q['id'] == r['id_quarto']:
                    id_quarto = q['id']
                    num_quarto = q['numero']
                
            print(f"ID da reserva - {r['id_reserva']}\nQuarto - ID do quarto = {id_quarto} / Numero do quarto = {num_quarto}\nCliente - ID do cliente = {id_cliente} / Nome do cliente = {cliente}\nCheck-IN - {r['check-in']}\nCheck-OUT - {r['check-out']}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        escolha = int(input("Escolha o ID da reserva que você quer editar: "))
        
        if escolha not in id_reservas:
            print("OPÇÃO INVALIDA!")
            continue
        
        for i in reservas:
            if i['id'] == escolha:
                # Modificando o id_quarto da reserva
                while True:
                    try:
                        x = int(input('Digite o ID do quarto(Se o ID for o mesmo digite 0): '))
                        if x == 0:
                            x = id_quarto   
                        break
                    except ValueError:
                        print("ID É DO TIPO NUMERICO!")
                        continue
                # Modificando o id_cliente da reserva
                while True:
                    try:
                        y = int(input('Digite o ID do cliente(Se o ID for o mesmo digite 0): '))
                        if y == 0:
                            y = id_cliente
                        break
                    except ValueError:
                        print("ID É DO TIPO NUMERICO!")
                        continue
        
        
#-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=-=-==-=-=--=-==-=-=-                 
quartos, clientes, reservas = carregar_dados()
editar_reserva(quartos, clientes, reservas)



#editar reserva
#1. precisamos saber qual reserva o usuario que mudar, escolher pelo id
#2. escolhido a reserva pergunta ao usuario se que manter o mudar o id de quarto e cliente
#3. Se mudar o quarto tem que mudar o status da reserva de 'sim' para 'nao'
#4. 