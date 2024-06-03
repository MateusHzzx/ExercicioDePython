num=[]
mai=0
men=0
for c in range (0,5):
    num.append(int(input(f'digite o {c+1} valor:')))
    if c==0:
        mai=men=num[c]
    else:
        if num[c]>mai:
            mai=num[c]
        if num[c]<men:
            men=num[c]

print (f'os números digitados foram {num}')
print (f'o maior número foi encontrado na posiçao {mai} nas posições: ', end='')
for i,v in enumerate(num):
    if v==mai:
        print (f'{i}...', end='')
print()
print (f'o menor valor foi {men} nas posições: ', end='')
for i,v in enumerate(num):
    if v==men:
        print (f'{i}...', end='')
print()