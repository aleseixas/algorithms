#funções
def imprime(matriz):
    for linha in matriz:
        for i in range(len(linha)):
            if i == len(linha) - 1:
                print(linha[i])
            else:
                print(linha[i], end=" ")

def espelhamento_h(matriz,x,y,largura,altura):
    for linha in range(y,y+altura):
        matriz[linha][x:x+largura]=list(reversed(matriz[linha][x:x+largura]))
            
def espelhamento_v(matriz,x,y,largura,altura):
    for coluna in range(x,x+largura):
        contador=0
        for linha in range(y,y+altura//2):
            valor=matriz[linha][coluna]
            matriz[linha][coluna]=matriz[y+altura-1-contador][coluna]
            matriz[y+altura-1-contador][coluna]=valor
            contador+=1

def recorte(matriz,x,y,largura,altura,x_superior,y_superior):
    nova_matriz=[]
    lista_zeros=['000' for j in range(largura)]
    for linha in range(y,y+altura):
        nova_matriz.append(matriz[linha][x:x+largura])
        matriz[linha][x:x+largura]=lista_zeros
    colar(matriz,nova_matriz,x_superior,y_superior)

def copiar(matriz,x,y,largura,altura,x_superior,y_superior):
    nova_matriz=[]
    for linha in range(y,y+altura):
        nova_matriz.append(matriz[linha][x:x+largura])
    colar(matriz,nova_matriz,x_superior,y_superior)

def rotacao(matriz,x,y,largura,altura):
    nova_matriz=[]
    contador=0
    for coluna in range(x,x+largura):
        nova_matriz.append([])
        for linha in range(y+altura-1,y-1,-1):
            nova_matriz[contador].append(matriz[linha][coluna])
            matriz[linha][coluna]='000'
        contador+=1
    colar(matriz,nova_matriz,x,y)

def colar(matriz,outra_matriz,x_colar,y_colar):
    contador=0
    for linha in range(y_colar,y_colar+len(outra_matriz)):
        matriz[linha][x_colar:x_colar+len(outra_matriz[0])]=outra_matriz[contador]
        contador+=1

#lista e variavel
matriz=[]
x=0
y=0
#entradas
largura,altura=input().split()
n_de_operacoes=int(input())
for _ in range(int(altura)):
    linha=input().split()
    matriz.append(linha)
altura_selecionada=len(matriz)
largura_selecionada=len(matriz[0])

for _ in range(n_de_operacoes):
    operação=input().split()
    if operação[0]=='rotacao':
        rotacao(matriz,x,y,largura_selecionada,altura_selecionada)
    if operação[0]=='selecao':
        x=int(operação[1])
        y=int(operação[2])
        largura_selecionada=int(operação[3])
        altura_selecionada=int(operação[4])

    if operação[0]=='copia':
        x_superior=int(operação[1])
        y_superior=int(operação[2])
        copiar(matriz,x,y,largura_selecionada,altura_selecionada,x_superior,y_superior)

    if operação[0]=='espelhamento':
        if operação[1]=='h':
            espelhamento_h(matriz,x,y,largura_selecionada,altura_selecionada)
        elif operação[1]=='v':
            espelhamento_v(matriz,x,y,largura_selecionada,altura_selecionada)


    if operação[0]=='recorte':
        x_superior=int(operação[1])
        y_superior=int(operação[2])
        recorte(matriz,x,y,largura_selecionada,altura_selecionada,x_superior,y_superior)
        

imprime(matriz)