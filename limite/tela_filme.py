import PySimpleGUI as sg

class TelaFilme():
    def tela_opcoes(self):
        # fazer aqui tratamento caso a entrada seja diferente do esperado
        print(" --------- FILME ---------")
        while True:
            try:
                print("Escolha a opcao")
                print("1 - Incluir Filme")
                print("2 - Alterar Filme")
                print("3 - Listar Filme")
                print("4 - Excluir Filme")
                print("0 - Retornar")
                opcoes = [0,1,2,3,4]
                opcao = int(input("\n Escolha a opcao: "))
                if opcao not in opcoes:
                    raise ValueError
                break
            except ValueError:
                print("Digite um número válido\n")
        return opcao

    def pega_dados_filme(self):
        print("-------- DADOS FILME ----------")
        titulo = input("Titulo: ")
        sinopse = input("Sinopse: ")
        genero = input("Gênero: ")
        while True:
            try:
                faixa_etaria = int(input("Faixa Etaria: "))
                break
            except ValueError:
                print("Digite um número válido")

        link_acesso = input("Link de acesso:")
        return {"titulo": titulo, "sinopse": sinopse, "genero": genero, "faixa_etaria": faixa_etaria, "link_acesso": link_acesso}

    def mostra_recomendacoes_antigo(self, recomendacao):
        print("Titulo: ", recomendacao.titulo, "Nota: ", recomendacao.nota())

    def mostra_recomendacoes(self, recom):
        layout = [
                    [sg.Text('Top Filmes')],    
                    ([sg.Text(filme.titulo), sg.Text(filme.nota())] for filme in recom),
                    [sg.Cancel(button_text = "Voltar")]]
        
        window = sg.Window('Filmes', layout)
        event, values = window.read()
        window.close()

    def mostra_filme(self, dados_filme):
        print("CODIGO: ", dados_filme["codigo"], "    TITULO DO FILME: ", dados_filme["titulo"])
        print("\n")

    def mostra_filme_catalogo(self, dados_filme):
        print("TITULO DO FILME: ", dados_filme["titulo"])
        print("SINOPSE: ", dados_filme["sinopse"])
        print("GÊNERO: ", dados_filme["genero"])
        print("FAIXA ETÁRIA: ", dados_filme["faixa_etaria"])
        if dados_filme["nota"] != None:
            print("NOTA: ", dados_filme["nota"])
            print("COMENTÁRIOS: \n", end='')
            for comentario in dados_filme["comentarios"]:
                print(comentario)
        print("\n")

    def seleciona_filme(self):
        codigo = int(input("Código do filme que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
