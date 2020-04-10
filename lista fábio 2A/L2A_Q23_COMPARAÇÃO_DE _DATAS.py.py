print('INSIRA DUAS DATAS(DIA, MÊS E ANO):')
dia1 = int(input('Dia da primeira data:\n'))
mes1 = int(input('Mês da primeira data(em valor numérico):\n'))
ano1 = int(input('Ano da primeira data:\n'))

dia2 = int(input('Dia da segunda data:\n'))
mes2 = int(input('Mês da segunda data(em valor numérico):\n'))
ano2 = int(input('Ano da segunda data:\n'))

print(f'As datas inseridas foram {dia1}/{mes1}/{ano1} e {dia2}/{mes2}/{ano2}, respectivamente;')

if mes1 > 12 or mes2 > 12:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 1 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 2 and (dia1 or dia2)>28:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 3 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 4 and (dia1 or dia2)>30:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 5 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 6 and (dia1 or dia2)>30:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 7 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 8 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 9 and (dia1 or dia2)>3:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 10 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 11 and (dia1 or dia2)>30:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif (mes1 or mes2) == 12 and (dia1 or dia2)>31:
    print('Uma ou ambas as datas inseridas são inválidas;')

elif ano1>ano2:
    print('A primeira data inserida é mais recente que a segunda data;')

elif ano1==ano2 and mes1>mes2:
    print('A primeira data inserida é mais recente que a segunda data;')

elif ano1==ano2 and mes1==mes2 and dia1>dia2:
    print('A primeira data inserida é mais recente que a segunda data;')

elif ano1==ano2 and mes1==mes2 and dia1==dia2:
    print('As datas inseridas são iguais;')

else:
    print('A segunda data inserida é mais recente que a primeira data;')


