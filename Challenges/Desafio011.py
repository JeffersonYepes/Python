b = float(input('Enter the width of the wall (in meters): '))
h = float(input('Enter the height of the wall (in meters): '))
a = b * h
ink = a / 2
print('It will take {} Litres of paint to cover {} m² of wall.'.format(ink, a))
