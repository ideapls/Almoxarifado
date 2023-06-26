from Almoxarifado.classes.pedido import Pedido
from datetime import date


class TestPedido:
    def test_quando_recebimento_possui_mais_ou_menos_que_o_solicitado(self):
        entrada_solicitado = 4
        entrada_recebido = 4
        esperado = True

        pedido = Pedido(1, '10/05/2022', 'Entregue', entrada_solicitado, entrada_recebido)
        resultado = pedido.recebimento_valido()

        assert resultado == esperado

    def test_quando_data_do_pedido_for_maior_que_data_atual(self):
        pedido = Pedido(1, date(2023, 6, 10), "Em transporte", 10, 0)
        data_validade = pedido.verificar_data_pedido()
        assert data_validade == True
