#                    CONDIÇÕES ALINHADAS                    
# É usado o if se houver apenas 2 opções,se haver mais de 2 é usado elif.EXEMPLO ABAIXO
nome= str (input('qual seu nome?'))
if nome=='Mateus':
    print (f'o nome {nome} é muito raro e lindo!')
elif nome=='Pedro' or nome== 'Carlos' or nome== 'Amanda' or nome== 'Maria':
    print(f'o nome {nome} é bem comum no Brasil!!')
elif nome in"Ana Julia Bianca Liz Lara":
    print(f'o nome {nome} é um nome feminino belo')
elif nome in 'Luiz Ricardo Paulo Marcos Eric':
    print(f'o nome {nome} é um nome masculino raro de se encontrar')
else:
    print (f'o nome {nome} é muito bosta!')

print (f'Tenha um bom dia {nome}!')