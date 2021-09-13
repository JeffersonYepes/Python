from random import choice
print('****** Sorteio de Alunos ******')
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
print('O aluno escolhido é: {}'.format(choice([a1, a2, a3, a4])))
