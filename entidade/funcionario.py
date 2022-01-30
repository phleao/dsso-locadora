from entidade.abstract_pessoa import AbstractPessoa

class Funcionario(AbstractPessoa):
    def __init__(self, nome: str, cpf: str, email: str, senha: str):
        self.__cpf = cpf
        super().__init__(nome, email, senha)

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

