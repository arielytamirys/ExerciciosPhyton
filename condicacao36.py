'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.'''

casa = float(input('Valor da casa R$:'))
salario = float(input('Qual o salario do comprador R$:'))
anosDefinan = int(input('Quantos anos o finaciamento?'))
prestacao = casa / (anosDefinan * 12)  #conta feita para saber o valor de paecelas da casa


mininoSalario = salario * 30 / 100 # qui diz que: para ser aprovado o valor de parcelas deve ser de 30% do salario

print('Valor da Casa: {:.2f}'.format(casa))
print('Anos de Finaciamento: {}'.format(anosDefinan))
print('As Prestaçoes sera de: {:.2f}'.format(prestacao))

if prestacao <= mininoSalario:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')


