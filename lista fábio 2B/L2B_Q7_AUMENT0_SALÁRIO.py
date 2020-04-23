
'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contrataram para desenvolver o programa que calculará os reajustes.
Escreva um algoritmo que leia o salário de um colaborador e o reajuste
segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após
o aumento ser realizado, informe na tela: 
· o salário antes do reajuste; 
· o percentual de aumento aplicado; 
· o valor do aumento; 
· o novo salário, após o aumento. '''

valor=float(input('Quanto você recebe?\n'))

porcento1 = (valor*0.2)
aumento1 = valor+porcento1

porcento2 = (valor*0.15)
aumento2 = valor+porcento2

porcento3 = (valor*0.1)
aumento3 = valor+porcento3

porcento4 = (valor*0.05)
aumento4 = valor+porcento4

if valor<=280:
    print(f'Você recebe R${valor}')
    print('Você terá 20 porcento de aumento')
    print(f'Essa porcentagem corresponde à R${porcento1}')
    print(f'Seu novo salário será R${aumento1};')

if valor>280 and valor<=700:
    print(f'Você recebe R${valor}')   
    print('Você terá 15 porcento de aumento')
    print(f'Essa porcentagem corresponde à R${porcento2}')
    print(f'Seu novo salário será R${aumento2};')

if valor>700 and valor<=1500:
    print(f'Você recebe R${valor}')   
    print('Você terá 10 porcento de aumento')
    print(f'Essa porcentagem corresponde à R${porcento3}')
    print(f'Seu novo salário será R${aumento3};')

if valor>1500:
    print(f'Você recebe R${valor}')   
    print('Você terá 5 porcento de aumento')
    print(f'Essa porcentagem corresponde à R${porcento4}')
    print(f'Seu novo salário será R${aumento4};')
 