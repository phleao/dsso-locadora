import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaLocacao():

  def mostra_locacao_antigo(self, dados_locacao):
    status = dados_locacao["status"]
    if status == False:
        status = "Não está ativa"
    else:
        status = "Está ativa"
    print(dados_locacao["codigo"], "  ", dados_locacao["titulo_filme"], "  ", dados_locacao["email"], "  ", dados_locacao["data_aluguel"], "   ", status)
    print("\n")

  def mostra_locacao(self, locs):
   
    layout = [   
          [sg.Text('Filmes')],    
          ([sg.Text(loc["codigo"]), sg.Text(loc["titulo_filme"]), sg.Text(loc["email"]), sg.Text(loc["data_aluguel"]), sg.Text(loc["status"])] for loc in locs),
          [sg.Cancel(button_text = "Voltar")]]
    window = sg.Window('Filmes', layout)
    event, values = window.read()
    window.close()

  def seleciona_locacao(self):
    codigo = input("Código da locação que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):

      sg.Popup("", msg + "\n")

  def pega_avaliacao(self):
      # "Filme devolvido com sucesso, agora é hora de avaliar o filme, que tal?"
      layout = [
          [sg.Text('')],
          [sg.Text("Filme devolvido com sucesso, agora é hora de avaliar o filme, que tal?\n\n"
                   "De uma nota de 0 a 5!")],
          [sg.Slider(range=(0, 5), orientation='h', default_value=5, size=(45, 30))],
          [sg.Submit()]]
      window = sg.Window('Locação atual', layout)
      event, values = window.read()
      window.close()
      return values[0]

  def mostra_historico_locacao_antigo(self, locacao):
    print("FILME: ", locacao["titulo_filme"], "no dia: ", locacao["data_aluguel"])

  def mostra_historico_locacao(self, locacao):
    if len(locacao) > 0:
            items = []
            for loc in locacao:
                items.append([loc["titulo_filme"], loc["data_aluguel"]])

            headings = [' Filme','Data']

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Cancel(button_text="Voltar")]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            
    else:
        layout = [[sg.Text("\nVocê nunca alugou um filme :(\n")],
                  [sg.Cancel(button_text="Voltar")]]

        window = sg.Window('tabela de teste', layout)
        event, values = window.read()
        window.close()
        return event, values

  def mostra_locacao_atual(self, locacao):
    layout = [   
          [sg.Text('Locação')],
          [sg.Text(locacao["titulo_filme"]), sg.Text(locacao["sinopse"]), sg.Text(locacao["data_aluguel"])] ,
          [sg.Button(button_text="Finalizar Locacao"), sg.Button(button_text = "Voltar")]]
    window = sg.Window('Locação atual', layout)

    event, values = window.read()
    window.close()
    return event
