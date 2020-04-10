
'''Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
sua idade exata (em anos).'''

adia=int(input('Que dia é hoje?  '))
ames=int(input('Em que mês você está?  '))
aano=int(input('Em ano você está?  '))
ndia=int(input('Que dia você nasceu?  '))
nmes=int(input('Que mês você nasceu?  '))
nano=int(input('Que ano você nasceu?  '))

anos = aano-nano
anos1 = anos-1

print ('--------------------------------------')
print (f'Hoje é {adia}/{ames}/{aano}')
print (f'Você nasceu em {ndia}/{nmes}/{nano}')
print ('---------------------------------------')

if (ames==nmes) and (adia==ndia):
    print(f'Você possui {anos} anos')

elif (ames<nmes) and (adia>ndia):
    print(f'Você possui {anos1} anos')

elif (ames<nmes) and (adia<ndia):
    print(f'Você possui {anos1} anos')

elif (ames<nmes) and (adia==ndia):
    print(f'Você possui {anos1} anos')

elif (ames>nmes) and (adia>ndia):
    print(f'Você possui {anos} anos')

elif (ames>nmes) and (adia<ndia):
    print(f'Você possui {anos} anos')

elif (ames>nmes) and (adia==ndia):
    print(f'Você possui {anos} anos')

elif (ames==nmes) and (adia<ndia):
    print(f'Você possui {anos1} anos')
    
elif (ames==nmes) and (adia>ndia):
    print(f'Você possui {anos} anos')
