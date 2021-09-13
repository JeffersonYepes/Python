r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('É triângulo!')
else:
    print('Não é triângulo!')
