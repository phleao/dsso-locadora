from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from limite.tela_sistema import TelaSistema
from controle.controlador_filmes import ControladorFilmes
from limite.tela_pessoa import TelaPessoa
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_locacao import ControladorLocacao

class ControladorSistema:

    def __init__(self):
        self.__controlador_filmes = ControladorFilmes(self)
        self.__controlador_locacao = ControladorLocacao(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_sistema = TelaSistema()
        self.__tela_pessoa = TelaPessoa()
        self.__email_logado = ""

    @property
    def controlador_filmes(self):
        return self.__controlador_filmes

    @property
    def controlador_locacao(self):
        return self.__controlador_locacao

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def inicializa_sistema(self):
        self.__tela_sistema.mostra_mensagem("BEM VINDO AO SISTEMA LOCAÇON")
        self.abre_tela_login() 

    def abre_tela_funcionario(self):
        lista_opcoes = {1: self.cadastra_filmes, 2: self.cadastra_locacao, 3: self.opcao3,
                        0: self.abre_tela_login}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_do_funcionario()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_cliente(self):
        lista_opcoes = {1: self.ver_catalogo, 2: self.fazer_locacao, 3: self.opcao3,
                        0: self.abre_tela_login}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_do_cliente()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def ver_catalogo(self):
        self.__controlador_filmes.lista_filme()

    def cadastra_filmes(self):
        self.__controlador_filmes.abre_tela()

    def cadastra_locacao(self):
        pass

    def fazer_locacao(self):
        self.__controlador_locacao.incluir_locacao()

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
            if opcao_escolhida == 1:
                retorno = funcao_escolhida()
                if retorno != 0:
                    return retorno
            else:
                funcao_escolhida()
    
    def verifica_login(self, email, senha):
        #retorno 0 se login deu errado, retorno 1 se é funcionário, retorno 2 se é cliente
        for funcionario in self.__controlador_pessoa.funcionarios:
            if funcionario.email == email and funcionario.senha == senha:
                return 1
        for cliente in self.__controlador_pessoa.clientes:
            if cliente.email == email and cliente.senha == senha:
                return 2
        return 0
    
    def acessa_login(self):
        dados = self.__tela_pessoa.pega_dados_login()
        verificacao = self.verifica_login(dados["email"], dados["senha"])
        if verificacao == 0:
            self.__tela_sistema.mostra_mensagem("Email ou senha digitados não foram encontrados, tente novamente")
            return verificacao
        elif verificacao == 1:
            self.__tela_sistema.mostra_mensagem("Bem vindo funcionário!")
            self.abre_tela_funcionario()
        else:
            self.__tela_sistema.mostra_mensagem("Bem vindo cliente!")
            self.guarda_email_login(dados["email"])
            self.abre_tela_cliente()

    def guarda_email_login(self, email):
        self.__email_logado = email

    @property
    def email_logado(self):
        return self.__email_logado

    def acessa_cad_cliente(self):
        self.__controlador_pessoa.incluir_cliente()


    def acessa_cad_funcionario(self):
        tentativa_de_senha = self.__tela_pessoa.pega_senha_de_cadastro()
        senha_acesso = "123"
        if tentativa_de_senha == senha_acesso:
            self.__controlador_pessoa.incluir_funcionario()
        else:
            self.__tela_sistema.mostra_mensagem("Senha inválida")