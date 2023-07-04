class ItemPedido:
    def __init__(self, codigo, quantidade_solicitada, quantidade_recebida):
        self._codigo = codigo
        self._quantidade_solicitada = quantidade_solicitada
        self._quantidade_recebida = quantidade_recebida

    @property
    def codigo(self):
        return self._codigo

    @property
    def quantidade_solicitada(self):
        return self._quantidade_solicitada

    @property
    def quantidade_recebida(self):
        return self._quantidade_recebida

    def verificar_preenchimento(self):
        if not self._codigo or not self._quantidade_solicitada or not self._quantidade_recebida:
            return False
        return True

    def recebimento_valido(self):
        if self.quantidade_recebida < self.quantidade_solicitada:
            return False
        elif self.quantidade_recebida > self.quantidade_solicitada:
            return False
        else:
            return True
