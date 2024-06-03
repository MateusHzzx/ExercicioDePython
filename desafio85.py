n=[[],[]]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c} valor: '))
    if valor%2==0:
        n[0].append(valor)
    else:
        if valor % 2==1:
            n[1].append(valor)
n[0].sort
n[1].sort
print (f'os valores pares são {n[0]}')
print (f'os valores impares são {n[1]}')