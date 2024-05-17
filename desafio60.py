n=int(input('digite o número que deseja saber o fatorial: '))

if n<0:
    print('fatorial negativo ou igual a 0 não é calculavel')
else:
    fatorial=1
    contador=1

while contador<=n:
    fatorial*=contador
    contador+=1
print(f'o valor do fatorial {n}! é {fatorial}')