import random
a1=str(input ('Qual nome do primeiro aluno?'))
a2=str(input ('Qual nome do segundo aluno?'))
a3=str(input ('Qual nome do terceiro aluno?'))
a4=str(input ('Qual nome do quarto aluno?'))
lista=[a1,a2,a3,a4]
random.shuffle (lista)
print ('a ordem de apresentaçao sera')
print(lista)
result = " e ".join(lista)
print(result)