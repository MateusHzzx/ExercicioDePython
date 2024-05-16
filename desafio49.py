n = int(input('Digite um número para ver sua tabuada: '))
e=int (input('ate que numero deseja multiplicar'))
print ('aqui está a tabuada de {n}')
for c in range (1,e+1):
    print(f'{n}x{c}={n*c}')