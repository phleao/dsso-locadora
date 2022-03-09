from controle.abstract_DAO import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super ().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (funcionario is not None) and isinstance(funcionario, Funcionario):
            super().add(funcionario.email, funcionario)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)