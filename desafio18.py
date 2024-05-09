import math
ca = float (input('numero do cateto adjacente'))
co = float (input('numero do cateto opoto'))
soma1=ca**2
soma2=co**2
total=soma1+soma2
hipotenusa=math.sqrt(total)
seno=soma2/hipotenusa
cosseno=soma1/hipotenusa
tangente=soma1/soma2
print (f'o seno é {seno} seu cosseno é {cosseno} e seu tangente é {tangente}')