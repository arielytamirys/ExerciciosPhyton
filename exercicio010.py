real = float(input("quanto você tem em Reais?: R$"))
dolar = real / 5.01
euro = real / 5.51
pesosAgentinos = real / 0.022
print('Você tem: {:.f2} Dolares, {:.f2} Euros, {:.f2} Pesos Argentinos'.format(dolar, euro, pesosAgentinos))