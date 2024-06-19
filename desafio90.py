aluno=dict()

aluno['nome']=str(input('Qual o nome do Aluno? '))
aluno['média']=float(input(f'Qual a média de {aluno['nome']} ? '))

if aluno['média']>=6.0:
    print(f'O nome do aluno é {aluno['nome']}')
    print (f'A sua média é {aluno["média"]}')
    print (f'\33[32m'+'__________APROVADO__________''\033[0;0m')
else:
    print(f'O nome do aluno é {aluno['nome']}')
    print (f'A sua média é {aluno["média"]}')
    print(f'\33[35m''REPROVADO''\033[0;0m')