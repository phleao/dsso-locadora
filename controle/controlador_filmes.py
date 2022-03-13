from entidade import filme
from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from controle.filme_DAO import FilmeDAO

class ControladorFilmes():

    def __init__(self, controlador_sistema):
        self.__filme_dao = FilmeDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_filme = TelaFilme()

    @property
    def filmes(self):
        return self.__filme_dao.get_all()


    def pega_filme_por_titulo(self, titulo):
        for filme in self.__filme_dao.get_all():
            if(filme.titulo == titulo):
                return filme
        return None

    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        if dados_filme == None:
            return None
        ja_existe = False
        for filme in self.__filme_dao.get_all():
            if filme.titulo == dados_filme["titulo"]:
                ja_existe = True
        if not ja_existe:
            gen = self.__controlador_sistema.verifica_se_ja_tem_genero(dados_filme['genero'])
            if gen == False:
                genero = self.__controlador_sistema.pega_nome_para_criar_genero(dados_filme['genero'])
                filme = Filme(dados_filme["titulo"], (len(self.__filme_dao.get_all()) + 1), dados_filme['sinopse'],
                              dados_filme['faixa_etaria'], genero.nome, dados_filme['link_acesso'])
                genero.adiciona_filme(filme)
                self.__controlador_sistema.atualiza_gen(genero)
            else:
                filme = Filme(dados_filme["titulo"], (len(self.__filme_dao.get_all()) + 1), dados_filme['sinopse'],
                              dados_filme['faixa_etaria'], gen.nome, dados_filme['link_acesso'])
                gen.adiciona_filme(filme)
                self.__controlador_sistema.atualiza_gen(gen)
            self.__filme_dao.add(filme)

        else:
            self.__tela_filme.mostra_mensagem("Um Filme com esse titulo já existe!")

    def alterar_filme(self, titulo):
        if self.lista_filme() == False:
            return False

        filme = self.pega_filme_por_titulo(titulo)

        if(filme is not None):
            novos_dados_filme = self.__tela_filme.pega_dados_filme_alterar({"titulo": filme.titulo, "sinopse": filme.sinopse, "genero": filme.genero, "faixa_etaria": filme.faixa_etaria,
                                                         "link_acesso" : filme.link_acesso})
            if novos_dados_filme == None:
                return None
            filme.titulo = novos_dados_filme["titulo"]
            filme.sinopse = novos_dados_filme["sinopse"]
            if filme.genero != novos_dados_filme["genero"]:
                gen = self.__controlador_sistema.verifica_se_ja_tem_genero(novos_dados_filme["genero"])
                if not gen:
                    genero = self.__controlador_sistema.pega_nome_para_criar_genero(novos_dados_filme["genero"])
                    filme.genero = genero.nome
                    genero.adiciona_filme(filme)
                    self.__controlador_sistema.atualiza_gen(genero)
                else:
                    genero = self.__controlador_sistema.verifica_se_ja_tem_genero(filme.genero)
                    genero.remove_filme(filme)
                    self.__controlador_sistema.atualiza_gen(genero)
                    filme.genero = gen.nome
                    gen.adiciona_filme(filme)
                    self.__controlador_sistema.atualiza_gen(gen)

            filme.faixa_etaria = novos_dados_filme["faixa_etaria"]
            filme.link_acesso = novos_dados_filme["link_acesso"]
            self.__filme_dao.add(filme)
        else:
            self.__tela_filme.mostra_mensagem("ATENCAO: Filme não existente")

    def lista_filme(self):
        if len(self.__filme_dao.get_all()) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
            return False

    def lista_filme_catalogo(self):
        dados_filmes = []
        for filme in self.__filme_dao.get_all():
            dados_filmes.append({"titulo": filme.titulo, "sinopse": filme.sinopse, "genero": filme.genero, "faixa_etaria": filme.faixa_etaria,
                                                         "nota": filme.nota()})

        lista_opcoes = {"Alugar": self.__controlador_sistema.locar, "Cancel": self.retornar}
        while True:

            try:
                evento, titulo = self.__tela_filme.mostra_filme_catalogo(dados_filmes)
                break
            except IndexError:
                self.__tela_filme.mostra_mensagem("Para escolher essa opção, um item da tabela precisa ser escolhido!")
        
        if evento == "Alugar" :
            lista_opcoes[evento](titulo)
        else:
            pass
            
    def excluir_filme(self, titulo):
        if self.__filme_dao.get_all() == False:
            return False
        self.lista_filme()
        filme = self.pega_filme_por_titulo(titulo)

        if(filme is not None):
            self.__filme_dao.remove(filme.titulo)
            self.__tela_filme.mostra_mensagem("Filme removido com sucesso!")
        else:
            self.__tela_filme.mostra_mensagem("ATENCAO: Filme não existente")

    def lista_filmes_avaliados(self):
        if len(self.__filme_dao.get_all()) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
            return False
        notas = []
        recomendacoes = []
        for filme in self.__filme_dao.get_all():
            nota = filme.nota()
            if nota != None:
                notas.append(nota)

        recom = []

        notas.sort(reverse=True)
        for i in notas:
            for j in self.__filme_dao.get_all():
                if i == j.nota():
                    recomendacoes.append(j)
        if len(recomendacoes) < 3 and len(recomendacoes) != 0:
            for l in range(len(recomendacoes)):
                recom.append({"titulo":recomendacoes[l].titulo, "nota": recomendacoes[l].nota()})
            self.__tela_filme.mostra_recomendacoes(recom)
        elif len(recomendacoes) == 0:
            self.__tela_filme.mostra_mensagem("Ainda não existem filmes avaliados!\n")
        elif len(recomendacoes) >= 3:
            for l in range(3):
                recom.append({"titulo":recomendacoes[l].titulo, "nota": recomendacoes[l].nota()})
            self.__tela_filme.mostra_recomendacoes(recom)
        
    def retornar(self):
        self.__controlador_sistema.abre_tela_funcionario()

    def abre_tela(self):
        dados_filmes = []
        for filme in self.__filme_dao.get_all():
            dados_filmes.append({"titulo": filme.titulo, "sinopse": filme.sinopse, "genero": filme.genero, "faixa_etaria": filme.faixa_etaria,
                                                         "nota": filme.nota()})

        lista_opcoes = {"Incluir": self.incluir_filme, "Editar": self.alterar_filme, "Excluir": self.excluir_filme, "Cancel": self.retornar}
        evento, titulo = self.__tela_filme.tela_opcoes_nova(dados_filmes)

        if evento == "Incluir" or evento == "Cancel":
            lista_opcoes[evento]()
        else:
            lista_opcoes[evento](titulo)
   
    def atualizar_filme(self, filme):
        self.__filme_dao.add(filme)
            

