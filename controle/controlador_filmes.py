
from limite.tela_filme import TelaFilme
from entidade.filme import Filme


class ControladorFilmes():

    def __init__(self, controlador_sistema):
        self.__filmes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_filme = TelaFilme()

    def pega_filme_por_codigo(self, codigo: int):
        for filme in self.__filmes:
            if(filme.codigo == codigo):
                return filme
        return None

    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        filme = Filme(dados_filme["titulo"], (len(self.__filmes) + 1), dados_filme['sinopse'], dados_filme['faixa_etaria'], dados_filme['genero'], dados_filme['link_acesso'])
        self.__filmes.append(filme)

    def alterar_filme(self):
        self.lista_filme()
        codigo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_codigo(codigo_filme)

        if(filme is not None):
            novos_dados_filme = self.__tela_filme.pega_dados_filme()
            filme.titulo = novos_dados_filme["titulo"]
            filme.sinopse = novos_dados_filme["sinopse"]
            filme.genero.nome = novos_dados_filme["genero"]
            filme.faixa_etaria = novos_dados_filme["faixa_etaria"]
            filme.link_acesso = novos_dados_filme["link_acesso"]
            self.lista_filme()
        else:
            self.__tela_filme.mostra_mensagem("ATENCAO: Filme não existente")

    def lista_filme(self):
        if len(self.__filmes) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
        else:
            for filme in self.__filmes:
                self.__tela_filme.mostra_filme({"titulo": filme.titulo, "codigo": filme.codigo})

    def lista_filme_catalogo(self):
        if len(self.__filmes) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
        else:
            for filme in self.__filmes:
                self.__tela_filme.mostra_filme_catalogo({"titulo": filme.titulo, "sinopse": filme.sinopse, "genero": filme.genero.nome,
                                                         "nota": filme.nota(), "comentarios": filme.comentarios()})
            
    def excluir_filme(self):
        self.lista_filme()
        codigo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_codigo(codigo_filme)

        if(filme is not None):
            self.__filmes.remove(filme)
            self.lista_filme()
        else:
            self.__tela_filme.mostra_mensagem("ATENCAO: Filme não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela_funcionario()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_filme, 2: self.alterar_filme, 3: self.lista_filme_catalogo, 4: self.excluir_filme, 0: self.retornar}

        continua = True
        while continua:
            try:
                lista_opcoes[self.__tela_filme.tela_opcoes()]()
            except KeyError:
                self.__tela_filme.mostra_mensagem("Opção inválida")
                

            

