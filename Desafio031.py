print('*** Calculadora de preço de passagem ***\n')
d = float(input('Digite a distância da viagem em Km: '))
p = d * 0.50 if d <= 200 else d * 0.45
print('Você deverá pagar: R${:.2f}'.format(p))
