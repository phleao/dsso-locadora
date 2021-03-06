
from limite.tela_locacao import TelaLocacao
from entidade.locacao import Locacao
from persistencia.locacao_DAO import LocacaoDAO

class ControladorLocacao():

  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__locacao_dao = LocacaoDAO()
    self.__tela_locacao = TelaLocacao()

  def pega_locacao_por_codigo(self, codigo: int):
    for locacao in self.__locacao_dao.get_all():
      if(locacao.codigo == codigo):
        return locacao
    return None

  def incluir_locacao(self, titulo):
    if self.__controlador_sistema.controlador_filmes.lista_filme() == False:
      return False

    filme = self.__controlador_sistema.controlador_filmes.pega_filme_por_titulo(titulo)

    if self.verifica_faixa_etaria(filme) == True:
      locacao = Locacao(self.__controlador_sistema.cliente_logado, (len(self.__locacao_dao.get_all()) + 1), filme)
      self.__locacao_dao.add(locacao)
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
    locs = []
    for e in self.__locacao_dao.get_all():
      locs.append({"codigo": e.codigo,
                                                "titulo_filme": e.filme.titulo,
                                                "email": e.cliente.email,
                                                "data_aluguel": e.data_aluguel,
                                                "status": e.status})
      
    if len(self.__locacao_dao.get_all()) == 0:
      self.__tela_locacao.mostra_mensagem("Ainda não foram feitas locações")
      return None

    self.__tela_locacao.mostra_locacao(locs)

  def excluir_locacao(self):
    self.lista_locacao()
    codigo_locacao = self.__tela_locacao.seleciona_locacao()
    locacao = self.pega_locacao_por_codigo(int(codigo_locacao))

    if (locacao is not None):
      self.__locacao_dao.remove(locacao.codigo)
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
    for locacao in self.__locacao_dao.get_all():
      if self.__controlador_sistema.cliente_logado.email == locacao.cliente.email and locacao.status == True:
        loc = {"titulo_filme": locacao.filme.titulo, "link_acesso": locacao.filme.link_acesso, "data_aluguel": locacao.data_aluguel}
        evento = self.__tela_locacao.mostra_locacao_atual(loc)
        break
    if evento == "Finalizar Locacao":
      self.__controlador_sistema.finalizar_locacao()
    else:
      return None

  def incluir_avaliacao(self):
    nota = self.__tela_locacao.pega_avaliacao()

    locacao = self.pega_locacao_cliente()
    filme = locacao.filme
    cliente = locacao.cliente
    dados_avaliacao = {"nota":nota, "cliente":cliente, "comentario": ''}
    filme.nova_avaliacao(dados_avaliacao)
    return filme

  def alterar_locacao(self, locacao):
    locacao.status = False
    self.__locacao_dao.add(locacao)

  def lista_historico_locacao(self):
    locs = []
    for locacao in self.__locacao_dao.get_all():
      locacoes_cliente = 0
      if (locacao.cliente.email == self.__controlador_sistema.cliente_logado.email):
        locacoes_cliente += 1
        dados_locacao = {"data_aluguel": locacao.data_aluguel, "titulo_filme": locacao.filme.titulo}
        locs.append(dados_locacao)
    self.__tela_locacao.mostra_historico_locacao(locs)

  def atualizar_locacao(self, loc):
    self.__locacao_dao.add(loc)

  def pega_locacao_cliente(self):
    for locacao in self.__locacao_dao.get_all():
      if self.__controlador_sistema.cliente_logado.email == locacao.cliente.email and locacao.status == True:
        return locacao