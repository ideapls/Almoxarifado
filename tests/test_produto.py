from Almoxarifado.classes.produto import Produto
from datetime import date


class TestProduto:
    def test_verificar_preenchimento(self):
        produto = Produto(1, "Mouse", "Periférico de entrada", 4, date(2023, 6, 1))
        preenchido = produto.verificar_preenchimento()
        assert preenchido == True

    def test_verificar_validade_do_produto(self):
        produto = Produto(1, "Liquid paper", "Material escolar", 4, date(2023, 6, 28))
        data_validade = produto.verificar_data_validade()
        assert data_validade == True
