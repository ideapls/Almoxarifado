import re

class Fornecedor:
    def __init__(self, codigo, nome, cnpj, endereco, telefone, email):
        self._codigo = codigo
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def codigo(self):
        return self._codigo

    def validar_cnpj(self):
        # Remove caracteres não numéricos
        cnpj = re.sub(r'[^0-9]', '', self._cnpj)

        # Verifica se possui 14 dígitos
        if len(cnpj) != 14:
            return False

        # Verifica se todos os dígitos são iguais
        if cnpj == cnpj[0] * 14:
            return False

        # Validação do primeiro dígito verificador
        soma = sum([int(cnpj[i]) * (5 - i) for i in range(4)]) + sum([int(cnpj[i]) * (13 - i) for i in range(4, 12)])
        digito1 = (soma % 11)
        if digito1 < 2:
            digito1 = 0
        else:
            digito1 = 11 - digito1
        if int(cnpj[12]) != digito1:
            return False

        # Validação do segundo dígito verificador
        soma = sum([int(cnpj[i]) * (6 - i) for i in range(5)]) + sum([int(cnpj[i]) * (14 - i) for i in range(5, 13)])
        digito2 = (soma % 11)
        if digito2 < 2:
            digito2 = 0
        else:
            digito2 = 11 - digito2
        if int(cnpj[13]) != digito2:
            return False

        return True

    def __str__(self):
        return f'Fornecedor("{self._nome}", "{self._cnpj}", "{self._codigo}", "{self._endereco}", "{self._telefone}", "{self._email}")'
