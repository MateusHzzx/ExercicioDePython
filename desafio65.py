c='S'
s=q=m=maior=menor=0
while c in 'Ss':
    n=int(input('digite um número'))
    s+=n
    q+=1
    if q==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    c=str(input('Deseja continuar? S/N')).upper().strip()[0]
media=s/q
print(f'você digitou um total de {q} números e a média foi de {media}')
print(f'o maior número foi {maior} e o menor número foi {menor}')