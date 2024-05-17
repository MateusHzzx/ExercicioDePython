from datetime import date
maior=0
menor=0
atual=date.today().year
for c in range(0,7):
    n=int(input(f'informe a data de nascimento da {c+1} pessoa: '))
    idade=atual-n
    if idade>=18:
        maior+=1
    else:
        menor+=1
print(f'''no total foram:
{maior} maiores de idade
{menor} menores de idade''')