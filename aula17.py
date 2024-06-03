#___________________________________LISTAS______________________________________
# As listas são mutáveis,ou seja pode ser trocada
# num = [2,5,9,1]
# num[2]=18
# num.append(8)
# num.insert(0,2)
# num.sort()
# if 4 in num:
#     num.remove(4)
# print (num)
# num.pop(2)
# num.sort(reverse=True)
# print (f'essa lista tem {len(num)} elementos')
# valores=[]
# valores.append(4)
# valores.append(9)
# valores.append(4)
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor: ')))
# valores.sort()
# for c,v in enumerate(valores):
#     print(f'na posiçao {c} há o número {v}...')
a=[2,3,4,7]
b=a[:]
b[2]=8
print(f'lista A: {a}')
print (f'lista B: {b}')