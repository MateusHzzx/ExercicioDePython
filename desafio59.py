n1=float(input('digite um número: '))
n2=float(input('digite outro número: '))

continuar=1

while continuar!=5:
      print('''O que deseja fazer?
            [1]somar os dois números
            [2]multiplicar os dois números
            [3]saber qual é o maior
            [4]escolher novos números
            [5]sair do menu''')
      opção= int (input('qual sua escolha?'))
      if opção==1:
            soma=n1+n2
            print(f'a soma entre os dois é {soma}')
      elif opção==2:
            mt=n1*n2
            print(f'a multiplicação entre esses dois é {mt}')
      elif opção==3:
            if n1>n2:
                  maior=n1
            else:
                  maior=n2
            print(f'o maior valor entre {n1} e {n2} é o {maior}')
      elif opção==4:
            n1=float(input('digite um novo número'))
            n2=float(input('digite outro novo número'))
      elif opção==5:
            print('fechando o menu...')
            continuar=5
      else:
            print('escolha inválida,tente novamente')