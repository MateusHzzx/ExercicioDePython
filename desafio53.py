frase=(input('digite uma frase que deseja saber se é palíndromo')).strip().lower().replace(' ', '')
if frase==frase[::-1]:
    print('é palíndromo')
else:
    print('não é palíndromo')