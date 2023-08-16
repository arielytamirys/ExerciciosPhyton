'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
primeiro = int(input('Primeiro Termo : '))
razao = int(input('Razâo : '))
descimo = primeiro + ( 11 -1 ) * razao # para calcular até 10 numeros, foi feita esta conta.
for c in range (primeiro,descimo  , razao):
    print(f'{c}', end= '> ' )
print('FIM')
