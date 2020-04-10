'''Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos''' 


print('Digite os três lados de um triângulo:')

lado1 = int(input('LADO 1:  '))
lado2 = int(input('LADO 2:  '))
lado3 = int(input('LADO 3:  '))

import math

if lado1==lado2==lado3:
    print('Os lados inseridos  formam um triângulo equilátero.\nTriângulos equiláteros não possuem hipotenusa e catetos.')

elif lado1==lado2 and lado1>lado3:
    print('Erro! Insira valores possíveis!')

elif lado1==lado3 and lado1>lado2:
    print('Erro! Insira valores possíveis!')

elif lado3==lado2 and lado3>lado1:
    print('Erro! Insira valores possíveis!')



elif lado1>lado2 and lado1>lado3:
    h1=lado1**2
    c1=(lado2**2)+(lado3**2)
    if h1==c1:
        print(f'A hipotenusa é {lado1} e os catetos são {lado2} e {lado3}')
    else:
        print('os valores inseridos não formam um triângulo retângulo.\nPortanto não possui catetos nem hipotenusa.')


elif lado2>lado1 and lado2>lado3:
    h2=lado2**2
    c2=(lado1**2)+(lado3**2)
    if h2==c2:
        print(f'A hipotenusa é {lado2} e os catetos são {lado1} e {lado3}')
    else:
        print('os valores inseridos não formam um triângulo retângulo.\nPortanto não possui catetos nem hipotenusa.')

elif lado3>lado1 and lado3>lado2:
    h3=lado3**2
    c3=(lado2**2)+(lado1**2)
    if h3==c3:
        print(f'A hipotenusa é {lado3} e os catetos são {lado2} e {lado1}')
    else:
        print('os valores inseridos não formam um triângulo retângulo.\nPortanto não possui catetos nem hipotenusa.')


