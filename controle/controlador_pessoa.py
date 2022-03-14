from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from limite.tela_pessoa import TelaPessoa
from persistencia.cliente_DAO import ClienteDAO
from persistencia.funcionario_DAO import FuncionarioDAO

class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__funcionario_dao = FuncionarioDAO()
        self.__cliente_dao = ClienteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()

    @property
    def funcionarios(self):
        return self.__funcionario_dao.get_all()

    @property
    def clientes(self):
        return self.__cliente_dao.get_all()

    def verificar_se_email_existe(self, email):
        for funcionario in self.__funcionario_dao.get_all():
            if funcionario.email == email:
                return False
        for cliente in self.__cliente_dao.get_all():
            if cliente.email == email:
                return False
        return True

    def incluir_funcionario(self):
        while True:
            try:
                dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
                break
            except ValueError:
                self.__tela_pessoa.mostra_mensagem("O campo de CPF aceita apenas números")

        if dados_funcionario == None:
            return None

        if self.verificar_se_email_existe(dados_funcionario["email"]) == True:
            funcionarios = Funcionario(dados_funcionario["nome"], dados_funcionario['cpf'], dados_funcionario['email'], dados_funcionario['senha'])
            self.__funcionario_dao.add(funcionarios)
        else:
            self.__tela_pessoa.mostra_mensagem("Esse email já está sendo usado")
    
    def incluir_cliente(self):
        while True:
            try:
                dados_cliente = self.__tela_pessoa.pega_dados_cliente()
                break
            except ValueError:
                self.__tela_pessoa.mostra_mensagem("O campo de idade aceita apenas números")
        if dados_cliente == None:
            return None



        if self.verificar_se_email_existe(dados_cliente["email"]) == True:
            clientes = Cliente(dados_cliente["nome"], dados_cliente['idade'], dados_cliente['email'], dados_cliente['senha'], dados_cliente["status"])
            self.__cliente_dao.add(clientes)
        else:
            self.__tela_pessoa.mostra_mensagem("Esse email já está sendo usado")

    def lista_clientes(self):
        if len(self.__cliente_dao.get_all()) == 0:
            self.__tela_pessoa.mostra_mensagem("Ainda não existem clientes cadastrados!")
            return None
        dados_cliente = []
        for cliente in self.__cliente_dao.get_all():
            dados_cliente.append({"nome": cliente.nome, "email": cliente.email, "status": cliente.status, "idade": cliente.idade})
        evento = self.__tela_pessoa.mostra_clientes(dados_cliente)
        if evento == None:
            return None

    def pega_dados_log(self):
        return self.__tela_pessoa.pega_dados_login()

    def pega_senha_cad(self):
        return self.__tela_pessoa.pega_senha_de_cadastro()

    def alterar_status(self, cliente , status):
        cliente.status = status
        self.__cliente_dao.add(cliente)