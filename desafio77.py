palavra=('aprender','jogar','programar','estudar','trabalho','notas','dinheiro')
for p in palavra:
    print(f'\nna palavra {p} temos  ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra, end=' ')