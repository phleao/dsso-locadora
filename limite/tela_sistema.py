#tela inicial do sistema

import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaSistema:

    def tela_login_antiga(self):
        while True:
            try:
                print("Escolha sua opcao")
                print("1 - Login")
                print("2 - Cadastrar como Cliente")
                print("3 - Cadastrar como Funcionário")
                print("0 - Finalizar sistema")
                opcoes = [0,1,2,3]
                opcao = int(input("\n Escolha a opcao: "))
                if opcao not in opcoes:
                    raise ValueError
                break
            except ValueError:
                print("Digite um número válido\n")
        return opcao

    def tela_login(self):
        
        layout = [  [sg.Text('Bem-vindo ao Locaçon')],
                    [sg.Button('Login')], 
                    [sg.Button('Cadastrar Cliente')], 
                    [sg.Button('Cadastrar Funcionario')],
                    [sg.Button('Finalizar')]]


        window = sg.Window('Home - Locaçon', layout)

        while True:
            values = window.read()
            if values == sg.WIN_CLOSED or values[0] == '0': 
                break
        
            else:
                window.close()
                return values[0]
        
    def tela_opcoes_do_funcionario(self):
        print("-------- LocadaçON ---------")
        while True:
            try:
                print("Escolha sua opcao")
                print("1 - Filmes")
                print("2 - Locações")
                print("3 - Clientes")
                print("0 - Deslogar")
                opcoes = [0,1,2,3]
                opcao = int(input("\n Escolha a opcao: "))
                if opcao not in opcoes:
                    raise ValueError
                break
            except ValueError:
                print("Digite um número válido\n")
        return opcao

    def tela_opcoes_do_cliente(self):
        print("\n-------- LocadaçON ---------")
        
        while True:
            try:
                print("Escolha sua opcao")
                print("1 - Cátalogo de filmes") 
                print("2 - Fazer locação")
                print("3 - Histórico de locações")
                print("4 - Filmes mais bem avaliados")
                print("0 - Deslogar")
                opcoes = [0,1,2,3,4]
                opcao = int(input("\n Escolha a opcao: "))
                if opcao not in opcoes:
                    raise ValueError
                break
            except ValueError:
                print("Digite um número válido\n")
        return opcao

    def tela_opcoes_do_cliente_status_true(self):
        print("\n-------- LocadaçON ---------")
        while True:
            try:
                print("Escolha sua opcao")
                print("1 - Cátalogo de filmes")
                print("2 - Verificar locação atual")
                print("3 - Finalizar locação atual")
                print("4 - Filmes mais bem avaliados")
                print("0 - Deslogar")
                opcoes = [0,1,2,3,4]
                opcao = int(input("\n Escolha a opcao: "))
                if opcao not in opcoes:
                    raise ValueError
                break
            except ValueError:
                print("Digite um número válido\n")
        return opcao

    def mostra_mensagem(self, msg):
        print(msg)
        sg.Popup("", msg+'\n')