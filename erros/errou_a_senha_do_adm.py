
class ErrouSenhaDoAdmError(Exception):
    def __init__(self):
        self.__mensagem = "senha errada"
        super().__init__(self.__mensagem)

