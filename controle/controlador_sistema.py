#arquivo controlador do sistema

class ControladorSistema:

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: "Opcao 1", 2: "Opcao 2", 3: "Opcao 3", 0: "Encerra sistema"}

        print(lista_opcoes)
