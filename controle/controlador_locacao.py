from entidade.avaliacao import Avaliacao
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
    if self.__controlador_sistema.controlador_filmes.lista_filme() == False:
      return False
    dados_locacao = self.__tela_locacao.pega_dados_locacao()
    filme = self.__controlador_sistema.controlador_filmes.pega_filme_por_codigo(dados_locacao["codigo"])
    if filme == None:
      self.__tela_locacao.mostra_mensagem("Não existe filme com esse código!")
      return False

    if self.verifica_faixa_etaria(filme) == True:
      locacao = Locacao(self.__controlador_sistema.cliente_logado, (len(self.__locacoes) + 1), filme)
      self.__locacoes.append(locacao)
      return True
    else:
      return False

  def verifica_faixa_etaria(self, filme):
    if filme.faixa_etaria >= self.__controlador_sistema.cliente_logado.idade:
      self.__tela_locacao.mostra_mensagem("Você não tem idade para alugar esse filme!")
      return False
    else:
      return True

  def lista_locacao(self):
    for e in self.__locacoes:
      self.__tela_locacao.mostra_locacao({"codigo": e.codigo,
                                                "titulo_filme": e.filme.titulo,
                                                "email": e.cliente.email,
                                                "data_aluguel": e.data_aluguel,
                                                "status": e.status})

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

  def incluir_avaliacao(self):
    dados_avaliacao = self.__tela_locacao.pega_avaliacao()
    locacao = self.ver_locacao_atual_cliente()
    filme = locacao.filme
    cliente = locacao.cliente
    avaliacao = Avaliacao(dados_avaliacao["nota"], dados_avaliacao["comentario"], cliente)
    filme.avaliacoes.append(avaliacao)

  def lista_historico_locacao(self):
    for locacao in self.__locacoes:
      locacoes_cliente = 0
      if (locacao.cliente == self.__controlador_sistema.cliente_logado):
        locacoes_cliente += 1
        self.__tela_locacao.mostra_historico_locacao(locacao)

      if locacoes_cliente == 0:
        self.__tela_locacao.mostra_mensagem("Você nunca alugou um filme :(")
  
