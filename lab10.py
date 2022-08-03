#função
def junta_genes(gene1,gene2):
    pares=[]
    for alelos in range(len(gene1)):
        pares.append(gene1[alelos]+gene2[alelos])
    return pares

def imprime(animais,adjetivos):
    contador=0
    for k in adjetivos:
        print('CARACTERÍSTICA: {}'.format(k))
        for id,valor in animais.items():
            for id_2,caracter in id_caracter.items():
                if id==id_2 and caracter==k:
                    print('{} {}'.format(id,valor.strip()))

#dicionario e lista
animais={}
ascentral_idade={}
id_caracter={}
adjetivos=[]
aux=0
#entradas
n_especies=int(input())
for k in range(n_especies):
    nomes=input().split('|')
    dic_especies=nomes[0].split(maxsplit=1)
    caracter=nomes[1].split()
    id=dic_especies[0]
    nome_científico=dic_especies[1]
    #add valores
    animais[id]=nome_científico
    id_caracter[id]=caracter

#entradas para os genes
qnt_caract=int(input())
nome_caracter=input()
gene_1=input()
gene_2=input()
par_especial=junta_genes(gene_1,gene_2)
ascentral_idade[0]=nome_caracter
for k in range(qnt_caract-1):
    contador=0
    nome_caracter=input()
    gene_1=input()
    gene_2=input()
    par_compara=junta_genes(gene_1,gene_2)
    for pares in range(len(par_especial)):
        if par_especial[pares]<par_compara[pares]:
            contador+=1
    ascentral_idade[contador]=nome_caracter

ordenando_ascentral=sorted(ascentral_idade.items())
for k in range(len(ordenando_ascentral)):
    adjetivos.append(ordenando_ascentral[k][1])

#descobre a caracteristica com maior numero de na especie mutações
for k in range(n_especies):
    aux=0
    for id,lista in id_caracter.items():
        for valores in lista: 
            for mutacoes,caracter in ascentral_idade.items():
                if valores==caracter and int(mutacoes)>=int(aux):
                    id_caracter[id]=valores
                    aux=mutacoes

imprime(animais,adjetivos)
