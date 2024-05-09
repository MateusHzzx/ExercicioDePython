
def execute():
    n= str (input('fale um numeor de 4 a maiss digitos '))
    dividido='000'+n
    print (f'unidade:{dividido[-1]}')
    print (f'dezena:{dividido[-2]}')
    print (f'centena{dividido[-3]}')
    print (f'milhar:{dividido[-4]}')
