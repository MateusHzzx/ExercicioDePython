tg=cm=nb=cont=0
barato=' '
while True:
    print ('-------------------------------------------------')
    print ('               LOJA DO MATEUS                    ')
    print ('-------------------------------------------------')
    n=str(input('Qual o nome do Produto?'))
    p=float(input('Qual o preço do produto? R$'))
    cont+=1
    tg+=p
    if p>1000:
        cm+=1
    if cont==1:
        nb=p
        barato=n
    else:
        if p<nb:
            nb=p
            barato=n
    r=' '
    while r not in 'SN':
        r=input('Deseja continuar as compras?[S/N]').upper().split()[0]
    if r=='N':
        break
print('compras finalizadas')
print(f'o total gasto foi de R${tg}')
print(f'os produtos que custam mais de R$1000 é de {cm}')
print(f'o nome do produto mais barato é de {barato} e seu custo é de R${nb}')