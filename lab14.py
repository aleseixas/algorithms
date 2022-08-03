def cria_cofator(tamanho_matriz, j, lista):
    outra_matriz=[[] for k in range(tamanho_matriz-1)]
    for linha in range(tamanho_matriz):
        for coluna in range(tamanho_matriz):
            if linha==0 or coluna==j:
                pass
            else:
                outra_matriz[linha-(tamanho_matriz)].append(lista[linha][coluna])      
    return outra_matriz

def determinante(lista):
    adiciona=0
    linha=0
    if len(lista)==2:
        calculo=int(lista[0][0])*int(lista[1][1])-int(lista[0][1])*int(lista[1][0])
        return calculo
    elif len(lista)>2:
        for k in range(len(lista)):
            b=int(lista[linha][k])
            termo=(-1)**(k)  
            cofator=determinante(cria_cofator(len(lista),k,lista))
            adiciona+=b*termo*cofator
        return adiciona

#listas e variaveis
matriz=[]
multiplica=1
#entradas
m_matrizes=int(input())
n_n=int(input())
for matrizes in range(m_matrizes):
    for linha in range(n_n):
        linha_matriz=input().split()
        matriz.append(linha_matriz)
    multiplica *= determinante(matriz)
    matriz.clear()
    
print('Após as {m} transformações, o objeto {n}-dimensional teve o volume multiplicado no valor {d}.'.format(m=m_matrizes,n=n_n,d=multiplica))