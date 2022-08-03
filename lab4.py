#entrando com o primeiro valor
dados=[1,2,3]
modulo=[]
#entrando com o laço
while dados[0]!='0':
    dados.clear()
    dados=str(input('')).split(' ')
    if len(dados)<=2:
        break
    operador=dados[0]
    n1=int(dados[1])
    n2=int(dados[2])
    if operador=='+':
        print(n1+n2)
    if operador=='-':
        print(n1-n2)
    if operador=='*':
        print(n1*n2)
    if operador=='/':
        print(n1//n2,n1%n2)
    if operador==';':
        contador=0
        dados=[n1,n2]
        if n1==n2:
            n1=n1+contador
            print(0,end='')
            print('')
            
        else: 
            while contador<max(dados):
                contador+=1
                x=(n1-n2)%contador
                if x==0 and contador<max(dados):
                    modulo.append(contador)
        for k in range(len(modulo)-1):
            print(modulo[k],end=' ')
        if n1!=n2 and len(modulo)!=1:
            print(modulo[k+1])
        if len(modulo)==1:
            print(1)
        modulo.clear()