n1=int (input('digite um numero'))
n2=int (input('digite outro numero'))
print ('====='*25)
if n1>n2:
    print (f'o primeiro valor é maior')
elif n2>n1:
    print (f'o segundo valor é maior')
else:
    print (f'não existe valor maior,ambos os números são iguais')
