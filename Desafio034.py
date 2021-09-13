sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250.00:
    print('O novo salário será de R${:.2f} com 10% de aumento!'.format(sal + (sal * 10 / 100)))
else:
    print('O novo salário será de R${:.2f} com 15% de aumento!'.format(sal + (sal * 15 / 100)))
