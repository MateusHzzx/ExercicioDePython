s=0
cont=0
for c in range(1,501,2):
    if c % 3==0:
        print(c)
        s=s+c
        cont=cont+1
print(f'a soma dos {cont} vai ser {s}')