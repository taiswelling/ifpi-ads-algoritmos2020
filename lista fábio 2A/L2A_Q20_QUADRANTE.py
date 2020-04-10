'''Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
quarto) em que o ângulo se localiza.'''

ang= int(input('Digite um ângulo inteiro entre 0 e 360°: \n'))

if ang>=0 and ang<=90:
    print('O ângulo digitado pertence ao primeiro quadrante;')

elif ang>=91 and ang<=180:
    print('O ângulo digitado pertence ao segundo quadrante;')

elif ang>=181 and ang<=270:
    print('O ângulo digitado pertence ao terceiro quadrante;')

elif ang>=271 and ang<=360:
    print('O ângulo digitado pertence ao quarto quadrante;')

else:
    print('O ângulo digitado não é válido')