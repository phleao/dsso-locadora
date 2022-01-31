class TelaPessoa():
    
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_pessoa(self):
        print("-------- DADOS DO USUARIO ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        return {"nome": nome, "email": email, "senha": senha}

    def pega_dados_cliente(self):
        dados_pessoa = self.pega_dados_pessoa()
        idade = input("Idade: ")
        dados_pessoa["idade"] = idade
        return dados_pessoa

    def pega_senha_de_cadastro(self):
        senha = str(input("Essa ação só é permitida para pessoas autorizadas, digite a senha de acesso:"))
        return senha

    def pega_dados_funcionario(self):
        dados_pessoa = self.pega_dados_pessoa()
        cpf = input("CPF: ")
        dados_pessoa["cpf"] = cpf
        return dados_pessoa
    
    def pega_dados_login(self):
        email = input("Email: ")
        senha = input("Senha: ")

        return {"email": email, "senha": senha}