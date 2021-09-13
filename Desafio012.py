print('Calculadora de descontos')
d = float(input('Digite o desconto (em %): '))
p = float(input('Valor do produto: R$'))
print('O valor final do produto com um desconto de {}% cai custar R${:.2f}.'.format(d, p-(d*p/100)))
