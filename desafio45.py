import random
esco=('tesoura','pedra','papel')
maq=random.randint(0,2)
print('''faça sua escolha
[0]tesoura
[1]papel
[2]pedra''')
opc=int (input('escolha'))
print (f'''jogador:{opc}
 maquina{maq}''')

print('==='*30)
if maq==0:
    if opc==0:
         print('empate')
    elif opc==1: 
     print('jogador perde')
    elif opc==2:
     print ('jogador vence')
    else:
     print('jogada incorreta')
elif maq==1:
    if opc==1:
         print('empate')
    elif opc==0: 
     print('jogador vence')
    elif opc==2:
     print ('jogador perde')
    else:
     print('jogada incorreta')
elif maq==2:
    if opc==2:
         print('empate')
    elif opc==1: 
     print('jogador vence')
    elif opc==0:
     print ('jogador perde')
    else:
     print('jogada incorreta')
