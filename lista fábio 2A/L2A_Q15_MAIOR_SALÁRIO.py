'''Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
Escreva na tela qual dos professores tem salário total maior.'''

prof1 = int(input('Quantas horas aula o primeiro professor trabalha? \n '))
valor1 = float(input('Qual o valor da hora aula cobrado pelo primeiro professor? \n '))

prof2 = int(input('Quantas horas aula o segundo professor trabalha? \n '))
valor2 = float(input('Qual o valor da hora aula cobrado pelo segundo professor? \n '))

sal1 = prof1*valor1
sal2 = prof2*valor2

if sal1>sal2:
    print(f'Quem tem maior salário é o Professor 1, que recebe {sal1}.')

elif sal2 > sal1:
    print(f'Quem tem maior salário é o Professor 2, que recebe {sal2}.')