n1=float(input('escreva a primeira reta'))
n2=float(input('escreva a segunda reta'))
n3=float(input('escreva a terceira reta'))
if n1<n3+n2 and n2<n1+n3 and n1<n2+n3:
    print('essas retas PODEM FORMAR um triangulo,sendo ele:')
    if n1==n2==n3:
        print('EQUILÁTERO')
    if n1==n2!=n3 or n1==n3!=n2 or n2==n3!=n1:
        print ('ISÓSCELES')
    if n1!=n2!=n3!=n1:
        print('ESCALENO')