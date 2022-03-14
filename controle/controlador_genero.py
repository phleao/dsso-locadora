from persistencia.genero_DAO import GeneroDAO
from entidade.genero import Genero

class ControladorGenero():

    def __init__(self, controlador_sistema):
        self.__generos = GeneroDAO()
        self.__controlador_sistema = controlador_sistema

    def verifica_genero(self, nome_genero):
        for genero in self.__generos.get_all():
            if genero.nome == nome_genero:
                return genero
        return False

    def inclui_genero(self, nome):
        novo_gen = Genero(nome)
        self.__generos.add(novo_gen)
        return novo_gen

    def atualiza_genero(self, genero):
        self.__generos.add(genero)