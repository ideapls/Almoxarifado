from unittest import TestCase
from Almoxarifado.classes.usuario import Usuario


class TestUsuario:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        usuario_teste = Usuario(1, 'Teste', 'testando', entrada)
        resultado = usuario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_igor_molina(self):
        entrada = ' Igor Molina '
        esperado = 'Molina'

        igor = Usuario(2, 'Igor', entrada, '13/03/2000')
        resultado = igor.sobrenome()

        assert resultado == esperado
