import random
m=random.randint(1,5)
u=int (input('tente advinhar o numero de 1 a 5'))
if m==u:
    print ('você acertou o número')
else:
    print (f'não foi dessa vez o número era {m}')