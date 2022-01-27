#tela inicial do sistema

class TelaSistema:

    def tela_login(self):
        print("BEM VINDO AO SISTEMA LOCAÇON")
        print("Escolha sua opcao")
        print("1 - Login")
        print("2 - Cadastrar como Cliente")
        print("3 - Cadastrar como Funcionário")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes(self):
        print("-------- LocadaçON ---------")
        print("Escolha sua opcao")
        print("1 - Filmes")
        print("2 - Locações")
        print("3 - Opcao 3")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao
