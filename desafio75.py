
a=(int(input('Número: ')),int(input('Número: ')),int(input('Número: ')),int(input('Número: ')))
print(f'os números selecionados foram: {a}')
print(f'o número 9 apareceu um total de: {a.count(9)}')
if 3 in a:
    print(f'a posição que aparece o primeiro 3 é: {a.index(3)}')
print(f'os números pares foram: ', end=' ')
for n in a:
    if n%2==0:
        print(n, end=' ')