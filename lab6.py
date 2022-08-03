class Salas:
    '''Essa classe define quais sãos as possíveis salas que a sarah pode se mover
,também diz em que sala a sarah e o seu clone estão'''

    def __init__(self,atual_clone,sala_inicial,tamanho_inventario):
        self.atual_clone=atual_clone
        self.sala_inicial=sala_inicial
        self.tamanho_inventario=tamanho_inventario
    
    def posicao_clone(self):
        '''informa a posição do clone'''
        print('DEBUG - O clone está na sala: {X}'.format(X=self.atual_clone))
    
    def sala_inicial_sarah(self):
        '''informa a sala inical em que a sarah está,além disso
        detecta se há itens dentro da sala ,quais sãos as possíveis salas para se mover
        e controla os itens presentes no inventário'''
        global coletar
        global proxima_sala
        global sala_bot
        k=0
        print('Você está na sala de número {}'.format(self.sala_inicial),end='')
        for x in numero_sala:
            if x==self.sala_inicial:
                print(' ela contém um baú com {item}'.format(item=nome_item[k]),end='')
                inventario.append(nome_item[k])
                if self.tamanho_inventario>=len(inventario):
                    nome_item.pop(k)
                    numero_sala.pop(k)
                coletar=True
            k+=1
        print(' e dela você pode ir para as salas {salas}'.format(salas=conexoes_salas[sala_bot]))
        proxima_sala+=1

    
    def sala_atual_sarah(self):
        '''informa a atual sala  em que a sarah está,além disso
        detecta se há itens dentro da sala ,quais sãos as possíveis salas para se mover
        e controla os itens presentes no inventário'''
        global coletar
        global proxima_sala
        k=0
        print('Você está na sala de número {}'.format(sequencia_sala[proxima_sala]),end='')
        for x in numero_sala:
            if x==sequencia_sala[proxima_sala]:
                print(' ela contém um baú com {item}'.format(item=nome_item[k]),end='')
                inventario.append(nome_item[k])
                if self.tamanho_inventario>=len(inventario):
                    nome_item.pop(k)
                    numero_sala.pop(k)
                coletar=True
            k+=1
        print(' e dela você pode ir para as salas {salas}'.format(salas=conexoes_salas[int(sequencia_sala[proxima_sala])]))
        proxima_sala+=1



class Bot:
    '''Essa classe possue as funções que o bot tem no jogo, como:coletar itens e mover.
Além disso, ele define se o inventário está cheio ou não,também tem a função vitoria ou derrota'''
    def __init__(self,tamanho_inventario,atual_clone,atual_sarah):
        self.tamanho_inventario=tamanho_inventario
        self.atual_clone=atual_clone
        self.atual_sarah=atual_sarah
    
    def coletar(self):
        '''determina se o inventário de sarah está cheio ou não'''
        global coletar
        if self.tamanho_inventario>=len(inventario) and coletar==True:
            print('Pegar {item}'.format(item=inventario[-1])) 
            print('{} adicionado ao inventário'.format(inventario[-1]))
            coletar=False

        elif self.tamanho_inventario<len(inventario) and coletar==True:
            print('Pegar {item}'.format(item=inventario[-1])) 
            print('Inventário cheio!')
            coletar=False
            if inventario.count('espada')==1:
                inventario.remove('espada')

    def mover(self):
        '''muda a sala que a sarah está'''
        global proxima_sala
        print('Mover para sala {}'.format(sequencia_sala[proxima_sala]))
        if len(sequencia_sala)>=proxima_sala:
            self.atual_sarah=sequencia_sala[proxima_sala]

        

    def vitoria_derrota(self):
        '''determina se houve vitoria oou derrota de sarah'''
        if inventario.count('poção')==1:
            print('Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...')
            return True
        elif self.atual_clone==self.atual_sarah and inventario.count('espada')==0:
            print('Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...')
            return True
        elif  self.atual_clone==self.atual_sarah and inventario.count('espada')!=0:
            print('Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.')
            print('PARABÉNS!')
            return True
        else:
            return False
 
#listas e variaveis globais
proxima_sala=-1
coletar=False
numero_sala=[]
nome_item=[]
inventario=[]
conexoes_salas=[]
#entradas
quantidade_sala=int(input(''))
for _ in range (quantidade_sala):
    sala,conexao_1,conexao_2,conexao_3,conexao_4=input('').split()
    conexoes_salas.append([int(conexao_1),int(conexao_2),int(conexao_3),int(conexao_4)])
total_itens=int(input(''))
for k in range(total_itens):
    valores=input('').split()
    numero_sala.append(valores[0])
    nome_item.append(valores[1])
sala_clone=int(input(''))
sala_bot=int(input(''))
tamanho_inventario=int(input(''))
sequencia_sala=input('').split()
teste=len(sequencia_sala)
#classes usadas
locomoção=Salas(sala_clone,str(sala_bot),tamanho_inventario)
bot_jogo=Bot(tamanho_inventario,str(sala_clone),str(sala_bot))


#jogo
print('Bem-vindo as Aventuras de Sarah 2.0')
print('Sarah acorda no saguão do antigo castelo de sua família,ela tem a oportunidade única de derrotar o seu clone maligno que se apoderou do reino.')
print('Para isso ela deve encontrar o baú da sua família que contém a espada mágica que apenas a verdadeira herdeira pode utilizar.')
print('Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?')
locomoção.posicao_clone()
locomoção.sala_inicial_sarah()
bot_jogo.coletar()
while bot_jogo.vitoria_derrota()==False:
    bot_jogo.mover()
    if bot_jogo.vitoria_derrota()==True:
        break
    locomoção.sala_atual_sarah()
    bot_jogo.coletar()
    if bot_jogo.vitoria_derrota()==True:
        break






    
    

