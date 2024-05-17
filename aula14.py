# c=0
# while c < 11:
#     print(c)
#     c+=1
# print("======"*20)
# print ('                                                    FIM')
# r='S'
# while r=='S':
#     n=int (input('Digite um valor: '))
#     r=str (input('Deseja continuar?[S/N]')).upper()
n = 1
par=impar=0
while n!=0:
    n=int(input('digite um valor: '))
    if n!=0:
        if n  % 2==0:
            par+=1
        else:
            impar+=1
print(f'a quantidade de números pares é de {par}')
print (f'já a quantidade de números impares é de {impar}')