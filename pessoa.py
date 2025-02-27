from flask import Flask, render_template, request, redirect, url_for, session
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"


class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False, salario=0):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo

        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def apresentar_ex(self):
        print("+", "-" * 20, "+")
        print(f'Olá, sou {self.get_nome()},\n'
              f'meu aniversário é dia {self.get_data_nascimento()},\n'
              f'n de rg {self.get_codigo()}.\n')
        print("+", "-" * 20, "+")
        print("\n")

    # GET voce recebe informação, SET é para mandar informação

    def get_nome(self):
        return self.__nome

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_codigo(self):
        return self.__codigo

    def get_estudando(self):
        return self._estudando

    def get_trabalhando(self):
        return self._trabalhando

    def get_salario(self):
        return self._salario

    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print('salário inválido')


    # Exemplos:
    def is_estudando(self):
        return self._estudando

    def is_trabalhando(self):
        return self._trabalhando

    def set_trabalhar(self, status):
        if self._trabalhando and status:
            print('Já esta trabalhando')
        elif not self._trabalhando and not status:
            print('Não esta trabalhando')

        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(100)

        else:
            self._trabalhando = status
            self.set_salario(0)

    def set_estudar(self, status):
        if self._estudando and status:
            print(f'está estudando')
        elif not self._estudando and not status:
            print(f'Não está estudando')
        elif self._estudando and self._trabalhando and status:
            self.set_salario(self.get_salario() + 500)
            print(f'Você está trabalhando e estudando, seu salário será R$ {self._salario}')


    # EX: p1.pessoa.set_trabalhar(True)

p1 = Pessoa(f'Vini', '26/03/2008','76545678','Sim', 'Não')
p1.apresentar_ex()
p1.set_estudar(True)
p1.set_trabalhar(False)



# def apresentar_ex(self):
#     print("+", "-" * 20, "+")
#     print(f'Olá, sou {self.get_nome()},\n'
#           f'meu aniversário é dia {self.get_data_nascimento()},\n'
#           f'n de rg {self.get_codigo()}.\n')
#     print(f'Estudando: {'Sim' if self.is_estudando() else'Não'}')
#     print(f'Trabalhando: {'Sim' if self.is_trabalhando() else 'Não'}')
#     if self.is_trabalhando():
#         print(f'Salário:R$ {self.get_salario():.2f}')
#     print("+", "-" * 20, "+")
#     print("\n")
