from Almoxarifado.classes.itemPedido import ItemPedido


class TestItemPedido:
    def test_quando_recebimento_possui_mais_ou_menos_que_o_solicitado(self):
        entrada_solicitado = 4
        entrada_recebido = 4
        esperado = True

        item_pedido = ItemPedido(1, entrada_solicitado, entrada_recebido)
        resultado = item_pedido.recebimento_valido()

        assert resultado == esperado

    def test_verifica_preenchimento(self):
        itemPedido = ItemPedido(1, 'Pedido teste', 10)
        preenchido = itemPedido.verificar_preenchimento()
        assert preenchido == True