import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaLocacao():

  def mostra_locacao_antigo(self, locs):
   
    layout = [   
          [sg.Text('Filmes')],    
          ([sg.Text(loc["codigo"]), sg.Text(loc["titulo_filme"]), sg.Text(loc["email"]), sg.Text(loc["data_aluguel"]), sg.Text(loc["status"])] for loc in locs),
          [sg.Cancel(button_text = "Voltar")]]
    window = sg.Window('Filmes', layout)
    event, values = window.read()
    window.close()

  def mostra_locacao(self, locacao):
    if len(locacao) > 0:
            items = []
            for loc in locacao:
                items.append([loc["codigo"], loc["titulo_filme"], loc["email"], loc["data_aluguel"], loc["status"]])

            headings = [' Codigo','Filme', 'Cliente', 'Data', 'Status']

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Cancel(button_text="Voltar", button_color="Light Grey", size=(20,1))]]

            window = sg.Window('Locações', layout, element_justification='center')
            event, values = window.read()
            window.close()
            
    else:
        layout = [[sg.Text("\nNão houve nenhuma locação ainda\n")],
                  [sg.Cancel(button_text="Voltar")]]

        window = sg.Window('Locações', layout, element_justification='center')
        event, values = window.read()
        window.close()
        return event, values

  def mostra_mensagem(self, msg):

      sg.Popup("", msg + "\n")

  def pega_avaliacao(self):
      # "Filme devolvido com sucesso, agora é hora de avaliar o filme, que tal?"
      layout = [
          [sg.Text('')],
          [sg.Text("Filme devolvido com sucesso, agora é hora de avaliar o filme, que tal?\n\n"
                   "De uma nota de 0 a 5!")],
          [sg.Slider(range=(0, 5), orientation='h', default_value=5, size=(45, 30))],
          [sg.Submit(button_text="Enviar Avaliação")]]
      window = sg.Window('Avaliação do filme', layout, element_justification='center')
      event, values = window.read()
      window.close()
      return values[0]

  def mostra_historico_locacao(self, locacao):
    if len(locacao) > 0:
            items = []
            for loc in locacao:
                items.append([loc["titulo_filme"], loc["data_aluguel"]])

            headings = [' Filme','Data']

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Cancel(button_text="Voltar", button_color="Light Grey", size=(15,1))]]

            window = sg.Window('Histórico de Locações', layout, element_justification='center')
            event, values = window.read()
            window.close()
            
    else:
        layout = [[sg.Text("\nVocê nunca alugou um filme :(\n")],
                  [sg.Cancel(button_text="Voltar", button_color="Light Grey", size=(15,1))]]

        window = sg.Window('Histórico de Locações', layout, element_justification='center')
        event, values = window.read()
        window.close()
        return event, values

  def mostra_locacao_atual(self, locacao):
    layout = [   
          [sg.Text('Informações da locação atual')],
          [sg.Text("Filme locado: ", size=(15,1)), sg.Text(locacao["titulo_filme"])],
          [sg.Text("Link: ", size=(15,1)), sg.Text(locacao["link_acesso"])],
          [sg.Text("Data de aluguel: ", size=(15,1)), sg.Text(locacao["data_aluguel"])],
          [sg.Button(button_text = "Voltar", button_color="Light Grey", size=(15,1)), sg.Button(button_text="Finalizar Locacao", size=(20,1))]]
    window = sg.Window('Locaçõa Atual', layout, element_justification='left')

    event, values = window.read()
    window.close()
    return event
