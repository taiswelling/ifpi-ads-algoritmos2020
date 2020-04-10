'''Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
possíveis para a variável opção são 1, 2 e 3.'''

opcao= int(input('Digite um número de 1 a 3:  '))
num1= int(input('Digite um número:  '))
num2= int(input('Digite um número:  '))
num3= int(input('Digite um número:  '))

if opcao==1:
    print(4*"-")
    print(f"{num1}")
    print(4*"-")

elif opcao==2:
    print(4*"-")
    print(f'{num2}')
    print(4*"-")

elif opcao==3:
    print(4*"-")
    print(f'{num3}')
    print(4*"-")

else:
    print(25*"X")
    print('Você digitou um valor inválido! Tente novamente.')
    print(25*"X")