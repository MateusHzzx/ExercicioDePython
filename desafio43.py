a=float(input('qual a sua altura?'))
p=float(input('qual seu peso?'))
imc=p/(a*a)
print (f'seu IMC com base na sua altura e peso é de {imc:.2f}')
if imc<18.5:
    print ('\033[91m''ABAIXO DO PESO''\033[0;0m')
elif imc>=18.5 and imc<=25:
    print ('\33[94m''PESO IDEAL''\033[0;0m')
elif imc>=25 and imc<=30:
    print ('\33[34m''SOBRE PESO''\033[0;0m')
elif imc>=30 and imc<=40:
    print('\33[31m''OBESIDADE''\033[0;0m')
else:
    print ('\33[30m''OBESIDADE MÓRBIDA''\033[0;0m')