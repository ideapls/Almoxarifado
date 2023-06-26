# ID do produto, nome, descrição, quantidade em estoque, data de validade
from datetime import date


class Produto:
    def __init__(self, codigo, nome, descricao, quantidade_estoque, validade):
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao
        self._quantidade_estoque = quantidade_estoque
        self._validade = validade

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @property
    def validade(self):
        return self._validade

    def verificar_preenchimento(self):
        if not self._codigo or not self._nome or not self._descricao or not self._quantidade_estoque or not self._validade:
            return False
        return True

    def verificar_data_validade(self):
        hoje = date.today()
        if self._validade < hoje:
            return False
        return True
