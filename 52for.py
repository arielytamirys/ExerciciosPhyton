num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0: # se num for divisivel por c começando do 0.
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
    print('O num')
