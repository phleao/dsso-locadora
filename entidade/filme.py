from cmath import sin


class Filme:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, titulo: str, codigo: int, sinopse: str, faixa_etaria: int, genero: str, link_acesso: str):
    self.__titulo = titulo
    self.__codigo = codigo
    self.__sinopse = sinopse
    self.__faixa_etaria = faixa_etaria
    self.__genero = genero
    self.__link_acesso = link_acesso
    self.__avaliacoes = []

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