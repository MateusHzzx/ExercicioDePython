from random import randint
from operator import itemgetter
from time import sleep
jogadas={
    'Jogador 1':randint(0,6),
    'Jogador 2':randint(0,6),
    'Jogador 3':randint(0,6),
    'Jogador 4':randint(0,6),
}
for nome,número in jogadas.items():
    print(f'o {nome} jogou o número {número}')
    
ranking=sorted(jogadas.items(),key=itemgetter(1),reverse=True)
print('=-=-=-'*10)
print('            =-=-RANKING-=-=')
for i,v in enumerate(ranking):
    print(f'           {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('=-=-=-'*10)