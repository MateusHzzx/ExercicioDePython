from datetime import datetime
dados=dict()
dados['nome']=str(input('Seu nome: '))
nasc=int(input('Sua data de nascimento: '))
dados['idade']=datetime.now().year-nasc
dados['ctps']=int(input('Carteira de Trabalho(0 não tem)'))
if dados['ctps']!=0:
    dados['contrato']=int(input('Ano de Contratação: '))
    dados['salário']=float(input('Qual o seu salário?'))
    dados['aposentadoria']=dados['idade']+(dados['contrato']+35)-datetime.now().year
print(f'Seu nome é {dados['nome']}')
print(f'Sua idade é de {dados["idade"]} anos')
print(f'Sua CTPS é {dados['ctps']}')
print(f'Seu ano de contrato é {dados['contrato']}')
print(f'Seu salário é de R${dados['salário']}')
print(f'Sua aposentadoria vai ser com {dados['aposentadoria']} anos!')