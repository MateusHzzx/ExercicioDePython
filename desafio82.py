lista1=[]
lista2=[]
lista3=[]
par=ímpar=0
while True:
    n=int(input('Digite um valor: '))
    lista1.append(n)
    r=str(input('Deseja continuar?[S/N]')).upper().strip()
    while r not in 'SN':
        r=str(input('Deseja continuar?[S/N]')).upper().strip()
    if r=='N':
        break
    if n%2==0:
        lista2.append(n)
        par+=1
    else:
        if n%2==1:
            lista3.append(n)
            ímpar+=1
print(f'''as listas foram:
     {lista1} 
     a lista com apenas valores pares foi:
     {lista2} total de {par} números pares
     a lista com apenas valores ímpares foi:
     {lista3} total de {ímpar} números ímpares''')