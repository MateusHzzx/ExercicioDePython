# #                                          CONDIÇÕES                                               
# # nas condições você pode escolher que caminho quer seguir,por exemplo,um carro está andando na rua e tem uma rua em
# # sua direita e outra rua em sua esquerda,então você fará a escolha para onde seguir
# # if=será usado como 'se' então automaticamente se o carro virar a esquerda ele seguirá um comando
# #         True
# # else=senão virar a esquerda,seguirá outro comando
# #         False
# #EX:
# tempo=int(input('quanto tempo seu carro está sendo usado?'))
# print ('carro novo'if tempo <=3 else'carro velho')
# # if tempo <=3:
# #     print('carro novo')
# # else:
# #     print('carro velho')
# print('_____FIM_____')
# nome=str(input('qual seu nome?'))
# if nome == 'Mateus':
#     print ('que belo nome você tem')
# else:
#     print('que nome bosta mano!')
# print(f'Bom Dia,{nome}')
n1=float (input('1 nota'))
n2=float (input('2 nota'))
m=(n1+n2)/2
print (f'a sua media foi {m}')
if m >=7:
    print('sua média está perfeita!continue assim')
else:
    print('sua média foi ruim seu BURRO!')
   