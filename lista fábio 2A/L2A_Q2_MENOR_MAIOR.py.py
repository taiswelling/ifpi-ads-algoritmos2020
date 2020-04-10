#Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1>num2:
    print (f'{num1} é maior que {num2}.')
elif num1<num2:
    print(f'{num2} é maior que {num1}.')
else:
    print( 'Os números são iguais.')
    