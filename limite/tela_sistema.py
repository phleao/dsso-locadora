#tela inicial do sistema

class TelaSistema:
    def tela_opcoes(self):
        print("-------- LocadaçON ---------")
        print("Escolha sua opcao")
        print("1 - Opcao 1")
        print("2 - Opcao 2")
        print("3 - Opcao 3")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao
