class TelaLocacao():
  def tela_opcoes(self):
    print("-------- LOCAÇÕES ----------")
    print("Escolha a opcao")
    print("1 - Fazer locação")
    print("2 - Listar locações")
    print("3 - Devolver locação")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
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

  def mostra_locacao(self, dados_locacao):
    print(dados_locacao["codigo"], "  ", dados_locacao["titulo_filme"], "  ", dados_locacao["email"], "  ", dados_locacao["data_aluguel"], dados_locacao["status"])
    print("\n")

  def seleciona_locacao(self):
    codigo = input("Código da locação que deseja selecionar: ")
    return codigo

  def mostra_mensagem(self, msg):
    print(msg)
  
  def pega_avaliacao(self):
    nota = int(input("DIGITE UMA NOTA DE 0 A 5 PARA O FILME QUE ALUGOU: "))
    comentario = input("FAÇA UM COMENTÁRIO SOBRE O QUE ACHOU DO FILME: ")
    
    return {"nota": nota, "comentario": comentario}

  def mostra_historico_locacao(self, locacao):
    print("FILME: ", locacao.filme.titulo, "no dia: ", locacao.data_aluguel)
  