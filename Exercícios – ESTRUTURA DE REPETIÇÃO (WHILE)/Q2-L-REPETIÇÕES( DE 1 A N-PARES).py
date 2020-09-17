num=int(input('Digite um valor: '))
a=2

resto=num%2

while a<=num:
    if resto==0:
        print('{}'.format(a))
        a+=2

    if resto!=0:
        while a<num:
            print('{}'.format(a))
            a+=2