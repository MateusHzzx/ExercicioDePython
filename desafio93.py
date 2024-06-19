fut=dict()
partidas=list()
fut['jogador']=str(input('Nome do jogador: '))
tot=int(input('Quantas partidas jogadas? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
fut['gols']=partidas[:]
fut['total']=sum(partidas)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-')
print(fut)
for k,v in fut.items():
    print(f'O campo {k} tem o valor {v}')
    
print(f'O jogador {fut['jogador']} jogou {len(fut["gols"])} partidas')
for i,v in enumerate(fut['gols']):
    print(f'       NA PARTIDA {i} FEZ {v} GOLS.')