''''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se
encontram no intervalo de 1 até 500.'''
soma = 0
contador = 0
for n in range (1, 501, 2):
    if n % 3 == 0: #conta feita para mostrar os divisores de 3
        contador = contador + 1  #contador
        soma = soma + n  #acumulador
print(f'a soma de {contador} valores solicitados é {soma}')
