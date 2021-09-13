from math import hypot
print('****** Calculadora de Hipotenusa ******')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
print('O valor da hipotenusa do triângulo retângulo cujo os catetos são {} e {} é igual a {:.3f}.'.format(co, ca, hypot(co,ca)))
