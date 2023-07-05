class Sistema:
    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, usuario):
        if self._verificar_codigo_unico(usuario.codigo):
            self._usuarios.append(usuario)
            return True
        else:
            return False

    def _verificar_codigo_unico(self, codigo):
        for usuario in self._usuarios:
            if usuario.codigo == codigo:
                return False
        return True