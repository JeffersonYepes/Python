frase = str(input('Digite uma frase: ')).upper().strip()
#tam = len(frase)
#print(tam)
#ult = frase
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {} e por último na posição {}.'.format(frase.find('A')+1, frase.rfind('A')+1))
