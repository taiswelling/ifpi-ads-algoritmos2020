n=int(input('Quantos funcionários deseja consultar? '))
a=0

while a<n:
    a+=1

    print('______________________________________')
    print(f'PREENCHA A FICHA do {a}º FUNCIONÁRIO')
    print('______________________________________')

    codigo=input(' CÓDIGO DO FUNCIONÁRIO: ')
    horas=int(input(' QUANTAS HORAS POR DIA ELE(A) TRABALHA? '))
    dependentes=int(input(' QUANTOS DEPENDENTES ELE(A) POSSUI? '))
    print('                                     ')
    print('                                     ')

    salario=(dependentes*40) + (horas*12)
    IR=salario*0.05
    INSS=salario*0.085

    print(f"O salário líquido deste funcionario é R$ {salario}.00")
    print(f'Seu desconto em IR É R${IR:.2f}')
    print(f'Seu desconto de INSS É R${INSS}')
