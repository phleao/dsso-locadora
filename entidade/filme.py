from cmath import sin


class Filme:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, titulo: str, codigo: int, sinopse: str, faixa_etaria: int, idioma: str, link_acesso: str):
    self.__titulo = titulo
    self.__codigo = codigo
    self.__sinopse = sinopse
    self.__faixa_etaria = faixa_etaria
    self.__idioma = idioma
    self.__link_acesso = link_acesso

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
  def idioma(self):
    return self.__idioma

  @idioma.setter
  def idioma(self, idioma):
    self.__idioma = idioma

  @property
  def link_acesso(self):
    return self.__link_acesso

  @link_acesso.setter
  def link_acesso(self, link_acesso):
    self.__link_acesso = link_acesso