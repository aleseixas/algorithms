#imports
from unicodedata import decimal
from recipes_decimal import pi 
from decimal import getcontext, Decimal
getcontext().prec=36
#funções
def zeta(s):
    soma=Decimal(0)
    for k in range(1,101):
        soma+=Decimal(1/k**s)
    return soma

def distancia(combustivel,a,b,c,d):
    p=pi()
    aux=p+a*combustivel.exp()-zeta(b*combustivel+p)
    aux2=(-(c*combustivel).sqrt()).exp()+d*(Decimal(2)*p**Decimal(3)-combustivel)
    return aux/aux2

def busca_binaria(a,b,c,d,x):
    esquerda = Decimal('0.')
    direita = Decimal('50.')
    while True:
        meio = (esquerda + direita) / 2
        if distancia(meio,a,b,c,d) < x: 
            esquerda = meio
        else:
            direita = meio
        erro = abs(esquerda - direita)
        if Decimal('1e-32') >= erro:
            break
    return meio

def limite_max(a,b,c,d):
    return distancia(Decimal(50.),a,b,c,d)

def limite_min(a,b,c,d):
    return distancia(Decimal(0.),a,b,c,d)

#dicionario e variaveis
planetas={}
n_rotas=None
maximo=Decimal(0)
maior_distancia=Decimal(0)
#entradas
n_rotas=int(input())
while n_rotas!=0:
    for k in range(n_rotas):
        nome_do_planeta=input()
        distancia_em_anos_luz=Decimal(input())
        planetas[distancia_em_anos_luz]=nome_do_planeta
    a=Decimal(input())
    b=Decimal(input())
    c=Decimal(input())
    d=Decimal(input())
    lista=reversed(sorted(planetas.items()))
    min_distancia=limite_min(a,b,c,d)
    max_distancia=limite_max(a,b,c,d)
    #entrando valores dos itens
    for k in lista:
        anos_luz=k[0]
        planeta=k[1]
        if anos_luz > maior_distancia and min_distancia <= anos_luz <= max_distancia:
            combustivel = busca_binaria(a,b,c,d,anos_luz) 
            if combustivel > maximo:
                maximo = combustivel 
                planeta_max = planeta
                maior_distancia = anos_luz
    #saída
    if maximo==Decimal(0):
        print('GRAU~~')
    else:
        print(planeta_max)     
        print('{:.28f}'.format(maximo))
    #valores para nova rota
    maximo=Decimal(0)
    maior_distancia=Decimal(0)
    planetas.clear()
    n_rotas=int(input())
            
