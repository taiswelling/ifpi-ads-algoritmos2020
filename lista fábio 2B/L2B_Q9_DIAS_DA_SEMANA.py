'''9. Leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda etc.), se digitar outro valor deve aparecer valor inválido'''

dia=int(input('Digite um número de 1 a 7:\n'))

if dia==1:
    print('O número 1 corresponde ao primeiro dia da semana, que é DOMINGO;')

elif dia==2:
    print('O número 2 corresponde ao segundo dia da semana, que é SEGUNDA;')

elif dia==3:
    print('O número 3 corresponde ao terceiro dia da semana, que é TERÇA;')

elif dia==4:
    print('O número 4 corresponde ao quarto dia da semana, que é QUARTA;')

elif dia==5:
    print('O número 5 corresponde ao quinto dia da semana, que é QUINTA;')

elif dia==6:
    print('O número 6 corresponde ao sexto dia da semana, que é SEXTA;')

elif dia==7:
    print('O número 7 corresponde ao sétimo dia da semana, que é SÁBADO;')

else:
    print('ERRO!\nVocê inseriu um valor inválido!\nTente novamente!')