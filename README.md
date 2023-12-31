<h2>Projeto de IP - Sistema de gestão hoteleira</h2>

<p>Sistema desenvolvido para avaliação de desempenho da cadeira de introdução a programação da UFAPE.</p>

<h3>Requisitos:</h3>

- 1.Desenvolver um software para gerenciamento de ambiente comercial (ex.: pousada, controle de estoque, venda de bilhetes aéreos, etc.)
- 2.O software deve apresentar:
	- 2.1.Menu inicial para o usuário selecionar a opção de interesse;
	- 2.2. Opção para cadastrar itens (com ao menos 3 propriedades)
	- 2.3. Opção para buscar por itens cadastrados (e suas propriedades)
		- 2.3.1. busca por nome do item
		- 2.3.2. busca por propriedade do item
	- 2.4. Opção para editar as propriedades de um item cadastrados
	- 2.5. Opção para remover um item cadastrado
	- 2.6. Persistência dos dados em arquivo .csv contendo itens e suas propriedades

<h3>Funções do sistema</h3>

1. Funções de reserva:
	- [x] Fazer reserva
	- [x] Editar reserva 
	- [x] Cancelar reserva
	- [x] Ver todos as reservas
	- [x] Buscar reserva por ID da reserva/ID do quarto

1. Funções de quarto:
	- [x] Cadastrar quarto
	- [x] Editar cadastro do quarto
	- [x] Remover quartos
	- [x] Buscar quartos por ID/Número do quarto

1. Funções do cliente:
	- [x] Cadastrar cliente
	- [x] Editar cadastro de cliente
	- [x] Excluir cadastro de cliente
	- [x] Buscar cliente por ID/Nome

1. Outras funções:
 	- [x] Mostar menu 
	- [x] Carregar dados do arquivo .CSV
	- [x] Salvar dados no arquivo .CSV
	

<h3>Atributos dos itens :</h3>

- Reserva:
	+ ID da reserva
	+ ID do cliente
	+ ID do quarto
	+ Check-IN
	+ Check-OUT

- Quarto:
	+ ID do quarto
	+ Número do quarto
	+ Status de reserva: "sim" ou "nao"

- Cliente:
	+ ID do cliente
	+ Nome do cliente
	+ Idade do cliente
	+ CPF
	+ RG


## :floppy_disk: Como executar o projeto

### Pré requisitos 

- [Git](https://git-scm.com) 
- [Python 3.7 ou superior](https://www.python.org/downloads/)

### Executando o projeto em sua maquina
```bash
1- Clone este repositorio:

$ git clone https://github.com/luisfelipe03/Projeto-IP.git

2- Abra o diretorio do projeto no terminal

3- Execute o projeto:

$ python app.py
```
