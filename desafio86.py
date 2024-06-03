matriz=[
    [1,2,3,4],
    [4,5,6],
    [7,8,9]]
for line in range(len(matriz)):
    for element in range(len(matriz[line])):
        num=int(input(f'Digite o valor para a posição {line},{element}:'))
        matriz[line][element]=num
for a in matriz:
    print(a)