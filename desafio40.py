n=float (input('digite sua primeira nota'))
n1=float (input('digite sua segunda nota'))
t=(n1+n)/2
print (f'a sua nota final foi de {t}')
if t<5.0:
    print (f'\033[31m'+'REPROVADO!'+'\033[0;0m')
elif t>7:
    print(f'\33[32m'+'APROVADO''\033[0;0m')
else:
    print(f'\33[35m''RECUPERAÇÃO''\033[0;0m')