a=int(input('em que ano você nasceu'))
t=2024-a
print (f'se você nasceu em {a} quer dizer que você tem {t} anos')
if t<=9:
    print('VOCÊ ESTÁ NA CATEGORIA ''\33[36m''MIRIM''\033[0;0m')
elif t>9 and t<=14:
    print ('VOCÊ ESTÁ NA CATEGORIA ''\33[34m''INFANTIL''\033[0;0m')
elif t>14 and t<=19:
    print('VOCÊ ESTÁ NA CATEGORIA ''\33[31m''JUNIOR''\033[0;0m')
elif t>19 and t<=20:
    print ('VOCÊ ESTÁ NA CATEGORIA ''\33[32m''SÊNIOR''\033[0;0m')
else:
    print ('VOCÊ ESTA NA CATEGORIA ''\33[30m''MASTER''\033[0;0m')