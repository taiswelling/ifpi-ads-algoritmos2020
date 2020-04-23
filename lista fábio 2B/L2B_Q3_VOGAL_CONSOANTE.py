'''3-Leia uma letra e verifique se a letra digitada é vogal ou consoante'''

letra = str(input('Insira uma letra:\n'))

vogais = str('a,A,e,E,i,I,o,O,u,U')

consoantes=str('b,B,c,C,d,D,f,F,g,G,h,H,j,J,k,K,l,L,m,M,n,N,p,P,q,Q,r,R,s,S,t,T,v,V,w,W,x,X,y,Y,z,Z')

if letra in vogais:
    print('A letra inserida é uma vogal')

elif letra in consoantes:
    print('A letra inserida é uma consoante')

else:
    print('Você digitou um valor inválido!\nTente novamente.')