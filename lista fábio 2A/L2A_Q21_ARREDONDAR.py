'''Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
contrario, é arredondado para o inteiro imediatamente inferior.'''

num = float(input('Digite um numero qualquer, fracionado: \n'))

arredondar = round(num)

print('O numero digitado, de forma arredondada é %.2f' %arredondar)