palavra = str(input('Digite a palavra a ser critografada:  '))
chave=int(input('Digite a chave:  '))

palavra=palavra.upper()

palavra_criptografada= ''

for letra in palavra:
    letra=ord(letra)
    nova_letra=letra+chave

    if nova_letra<65:
        nova_letra = 91 - (65- nova_letra )

    if nova_letra>90:
        nova_letra = 64 + (nova_letra-90)
    
    nova_letra=chr(nova_letra)


    palavra_criptografada+=nova_letra

print(f'{palavra_criptografada}')