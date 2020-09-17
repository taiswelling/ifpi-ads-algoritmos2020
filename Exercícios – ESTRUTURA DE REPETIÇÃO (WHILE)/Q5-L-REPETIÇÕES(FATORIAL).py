def fatorial (n):
    f=1
    for c in range(1,n+1):
        f=f*c
    return f

num = int(input(''))
fat = fatorial(num)
print (f'O FATORIAL DE {num} É {fat}.')