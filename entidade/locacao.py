from datetime import date
from entidade.cliente import Cliente
from entidade.filme import Filme

class Locacao():
    
    def __init__(self, cliente: Cliente, codigo: int, filme: Filme, data_final: str):
        data_atual = date.today()
        self.__filme = filme
        self.__cliente = cliente
        self.__codigo = codigo
        self.__status = True
        self.__data_aluguel = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
        self.__data_final = data_final

    @property
    def cliente(self):
        return self.__cliente

    @property
    def filme(self):
        return self.__filme

    @property
    def codigo(self):
        return self.__codigo

    @property
    def data_aluguel(self):
        return self.__data_aluguel

    @property
    def data_final(self):
        return self.__data_final


    @data_final.setter
    def data_final(self, data_final: str):
        self.__data_final = data_final


    @property
    def status(self):
        return self.__status


    @status.setter
    def status(self, status: bool):
        self.__status = status