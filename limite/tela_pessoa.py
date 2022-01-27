class TelaPessoa():
    
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_pessoa(self):
        print("-------- DADOS DO USUARIO ----------")
        nome = input("Nome: ")
        codigo = input("Codigo: ")
        email = input("Email: ")
        senha = input("Senha: ")

        return {"nome": nome, "codigo": codigo, "email": email, "faixa_etaria": email, "senha": senha}

    def pega_dados_cliente(self):
        self.pega_dados_pessoa()
        data_nascimento = input("Data de Nascimento: ")

        return {"data_nascimento": data_nascimento}
    
    def pega_dados_funcionario(self):
        self.pega_dados_pessoa()
        cpf = input("CPF: ")

        return {"cpf": cpf}
    
    def pega_dados_login(self):
        email = input("Email: ")
        senha = input("Senha: ")

        return {"email": email, "senha": senha}