from Almoxarifado.classes.pedido import Pedido


class TestPedido:
    def test_quando_recebimento_possui_mais_ou_menos_que_o_solicitado(self):
        entrada_solicitado = 4
        entrada_recebido = 4
        esperado = True

        pedido = Pedido(1, '10/05/2022', 'Entrege', entrada_solicitado, entrada_recebido)
        resultado = pedido.recebimento_valido()

        assert resultado == esperado
