import datetime
#função para datetime
def converter_datas(string):
    ano=int('{}{}{}{}'.format(string[-4],string[-3],string[-2],string[-1]))
    mes=int('{}{}'.format(string[-6],string[-5]))
    dia=int('{}{}'.format(string[-8],string[-7]))
    data_datetime=datetime.date(ano,mes,dia)
    return data_datetime
#armazenamento
modo_operar=3
categorias=set()
categorias_2=[]
produto_valores={}
reposição=set()
datas_vencimento=[]
saldo_total=0
#inputs com manipulação de dados
while modo_operar!='0':
    modo_operar=input()
    if modo_operar=='0':
        data=input()
        #organizando o dicionario e conjunto
        organizando_produto=sorted(produto_valores)
        organizando_categorias=sorted(categorias)
        organizando_reposição=sorted(reposição)
        #estoque
        print('* ESTOQUE')
        if len(categorias)>0:
            for valores in organizando_categorias:
                print('- {}'.format(valores))
                for chaves_dic in organizando_produto:
                    if valores==produto_valores[chaves_dic][1]:
                        print('{} {}'.format(chaves_dic,produto_valores[chaves_dic][0]))
        #saldo
        print('* SALDO {:.2f}'.format(saldo_total))
        #reposição
        if len(reposição)>0:
            print('* REPOSICAO')
            for k in organizando_reposição:
                if k not in produto_valores:
                    print(k)
        #promoções
        for chaves in produto_valores:
            vencimento=converter_datas(produto_valores[chaves][3])
            hoje=converter_datas(data)
            diferença=(vencimento-hoje).days
            if diferença<=7:
                datas_vencimento.append(chaves)
        if len(datas_vencimento)>0:
            print('* PROMOCAO')
            for k in datas_vencimento:
                print(k)

    
    elif modo_operar=='1':
        n_entradas=int(input())
        for k in range(n_entradas):
            operaçao=input().split()
            if operaçao[0]=='0':
                #inserir o valores no dicionario
                if operaçao[1] in produto_valores:
                    categorias_2.remove(produto_valores[operaçao[1]][1])
                produto_valores[operaçao[1]]=[operaçao[2],operaçao[3],operaçao[4],operaçao[5]]
                categorias.add(operaçao[3])
                categorias_2.append(operaçao[3])
            elif operaçao[0]=='1':
                #remover os valores no dicionario
                produto=operaçao[1]
                quantidade_excluir=int(operaçao[2])
                teste=produto_valores.get(produto, False)
                if teste==False:
                    print('ERROR')
                else:
                    quantidade_inicial=int(produto_valores[produto][0])
                    if quantidade_inicial>=quantidade_excluir:
                        produto_valores[produto][0]=str(quantidade_inicial-quantidade_excluir)
                        print('SUCCESS')
                    elif quantidade_inicial<quantidade_excluir:
                        print('ERROR')

    elif modo_operar=='2':
        #insere o porduto e quantidades entrando no estoque
        n_entradas=int(input())
        for k in range(n_entradas):
            operaçao=input().split()
            #variaveis
            produto=operaçao[0]
            quantidade_excluir=int(operaçao[1])
            teste=produto_valores.get(produto, False)
            #analisando os produtos vendidos 
            if teste==False:
                pass
            else:
                #variaveis
                quantidade_inicial=int(produto_valores[produto][0])
                valor_produto=float(produto_valores[produto][2])
                categoria=produto_valores[produto][1]
                #saldo
                saldo=0
                saldo=quantidade_excluir*valor_produto
                produto_valores[produto][0]=str(quantidade_inicial-quantidade_excluir)
                saldo_total+=saldo
                #funcioanamento
                if produto_valores[produto][0]<='0':
                    reposição.add(produto)
                    produto_valores.pop(produto)
                    categorias_2.remove(categoria)
                    if categorias_2.count(categoria)==0:
                        categorias.discard(categoria)
            
            
            