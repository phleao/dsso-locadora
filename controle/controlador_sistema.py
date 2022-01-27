from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from limite.tela_sistema import TelaSistema
from controle.controlador_filmes import ControladorFilmes
from limite.tela_pessoa import TelaPessoa
from controle.controlador_pessoa import ControladorPessoa

class ControladorSistema:

    def __init__(self):
        self.__controlador_filmes = ControladorFilmes(self)
        self.__tela_sistema = TelaSistema()
        self.__tela_pessoa = TelaPessoa()

    def inicializa_sistema(self):
        if self.abre_tela_login():
            self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_livros, 2: self.opcao2, 3: self.opcao3,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def cadastra_livros(self):
        self.__controlador_filmes.abre_tela()

    def opcao2(self):
        print("\nVocê escolheu a opcao 2")

    def opcao3(self):
        print("\nVocê escolheu a opcao 3")

    def encerra_sistema(self):
        exit(0)

    def abre_tela_login(self):
        lista_opcoes_login = {1: self.acessa_login, 2: self.acessa_cad_cliente, 3: self.acessa_cad_funcionario,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_login()
            funcao_escolhida = lista_opcoes_login[opcao_escolhida]
            funcao_escolhida()
            return True
    
    def verifica_login(self, email):

        print("FAZER VERIFICACAO EM QUAL TIPO DE PESSOA O EMAIL EXISTE")           
    
    def acessa_login(self):
        self.__tela_pessoa.pega_dados_login()
    
    
    def acessa_cad_cliente(self):
        self.__tela_pessoa.pega_dados_cliente()

    def acessa_cad_funcionario(self):
        self.__tela_pessoa.pega_dados_funcionario()
        