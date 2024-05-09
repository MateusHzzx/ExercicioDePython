a=int (input('em que ano você naceu?'))
at=2024-a
o=18-at
i=at-18
print (f'agora você tem {at} anos,então...')
if at>18:
    print('já passou do tempo de alistamento!')
    print (f'você tinha que ter se alistado á {i} atrás,SE FUDEU!')
elif at==18:
    print(f'está na hora de se alistar,ANDA VAGABUNDO!')
else:
    print (f'você só irá se alistar daqui a {o} anos')