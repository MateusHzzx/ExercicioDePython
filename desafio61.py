p=int(input('qual o primeiro termo da sua PA'))
r=int(input('qual a primeira razão de sua PA'))
ta=p
cont=1
print ('os 10 primeiros termos de sua razão é: ')
while cont<=10:
    print(ta)
    ta+=r
    cont +=1
print()