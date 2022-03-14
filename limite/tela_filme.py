
import PySimpleGUI as sg

class TelaFilme():

    def tela_opcoes_nova(self, filmes):

        if len(filmes) > 0:
            items = []
            for filme in filmes:
                items.append([filme["titulo"], filme["sinopse"], filme["genero"], filme["faixa_etaria"], filme["nota"]])

            headings = [' Título','Sinopse', 'Gênero', 'Faixa etária', 'Nota' ]

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Button(button_text = "Incluir", size=(15, 1)), sg.Submit(button_text = "Editar", size=(15, 1)), sg.Submit(button_text = "Excluir", size=(15, 1)), sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light grey")]]

            window = sg.Window('Catalogo de Filmes', layout, element_justification='center')
            event, values = window.read()
            window.close()
            if event != "Incluir" and event != "Voltar" and event != sg.WIN_CLOSED:
                filme = items[values["-TABLE-"][0]]
                return event, filme[0]
            else:
                return event, True

        else:
            layout = [[sg.Text("Sem filmes no cátalogo")],
                     [sg.Button(button_text="Incluir"), sg.Cancel(button_text="Voltar")]]

            window = sg.Window('Catalogo de Filmes', layout, element_justification='center')
            event, values = window.read()
            window.close()
            return event, values

    def pega_dados_filme_alterar(self, filme):
        layout = [
            [sg.Text('Preencha as informações necessárias')],
            [sg.Text('Titulo', size=(15, 1)), sg.InputText(filme["titulo"])],
            [sg.Text('Sinopse', size=(15, 1)), sg.InputText(filme["sinopse"])],
            [sg.Text('Gênero', size=(15, 1)), sg.InputText(filme["genero"])],  # colocar bolinhas em vez de texto aparecendo
            [sg.Text('Faixa Etaria', size=(15, 1)), sg.InputText(filme["faixa_etaria"])],
            [sg.Text('Link de acesso', size=(15, 1)), sg.InputText(filme["link_acesso"])],
            [sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light grey"), sg.Submit(button_text="Alterar",  size=(15, 1))]
        ]

        window = sg.Window('Alterar Filme', layout, element_justification='center')
        event, values = window.read()
        window.close()
        if event == sg.WIN_CLOSED or event == "Voltar":
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
            [sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light grey"), sg.Submit(button_text="Adicionar", size=(15, 1))]
        ]

        window = sg.Window('Novo Filme', layout, element_justification='center')
        event, values = window.read()
        window.close()
        if event == sg.WIN_CLOSED or event == "Voltar":
            return None
        return {"titulo": values[0], "sinopse": values[1], "genero": values[2], "faixa_etaria": int(values[3]), "link_acesso" : values[4]}

    def mostra_recomendacoes(self, recom):
        layout = [
                    [sg.Text('Esses são os nossos melhores filmes')],    
                    ([sg.Text(dic["titulo"]), sg.Text(dic["nota"])] for dic in recom),
                    [sg.Cancel(button_text="Voltar", button_color="Light Grey", size=(15,1))]]
        
        window = sg.Window('Melhores filmes', layout, element_justification='center')
        event, values = window.read()
        window.close()

    def mostra_filme(self, dados_filme):
        print("CODIGO: ", dados_filme["codigo"], "    TITULO DO FILME: ", dados_filme["titulo"])
        print("\n")

    def mostra_filme_catalogo(self, filmes):
        if len(filmes) > 0:
            items = []
            for filme in filmes:
                items.append([filme["titulo"], filme["sinopse"], filme["genero"], filme["faixa_etaria"], filme["nota"]])

            headings = [' Título','sinopse', 'Gênero', 'Faixa etária', 'nota' ]

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Submit(button_text = "Alugar", size=(20,1)), sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light grey")]]

            window = sg.Window('Catalogo de Filmes', layout, element_justification='center')
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

            window = sg.Window('Catalogo de Filmes', layout)
            event, values = window.read()
            window.close()
            return event, values

    def seleciona_filme(self):
        codigo = int(input("Código do filme que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):

        sg.Popup("", msg + "\n")
