n= int(input('QUANTOS NÚMEROS DESEJA TESTAR? '))

numeros=0
valores=0
lista=[]

while numeros<n:
    valores=int(input(''))
    numeros+=1
    lista.append(valores)

resposta= max(lista)
print(f'O MAIOR NÚMERO DIGITADO FOI: {resposta}')