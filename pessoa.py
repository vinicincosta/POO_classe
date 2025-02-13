from flask import Flask, render_template, request, redirect, url_for, session
import sqlalchemy
from models import *
app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET"

class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando = True, trabalhando = False, salario = 0):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario

    def apresentar(self):
        print(f'Olá sou {self.nome},\n' 
              f'minha data de nascimento é {self.data_nascimento},\n'
              f'meu código é {self.codigo},\n'
              f'no momento eu estou:')


        if self.estudando:
            print(f'Estudando')

        else:
            print(f'Não está estudando,')


        if self.trabalhando:
            print(f' Trabalhando')
        else:
            print(f'e não trabalhando')
        print('-'*20)

    def estudar(self):

        if self.estudando:
            print("self.salario = 0")
            print(f'Apenas estudando')

        elif self.trabalhando and self.estudando:
            print("self.salario += 1000")
            print(f'Você está trabalhando e estudando, Seu salário irá aumentar')

        else:
            self.estudando = True
            print(f'Começou estudar')

    def trabalhar(self):

        if self.trabalhando:
            self.salario += 500
            print('Está trabalhando, mas não aumentou seu salário')

        else:
            self.trabalhando = True
            print('Começou trabalhar')


p1 = Pessoa('Vini', "26/03/2008", "1788768326", )
p1.apresentar()
p1.trabalhar()
p1.estudar()
p1.apresentar()

# p2 = Pessoa('Dener', "05/10/2000", "9876543", )
# p2.apresentar()
#
# p3 = Pessoa('Jão', "13/13/2013", "72345678", )
# p3.apresentar()
#
# p4 = Pessoa('Luis', "31/02/1998", "28765432456", )
# p4.apresentar()
#
# p5 = Pessoa('Leticia', '10/10/2014', "87654345678", )
# p5.apresentar()


# # class Curso:
# #     def __init__(self, nome_curso, professor, aulas  ):
# #         self.nome_curso = nome_curso
# #         self.professor = professor
# #         self.aulas = aulas
# #
# #
# #     def apresentar_2(self):
# #         print(f'Olá sou o professor(a) {self.professor}, '
# #               f'minha matéria é {self.nome_curso} e '
# #               f'aplico aulas {self.aulas}')
# #
# # c1 = Curso('Matemática', "Jean", "presenciais")
# # c1.apresentar_2()
# #
# # c2 = Curso('Português', "Mateus", "onlines")
# # c2.apresentar_2()
# #
# # c3 = Curso( 'História', "Dailson", 'presenciais')
# # c3.apresentar_2()
# #
# # c4 = Curso ('Inglês', 'Nita', 'onlines')
# # c4.apresentar_2()
# #
# # c5 = Curso('Geografia', "Chata", 'onlines')
# c5.apresentar_2()