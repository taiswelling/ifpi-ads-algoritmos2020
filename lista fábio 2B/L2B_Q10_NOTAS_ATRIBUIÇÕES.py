'''Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0          A
Entre 7.5 e 9.0           B
Entre 6.0 e 7.5           C
Entre 4.0 e 6.0           D
Entre 4.0 e zero          E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a  mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. '''
nota1 = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))
nota3 = float(input('Terceira nota:\n'))
nota4 = float(input('Quarta nota:\n'))
nota5 = float(input('Quinta nota:\n'))
nota6 = float(input('Sexta nota:\n'))

med1= (nota1+nota2+nota3+nota4+nota5+nota6)/6

if nota1<0 or nota1>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')
    
elif nota2<0 or nota2>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')

elif nota3<0 or nota3>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')

elif nota4<0 or nota4>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')

elif nota5<0 or nota5>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')

elif nota6<0 or nota6>10:
    print('ERRO!\nExtiste pelo menos uma nota inserida, inválida!\nTente novamente!')


elif med1>=9 and med1<=10 :
    conc='A'
    sit='APROVADO'
    print('__________________________________________')
    print('|notas |  média |  conceito |   situação   |')
    print('__________________________________________')
    print(f'| {nota1}  |       |            |              |') 
    print(f'| {nota2}  |       |            |              |')
    print(f'| {nota3}  |   {med1:.2f} |     {conc}      |  {sit}   |')
    print(f'| {nota4}  |       |            |              |')
    print(f'| {nota5}  |       |            |              |')
    print(f'| {nota6}  |       |            |              |')
    print('__________________________________________')


elif med1>=7.5 and med1<9 :
    conc='B'
    sit='APROVADO'
    print('__________________________________________')
    print('|notas |  média |  conceito |   situação   |')
    print('__________________________________________')
    print(f'| {nota1}  |       |            |              |') 
    print(f'| {nota2}  |       |            |              |')
    print(f'| {nota3}  |   {med1:.2f} |     {conc}      |   {sit}   |')
    print(f'| {nota4}  |       |            |              |')
    print(f'| {nota5}  |       |            |              |')
    print(f'| {nota6}  |       |            |              |')
    print('__________________________________________')


elif med1>=6 and med1<7.5:
    conc='C'
    sit='APROVADO'
    print('__________________________________________')
    print('|notas |  média |  conceito |   situação   |')
    print('__________________________________________')
    print(f'| {nota1}  |       |            |              |') 
    print(f'| {nota2}  |       |            |              |')
    print(f'| {nota3}  |  {med1:.2f} |     {conc}      |   {sit}   |')
    print(f'| {nota4}  |       |            |              |')
    print(f'| {nota5}  |       |            |              |')
    print(f'| {nota6}  |       |            |              |')
    print('__________________________________________')


elif med1>=4 and med1<6 :
    conc='D'
    sit='REPROVADO'
    print('__________________________________________')
    print('|notas |  média |  conceito |   situação   |')
    print('__________________________________________')
    print(f'| {nota1}  |       |            |              |') 
    print(f'| {nota2}  |       |            |              |')
    print(f'| {nota3}  |   {med1:.2f} |     {conc}      |   {sit}   |')
    print(f'| {nota4}  |       |            |              |')
    print(f'| {nota5}  |       |            |              |')
    print(f'| {nota6}  |       |            |              |')
    print('__________________________________________')


elif med1>=0 and med1<4 :
    conc='E'
    sit='REPROVADO'
    print('__________________________________________')
    print('|notas |  média |  conceito |   situação   |')
    print('__________________________________________')
    print(f'| {nota1}  |       |            |              |') 
    print(f'| {nota2}  |       |            |              |')
    print(f'| {nota3}  |   {med1:.2f} |     {conc}      |   {sit}   |')
    print(f'| {nota4}  |       |            |              |')
    print(f'| {nota5}  |       |            |              |')
    print(f'| {nota6}  |       |            |              |')
    print('__________________________________________')