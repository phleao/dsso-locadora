from entidade.genero import Genero
from entidade.avaliacao import Avaliacao

class Filme:
    # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
    def __init__(self, titulo: str, codigo: int, sinopse: str, faixa_etaria: int, genero: Genero, link_acesso: str):
        self.__titulo = titulo
        self.__codigo = codigo
        self.__sinopse = sinopse
        self.__faixa_etaria = faixa_etaria
        self.__genero = genero
        self.__link_acesso = link_acesso
        self.__avaliacoes = []

    def nota(self):
        if len(self.__avaliacoes) > 0:
            nota = 0
            for avaliacao in self.__avaliacoes:
                nota += avaliacao.nota
            media_nota = round((nota / len(self.__avaliacoes)), 1)
            return media_nota
        else:
            return None

    def nova_avaliacao(self, dados):
        self.__avaliacoes.append(Avaliacao(dados["nota"], dados["comentario"], dados["cliente"]))

    def comentarios(self):
        coment = []
        if len(self.__avaliacoes) > 0:
            for avaliacao in self.__avaliacoes:
                coment.append((avaliacao.cliente.nome + " - " + avaliacao.comentario))
            return coment
        else:
            return None

    @property
    def avaliacoes(self):
        return self.__avaliacoes

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def sinopse(self):
        return self.__sinopse

    @sinopse.setter
    def sinopse(self, sinopse):
        self.__sinopse = sinopse

    @property
    def faixa_etaria(self):
        return self.__faixa_etaria

    @faixa_etaria.setter
    def faixa_etaria(self, faixa_etaria):
        self.__faixa_etaria = faixa_etaria

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def link_acesso(self):
        return self.__link_acesso

    @link_acesso.setter
    def link_acesso(self, link_acesso):
        self.__link_acesso = link_acesso
