#funções
def elementos_unicos(fotos):
    '''essa função fala o total de valores diferentes na lista'''
    a=[]
    for elementos in fotos:
        if elementos not in a:
            a.append(elementos)
    return len(a)

def elemento_consecutivo(fotos):
    '''encontra o elemento com maior numero de consecutivos e o seu total de consecutivos'''
    total=1
    final=1
    elemento=0
    for k in range(1,len(fotos)):
        if fotos[k]==fotos[k-1]:
            total+=1
        else:
            total=1

        if total>final:
            final=total
            elemento=fotos[k]

    return ('{} {}'.format(elemento,final))

def remover_bug(fotos):
    '''essa função remove o valor que é pedido para remover na entrada'''
    while ftos_separado_da_barra[1] in fotos:
        for k in fotos:
            if k==ftos_separado_da_barra[1]:
                apenas_ftos.remove(k)

def organizando_listas(fotos):
    ''' essa função organiza a lista sem reptição e deixa as strings com letra minuscula e com '-' '''
    remover_bug(fotos)
    for elementos in fotos:
        if elementos not in classifica_ftos:
            classifica_ftos.append(elementos)
    for n in range(len(classifica_ftos)):
        separa=classifica_ftos[n].split('_')
        classifica_ftos.append(separa[0])
        classifica_ftos.append(separa[1].replace(' ','-').lower())
    for k in range(len(classifica_ftos)):
        if classifica_ftos[k-1]=='HA':
            HA.append(classifica_ftos[k-1]+'_'+classifica_ftos[k])
        elif classifica_ftos[k-1]=='CR':
            CR.append(classifica_ftos[k-1]+'_'+classifica_ftos[k])
        elif classifica_ftos[k-1]=='CC':
            CC.append(classifica_ftos[k-1]+'_'+classifica_ftos[k])
    


if __name__=="__main__":
    #listas
    classifica_ftos=[]
    HA=[]
    CR=[]
    CC=[]
    #entrada que separa a lista de todas fotos da lista da foto a ser removida
    ftos_separado_da_barra=input().split('/ ')
    #criando listas só com fotos 
    apenas_ftos=ftos_separado_da_barra[0].split(', ')
    #saídas
    print(elemento_consecutivo(apenas_ftos))
    print(elementos_unicos(apenas_ftos))
    organizando_listas(apenas_ftos)
    print(HA)
    print(CR)
    print(CC)