maior=0
menor=0
for c in range (0,5):
    n=float(input('quanto você pesa?'))
    if c==1:
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
print (f'o maior peso é {maior} e o menor peso é {menor}')