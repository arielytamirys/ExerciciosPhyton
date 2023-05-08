n = int(input("Digite um numero:"))
d = n * 2  # numero digitado x dobro
t = n * 3  # tripo
r = n ** (1 / 2)  # raiz quadradrada do mesmo

print(" O dobro do numero {} é igual a {} ".format(n, d))
print(" O triplo do numero {} é igual a {} ".format(n, t))
print(" A Raiz Quadrada do numero {} é igual a {:.2f} ".format(n, r))
