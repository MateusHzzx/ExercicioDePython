n=int (input('fale um número'))
p=0
for c in range (2,n):
    if n%c==0:
        p=1
if p==0:
    print ('seu número é primo')
else:
    print('seu número não é primo')