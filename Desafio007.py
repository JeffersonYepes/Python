print('=== Grade Average Calculator ===')
name = str(input('Student name: '))
n1 = float(input('Type the first grade: '))
n2 = float(input('Type the second grade: '))
a = (n1+n2) / 2
print('The Grade Average of {} is {:.1f}'.format(name, a))
