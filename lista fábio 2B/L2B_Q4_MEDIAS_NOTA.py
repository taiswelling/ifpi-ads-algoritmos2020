'''Leia 2 (duas)  notas parciais de um aluno
calcule a média e escreva a mensagem:
"Aprovado" ,se a média alcançada for maior ou igual a sete;
"Reprovado", se a média for menor do que sete;
"Aprovado com Distinção", se a média for igual a dez. '''

nota1 = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))

med1= (nota1+nota2)/2

if nota1>10 or nota1<0:
    print('Erro! O valor inserido não corresponde a notas válidas!\nTente novamente\n(OBS: os valores válidos são de 0.0 a 10.0')

elif nota2>10 or nota2<0:
    print('Erro! O valor inserido não corresponde a notas válidas!\nTente novamente\n(OBS: os valores válidos são de 0.0 a 10.0')

elif med1==10.0:
    print('.......................')
    print('Aprovado com distinção') 
    print('.......................')

elif med1 >= 7.0:
    print('...........')
    print('Aprovado!')
    print('...........')

elif med1<7.0:
    print('...........')
    print('Reprovado')
    print('...........')