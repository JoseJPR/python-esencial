a = 1
b = 2

if a < b:
    print('A es menor que B')

c = 2
d = 1

if c < d:
    print('C es menor que D')
else:
    print('C es mayor que D')

e = 1
f = 1

if e < f:
    print('E es menor que F')
elif e > f:
    print('E es mayor que F')
else:
    print('E es igual a F')

x = True

if x:
    print('X es verdadero')
else:
    print('X es falso')

if type(x) is bool:
    print('X es boolean')
else:
    print('X no es boolean')

y = 1
z = 2

if y == 1 and z == 2:
    print('Y es uno y Z es dos')
else:
    print('Alguno de los valores es erroneo')

xx = 2
yy = 6

if yy == 1 or xx == 2:
    print('O xx o yy es correcto')
else:
    print('Ninguno es correcto')