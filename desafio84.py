temp = []
princ = []
mai=men=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ)==0:
        maior=menor=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer Continuar? ')).upper().strip()
    while resp in 'SN':
        resp=str(input('Quer Continuar? ')).upper().strip()
    if resp=='N':
        break
print ('=-=-='*20)
print (f'os dados foram {princ}')
print(f'ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg')
for p in princ:
    if p[1]==mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men}Kg')
for p in princ:
    if p[1]==men:
        print(f'{p[0]}')