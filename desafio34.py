s=float (input('qual é o seu atual salário?'))
if s>1250:
    calcule=s*0.10
    t=s+calcule
    print(f'seu salário aumentou de {s} para {t}')
else:
    calcule1=s*0.15
    t1=s+calcule1
    print(f'seu salário foi de {s} para {t1}')
