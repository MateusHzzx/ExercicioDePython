n=int(input('digite um número inteiro: '))
if n<=0:
    print('digite um número que não seja 0 por favor!!!')
else:
    a,b=0,1
    count=0
    while count<n:
        print(a)
        a,b=b,a+b
        count+=1   
    print()