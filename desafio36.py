v=float (input('quanto custa a casa?'))
s=float (input('qual sua renda mensal?'))
a=int(input('em quantos anos deseja pagar?'))
soma=v / (a*12)
ao=s*0.30
print (f'a prestação da cassa será de {soma:.2f}')
print (f'30% do seu seu salário seria {ao}')
print(f'calculando que 30% do seu salário é {ao} e a prestação é de {soma} para pagar em {a} anos então...')
print('==='*20)
if soma<=ao:
    print ('O SEU EMPRESTIMO FOI CONCEDIDO!')
else:
    print ('EMPRÉSTIMO NEGADO')