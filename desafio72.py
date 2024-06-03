n=('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    a=int(input('Digite um número de 1 a 20: '))
    if 0<= a <=20:
        break
    print('tente novamente')
print (f'o número {a} lido por extenso é {n[a-1]}')