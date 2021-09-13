n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#feito em aula
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))


'''if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
        if n2 > n3:
            print('O menor número é {}'.format(n3))
        else:
            print('O menor número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))
        print('O menor número é {}'.format(n2))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
        if n3 > n1:
            print('O menor número é {}'.format(n1))
        else:
            print('O menor número é {}'.format(n3))
    else:
         print('O maior número é {}'.format(n3))
         print('O menor número é {}'.format(n1))
'''