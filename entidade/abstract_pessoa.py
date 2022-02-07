from abc import ABC, abstractmethod


class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, email: str, senha: str):
        self.__email = email
        self.__senha = senha
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

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
