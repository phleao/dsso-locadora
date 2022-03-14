from persistencia.abstract_DAO import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super ().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.email, cliente)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)