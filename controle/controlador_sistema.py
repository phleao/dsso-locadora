from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from entidade.locacao import Locacao
from limite.tela_sistema import TelaSistema
from controle.controlador_filmes import ControladorFilmes
from limite.tela_pessoa import TelaPessoa
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_locacao import ControladorLocacao
from controle.controlador_genero import ControladorGenero
from erros.errou_a_senha_do_adm import ErrouSenhaDoAdmError

class ControladorSistema:

    def __init__(self):
        self.__controlador_genero = ControladorGenero(self)
        self.__controlador_filmes = ControladorFilmes(self)
        self.__controlador_locacao = ControladorLocacao(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__tela_sistema = TelaSistema()
        self.__tela_pessoa = TelaPessoa()
        self.__cliente_logado = ''

    @property
    def cliente_logado(self):
        return self.__cliente_logado

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
        lista_opcoes = {'Filmes': self.acessa_filmes, 'Locacoes': self.lista_locacoes, 'Clientes': self.mostra_clientes,
                        'Deslogar': self.abre_tela_login}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_do_funcionario()
            if opcao_escolhida == None:
                        self.encerra_sistema()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_cliente(self):
        while True:
            while self.__cliente_logado.status == False:
                lista_opcoes = {'Catalogo': self.ver_catalogo, 'Historico': self.historico_locacao, 'Melhores filmes': self.lista_filmes_avaliados,
                            'Deslogar': self.abre_tela_login}
                verificador = True
                while verificador == True:
                    opcao_escolhida = self.__tela_sistema.tela_opcoes_do_cliente()
                    if opcao_escolhida == None:
                        self.encerra_sistema()

                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                    verificador = False


            while self.__cliente_logado.status == True:
                lista_opcoes = {'Locacao Atual': self.verificar_locacao_atual, 'Melhores filmes': self.lista_filmes_avaliados,
                                'Deslogar': self.abre_tela_login}
                verificador = True
                while verificador == True:
                    opcao_escolhida = self.__tela_sistema.tela_opcoes_do_cliente_status_true()
                    if opcao_escolhida == None:
                        self.encerra_sistema()
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                    verificador = False

    def lista_filmes_avaliados(self):
        self.__controlador_filmes.lista_filmes_avaliados()

    def verificar_locacao_atual(self):
        self.__controlador_locacao.ver_locacao_atual_cliente()


    def finalizar_locacao(self):
        locacao = self.__controlador_locacao.pega_locacao_cliente()
        self.__controlador_pessoa.alterar_status(self.__cliente_logado, False)
        filme = self.__controlador_locacao.incluir_avaliacao()
        self.__controlador_filmes.atualizar_filme(filme)
        self.__controlador_locacao.alterar_locacao(locacao)
        

    def ver_catalogo(self):
        self.__controlador_filmes.lista_filme_catalogo()

    def acessa_filmes(self):
        self.__controlador_filmes.abre_tela()

    def lista_locacoes(self):
        self.__controlador_locacao.lista_locacao()

    def mostra_clientes(self):
        self.__controlador_pessoa.lista_clientes()

    def encerra_sistema(self):
        exit(0)

    def abre_tela_login(self):
        lista_opcoes_login = {'Login': self.acessa_login, 'Cadastrar Cliente': self.acessa_cad_cliente, 'Cadastrar Funcionario': self.acessa_cad_funcionario,
                        'Finalizar': self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_login()
            if opcao_escolhida == None:
                        self.encerra_sistema()
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
        dados = self.__controlador_pessoa.pega_dados_log()
        if dados == None:
            return 0
        verificacao = self.verifica_login(dados["email"], dados["senha"])
        if verificacao == 0:
            self.__tela_sistema.mostra_mensagem("Email ou senha digitados não foram encontrados, tente novamente")
            return verificacao
        elif verificacao == 1:
            self.__tela_sistema.mostra_mensagem("Bem vindo funcionário!")
            self.abre_tela_funcionario()
        else:
            self.__tela_sistema.mostra_mensagem("Bem vindo cliente!")
            for cliente in self.__controlador_pessoa.clientes:
                if cliente.email == dados["email"]:
                    self.__cliente_logado = cliente
            self.abre_tela_cliente()

    def guarda_email_login(self, email):
        self.__email_logado = email

    @property
    def email_logado(self):
        return self.__email_logado

    def acessa_cad_cliente(self):
        self.__controlador_pessoa.incluir_cliente()

    def acessa_cad_funcionario(self):
        while True:
            tentativa_de_senha = self.__controlador_pessoa.pega_senha_cad()
            if tentativa_de_senha == None:
                return None
            senha_acesso = "123"
            try:
                if tentativa_de_senha == senha_acesso:
                    self.__controlador_pessoa.incluir_funcionario()
                    break
                else:
                    raise ErrouSenhaDoAdmError
            except ErrouSenhaDoAdmError:
                self.__tela_sistema.mostra_mensagem("Senha para cadastrar funcionários Incorreta!!!")



    def historico_locacao(self):
        self.__controlador_locacao.lista_historico_locacao()

    def verifica_se_ja_tem_genero(self, nome_genero):
        return self.__controlador_genero.verifica_genero(nome_genero)

    def pega_nome_para_criar_genero(self, nome_genero):
        return self.__controlador_genero.inclui_genero(nome_genero)


    def atualiza_gen(self, genero):
        self.__controlador_genero.atualiza_genero(genero)

    def locar(self, loc):
        self.__controlador_pessoa.alterar_status(self.__cliente_logado, True)
        self.__controlador_locacao.incluir_locacao(loc)
