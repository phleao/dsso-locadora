from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, codigo: int, email: str, senha: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__email = email
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha
