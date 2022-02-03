
from entidade.cliente import Cliente


class Avaliacao():
    def __init__(self, nota: int, comentario: str, cliente: Cliente):
        self.__nota = nota
        self.__comentario = comentario
        self.__cliente = cliente

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota: str):
        self.__nota = nota

    @property
    def comentario(self):
        return self.__comentario

    @comentario.setter
    def comentario(self, comentario: str):
        self.__comentario = comentario

    @property
    def cliente(self):
        return self.__cliente
