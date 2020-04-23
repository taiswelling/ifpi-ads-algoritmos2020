'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:       Até 5 Kg            Acima de 5 Kg
File       R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra    R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha    R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de  carne
da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for
feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um
cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar. '''

print('PROMOÇÃO DISPONÍVEL:\n                   Confira:')
print('==================================================')
print('               Até 5 Kg            Acima de 5 Kg')
print('File       R$ 4,90 por Kg          R$ 5,80 por Kg')
print('Alcatra    R$ 5,90 por Kg          R$ 6,80 por Kg')
print('Picanha    R$ 6,90 por Kg          R$ 7,80 por Kg')
print('==================================================')


carne=str(input('ESCOLHA APENAS UM DOS TIPOS DE CARNE DISPONÍVEL:\n'))
kg=float(input('QUANTOS QUILOS VOCÊ DESEJA?\n'))
pagamento=str(input('QUAL SERÁ SUA FORMA DE PAGAMENTO: CARTÃO TABAJARAS OU OUTRA FORMA DE PAGAMENTO:\nDIGITE APENAS "TABAJARAS" OU "OUTROS"\n'))


valorfile1=kg*4.9
valoralcatra1=kg*5.9
valorpicanha1=kg*6.9

valorfile2=kg*5.8
valoralcatra2=kg*6.8
valorpicanha2=kg*7.8

if carne==('file'or 'filé' or 'FILÉ' or 'FILE') and pagamento==("tabajaras" or "Tabajaras" or "TABAJARAS"):
    if kg<=5:
        desconto=(valorfile1*0.5)
        valor=valorfile1-desconto
    elif kg>5:
        desconto=(valorfile2*0.5)
        valor=valorfile2-desconto

if carne==('file'or 'filé' or 'FILÉ' or 'FILE') and pagamento==('outros' or "OUTROS" or 'Outros'):
    if kg<=5:
        desconto=0
        valor=valorfile1
    elif kg>5:
        desconto=0
        valor=valorfile2

if carne==('alcatra'or 'Alcatra' or 'ALCATRA') and pagamento==("tabajaras" or "Tabajaras" or "TABAJARAS"):
    if kg<=5:
        desconto=(valoralcatra1*0.5)
        valor=valoralcatra1-desconto
    elif kg>5:
        desconto=(valoralcatra2*0.5)
        valor=valoralcatra2-(valoralcatra2*0.5)

if carne==('alcatra'or 'Alcatra' or 'ALCATRA')  and pagamento==('outros' or "OUTROS" or 'Outros'):
    if kg<=5:
        desconto=0
        valor=valoralcatra1
    elif kg>5:
        desconto=0
        valor=valoralcatra2


if carne==('picanha'or 'Picanha' or 'PICANHA') and pagamento==("tabajaras" or "Tabajaras" or "TABAJARAS"):
    if kg<=5:
        desconto=valorpicanha1*0.5
        valor=valorpicanha1-desconto
    elif kg>5:
        desconto=(valorpicanha2*0.5)
        valor=valorpicanha2-desconto

if carne==('picanha'or 'Picanha' or 'PICANHA')  and pagamento==('outros' or "OUTROS" or 'Outros'):
    if kg<=5:
        desconto=0
        valor=valorpicanha1-desconto
    elif kg>5:
        desconto=0
        valor=valorpicanha2-desconto


print('###################CUPOM FISCAL################')
print(f'TIPO DE CARNE                      {carne}')
print(f'QUANTIDADE DE CARNE                {kg}kg')
print(f'TIPO DE PAGAMENTO                  {pagamento}')
print(f'DESCONTO                           R${desconto}')
print(f'VALOR  A PAGAR                     R${valor}')
print('###################CUPOM FISCAL################')
