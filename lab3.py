#lista dos frascos
i=[]
n_de_frascos=1
#variaveis 
q=int(input(''))
T=float(input(''))
C=int(input(''))
n=int(input(''))
Vp=0
PA=0
m=0
#algoritmo para encontra os valores de V
while n_de_frascos<=q:
    i.append(n_de_frascos)
    Vi= T * i[n_de_frascos-1] + T * C
    Vp+=Vi
    print('{} {:.2f} {:.2f}'.format(n_de_frascos,Vi,Vp))
    n_de_frascos+=1
Vt=Vp
print('{:.2f}'.format(Vt))
#PA
while PA<=Vt:
    m+=1
    PA=m*n
    if PA<=Vt:
        print(PA)
    elif PA>Vt:
        break
print(m-1)
print('BATERIA DE TESTES TERMINADA')