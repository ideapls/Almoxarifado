# ID do item, quantidade solicitada, quantidade recebida

class Pedido:
    def __init__(self, codigo, data_pedido, status_pedido, quantidade_solicitada, quantidade_recebida):
        self._codigo = codigo
        self._data_pedido = data_pedido
        self._status_pedido = status_pedido
        self._quantidade_solicitada = quantidade_solicitada
        self._quantidade_recebida = quantidade_recebida

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def data_pedido(self):
        return self._data_pedido

    @property
    def status_pedido(self):
        return self._status_pedido

    @property
    def nome(self):
        return self._nome

    @property
    def quantidade_solicitada(self):
        return self._quantidade_solicitada

    @property
    def quantidade_recebida(self):
        return self._quantidade_recebida

    def recebimento_valido(self):
        if self.quantidade_recebida < self.quantidade_solicitada:
            return False
        elif self.quantidade_recebida > self.quantidade_solicitada:
            return False
        else:
            return True
