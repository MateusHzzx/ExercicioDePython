#                                   CÁLCULO DE MÉDIAS
opcoes=int(input('''quantas notas são?
                 [1]2 notas
                 [2]3 notas
                 [3]4 notas
                 [4]5 notas
                 [5]6 notas'''))
if opcoes==1:
    n1=float(input('nota 1: ')) 
    n2=float(input('nota 2: ')) 
    t=n1+n2
    tt=t/2
elif opcoes==2:
    n1=float(input('nota 1: ')) 
    n2=float(input('nota 2: ')) 
    n3=float(input('nota 3: ')) 
    t=n1+n2+n3
    tt=t/3
elif opcoes==3:
    n1=float(input('nota 1: ')) 
    n2=float(input('nota 2: ')) 
    n3=float(input('nota 3: '))
    n4=float(input('nota 4: '))
    t=n1+n2+n3+n4    
    tt=t/4
elif opcoes==4:
    n1=float(input('nota 1: ')) 
    n2=float(input('nota 2: ')) 
    n3=float(input('nota 3: '))
    n4=float(input('nota 4: '))
    n5=float(input('nota 5: '))
    t=n1+n2+n3+n4+n5
    tt=t/5
else:
    n1=float(input('nota 1: ')) 
    n2=float(input('nota 2: ')) 
    n3=float(input('nota 3: '))
    n4=float(input('nota 4: '))
    n5=float(input('nota 5: '))
    n6=float(input('nota 6: '))
    t=n1+n2+n3+n4+n5+n6
    tt=t/6
print(f'A MÉDIA {tt}')
#ARTES:6.0
#BIOLOGIA:5.0
#EDF:10.0
#FILOSOFIA:6.0
#FISICA:9.0
#GEOGRAFIA:7.5
#HISTÓRIA:7.0
#ESPANHOL:4.0
#INGLÊS:6.0
#PORTUGUÊS:8.0
#MATEMÁTICA:9.5 OU 9.0
#PV:NÃO LIBERADO
#QUIMICA:NÃO LIBERADO
#SOCIOLOGIA:7.0