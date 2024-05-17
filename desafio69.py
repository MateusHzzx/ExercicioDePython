t18=h=m20=0
while True:
    print('---------------CADASTRE UMA PESSOA---------------')
    idade=int(input('Idade: '))
    sexo='  ' 
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F]')).upper().strip()[0]
        if idade>18:
            t18+=1
        if sexo=='M':
            h+=1
        if sexo=='F' and idade<20:
            m20+=1
    c=input ('Quer continuar?[S/N]').upper().strip()
    while c not in 'SN':
        c=input ('Quer continuar?[S/N]').upper().strip()
    if c=='N':
        print('CADASTRO ACABADO')
        break
    else:
        print ('')
print(f'nos cadastros há {t18} pessoas com mais de 18 anos')
print(f'ao total foram {h} homens cadastrados')
print(f'o total de mulheres que tem menos de 20 anos é de {m20}')