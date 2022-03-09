from controle.abstract_DAO import DAO
from entidade.filme import Filme

class FilmeDAO(DAO):
    def __init__(self):
        super ().__init__('filmes.pkl')

    def add(self, filme: Filme):
        if (filme is not None) and isinstance(filme, Filme):
            super().add(filme.codigo, filme)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)