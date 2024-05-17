n=s=c=0
while True:
    n=int(input('digite um número: "999 para parar"'))
    c+=1
    if n==999:
        break
    s+=n
print(f'a quantidade de números foi de {c} e a soma entre eles foi de {s}')