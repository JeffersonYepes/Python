n = input('Type something: ')
menu = int(input('What do you want to know about this object?\n[1] Type\n[2] This is a number?\n[3] This is alphabetic?\n[4] This is alphanumeric?\nChoose an option: '))
if menu == 1:
    print('Type {}'.format(type(n)))
if menu == 2:
    print('This is a number? {}'.format(n.isnumeric()))
if menu == 3:
    print('This is a letter? {}'.format(n.isalpha()))
if menu == 4:
    print('This is alphanumeric? {}'.format(n.isalnum()))

#print('O que você digitou tem as seguintes caracteristicas:')
#print('Tipo primitivo {}'.format(type(n)))
#print('Ele pode ser um número? {}'.format(n.isnumeric()))
#print('Ele pode ser uma letra? {}'.format(n.isalpha()))
#print('Ele está em letra maiuscula? {}'.format(n.isupper()))
#print('Ele está em letra minuscula? {}'.format(n.islower()))
    print('This is alphanumeric? {}'.format(n.isalnum()))