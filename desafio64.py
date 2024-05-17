n=int(input('digite um número inteiro: '))
soma=0
qn=0
while n!=999:
    n=int(input('digite novamente'))
    soma+=n
    qn+=1
print(f'a quantidade de números digitados foi de {qn+1} e o cálculo entre todos os números tirando o 999 foi de {soma-999}')