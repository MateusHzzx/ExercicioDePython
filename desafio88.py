from random import randint 
from time import sleep
 
a=int(input('Quantos jogos deseja que eu sorteie?'))
 
print(f'-=-=-sorteando {a} jogos-=-=-')
sleep(1)
for c in range(a):
    lista=[randint(1,60) for l in range (6)]
    print(f'jogo {c+1}: {lista}')
    sleep(1)