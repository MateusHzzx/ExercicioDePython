s = 0

for c in range (0,6):
    n=int(input(f'escolha o {c+1} número inteiro'))
    if n%2==0:
        s = s + n

print(f'a soma entre os números pares é de {s}.')