from datetime import date
import re


class Usuario:
    def __init__(self, codigo, nome, email, sobrenome, data_nascimento):
        self._codigo = codigo
        self._nome = nome
        self._email = email
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def codigo(self):
        return self._codigo

    @property
    def email(self):
        return self._email

    def verificar_preenchimento(self):
        if not self._codigo or not self._nome or not self._sobrenome or not self._data_nascimento:
            return False
        return True

    def validar_email(self):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_regex, self._email):
            return True
        return False

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._sobrenome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def __str__(self):
        return f'Usuario({self._nome}, {self._data_nascimento}, {self._codigo})'
