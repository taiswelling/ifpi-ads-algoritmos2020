'''14. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
· até 20 litros, desconto de 3% por litro
· acima de 20 litros, desconto de 5% por litro
2. Gasolina:
· até 20 litros, desconto de 4% por litro
· acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
do litro do álcool é R$ 1,90.'''

pergunta1=str(input('O QUE DESEJA COMPRAE?:\nUse "G" para GASOLINA;\nUse "A" para ÁLCOOL;\n'))
pergunta2=float(input('Quantos litros você deseja?\n'))

valora=pergunta2*1.9
desa3=valora*0.03
desa5 = valora*0.05

valorg=pergunta2*2.5
desg4 = valorg*0.04
desg6 = valorg*0.06

if pergunta1==('g' or 'G') and pergunta2<=20:
    total1=valorg-desg4
    print(f'Você dejesa {pergunta2} litros de Gasolina.\nVocê deverá pagar {total1}')

if pergunta1==('g' or 'G') and pergunta2>20:
    total2=valorg-desg6
    print(f'Você dejesa {pergunta2} litros de Gasolina.\nVocê deverá pagar {total2}')

if pergunta1==('a' or 'A') and pergunta2<=20:
    total3=valora-desa3
    print(f'Você dejesa {pergunta2} litros de Gasolina.\nVocê deverá pagar {total3}')
    
if pergunta1==('a' or 'A') and pergunta2<=20:
    total4=valora-desa5
    print(f'Você dejesa {pergunta2} litros de Gasolina.\nVocê deverá pagar {total4}')