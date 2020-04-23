'''12. Leia um número e escreva se o número é inteiro ou decimal.'''

num = float(input('Digite um número:\n'))

num1=num//1


if num==num1:
    print(f'O valor digitado é um número inteiro.')

else:
    print(f'O valor digitado é um número decimal.')