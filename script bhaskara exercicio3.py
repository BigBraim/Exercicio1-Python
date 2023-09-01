print ('Escreva os valores a, b, c ')
a = int( input ('Escreva os valor de a:'))
b = int( input ('Escreva os valor de b:'))
c = int( input ('Escreva os valor de c:'))

delta = b**2 - 4*a*c
x1 = (((-1)*b) + (delta**0.5))/(2*a)
x2 = (((-1)*b) - (delta**0.5))/(2*a)

if delta == 0:
    print ('x1 = x2 =', x1)

elif delta<0:
    print('x1: ', x1)
    print('X2: ', x2)
    print('Delta: ', delta)
    
else:
    print('Raiz nao existe')



