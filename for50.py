'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.'''
from time import sleep

print('Digite o numero que você esta pensando, e somaremos os numeros pares')
print('=======================================================================')
soma = 0
cont = 0
for n in range(1, 7):
     num = int(input(f'Qual {n} numero você, penso ?'))
     if num % 2 == 0:
          soma += num
          cont += 1
    
     print(f'Você informou {cont} pares, a soma destes numero é de {num}')






