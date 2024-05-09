n=int (input('bota um numero ae'))
print('''qual base de conversão você deseja?
[1]binário
[2]octal
[3]hexadecimal''')
e=int (input('sua escolha é'))
print('===='*25)
if e==1:
    print(f'a conversão de {n} para binário é de {bin(n)[2:]}')
elif e==2:
    print(f'a conversão de {n} para octal é de {oct(n)[2:]}')
elif e==3:
     print(f'a conversão de {n} para hexadecimal é de {hex(n)[2:]}')
else:
    print ('a opção não existe,tente novamente seguindo a ordem')