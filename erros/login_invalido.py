
class LoginInvalido(Exception):
    def __init__(self):
        self.__mensagem = "Login Invalido"
        super().__init__(self.__mensagem)
