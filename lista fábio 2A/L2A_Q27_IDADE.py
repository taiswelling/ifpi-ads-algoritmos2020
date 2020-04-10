'''Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
nascimento e a data (dia, mês e ano) atual.'''

adia=int(input('Que dia é hoje?  '))
ames=int(input('Em que mês você está?  '))
aano=int(input('Em ano você está?  '))
ndia=int(input('Que dia você nasceu?  '))
nmes=int(input('Que mês você nasceu?  '))
nano=int(input('Que ano você nasceu?  '))

ano = aano-nano
ano1 = ano-1

mes = ames-nmes
mes1 = 12-(nmes-ames)

dia = adia-ndia
dia1 = 30-(ndia-adia)


if adia==ndia and ames==nmes and aano==nano:
    print(20*'.')
    print(f'UÉ? VOCÊ NASCEU HOJE?')
    print(20*'.')

if adia==ndia and ames==nmes and aano!=nano:
    print(20*'.')
    print(f'Parabens! Hoje é seu aniversário!\nVocê está completando {ano} anos')
    if ano<12:
        print('Tua mãe sabe que tu tá na internet?')
        print(20*'.')

# Mês atual após o mês de aniversário:

if adia>ndia and ames>nmes:
    print(f'Você possui {ano} anos,{mes} mes(es) e {dia} dias;')

if adia<ndia and ames>nmes:
    print(f'Você possui {ano} anos,{mes} mes(es) e {dia1} dias;')

if adia==ndia and ames>nmes:
    print(f'Você possui {ano} anos e {mes} mes(es);')
    


# Mês anterior ao mês de aniversário
if adia>ndia and ames<nmes:
    print(f'Você possui {ano1} anos,{mes1} mes(es) e {dia} dias;')

if adia<ndia and ames<nmes:
    print(f'Você possui {ano1} anos, {mes1} mes(es) e {dia1} dias;')

if adia==ndia and ames<nmes:
    print(f'Você possui {ano1} anos e {mes1} mes(es):')



#Mesmo mês
if adia>ndia and ames==nmes:
    print(f'Você possui {ano} anos e {dia} dias;')

if adia<ndia and ames==nmes:
    print(f'Você possui {ano1} anos e {dia1} dias;')


#incompleta







