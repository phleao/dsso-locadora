#tela inicial do sistema

import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaSistema:

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
        layout = [
                    [sg.Button(button_text = "Filmes", button_type = 7)],
                    [sg.Button(button_text = "Locacoes", button_type = 7)],
                    [sg.Button(button_text = "Clientes", button_type = 7)],
                    [sg.Cancel(button_text = "Deslogar")]]


        window = sg.Window('Home - Funcionario', layout)
        values = window.read()
        window.close()
        return values[0]

    def tela_opcoes_do_cliente(self):
        layout = [
                    [sg.Button(button_text = "Catalogo", button_type = 7)],
                    [sg.Button(button_text = "Historico", button_type = 7)],
                    [sg.Button(button_text = "Melhores filmes", button_type = 7)],
                    [sg.Cancel(button_text = "Deslogar")]]


        window = sg.Window('Home - Cliente', layout)
        values = window.read()
        window.close()
        return values[0]

    def tela_opcoes_do_cliente_status_true(self):
        layout = [
                    [sg.Button(button_text = "Locacao Atual", button_type = 7)],
                    [sg.Button(button_text = "Melhores filmes", button_type = 7)],
                    [sg.Cancel(button_text = "Deslogar")]]


        window = sg.Window('Home - Cliente', layout)
        values = window.read()
        window.close()
        return values[0]

    def mostra_mensagem(self, msg):
        print(msg)
        sg.Popup("", msg + "\n")
