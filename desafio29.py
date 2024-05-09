c=float (input('quantos km/h seu carro está?'))
if c>80:
    multa=(c-80)*7
    print (f'você excedeu o limite da via que é de 80,o total a pagar é de R${multa:.2f}')
else:
    print ('tenha um bom dia,seja sempre certo!')
