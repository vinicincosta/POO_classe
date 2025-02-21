from flask import Flask, render_template, request, redirect, url_for, session
import sqlalchemy
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"


class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False, salario=0):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo

        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario

    def apresentar(self):
        print(
            f' Olá, sou {self.nome}.\n',
            f'Data de nascimento: {self.data_nascimento}.\n',
            f'Código: {self.codigo}.\n',
            f'Situação atual:')
        print("\n")
        print('-' * 20)

        if self.estudando and self.trabalhando:
            print(f'Estudando e trabalhando. Salário atual: {self.salario} reais.')
        elif self.estudando:
            print(f'Apenas estudando. Salário atual: {self.salario} reais.')
        elif self.trabalhando:
            print(f'Apenas trabalhando. Salário atual: {self.salario} reais.')
        else:
            print(f'Nem estudando nem trabalhando. Salário atual: {self.salario} reais.')

        print("\n")
        print('-' * 20)

    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print('Continua apenas estudando.')

        elif self.estudando and self.trabalhando:
            self.salario += 500
            print(f'Agora está estudando e trabalhando. Salário aumentado para {self.salario} reais.')

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario = 500
            print(f'Agora está trabalhando. Salário inicial: {self.salario} reais.')
        else:
            print(f'Já estava trabalhando. Salário atual: {self.salario} reais.')

        # Testando a classe


class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, codigo,
                 estudando=True, trabalhando=True):
        super().__init__(nome, data_nascimento,
                         codigo, estudando, trabalhando)
        self.fome = True
        self.chorando = True
        self.dormindo = False
        self.estudando = estudando
        self.trabalhando = trabalhando
        print("\n")
        print('-' * 20)

    def apresentar(self):
        print(f'Olá, sou irmão do bebe {self.nome},\n'
              f'meu irmão nasceu {self.data_nascimento},\n'
              f'e seu registro é:{self.codigo}.\n'
              f'situação atual:')

        if self.fome and self.chorando:
            self.fome = True
            self.chorando = True
            print(f'o bebe está querendo mamar, ele está'
                  f' chorando e com fome')

        if not self.fome and self.dormindo:
            print(f'bebe está satisfeito e dormindo')

        else:
            print('Ele está acordado')
        print("\n")
        print('-' * 20)

    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            self.fome = True
            print(f'Bebe acordou, pois estava com fome:')
        else:
            print(f'bebe já está acordado')

    def mamar(self):
        if self.fome:
            self.chorando = False
            self.fome = False
            print(f'Bebê parou de chorar e não está mais com fome, pois já está satisfeito')

        else:
            print(f'bebe já mamou, ele já não tem mais fome')

    def chorar(self):
        if self.chorando:
            self.chorando = True
            self.fome = True
            print(f'Bebê está chorando, ele está com fome')

        else:

            print(f'Bebê não está chorando, pois não está com fome')

    def dormir(self):
        if self.dormindo:
            print(f'ele já está dormindo')

        else:
            if self.fome:
                print(f'Bebê está com fome, não pode dormir')
            else:
                self.dormindo = True
                print(f'Bebe pode dormir')

    def trabalhar(self):
        if self.trabalhando:
            self.trabalhando = True
            print(f'O bebe não pode trabalhar, só daqui 18 anos')

    def estudar(self):
        if self.estudando:
            self.estudando = True
            print(f'O bebe não está na creche ainda')


s1 = Bebe('Dener', "26/03/2008", "1788768326")
s1.apresentar()

p1 = Pessoa('Vini', "26/03/2008", "1788768326")
p1.apresentar()
p1.estudar()
p1.trabalhar()
