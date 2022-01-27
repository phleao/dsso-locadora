
from entidade.abstract_pessoa import AbstractPessoa

class Cliente(AbstractPessoa):
    def __init__(self, nome: str, data_de_nascimento: str, codigo: int, email: str, senha: str):
        self.__data_de_nascimento = data_de_nascimento
        self.__status = False
        super().__init__(nome, codigo, email, senha)

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: str):
        self.__data_de_nascimento = data_de_nascimento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status