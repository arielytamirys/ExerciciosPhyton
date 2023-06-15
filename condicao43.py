'''faça ym programa que calcule o indice de massa corporal (ImC) e mostre seus status'''

peso = float(input('Qual o seu Peso:'))
altura = float(input('Qual sua Altura:'))
'''calculo de imc'''
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso normal')
    '''se o imc for menor ou igual a 18.5 ou menor que 25 ...'''
elif 18.5 <= imc < 25:
    print('voce esta com o peso ideal')
elif 25.1 <= imc < 30:
    print('voce esta com sobre peso')
elif 30.1 <= imc < 40:
    print('Voce esta Obeso')
else:
    print('Voce esta com obesidade Morbida')



