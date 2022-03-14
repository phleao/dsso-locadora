from logging import PlaceHolder
import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaPessoa():
    
    def pega_dados_pessoa(self):
        print("-------- DADOS DO USUARIO ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        return {"nome": nome, "email": email, "senha": senha}

    def pega_dados_cliente(self):
        layout = [
                    [sg.Text('Preencha as informações necessárias')],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Email', size=(15, 1)), sg.InputText()],
                    [sg.Text('Senha', size=(15, 1)), sg.InputText()],  #colocar bolinhas em vez de texto aparecendo
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Cancel(button_text="Voltar", size=(15,1), button_color="Light Grey"), sg.Submit("Finalizar Cadastro", size=(20,1))]]
        
        window = sg.Window('Cadastro de Cliente', layout, element_justification='center')
        event, values = window.read()
        window.close()
        if event == "Voltar" or event == sg.WIN_CLOSED:
            return None
        return {"nome": values[0], "email": values[1], "senha": values[2], "idade": int(values[3]), "status": False}

    def pega_senha_de_cadastro(self):
        layout = [
                        [sg.Text('Senha de segurança', size=(15, 1)), sg.InputText(password_char='*')],
                        [sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light Gray"), sg.Submit(button_text="Acessar", size=(20,1))]]
            
        window = sg.Window('Senha de Administrador', layout, element_justification='center')
        event, values = window.read()
        window.close()
        if event == sg.WIN_CLOSED or event == "Voltar":
            return None
        return values[0]

    def pega_dados_funcionario(self):
        layout = [
                    [sg.Text('Preencha as informações necessárias')],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Email', size=(15, 1)), sg.InputText()],
                    [sg.Text('Senha', size=(15, 1)), sg.InputText()],  #colocar bolinhas em vez de texto aparecendo
                    [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                    [sg.Cancel(button_text="Voltar", size=(15,1), button_color="Light Grey"), sg.Submit("Cadastrar Funcionário", size=(20,1))]]
        
        window = sg.Window('Cadastro de Funcionário', layout, element_justification='center')

        event, values = window.read()

        window.close()
        if event == "Voltar" or event == sg.WIN_CLOSED:
            return None
        return {"nome": values[0], "email": values[1], "senha": values[2], "cpf": int(values[3]), "status": False}
    
    def pega_dados_login(self):
        layout = [
                [sg.Text('Preencha as informações necessárias')],
                [sg.Text('Email', size=(5, 1)), sg.InputText()],
                [sg.Text('Senha', size=(5, 1)), sg.InputText(password_char='*')],
                [sg.Cancel(button_text="Voltar", size=(20, 1), button_color="Light Gray"), sg.Submit(button_text="Acessar", size=(20, 1))]]


        window = sg.Window('Login', layout, element_justification='center')
        event, values = window.read()
        window.close()
        if event == "Voltar" or event == sg.WIN_CLOSED:
            return None

        return {"email": values[0], "senha": values[1]}

    def mostra_clientes(self, clientes):
        if len(clientes) > 0:
            items = []
            for cli in clientes:
                items.append([cli["nome"], cli["email"], cli["status"], cli["idade"]])

            headings = [' Nome','Email', 'Status', 'Idade']

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Cancel(button_text="Voltar", size=(15, 1), button_color="Light grey")]]

            window = sg.Window('Clientes', layout, element_justification='center')
            event, values = window.read()
            window.close()
            if event == "Voltar" or event == sg.WIN_CLOSED:
                return None

    def mostra_mensagem(self, msg):

        sg.Popup("", msg + "\n")
