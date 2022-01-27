from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from limite.tela_pessoa import TelaPessoa

class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_pessoa.pega_dados_funcionario()
        funcionarios = Funcionario(dados_funcionario["nome"], dados_funcionario["codigo"], dados_funcionario['email'], dados_funcionario['senha'], dados_funcionario['cpf'])
        self.__funcionarios.append(funcionarios)
    
    def incluir_cliente(self):
        dados_cliente = self.__tela_pessoa.pega_dados_cliente()
        clientes = Cliente(dados_cliente["nome"], dados_cliente["codigo"], dados_cliente['email'], dados_cliente['senha'], dados_cliente['data_nascimento'])
        self.__clientes.append(clientes)