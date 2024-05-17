p=int(input('primeiro termo: '))
r=int(input('razão: '))
ta=p
cont=1
tt=10
mt=-1
while mt !=0:
    while cont<=tt:
        print(ta)
        ta+=r
        cont+=1
    print()

    mt=int(input('quantos termos você deseja a mais?'  'digite 0 para sair'))
    tt+=mt
print ('programa encerrado!')