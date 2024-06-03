a=list()
while True:
    b=int(input('Digite um Número:'))
    if b not in a:
        a.append(b)
        print ('Valor adicionado com sucesso')
    else:
        print('Já existe esse valor,não será adicionado')
    r=str(input('Deseja continuar?[S/N]')).upper().strip()
    while r not in 'SN':
        r=str(input('Deseja continuar?[S/N]')).upper().strip()
    
    
    if r in 'N':
        break
a.sort()
print(f'os valores digitados foram: {a}')