print('****** Calculadora de aumento salarial ******')
s = float(input('Digite o salário atual do funcionário: R$'))
r = float(input('Qual será o aumento dele (em %) ? '))
print('O novo salário do funcionário será de R${:.2f}.'.format(s+(r*s/100)))
