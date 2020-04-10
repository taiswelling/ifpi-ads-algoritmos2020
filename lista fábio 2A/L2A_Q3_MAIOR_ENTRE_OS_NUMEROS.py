#Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

if num2>num3>num1:
    print(f'{num2} é o maior dos números citados.')
elif num3>num2>num1:
    print(f'{num3} é o maior dos números citados.')
elif num3>num1>num2:
    print(f'{num3} é o maior dos números citados.')
elif num2>num1>num3:
    print(f'{num2} é o maior dos números citados.')
elif num1>num3>num1:
    print(f'{num1} é o maior dos números citados.')
elif num1>num2>num3:
    print(f'{num1} é o maior dos números citados.')
elif num1==num2<num3:
    print(f'{num3} é o maior dos números citados.')
elif num1==num3<num2:
    print(f'{num2} é o maior dos números citados.')
elif num2==num3<num1:
    print(f'{num1} é o maior dos números citados.')
elif num1==num2>num3:
    print(f'{num1} é o maior dos números citados.')
elif num1==num3>num2:
    print(f'{num1} é o maior dos números citados.')
elif num2==num3>num1:
    print(f'{num2} é o maior dos números citados.')
else:
    print('Os números são iguais.')