import PySimpleGUI as sg

sg.theme('DarkAmber')

class TelaPessoa():
    
    def pega_dados_pessoa(self):
        print("-------- DADOS DO USUARIO ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        return {"nome": nome, "email": email, "senha": senha}

    def pega_dados_cliente_antiga(self):
        dados_pessoa = self.pega_dados_pessoa()
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except ValueError:
                print("Digite um número válido")
        dados_pessoa["idade"] = idade
        dados_pessoa["status"] = False
        return dados_pessoa

    def pega_dados_cliente(self):
        layout = [
                    [sg.Text('Preencha as informações necessárias')],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Email', size=(15, 1)), sg.InputText()],
                    [sg.Text('Senha', size=(15, 1)), sg.InputText()],  #colocar bolinhas em vez de texto aparecendo
                    [sg.Text('Idade', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]]
        
        window = sg.Window('Cadastro de cliente', layout)
        event, values = window.read()
        window.close()
        return {"nome": values[0], "email": values[1], "senha": values[2], "idade": values[3], "status": False}

    def pega_senha_de_cadastro(self):
        layout = [
                        [sg.Text('Senha de segurança', size=(15, 1)), sg.InputText()],
                        [sg.Submit()]]
            
        window = sg.Window('Cadastro de cliente', layout)
        event, values = window.read()
        window.close()
        return values[0]

    def pega_dados_funcionario_antigo(self):
        dados_pessoa = self.pega_dados_pessoa()
        while True:
            try:
                cpf = int(input("CPF: "))
                break
            except ValueError:
                print("Digite um número válido")

        dados_pessoa["cpf"] = cpf
        return dados_pessoa

    def pega_dados_funcionario(self):
        layout = [
                    [sg.Text('Preencha as informações necessárias')],
                    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
                    [sg.Text('Email', size=(15, 1)), sg.InputText()],
                    [sg.Text('Senha', size=(15, 1)), sg.InputText()],  #colocar bolinhas em vez de texto aparecendo
                    [sg.Text('CPF', size=(15, 1)), sg.InputText()],
                    [sg.Submit(), sg.Cancel()]]
        
        window = sg.Window('Cadastro de cliente', layout)
        event, values = window.read()
        window.close()
        return {"nome": values[0], "email": values[1], "senha": values[2], "cpf": values[3], "status": False}
    
    def pega_dados_login_antigo(self):
        email = input("Email: ")
        senha = input("Senha: ")

        return {"email": email, "senha": senha}

    def pega_dados_login(self):
        layout = [
                [sg.Text('Preencha as informações necessárias')],
                [sg.Text('Email', size=(15, 1)), sg.InputText()],
                [sg.Text('Senha', size=(15, 1)), sg.InputText()],
                [sg.Submit(), sg.Cancel()]]


        window = sg.Window('Cadastro de funcionario', layout)
        event, values = window.read()
        window.close()
        return {"email": values[0], "senha": values[1]}

    def mostra_clientes_antigo(self, dados_cliente):
        status = dados_cliente["status"]
        if status == True:
            status = "Locação ativa"
        else:
            status = "Sem locação ativa"
        print("Nome: ", dados_cliente["nome"], "   Email: ", dados_cliente["email"], "     Status: ", status, "     Idade: ", dados_cliente["idade"])
        print("\n")

    def mostra_clientes(self, clientes):
        if len(clientes) > 0:
            items = []
            for cli in clientes:
                items.append([cli["nome"], cli["email"], cli["status"], cli["idade"]])

            headings = [' Nome','Email', 'Status', 'Idade']

            layout = [[sg.Table(values= items, headings=headings, max_col_width=35,  justification='center', num_rows=6, key='-TABLE-', row_height=35)],
                    [sg.Cancel()]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            if event != "Incluir" and event != "Cancel":
                cliente = items[values["-TABLE-"][0]]
                return event, cliente[0]
            else:
                return event, True

        else:
            layout = [[sg.Text("Sem filmes no cátalogo")],
                     [sg.Button(button_text="Incluir"), sg.Cancel()]]

            window = sg.Window('tabela de teste', layout)
            event, values = window.read()
            window.close()
            return event, values

    def mostra_mensagem(self, msg):
        print(msg)
        sg.Popup("", msg + "\n")
