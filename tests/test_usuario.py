from Almoxarifado.classes.usuario import Usuario
from Almoxarifado.classes.sistema import Sistema


class TestUsuario:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        usuario_teste = Usuario(1, 'Teste', 'igordsmolina@gmail.com', 'testando', entrada)
        resultado = usuario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_igor_molina(self):
        entrada = ' Igor Molina '
        esperado = 'Molina'

        igor = Usuario(2, 'Igor', 'igordsmolina@gmail.com', entrada, '13/03/2000')
        resultado = igor.sobrenome()

        assert resultado == esperado

    def test_verificar_preenchimento(self):
        usuario = Usuario(1, 'Igor', 'igordsmolina@gmail.com', 'Molina', '13/03/2000')
        preenchido = usuario.verificar_preenchimento()
        assert preenchido == True

    def test_verifica_integridade_do_preenchimento_do_email(self):
        usuario = Usuario(1, 'Igor', 'igordsmolina@gmail.com', 'Molina', '13/03/2000')
        preenchido = usuario.validar_email()
        assert preenchido == True

    def test_quando_codigo_esta_duplicado(self):
        sistema = Sistema()

        usuario1 = Usuario(1, 'Igor', 'igordsmolina@gmail.com', 'Molina', '13/03/2000')
        adicionado1 = sistema.adicionar_usuario(usuario1)
        assert adicionado1 == True

        usuario2 = Usuario(2, 'Teste 2', 'teste2@gmail.com', 'Testudo', '13/03/2000')
        adicionado2 = sistema.adicionar_usuario(usuario2)
        assert adicionado2 == True

        usuario3 = Usuario(1, 'Teste 3', 'teste3@gmail.com', 'Testudo', '13/03/2000')
        adicionado3 = sistema.adicionar_usuario(usuario3)
        assert adicionado3 == False
