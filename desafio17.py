import math
ca = float (input('numero do cateto adjacente'))
co = float (input('numero do cateto opoto'))

soma= ca**2+co**2
hipotenusa=math.sqrt(soma)
print ('________________________________________________________')
print (f'o calculo entre {ca} e {co} é igual a hipotenusa de {hipotenusa}')