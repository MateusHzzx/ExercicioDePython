#_________________________CONTINUAÇÃO DE LISTAS_________________________
# teste=list()
# teste.append('Carlos')
# teste.append(18)
# galera=list()
# galera.append(teste[:])
# teste[0]='Maria'
# teste[1]=22
# galera.append(teste)
# print (galera)
# galera=[['João',29],['Carlos',22],['Gustavo',15],['Cleitin',89]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')
galera=list()
dado=[]
mai=men=0
for c in range (0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        mai+=1
    else:
        if p[1]<21:
            print (f'{p[0]} é menor de idade')
            men+=1
print(f'temos um total de {mai} maiores de idade e {men} menores de idade')