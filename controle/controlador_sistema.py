from limite.tela_sistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    def opcao1(self):
        print("\nVocê escolheu a opcao 1")

    def opcao2(self):
        print("\nVocê escolheu a opcao 2")

    def opcao3(self):
        print("\nVocê escolheu a opcao 3")

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.opcao1, 2: self.opcao2, 3: self.opcao3,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
