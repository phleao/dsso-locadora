import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaLocacao():
  def tela_opcoes(self):
    print("-------- LOCAÇÕES ----------")
    while True:
      try:
          print("Escolha a opcao")
          print("1 - Fazer locação")
          print("2 - Listar locações")
          print("3 - Devolver locação")
          print("0 - Retornar")
          opcoes = [0,1,2,3]
          opcao = int(input("\n Escolha a opcao: "))
          if opcao not in opcoes:
              raise ValueError
          break
      except ValueError:
          print("Digite um número válido\n")
    return opcao

  def pega_dados_locacao(self):
    print("-------- DADOS LOCACAO ----------")
    while True:
      try:
        codigo = int(input("Codigo Filme: "))
        break
      except ValueError:
        print("Digite um código válido!")

    return {"codigo": codigo}

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
    print(msg)
  
  def pega_avaliacao(self):
    while True:
      try:
        nota = int(input("DIGITE UMA NOTA DE 0 A 5 PARA O FILME QUE ALUGOU: "))
        opcoes = [0,1,2,3,4,5]
        if nota not in opcoes:
          raise ValueError
        break
      except ValueError:
        print("Digite uma nota válida!")

    comentario = input("FAÇA UM COMENTÁRIO SOBRE O QUE ACHOU DO FILME: ")
    
    return {"nota": nota, "comentario": comentario}

  def mostra_historico_locacao(self, locacao):
    print("FILME: ", locacao["titulo_filme"], "no dia: ", locacao["data_aluguel"])
