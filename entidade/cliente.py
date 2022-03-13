
from xmlrpc.client import boolean
from entidade.abstract_pessoa import AbstractPessoa

class Cliente(AbstractPessoa):
    def __init__(self, nome: str, idade: int, email: str, senha: str, status: boolean):
        super().__init__(nome, email, senha)
        self.__idade = int(idade)
        self.__status = status        

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: boolean):
        self.__status = status