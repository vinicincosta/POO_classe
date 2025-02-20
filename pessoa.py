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
            f'Olá, sou {self.nome}.',
            f'Data de nascimento: {self.data_nascimento}.',
            f'Código: {self.codigo}.',
            f'Situação atual:')

        if self.estudando and self.trabalhando:
            print(
                f'Estudando e trabalhando. Salário atual: {self.salario} reais.')  # append Adiciona qualquer valor completo,
            # por exemplo, se enviarmos um objeto,
            # ele ad
            # iciona o objeto, se enviarmos uma lista,
            # ele adiciona a lista inteira ao invés de seus itens.
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

p1 = Pessoa('Vini', "26/03/2008", "1788768326")
# p1.apresentar()



class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento,codigo,
                 estudando=True, trabalhando=True):
        super().__init__(nome, data_nascimento, codigo, estudando, trabalhando)
        self.fome = True
        self.chorando = True
        self.dormindo = False
        self.estudando =estudando
        self.trabalhando = trabalhando



    def situacao_bebe(self):
        print(f'Olá, sou irmão do bebe {self.nome},\n'
              f' meu irmão nasceu {self.data_nascimento},\n'
              f' e seu registro é{self.codigo}.\n'
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
           self.fome= False
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



s1 = Bebe('Dener', "26/03/2008", "1788768326" )
s1.situacao_bebe()

s1.trabalhar()
s1.estudar()
s1.acordar()
s1.dormir()
s1.mamar()
s1.mamar()
s1.chorar()
s1.dormir()
s1.dormir()
s1.dormir()
s1.situacao_bebe()
s1.trabalhar()




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

#
