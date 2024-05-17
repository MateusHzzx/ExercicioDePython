import random
m=random.randint(1,10)
j=int(input('tente adivinhar o número que a maquina pensou!'))
t=0
while j!=m:
    j=int(input('''a maquina escolheu um número diferente,tente novamente! 
'''))
    t+=1
print(f'o número que a maquina pensava era {m} parabéns!!!')
print(f'a quantidade de palpites foi de {t+1}')