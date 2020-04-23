'''15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
               Até 5 Kg               Acima de 5 Kg
Morango      R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã         R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00 receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''


print('Respondas as perguntas a seguir:\nResponda apenas SIM ou NÃO(exatamente neste formato);')
morango=float(input('Deseja comprar morangos?\nEm caso afirmarivo, digite a quantidade em kg. Em negativo, digite "0";\n'))
maca=float(input('Deseja comprar maçãs?\nEm caso afirmarivo, digite a quantidade em kg. Em negativo, digite "0";\n'))




precomorango1=morango*2.5
precomorango2=morango*2.20

precomaca1=maca*1.8
precomaca2=maca*1.5

if  morango<=5:
    precomorango=precomorango1

if morango>5:
    precomorango=precomorango2

if maca<=5:
    precomaca=precomaca1

if maca>5:
    precomaca=precomaca2


preco=precomorango+precomaca
kg=morango+maca
desconto=preco*0.1


if preco>25 or kg>8:
    preco=preco-desconto

print(f'O valor final da sua compra é R${preco}')