from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
print('Ângulo: {} \nSeno: {:.3f} \nCosseno: {:.3f} \nTangente: {:.3f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
