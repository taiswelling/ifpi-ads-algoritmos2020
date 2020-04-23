'''13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
a) "Telefonou para a vítima ?" 
b) "Esteve no local do crime ?" 
c) "Mora perto da vítima ?" 
d) "Devia para a vítima ?" 
e) "Já trabalhou com a vítima ?"  
O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente". '''

print('Respondas as perguntas a seguir:\nResponda apenas SIM ou NÃO(exatamente neste formato);')

perg1=str(input('Telefonou para a vítima ?\n'))
perg2=str(input('Esteve no local do crime ?\n'))
perg3=str(input('Mora perto da vítima ?\n'))
perg4=str(input('Devia para a vítima ?\n'))
perg5=str(input('Já trabalhou com a vítima ?\n'))  


if perg1=='NÃO':
    res1=0
elif perg1=='SIM':
    res1=1
else:
    print('O primeiro valor foi digitado INCORRETAMENTE!\nTente novamente!\nLembrando: os valores aceitos são "SIM" e "NÃO", com letras maísculas e acentuação.')
    print('_______________________________________________________________________')


if perg2=='NÃO':
    res2=0
elif perg2=='SIM':
    res2=1
else:
    print('O segundo valor foi digitado INCORRETAMENTE!\nTente novamente!\nLembrando: os valores aceitos são "SIM" e "NÃO", com letras maísculas e acentuação.')
    print('_______________________________________________________________________')

if perg3=='NÃO':
    res3=0
elif perg3=='SIM':
    res3=1
else:
    print('O terceiro valor foi digitado INCORRETAMENTE!\nTente novamente!\nLembrando: os valores aceitos são "SIM" e "NÃO", com letras maísculas e acentuação.')
    print('_______________________________________________________________________')

if perg4=='NÃO':
    res4=0
elif perg4=='SIM':
    res4=1
else:
    print('O quarto valor foi digitado INCORRETAMENTE!\nTente novamente!\nLembrando: os valores aceitos são "SIM" e "NÃO", com letras maísculas e acentuação.')
    print('_______________________________________________________________________')

if perg5=='NÃO':
    res5=0
elif perg5=='SIM':
    res5=1
else:
    print('O quinto valor foi digitado INCORRETAMENTE!\nTente novamente!\nLembrando: os valores aceitos são "SIM" e "NÃO", com letras maísculas e acentuação.')


resultado = res1+res2+res3+res4+res5

if resultado==1 or resultado==0:
    print('xxxxxxxxxxxxxxxx')
    print('Você é inocente!')
    print('xxxxxxxxxxxxxxxx')

elif resultado==2 :
    print('xxxxxxxxxxxxxxxxxxx')
    print('Você é um suspeito!')
    print('xxxxxxxxxxxxxxxxxxx')

elif resultado==3 or resultado==4:
    print('xxxxxxxxxxxxxxxx')
    print('Você é cúmplice!')
    print('xxxxxxxxxxxxxxxx')

elif resultado==5:
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('Você é culpado! TÊJE PRESO!')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')