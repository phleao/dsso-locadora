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


    def incluir_funcionario(self):
        dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
        funcionarios = Funcionario(dados_funcionario["nome"], dados_funcionario['cpf'], dados_funcionario['email'], dados_funcionario['senha'])
        self.__funcionarios.append(funcionarios)
    
    def incluir_cliente(self):
        dados_cliente = self.__tela_pessoa.pega_dados_cliente()
        clientes = Cliente(dados_cliente["nome"], dados_cliente['idade'], dados_cliente['email'], dados_cliente['senha'], )
        self.__clientes.append(clientes)