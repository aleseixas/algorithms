#função
def alterando_nomes():
    ''''essa função utiliza da recursão para printar os valores na tela, quando acabar
    o looping, a função retorna TRUE'''
    if len(lista_arquivos) == 0:
        return True
    arquivo=lista_arquivos[0]
    if len(lista_arquivos) > 0:
        print(arquivo)
        lista_arquivos.pop(0)
        return alterando_nomes()
#variaveis
lista_arquivos=[]
#entradas 
pasta_raiz,n=input().split()
for k in range(int(n)):
    arquivo,nome_pasta=input().split()
    #manipulando entradas
    lista_arquivos.append(nome_pasta+'_'+arquivo)
    tamanho_pasta=len(nome_pasta.split('_'))
    #analisando o caminho do arquivo
    for valores in lista_arquivos:
        if tamanho_pasta >= 2:
            parte_arquivo = valores.split('_', maxsplit = 1) 
            parte_arquivo = parte_arquivo[-1]
        else:
            parte_arquivo = valores.split('_')
            parte_arquivo = parte_arquivo[-1]
        if parte_arquivo == nome_pasta:
            lista_arquivos.pop()
            lista_arquivos.append(valores+'_'+arquivo)
#recursão
alterando_nomes()