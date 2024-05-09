# aula de hoje é como manipular uma cadeia de texto
# frase = 'curso em video python'
# #fatiar uma string é conseguir pegar pedaços dela
# frase[9]
# frase [9:19] indica o inicio e o final
# frase [:5] não foi indicado inicio ou seja,irá pegar tudo antes do cinco
# frase [9:21:1] indica o inicio e o final,mas por conta do 1 ele irá pulando de 1 em 1 até o final
# frase [15:] não foi indicado um final ou seja,ira parar o quando acabar a frase
# frase [9::3]  o 9 é onde inicia,como não tem nada no meio ira até o final pulando de 3 em 3
# Analise-como o nome já diz irá analisar a string,sabendo a quantidade de letras e etc
# len(frase) len siginifica lenght ou seja comprimento da frase
# frase.count('o') pede para contar quantas letras O tem na frase,ou qualquer outra letra
# frase.count ('o',0,13) ira coniderar de n até o outro n,ou seja vai contar quantass letras tem do 0 até 13
# frase.find('deo') dirá quantas vezes encontrou a palavra desejada,ou seja ira dizer em que momento começou oque você pediu
# frase.find('android')se você colocar uma palavra que não exista na sua frase ele retornará o número -1 ou seja,não foi encontrado
# 'curso' in frase ou seja,dentro da frase existe a palavra curso?se sim ele ira falar True se não ele ira falar False
# TRANSFORMAÇÃO-transformar a string
# frase.replace('python','android')ira trocar uma palavra por outra
# frase.upper() vai deixar as letras todas maiusculas
# frase.lower() vai deixar todas as letras minusculas
# frase.capitalize()vai jogar todas letras para minusculo e apenas o primeiro caractere maisculo
# frase.title()vai analisar quantas palavras tem e deixar todas as letras após um espaço maiusculas
# frase1= '   aprendendo python   '
# frase1.strip() ele vai remover todos os espaços inuteis
# frase1.rstrip() vai remover somente os ultimos espaços 
# frase1.lstrip() mesma função que o rstrip mas esse remove todos os espaços da esquerda
# divisão-pode se dividir strings
# frase.split() vai pegar onde tiver espaços e vai criar uma divisão,irá separar um por um
# junção-juntar a string
# '-'.join(frase)
frase='curso em video python'
# print (frase[10])
# print (frase[1:11])
# print (frase[14:])
# print (frase[:11])
# print (frase[1::4])
# print (frase[::2])
# print ("""kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk""")
print (frase.count('o'))
print (frase.upper().count('O'))
print (len(frase))
print (len(frase.strip()))
print (frase.replace('python','android'))
print ('curso'in frase)
print (frase.find('em'))
print (frase.lower().find('video'))
print(frase.split())
dividido=frase.split()
print (dividido[2])
