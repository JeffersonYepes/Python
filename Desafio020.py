from random import shuffle
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
ordem = [a1, a2, a3, a4]
shuffle(ordem)
print('A ordem sorteada é: {}'.format(ordem))