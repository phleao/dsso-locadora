class Genero:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__filmes = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def adiciona_filme(self, filme):
        self.__filmes.append(filme)