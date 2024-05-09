p=float(input('qual o preço do produto'))
print('''QUAL A FORMA DE PAGAMENTO?
[1]Á VISTA NO DINHEIRO/CHEQUE
[2]Á VISTA NO CARTÃO
[3]2X NO CARTÃO
[4]3X OU MAIS NO CARTÃO''')
o=int (input('oque deseja?'))
print('==='*20)
if o==1:
    c=p*0.10
    c1=p-c
    print('há um desconto de 10%,por ser em dinheiro')
    print(f'o preço a pagar após o desconto é de R${c1}')
elif o==2:
    c=p*0.05
    c1=p-c
    print ('há um desconto de 5%')
    print(f'o preço após desconto é de {c1}')
elif o==3:
    c=p/2
    print(f'o preço parcelado em 2X é de {c}')
else:
    e=p/3
    c=e*0.20
    c1=e+c
    print(f'o valor a pagar,com juros mensal é de {c1} ')