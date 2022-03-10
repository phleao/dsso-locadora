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

    def pega_filme_por_codigo(self, codigo: int):
        for filme in self.__filme_dao.get_all():
            if(filme.codigo == codigo):
                return filme
            else:
                return None

    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        ja_existe = False
        for filme in self.__filme_dao.get_all():
            if filme.titulo == dados_filme["titulo"]:
                ja_existe = True
        if not ja_existe:
            gen = self.__controlador_sistema.verifica_se_ja_tem_genero(dados_filme['genero'])
            if gen == False:
                genero = self.__controlador_sistema.pega_nome_para_criar_genero(dados_filme['genero'])
                filme = Filme(dados_filme["titulo"], (len(self.__filme_dao.get_all()) + 1), dados_filme['sinopse'],
                              dados_filme['faixa_etaria'], genero, dados_filme['link_acesso'])

            else:
                filme = Filme(dados_filme["titulo"], (len(self.__filme_dao.get_all()) + 1), dados_filme['sinopse'],
                              dados_filme['faixa_etaria'], gen, dados_filme['link_acesso'])
            self.__filme_dao.add(filme)

        else:
            self.__tela_filme.mostra_mensagem("Um Filme com esse titulo já existe!")

    def alterar_filme(self):
        if self.lista_filme() == False:
            return False
        codigo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_codigo(codigo_filme)

        if(filme is not None):
            novos_dados_filme = self.__tela_filme.pega_dados_filme()
            filme.titulo = novos_dados_filme["titulo"]
            filme.sinopse = novos_dados_filme["sinopse"]
            gen = self.__controlador_sistema.verifica_se_ja_tem_genero(novos_dados_filme["genero"])
            if not gen:
                genero = self.__controlador_sistema.pega_nome_para_criar_genero(novos_dados_filme["genero"])
                filme.genero = genero
            else:
                filme.genero = gen
            filme.faixa_etaria = novos_dados_filme["faixa_etaria"]
            filme.link_acesso = novos_dados_filme["link_acesso"]
            self.__filme_dao.add(filme)
            self.lista_filme()
        else:
            self.__tela_filme.mostra_mensagem("ATENCAO: Filme não existente")

    def lista_filme(self):
        if len(self.__filme_dao.get_all()) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
            return False
        else:
            for filme in self.__filme_dao.get_all():
                self.__tela_filme.mostra_filme({"titulo": filme.titulo, "codigo": filme.codigo})

    def lista_filme_catalogo(self):
        if len(self.__filme_dao.get_all()) == 0:
            self.__tela_filme.mostra_mensagem("Nenhum filme foi cadastrado ainda :(\n")
        else:
            for filme in self.__filme_dao.get_all():
                self.__tela_filme.mostra_filme_catalogo({"titulo": filme.titulo, "sinopse": filme.sinopse, "genero": filme.genero.nome, "faixa_etaria": filme.faixa_etaria,
                                                         "nota": filme.nota(), "comentarios": filme.comentarios()})
            
    def excluir_filme(self):
        if self.__filme_dao.get_all() == False:
            return False
        self.lista_filme()
        codigo_filme = self.__tela_filme.seleciona_filme()
        filme = self.pega_filme_por_codigo(codigo_filme)

        if(filme is not None):
            self.__filme_dao.remove(filme.codigo)
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

        notas.sort(reverse=True)
        for i in notas:
            for j in self.__filme_dao.get_all():
                if i == j.nota():
                    recomendacoes.append(j)
        if len(recomendacoes) < 3 and len(recomendacoes) != 0:
            for l in range(len(recomendacoes)):
                self.__tela_filme.mostra_recomendacoes(recomendacoes[l])
        elif len(recomendacoes) == 0:
            self.__tela_filme.mostra_mensagem("Ainda não existem filmes avaliados!\n")
        elif len(recomendacoes) >= 3:
            for l in range(3):
                self.__tela_filme.mostra_recomendacoes(recomendacoes[l])
        
    def retornar(self):
        self.__controlador_sistema.abre_tela_funcionario()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_filme, 2: self.alterar_filme, 3: self.lista_filme_catalogo, 4: self.excluir_filme, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_filme.tela_opcoes()]()
                
    def atualizar_filme(self, filme):
        self.__filme_dao.add(filme)
            

