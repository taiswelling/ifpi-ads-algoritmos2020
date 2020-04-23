'''8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do salário bruto, mas não é descontado (é a empresa que deposita).
O salário líquido corresponde ao salário bruto menos os descontos. O programa deverá pedir
ao usuário o valor da sua hora e a quantidade de horas trabalhadano mês.

Desconto do IR: 
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%  

Escreva na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
         Salário Bruto: (5 * 220)        : R$ 1100,00         
         (-) IR (5%)                     : R$   55,00           
         (-) INSS ( 10%)                 : R$  110,00         
         FGTS (11%)                      : R$  121,00         
         Total de descontos              : R$  165,00         
         Salário Liquido                 : R$  935,00 '''


horas=int(input('Quantas horas você trabalha por mês?\n'))
valor=float(input('Quanto você ganha por hora?\n'))

sal_bruto=(horas*valor)


if sal_bruto>0 and sal_bruto<=900:
    ir=0

if sal_bruto>900 and sal_bruto<=1500:
    ir= sal_bruto*0.05

if sal_bruto>1500 and sal_bruto<=2500:
    ir= sal_bruto*0.1

if sal_bruto>2500:
    ir= sal_bruto*0.2

inss = (sal_bruto*0.1)
fgts = (sal_bruto*0.11)

descontos=ir+inss

sal_liquido = sal_bruto - descontos

print('#####################################################')
print(f'#Salário Bruto:({horas}*{valor})         : R${sal_bruto}')
print(f'#(-) IR                          : R$  {ir}')
print(f'#(-) INSS ( 10%)                 : R$  {inss}')   
print(f'#FGTS (11%)                      : R$  {fgts}')
print(f'#Total de descontos              : R$  {descontos:.2f}')
print(f'#Salário Liquido                 : R$  {sal_liquido}')
print('#####################################################')