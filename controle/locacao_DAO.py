from controle.abstract_DAO import DAO
from entidade.locacao import Locacao

class LocacaoDAO(DAO):
    def __init__(self):
        super ().__init__('locacoes.pkl')

    def add(self, locacao: Locacao):
        if (Locacao is not None) and isinstance(locacao, Locacao):
            super().add(locacao.codigo, locacao)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)