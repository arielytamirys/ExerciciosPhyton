from random import randint  # randint() geram aleatoriamente um número inteiro dentro de um intervalo dado pelo usuário
from time import sleep  # O método sleep suspende a execução pelo número de segundos informado em seu parâmetro

computador = randint(0, 5) # faz p computador sortear
print("- + -" * 10)
print('Bora Advinha!!!')
jogador = int(input("Em que numero pensei?")) # o usuario digita um numero
print("- + -" * 10)
print('Pensando...')
sleep(3)
if jogador == computador:
    print("Parabens, você venceu")
else:
    print('Ganhei, pensei no numero {} e não no {}'.format(computador, jogador ))
