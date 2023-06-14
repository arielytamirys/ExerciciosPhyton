'''A confederação de natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua caregoria, de acordo com a idade:'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano do nascimento:'))
idade = atual - nascimento
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação Mirim')
elif idade <= 14:
    print("classificação: Infantil")
elif idade <= 19:
    print("classificação: Junior")
elif idade <= 25:
    print("classificação: Senior")
else:
    print('classificação: Master')