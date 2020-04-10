'''Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
(IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).'''

peso = float(input('Qual sua massa corporal(em kg)?\n'))
altura = float(input('Qual sua altura(em metros)?\n'))

imc = peso / (altura**2)

if imc<25:
    print(20*'-')
    print('Você está com com o peso NORMAL;')
    print(20*'-')


elif imc>25 and imc<30:
    print(20*'-')
    print('Você está OBESO;')
    print(20*'-')

elif imc>30:
    print(20*'-')
    print('Você sofre de OBESIDADE MÓRBIDA ;')
    print(20*'-')


