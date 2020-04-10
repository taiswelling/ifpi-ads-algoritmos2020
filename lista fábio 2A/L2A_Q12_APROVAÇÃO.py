'''Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
escreva “Reprovado”.'''

nota1 = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))

med1= (nota1+nota2)/2

if med1 >= 7.0:
    print('...........')
    print('Aprovado!')
    print('...........')

elif med1<7.0:
    print('O aluno está de exame final.')
    nota3= float(input('Nota do exame final:\n'))

    med2=(nota3+med1)/2

    if med2 >= 5.0:
        print('Aprovado em EXAME FINAL.')
    else:
        print('...........')
        print('reprovado')
        print('...........')