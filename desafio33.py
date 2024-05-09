n1=int (input('fale um numero'))
n2=int (input('fale outro numero'))
n3=int (input('fale outro numero'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#VERIFICANDO
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n2 and n3>n1:
    maior=n3
print (f'o menor número é {menor}')
print(f'o maior número é {maior}')