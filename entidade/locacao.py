class Locacao():

    def __init__(self, cliente: Cliente, codigo: int, filme: Filme, data_aluguel: str, data_fim: str):
        self.__filme = filme
        self.__cliente = cliente
        self.__codigo = codigo
        self.__status = True
        self.__data_aluguel = data_aluguel
        self.__data_fim = data_fim

    @property
    def data_aluguel(self):
        return self.data_aluguel

    @data_aluguel.setter
    def data_aluguel(self, data_aluguel: str):
        self.__data_aluguel = data_aluguel


    @property
    def data_fim(self):
        return self.data_fim


    @data_fim.setter
    def data_fim(self, data_fim: str):
        self.__data_fim = data_fim


    @property
    def status(self):
        return self.status


    @status.setter
    def status(self, status: boolean):
        self.__status = status