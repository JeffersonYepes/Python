print('='*60)
p = float(input('Digite a quantidade de Km percorridos: '))
d = int(input('Quantidade de dias do aluguel: '))
#R$60 por dia e R$0,15 por Km rodado
print('Você terá que pagar R$ {:.2f} pelo aluguel do carro.'.format(60*d + 0.15*p))
print('='*60)
