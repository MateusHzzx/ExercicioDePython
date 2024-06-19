pessoas=[]
while True:
    nome=str(input('Qual o nome da pessoa? '))
    sexo=str(input('Qual o sexo da pessoa?[M/F] ')).upper().strip()
    idade=int(input('Qual a idade da pessoa? '))
    pessoa={"nome":nome,"sexo":sexo,"idade":idade}
    
    pessoas.append(pessoa)
    while sexo not in 'FM':
        sexo=str(input('Qual o sexo da pessoa?[M/F] ')).upper().strip()
    resp=str(input('Deseja adicionar outra pessoa?[S/N] ')).upper().strip()
    while resp not in 'SN':
        resp=str(input('Deseja adicionar outra pessoa?[S/N] ')).upper().strip()
    if resp=='N':
        break
for pessoa in pessoas:
    print(f'Nome {pessoa["nome"]}')