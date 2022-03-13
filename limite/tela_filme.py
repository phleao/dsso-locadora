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

    def tela_opcoes_nova(self, filmes):

        if len(filmes) > 0:
            items = []
            for filme in filmes:
                items.append([filme["titulo"], filme["sinopse"], filme["genero"], filme["faixa_etaria"], filme["nota"]])

            headings = [' Título','sinopse', 'Gênero', 'Faixa etária', 'nota' ]

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Button(button_text = "Incluir"), sg.Submit(button_text = "Editar"), sg.Submit(button_text = "Excluir"), sg.Cancel(button_text="Voltar")]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            if event != "Incluir" and event != "Voltar" and event != sg.WIN_CLOSED:
                filme = items[values["-TABLE-"][0]]
                return event, filme[0]
            else:
                return event, True

        else:
            layout = [[sg.Text("Sem filmes no cátalogo")],
                     [sg.Button(button_text="Incluir"), sg.Cancel()]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            return event, values

    def pega_dados_filme_antigo(self):
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

    def pega_dados_filme_alterar(self, filme):
        layout = [
            [sg.Text('Preencha as informações necessárias')],
            [sg.Text('Titulo', size=(15, 1)), sg.InputText(filme["titulo"])],
            [sg.Text('Sinopse', size=(15, 1)), sg.InputText(filme["sinopse"])],
            [sg.Text('Gênero', size=(15, 1)), sg.InputText(filme["genero"])],  # colocar bolinhas em vez de texto aparecendo
            [sg.Text('Faixa Etaria', size=(15, 1)), sg.InputText(filme["faixa_etaria"])],
            [sg.Text('Link de acesso', size=(15, 1)), sg.InputText(filme["link_acesso"])],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Cadastro de cliente', layout)
        event, values = window.read()
        window.close()
        if event == sg.WIN_CLOSED or event == "Cancel":
            return None
        return {"titulo": values[0], "sinopse": values[1], "genero": values[2], "faixa_etaria": int(values[3]), "link_acesso" : values[4]}

    def pega_dados_filme(self):
        layout = [
            [sg.Text('Preencha as informações necessárias')],
            [sg.Text('Titulo', size=(15, 1)), sg.InputText()],
            [sg.Text('Sinopse', size=(15, 1)), sg.InputText()],
            [sg.Text('Gênero', size=(15, 1)), sg.InputText()],  # colocar bolinhas em vez de texto aparecendo
            [sg.Text('Faixa Etaria', size=(15, 1)), sg.InputText()],
            [sg.Text('Link de acesso', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Cadastro de cliente', layout)
        event, values = window.read()
        window.close()
        if event == sg.WIN_CLOSED or event == "Cancel":
            return None
        return {"titulo": values[0], "sinopse": values[1], "genero": values[2], "faixa_etaria": int(values[3]), "link_acesso" : values[4]}

    def mostra_recomendacoes_antigo(self, recomendacao):
        print("Titulo: ", recomendacao.titulo, "Nota: ", recomendacao.nota())

    def mostra_recomendacoes(self, recom):
        layout = [
                    [sg.Text('Top Filmes')],    
                    ([sg.Text(dic["titulo"]), sg.Text(dic["nota"])] for dic in recom),
                    [sg.Cancel(button_text = "Voltar")]]
        
        window = sg.Window('Filmes', layout)
        event, values = window.read()
        window.close()

    def mostra_filme(self, dados_filme):
        print("CODIGO: ", dados_filme["codigo"], "    TITULO DO FILME: ", dados_filme["titulo"])
        print("\n")

    def mostra_filme_catalogo_antigo(self, dados_filme):
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

    def mostra_filme_catalogo(self, filmes):
        if len(filmes) > 0:
            items = []
            for filme in filmes:
                items.append([filme["titulo"], filme["sinopse"], filme["genero"], filme["faixa_etaria"], filme["nota"]])

            headings = [' Título','sinopse', 'Gênero', 'Faixa etária', 'nota' ]

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Submit(button_text = "Alugar"), sg.Cancel(button_text="Voltar")]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            if event != "Voltar" and event != sg.WIN_CLOSED:
                filme = items[values["-TABLE-"][0]]
                return event, filme[0]
            else:
                return event, True

        else:
            layout = [[sg.Text("Sem filmes no cátalogo")],
                     [sg.Cancel(button_text="Voltar")]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            return event, values

    def seleciona_filme(self):
        codigo = int(input("Código do filme que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
        sg.Popup("", msg + "\n")
