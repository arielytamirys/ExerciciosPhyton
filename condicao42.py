'''Mostre o tipo de triangolo que sera formado: -Equilatero, -isoscels, -escaleno.'''

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem forma um Triangulo:')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Equilatero')
    else:
        print('Escaleno')
else:
    print('Os segmentos acima podem não forma um Triangulo!')