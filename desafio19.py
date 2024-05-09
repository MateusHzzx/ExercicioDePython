import random
a1=input ('nome do aluno')
a2=input ('nome do aluno')
a3=input ('nome do aluno')
a4=input ('nome do aluno')
lista=a1,a2,a3,a4
sorteio=random.choice(lista)
print (f'o ganhador do sorteio foi {sorteio}')