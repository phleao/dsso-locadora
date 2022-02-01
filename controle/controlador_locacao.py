
from limite.tela_locacao import TelaLocacao
from entidade.locacao import Locacao


class ControladorLocacao():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__locacoes = []
    self.__tela_locacao = TelaLocacao()

  def pega_locacao_por_codigo(self, codigo: int):
    for locacao in self.__locacoes:
      if(locacao.codigo == codigo):
        return locacao
    return None

  def incluir_locacao(self):
    self.__controlador_sistema.controlador_filmes.lista_filme()
    dados_locacao = self.__tela_locacao.pega_dados_locacao()

    filme = self.__controlador_sistema.controlador_filmes.pega_filme_por_codigo(dados_locacao["codigo"])
    locacao = Locacao(self.__controlador_sistema.cliente_logado, (len(self.__locacoes) + 1), filme)
    self.__locacoes.append(locacao)


  def lista_locacao(self):
    for e in self.__locacoes:
      self.__tela_locacao.mostra_locacao({"codigo": e.codigo,
                                                "titulo_filme": e.filme.titulo,
                                                "codigo_filme": e.filme.codigo,
                                                "email": e.cliente.email})

  def excluir_locacao(self):
    self.lista_locacao()
    codigo_locacao = self.__tela_locacao.seleciona_locacao()
    locacao = self.pega_locacao_por_codigo(int(codigo_locacao))

    if (locacao is not None):
      self.__locacoes.remove(locacao)
      self.lista_locacao()
    else:
      self.__tela_locacao.mostra_mensagem("ATENCAO: Locação não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_locacao, 2: self.lista_locacao, 3: self.excluir_locacao, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_locacao.tela_opcoes()]()

  def ver_locacao_atual_cliente(self):
    for locacao in self.__locacoes:
      if self.__controlador_sistema.cliente_logado == locacao.cliente and locacao.status == True:
        return locacao
