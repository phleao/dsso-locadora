#tela inicial do sistema

class TelaSistema:

    def tela_login(self):
        print("Escolha sua opcao")
        print("1 - Login")
        print("2 - Cadastrar como Cliente")
        print("3 - Cadastrar como Funcionário")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_do_funcionario(self):
        print("-------- LocadaçON ---------")
        print("Escolha sua opcao")
        print("1 - Filmes")
        print("2 - Locações")
        print("3 - Clientes")
        print("0 - Deslogar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_do_cliente(self):
        print("-------- LocadaçON ---------")
        print("Escolha sua opcao")
        print("1 - Cátalogo de filmes") 
        print("2 - Fazer locação")
        print("3 - Histórico de locações")
        print("0 - Deslogar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_do_cliente_status_true(self):
        print("-------- LocadaçON ---------")
        print("Escolha sua opcao")
        print("1 - Cátalogo de filmes")
        print("2 - Verificar locação atual")
        print("3 - Finalizar locação atual")
        print("0 - Deslogar")
        opcao = int(input("Escolha a opcao: "))
        return opcao


    def mostra_mensagem(self, msg):
        print(msg)