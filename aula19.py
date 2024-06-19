from time import sleep
#__________________________________________________-DICIONÁRIOS-______________________________________________________________
#                                           dados=dict() ou dados={}
# dados={'nome':'Pedro','idade':25}
# print (dados['nome'])
# print (dados['idade'])
# dados['sexo']='M'
# print (dados['sexo'])
# del dados['idade']
#                              PRÁTICA                              
# pessoa={'nome':'Mateus','sexo':'M','idade':15}
# print (f'Seu nome é {pessoa["nome"]},sua idade é {pessoa["idade"]} e o seu sexo é {pessoa["sexo"]}')
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
# for k in pessoa.keys():
#         print(k)
# pessoa['idade']=20
# pessoa['peso']=60.5#Para adicionar outro elemento não precisa se utilizar o append.
# for k,v in pessoa.items():
#         print(f'{k} = {v}')
#         sleep(0.5)
# print('-=-=-=-=-FIM-=-=-=-=-')
Brasil=[]
estado1={'UN':'Rio de Janeiro','Sigla':'RJ'}
estado2={'UN':'São Paulo','Sigla':'SP'}
Brasil.append(estado1)
Brasil.append(estado2)

print (Brasil)
# estado=dict()
# brasil=list()
# for c in range(0,3):
#     estado['UF']=str(input('Unidade Federativa: '))
#     estado['Sigla']=str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# print(brasil)
# print(estado)
# for e in brasil:
#     for k,v in e.items():
#         print(f'A {k} é {v}')
    # for v in e.values():
    #     print(k,end='')
    # print()
   