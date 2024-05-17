import random
v=0
while True:
    jn=int(input('escolha um número de 1-10: '))
    c=random.randint(1,10)
    t=jn+c
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Escolha Ímpar ou Par,I/P')).upper().strip()
    print(f'você escolheu {jn} e o computador {c}. Total de {t}')
    if tipo=='P':
        if t%2==0:
            print('você venceu!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    elif tipo=='I':
            if t%2==1:
                print ('VOCÊ VENCEU!')
                v+=1
            else:
                print('VOCÊ PERDEU!')
                break
    print('vamos jogar NOVAMENTE')
print(f'o total de vitórias consecutivas foi de {v}')