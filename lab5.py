#sarah e clone lista
sarah=[]
clone=[]
#entradas
sarah=input('').split(' ')
clone=input('').split(' ')
semente=int(input(''))
#vida,ataque,defesa,listas e variaveis
n=[semente]
rodada=0
contador=0
vida_sarah=int(sarah[0])
vida_clone=int(clone[0])
ataque_sarah=int(sarah[1])
ataque_clone=int(clone[1])
defesa_sarah=int(sarah[2])
defesa_clone=int(clone[2])

#funções
def n_aleatorio(n_gerados):
    global contador 
    k=0
    while k<n_gerados:
        x=(7*n[contador]+111)%1024
        print('MENSAGEM DEBUG - número gerado:',x)
        n.append(x)
        contador+=1
        k+=1
        return x
    if n_gerados==-1:
        return int(n[contador])

def fim_luta():
    if vida_sarah<0:
        print('Sarah foi derrotada...')
    if vida_clone<0:
        print('O clone foi derrotado! Sarah venceu!')
        print('FIM - PARABENS')
    
    

def soco(m,x):
    dano=0
    m=n_aleatorio(m)%3
    global vida_sarah
    global vida_clone
    global defesa_clone
    global defesa_sarah
    global ataque_clone
    global ataque_sarah
    if x==0:
        dano=m*(ataque_sarah-defesa_clone)
        if dano<0:
            dano=0
            print('O clone sofreu {} pontos de dano!'.format(dano))
        else:
            print('O clone sofreu {} pontos de dano!'.format(dano))
        return vida_clone-dano
    elif x==1:
        dano=m*(ataque_clone-defesa_sarah)
        if dano<0:
            dano=0
            print('Sarah sofreu {} pontos de dano!'.format(dano))
        else:
            print('Sarah sofreu {} pontos de dano!'.format(dano))
        return vida_sarah-dano

def arremeso_de_faca(n,x):
    n=n_aleatorio(n)%6
    dano=0
    if x==0:
        for quantidade in range(1,n+1):
            i=ataque_sarah//3**quantidade
            dano+=i
        if dano<0:
            dano=0
            print('O clone sofreu {} pontos de dano!'.format(dano))
        else:
            print('O clone sofreu {} pontos de dano!'.format(dano))
        return vida_clone-dano
    elif x==1:
        for quantidade in range(1,n+1):
            i=ataque_clone//3**quantidade
            dano+=i
        if dano<0:
            dano=0
            print('Sarah sofreu {} pontos de dano!'.format(dano))
        else:
            print('Sarah sofreu {} pontos de dano!'.format(dano))
        return vida_sarah-dano

def invocacao_de_fada(p,q,x):
    global vida_sarah
    global vida_clone
    global defesa_clone
    global defesa_sarah
    global ataque_clone
    global ataque_sarah
    p=n_aleatorio(p)%100
    q=n_aleatorio(q)
    if x==0:
        vida_sarah=vida_sarah+p
        if 0<q<100 and q%2==0:
            defesa_sarah=defesa_sarah+q
            print('Sarah ganhou {} pontos de vida!'.format(p))
            print('Sarah ganhou {} pontos de defesa!'.format(q))
        elif q<100 and q%2==1:
            ataque_sarah=ataque_sarah+q
            print('Sarah ganhou {} pontos de vida!'.format(p))
            print('Sarah ganhou {} pontos de ataque!'.format(q))
        elif q>=1019:
            vida_clone=0
            print('Sarah ganhou {} pontos de vida!'.format(p))
            print('O quê? A fada trouxe um monstro gigante com ela!')
            print('O Clone e o castelo foram destruídos,')
            print('e Sarah agora tem um novo pet.')
            print('FINAL SECRETO - PARABENS???')
        else:
            print('Sarah ganhou {} pontos de vida!'.format(p))
        
        return vida_clone
        
        
    elif x==1:
        vida_clone=vida_clone+p
        if 0<q<100 and q%2==0:
            defesa_clone=defesa_clone+q
            print('O clone ganhou {} pontos de vida!'.format(p))
            print('O clone ganhou {} pontos de defesa!'.format(q))
        elif q<100 and q%2==1:
            ataque_clone=ataque_clone+q
            print('O clone ganhou {} pontos de vida!'.format(p))
            print('O clone ganhou {} pontos de ataque!'.format(q))
        elif q>=1019:
            vida_sarah=0
            print('O clone ganhou {} pontos de vida!'.format(p))
            print('O quê? A fada trouxe um monstro gigante com ela!')
            print('Sarah foi derrotada...')
        else:
            print('O clone ganhou {} pontos de vida!'.format(p))
        
    return vida_sarah
        

        

#luta
while vida_sarah>0 or vida_clone>0:
    comando=input('')
    if comando=='soco':
        if rodada==0:
            vida_clone=soco(1,0)
            rodada=rodada+1
       
        elif rodada==1:
            vida_sarah=soco(1,1)
            rodada=rodada-1
    
    if comando=='facas':
        if rodada==0:
            vida_clone=arremeso_de_faca(1,0)
            rodada=rodada+1
       
        elif rodada==1:
            vida_sarah=arremeso_de_faca(1,1)
            rodada=rodada-1
    
    if comando=='fada':
        if rodada==0:
            vida_clone=invocacao_de_fada(1,1,0)
            rodada=rodada+1
        elif rodada==1:
            vida_sarah=invocacao_de_fada(1,1,1)
            rodada=rodada-1
            
    fim_luta()
    if vida_sarah<=0 or vida_clone<=0: 
        break



