print('*** RADAR ***')
vel = float(input('Digite a velocidade do veículo em Km/h: '))
if vel > 80:
    m = 7 * (vel-80)
    print('Você excedeu o limite de velocidade! Você foi multado em R${:.2f}!'.format(m))
else:
    print('Velocidade dentro do limite!')
