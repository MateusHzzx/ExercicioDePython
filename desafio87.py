matriz=[
    [1,2,3],
    [8, 1, 4],
    [7,8,9]]
soma=somaelemento=0
# for line in range(len(matriz)):
#     for element in range(len(matriz[line])):
#         num=int(input(f'Digite o valor para a posição {line},{element}:'))
#         teste = 1
#         if num%2==0:
#             soma+=num
#         matriz[line][element]=num
#         if element==2:
#             somaelemento+=matriz[line][2]
for a in matriz:
    print(a)
print (f'a soma entre todos os números pares é de {soma}')
print(f'o soma entre todos os elementos da 3a coluna é de {somaelemento}')
linha2 = matriz[1]
linha2.sort()
print(linha2)
print(f"O maior número da segunda linha é {linha2[-1]}")