'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date # importando biblioteca de calendario
atual = date.today().year # fala é a qual o ano estamos
nasc = int(input('Ano de nacimento'))
idade = atual - nasc

print('Você nasceu em {}, e hoje tem {} anos'.format(nasc,idade))

if idade < 18:
    print('voce tem menos de 18, aguarde mais um pouco')

elif idade == 18:
    print('Voce ja tem 18 anos, pode se alistar')

else:
    print('espero que voce ja tenha se alistado')