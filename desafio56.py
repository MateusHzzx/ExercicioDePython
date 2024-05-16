m=0
mv=0
mn=0
nmv=''
for c in range (1,5):
    nome=input(f'fale o nome da {c} pessoa?')
    i=int(input(f'qual a idade da {c} pessoa?'))
    sexo=int(input('''qual o sexo da {c} pessoa?
          [1]masculino
          [2]feminino'''))
    if sexo==1:
        if i>mv:
            mv=i
            nmv=nome
    elif sexo==2:
        if i<18:
            mn=mn+1
md=m/4
print (f'a média de idade do grupo é {md}')
print (f'o nome do homem mais velho é {mv}')
print(f'a quantidade de mulheres menores de idade é [mn]')