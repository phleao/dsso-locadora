from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from limite.tela_pessoa import TelaPessoa

class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def clientes(self):
        return self.__clientes

    def verificar_se_email_existe(self, email):
        for funcionario in self.__funcionarios:
            if funcionario.email == email:
                return False
        for cliente in self.__clientes:
            if cliente.email == email:
                return False
        return True

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
        if self.verificar_se_email_existe(dados_funcionario["email"]) == True:
            funcionarios = Funcionario(dados_funcionario["nome"], dados_funcionario['cpf'], dados_funcionario['email'], dados_funcionario['senha'])
            self.__funcionarios.append(funcionarios)
        else:
            self.__tela_pessoa.mostra_mensagem("Esse email já está sendo usado")
    
    def incluir_cliente(self):
        dados_cliente = self.__tela_pessoa.pega_dados_cliente()
        if self.verificar_se_email_existe(dados_cliente["email"]) == True:
            clientes = Cliente(dados_cliente["nome"], dados_cliente['idade'], dados_cliente['email'], dados_cliente['senha'], )
            self.__clientes.append(clientes)
        else:
            self.__tela_pessoa.mostra_mensagem("Esse email já está sendo usado")

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_pessoa.mostra_clientes({"nome": cliente.nome, "email": cliente.email, "status": cliente.status, "idade": cliente.idade})
        if len(self.__clientes) == 0:
            self.__tela_pessoa.mostra_mensagem("Ainda não existem clientes cadastrados!")