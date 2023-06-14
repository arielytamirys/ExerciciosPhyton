'''Faça a media entre duas notas ,e fale no fim se o aluno foi reprovado ou não'''

print('Ola vamos ver sua media de nota.')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2 ) / 2
print('a primeira nota foi {:.1f} a segunda {:.1f}, a media dessa notas é de: {:.1f}'.format(nota1, nota2, media))

'''se a media for maior ou igual a cinco ou menor que 7 aluno esta reprovado'''
if media >=5 and media < 7:
    print('Aluno esta de recuperação')
elif media < 5:
    print('Aluno esta reprovado')
else:
    print('Aluno esta Aprovado')
