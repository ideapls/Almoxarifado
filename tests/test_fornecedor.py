from Almoxarifado.classes.fornecedor import Fornecedor


class TestFornecedor:
    def test_quando_cnpj_e_invalido(self):
        entrada = "72299804000144"
        esperado = True

        fornecedor_cnpj = Fornecedor(1, 'Fornecedor teste', entrada, 'Rua 2', '992432053', 'igordsmolina@gmail.com')
        resultado = fornecedor_cnpj.validar_cnpj()

        assert resultado == esperado

    def test_verifica_preenchimento(self):
        fornecedor = Fornecedor(1, 'Fornecedor teste', '72299804000144', 'Rua teste', '992432053', 'igordsmolina@gmail.com')
        preenchido = fornecedor.verificar_preenchimento()
        assert preenchido == True

    def test_verifica_integridade_do_preenchimento_do_email(self):
        fornecedor = Fornecedor(1, 'Fornecedor teste', '72299804000144', 'Rua teste', '992432053',
                                'igordsmolina@gmail.com')
        preenchido = fornecedor.validar_email()
        assert preenchido == True
