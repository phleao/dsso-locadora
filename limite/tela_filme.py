class TelaFilme():
    def tela_opcoes(self):
        # fazer aqui tratamento caso a entrada seja diferente do esperado
        print(" --------- FILME ---------")
        print("Escolha a opcao")
        print("1 - Incluir Filme")
        print("2 - Alterar Filme")
        print("3 - Listar Filme")
        print("4 - Excluir Filme")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("\n Escolha a opcao: "))
                break
            except ValueError:
                print("Digite um número válido")
        return opcao

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
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

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado, tbm alterar modo de mostrar
    def mostra_filme(self, dados_filme):
        print("CODIGO: ", dados_filme["codigo"], "    TITULO DO FILME: ", dados_filme["titulo"])
        print("\n")

    def mostra_filme_catalogo(self, dados_filme):
        print("TITULO DO FILME: ", dados_filme["titulo"])
        print("SINOPSE: ", dados_filme["sinopse"])
        print("GÊNERO: ", dados_filme["genero"])
        if dados_filme["nota"] != None:
            print("NOTA: ", dados_filme["nota"])
            print("COMENTÁRIOS: \n", end='')
            for comentario in dados_filme["comentarios"]:
                print(comentario)
        print("\n")

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_filme(self):
        codigo = int(input("Código do filme que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
