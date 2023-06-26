from Almoxarifado.classes.produto import Produto


class TestProduto:
    def test_verificar_preenchimento(self):
        produto1 = Produto(1, "Mouse", "Periférico de entrada", 4, "02/12/2024")
        preenchido1 = produto1.verificar_preenchimento()
        assert preenchido1 == True
