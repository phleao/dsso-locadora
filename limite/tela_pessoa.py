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

    def pega_senha_de_cadastro(self):
        senha = str(input("Essa ação só é permitida para pessoas autorizadas, digite a senha de acesso: "))
        return senha

    def pega_dados_funcionario(self):
        dados_pessoa = self.pega_dados_pessoa()
        while True:
            try:
                cpf = int(input("CPF: "))
                break
            except ValueError:
                print("Digite um número válido")

        dados_pessoa["cpf"] = cpf
        return dados_pessoa
    
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

    def mostra_clientes(self, dados_cliente):
        status = dados_cliente["status"]
        if status == True:
            status = "Locação ativa"
        else:
            status = "Sem locação ativa"
        print("Nome: ", dados_cliente["nome"], "   Email: ", dados_cliente["email"], "     Status: ", status, "     Idade: ", dados_cliente["idade"])
        print("\n")

    def mostra_mensagem(self, msg):
        print(msg)
        sg.Popup("Erro", msg)