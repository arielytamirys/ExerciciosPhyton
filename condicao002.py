velocidade = float(input('Digite sua velocidade:'))
if velocidade > 60:
    print('Você excedeu a  velocidade de 60 kms/h!')
    multa = (velocidade - 60) * 8 # apos 60 kms, gerar multa de 8 reais cada.
    print('você deve pagar a multa de R$ {:.2f}'.format(multa))
    print("Tenha um bom dia, Dirija com segurança!")
