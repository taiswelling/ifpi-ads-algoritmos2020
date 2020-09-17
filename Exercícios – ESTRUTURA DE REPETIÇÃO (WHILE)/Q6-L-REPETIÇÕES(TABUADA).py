valor= input ("Digite o valor correspondente:\n1)soma \n2)subtração \n3)multiplicação \n4)divisão\n")
numero = int(input("De que numero?\n"))

n=0


if valor=='1' or valor=='soma':
    while n<=10:
        num = numero+n
        print(f"{numero} + {n} = {num}")
        n+=1

if valor=='2' or valor=='subtração':
    while n<=10:
        num = numero-n
        print(f"{numero} - {n} = {num}")
        n+=1

if valor=='3' or valor=='multiplicação':
    while n<=10:
        num = numero*n
        print(f"{numero} * {n} = {num}")
        n+=1


if valor=='4' or valor=='divisão':
    while n<=10:
        if n==0:
            None
            n+=1

        else:
            num = numero/n
            print(f"{numero} / {n} = {num}")
            n+=1