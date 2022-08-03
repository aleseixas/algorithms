#funções
def cria_relatorio(numero,nld,qntdleitores,qntdlfinal,qntcliques,t):
    nome_relatorio='relatorio_'+numero+'.txt'
    with open(nome_relatorio,'w') as arquivo:
        arquivo.write(nld)
        arquivo.write(qntdleitores)
        arquivo.write(qntdlfinal)
        arquivo.write(qntcliques)
        arquivo.write(t)

def fmedia_paragrafos_e_cliques(lista,qnt_arquivos):
    soma=0
    for k in lista:
        soma+=k
    media=soma//qnt_arquivos
    return media

def fmedia_leitorestotais(dicionario,qntarquivos):
    lista=dicionario.keys()
    soma=0
    for k in lista:
        soma+=k
    media=soma//qntarquivos
    return media

def leitores(dicionario):
    lista=sorted(dicionario.items())
    total=lista[-1][0]
    titulo=lista[-1][1]
    return titulo,total
#entradas
noticias=[]
leitores_totais={}
leitores_finais={}
media_cliques=[]
tempo_lista=[]
media_paragrafos=[]
qnt_arquivos=int(input())
for k in range(qnt_arquivos):
    nome_arquivo=input()
    noticias.append(nome_arquivo)
#pegando dados dos arquivos e crias seus repectivos relatorioa
for k in noticias:
    with open(k,'r') as arquivo:
        nld=arquivo.readline()
        titulo=arquivo.readline()
        #quantidade leitores
        qtdLeitores=arquivo.readline()
        leitores_totais[int(qtdLeitores[13:-1])]=titulo
        #leitores finais
        qtdLeitoresFinal=arquivo.readline()
        leitores_finais[int(qtdLeitoresFinal[18:-1])]=titulo
        #cliques
        qtdCliques=arquivo.readline()
        media_cliques.append(int(qtdCliques[12:-1]))
        #tempo
        tempo=arquivo.readline()
        tempo_lista.append(int(tempo[7:-1]))
        numero_noticia=nld[5:-1]
        cria_relatorio(numero_noticia,nld,qtdLeitores,qtdLeitoresFinal,qtdCliques,tempo)
        #conta paragrafos
        qntdparagrafos=len(arquivo.readlines())
        media_paragrafos.append(qntdparagrafos)


#criando relatorio final
titulo=leitores(leitores_totais)
titulo2=leitores(leitores_finais)
with open('relatorio_final.txt','w') as arquivo:
        arquivo.write(str(fmedia_leitorestotais(leitores_totais,qnt_arquivos))+'\n')
        arquivo.write('"{}" {}'.format(titulo[0][8:-1],titulo[1])+'\n')
        arquivo.write('"{}" {}'.format(titulo2[0][8:-1],titulo2[1])+'\n')
        arquivo.write(str(fmedia_paragrafos_e_cliques(media_cliques,qnt_arquivos))+'\n')
        arquivo.write(str(max(tempo_lista))+'\n')
        arquivo.write(str(fmedia_paragrafos_e_cliques(media_paragrafos,qnt_arquivos))+'\n')