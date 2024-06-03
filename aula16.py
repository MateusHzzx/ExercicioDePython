# # #____________________________________VARIÁVEIS COMPOSTAS____________________________________ 
# # #__________________________________________(TUPLAS)____________________________________ 
# # 'AS TUPLAS SÃO IMUTÁVEIS'signinifica que não e possivel mudar alguma coisa
# #                                            -PRÁTICA-
lanche=('Hambúrger','Suco','Pizza','Pudim')
print (lanche)
print (lanche[2])
print (lanche[1:])
print (lanche[-4])
print (lanche[1:3])
print (lanche[:2])
print (lanche[-2:])
for cont in range (0,len(lanche)):
    print (lanche[cont])
for pos,c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('comi demaize so!')
# # print (sorted(lanche))
# a=(2,5,6,7)
# b=(2,6,9,12)
# c=a+b
# print (a)
# print (b)
# print (c)
# print (c.count(6))
# print (c.index(12))

