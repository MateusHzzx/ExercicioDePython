while True:
        n=int(input('Número que deseja: '))
        if n<=0:
            print('número negativo ou igual a 0,fechando programa')
            break
        
        print(f'tabuada do {n}')
        m=1
        while m<=10:
            r=n*m
            print(f'{n} X {m}={r}')
            m+=1
        print()