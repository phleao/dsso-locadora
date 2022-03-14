#tela inicial do sistema

import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaSistema:

    def tela_login(self):
        
        layout = [  [sg.Button('Login', size=(20, 1))], 
                    [sg.Button('Cadastrar Cliente', size=(20, 1))], 
                    [sg.Button('Cadastrar Funcionario', size=(20, 1))],
                    [sg.Button('Finalizar', size=(20, 1))]]


        window = sg.Window('Locaçon', layout, element_justification='center')

        while True:
            values = window.read()
            if values == sg.WIN_CLOSED or values[0] == '0': 
                break
        
            else:
                window.close()
                return values[0]

    def tela_opcoes_do_funcionario(self):
        layout = [
                    [sg.Button(button_text = "Filmes", button_type = 7, size=(20, 1))],
                    [sg.Button(button_text = "Locacoes", button_type = 7, size=(20, 1))],
                    [sg.Button(button_text = "Clientes", button_type = 7, size=(20, 1))],
                    [sg.Cancel(button_text = "Deslogar", size=(20, 1), button_color="Light Grey")]]


        window = sg.Window('Home - Funcionario', layout, element_justification='center')
        values = window.read()
        window.close()
        return values[0]

    def tela_opcoes_do_cliente(self):
        layout = [
                    [sg.Button(button_text = "Catalogo", button_type = 7, size=(20, 1))],
                    [sg.Button(button_text = "Historico", button_type = 7, size=(20, 1))],
                    [sg.Button(button_text = "Melhores filmes", button_type = 7, size=(20, 1))],
                    [sg.Cancel(button_text = "Deslogar", size=(20, 1), button_color="Light grey")]]


        window = sg.Window('Home - Cliente', layout, element_justification='center')
        values = window.read()
        window.close()
        return values[0]

    def tela_opcoes_do_cliente_status_true(self):
        layout = [
                    [sg.Button(button_text = "Locacao Atual", button_type = 7, size=(20, 1))],
                    [sg.Button(button_text = "Melhores filmes", button_type = 7, size=(20, 1))],
                    [sg.Cancel(button_text = "Deslogar", size=(20, 1), button_color="Light grey")]]


        window = sg.Window('Home - Cliente', layout, element_justification='center')
        values = window.read()
        window.close()
        return values[0]

    def mostra_mensagem(self, msg):
        sg.Popup("", msg + "\n")
