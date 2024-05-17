# #                                               LAÇOS DE REPETIÇÃO (PART 3)
# # para parar a execução de um comando é usado o break dentro do while
# while True=loop infinito,nunca acabará até chegar aonde especificou
#     break=usado para parar o loop infinito,quando chegar aonde você quer ele irá parar
# cont = 1
# while True:
#     print(cont,  end='    ')
#     cont+=1
# print('acabou')
n=s=c=0
while True:
    n=int(input('número'))
    if n==999:
        break
    s+=n
print(f'{s}')