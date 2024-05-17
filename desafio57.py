sexo=input('Qual o sexo da pessoa M/F?  ').strip().upper()
while sexo!='M' and sexo!='F':
    print('Opção incorreta,tente novamente!')
    sexo=input('qual o sexo da pessoa?M ou F?  ').strip().upper()
input(f'seu sexo é {sexo},certo?')