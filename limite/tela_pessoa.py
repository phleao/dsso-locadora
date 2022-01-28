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
        dados_pessoa = self.pega_dados_pessoa()
        data_nascimento = input("Data de Nascimento: ")
        dados_pessoa["data_nascimento"] = data_nascimento
        return dados_pessoa
    
    def pega_dados_funcionario(self):
        dados_pessoa = self.pega_dados_pessoa()
        cpf = input("CPF: ")
        dados_pessoa["cpf"] = cpf
        return dados_pessoa
    
    def pega_dados_login(self):
        email = input("Email: ")
        senha = input("Senha: ")

        return {"email": email, "senha": senha}