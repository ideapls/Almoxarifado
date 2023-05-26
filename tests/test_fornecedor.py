from Almoxarifado.classes.fornecedor import Fornecedor


class TestFornecedor:
    def test_quando_sobrenome_recebe_igor_molina(self):
        entrada = "72299804000144"
        esperado = True

        fornecedor_cnpj = Fornecedor(1, 'Cacau Show', entrada, 'Rua 2', '992432053', 'igordsmolina@gmail.com')
        resultado = fornecedor_cnpj.validar_cnpj()

        assert resultado == esperado
