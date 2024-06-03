lista=[]
num=0
cincão=0
while True:
    n=int(input('Digite um número: '))
    num+=1
    if n==5:
        cincão+=1
    lista.append(n)
    r=str(input('Deseja continuar?[S/N]')).upper().strip()
    while r not in 'SN':
        r=str(input('Deseja continuar?[S/N]')).upper().strip()
    if r=='N':
        break   
lista.sort(reverse=True)    
print(f'a quantia de números digitados foi {num}')
print(f'a lista ordenada em ordem decrescente é: {lista}')
if 5 in lista:
    print(f'o valor 5 foi digitado {cincão} vezes e está na lista')
else:
    print('o cinco não está na lista')