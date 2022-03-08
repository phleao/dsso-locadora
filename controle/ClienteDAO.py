from controle.abstract_DAO import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super ().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance(cliente.email, int)) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.email, cliente)

    def get(self, key: int):
        if isinstance (key, int):
            return super().get(key)

    def remove(self, key: int) :
        if isinstance(key, int):
            return super().remove(key)