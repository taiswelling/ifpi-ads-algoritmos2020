'''2-Leia uma letra, verifique se  letra é "F" ou "M" e escreva F - Feminino,
M - Masculino, Sexo Inválido'''

sexo = str(input('Digite "F" para feminino ou "M" para Masculino: '))

if sexo == 'M' or sexo == 'm':
    print("MASCULINO")

elif sexo == 'F' or sexo == 'f':
    print('FEMININO')

else:
    print('Sexo inválido!\nTENTE NOVAMENTE!')