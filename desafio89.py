ficha=list()
while True:
    nome=str(input('Nome:'))
    nota1=float(input('Nota1: '))
    nota2=float(input('Nota2: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input('Deseja continuar?[S/N]')).upper().strip()
    while resp not in 'SN':
        resp=str(input('Deseja continuar?[S/N]')).upper().strip()
    if resp=='N':
        break
print('-=-=-=-'*20)
print(f'{'NO.':<4}{'Nome':<10}{'Média':>8}')
print('___'*20)
for i,a in enumerate(ficha):
        print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')