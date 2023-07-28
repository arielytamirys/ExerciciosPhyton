'''o simbolo ^ significa centralizado em 30 espaços '''
print('{:/^50}'.format('  lojas Santos  '))
preço =float(input('Preço das Compras: R$ '))
print('''Formas de Pagamento
[ 1 ] á vista dinheiro ou pix
[ 2 ] á  vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x vezes ou mais no cartão...''')
opcao = int(input(' Qual é a opção ?'))
if opcao == 1:
    '''cota de porcetagem '''
    total = preço - (preço * 15 / 100)
elif opcao == 2:
    total = preço - (preço * 8 / 100)
elif opcao == 3:
    total = preço / 2
    print(f'Sua compra de R${preço:.2f}, sera parcelada em 2 vezes de R${total:.2f}, sem juros')
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalpar = (int(input('Quantas parcelas ?')))
    parcela = total / totalpar
    print(f'O total da compra foi R$ {preço} com em {totalpar}x , cada valor de parcela com juros ficou em R${parcela} por mês.')





print(f'Sua compra no valor total de R${preço:.2f} com desconto, vai custar R${total:.2f}')


