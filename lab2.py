#titulo da página
from pprint import pformat


print('*Que página de meme do Instagram você é?*')

#váriaveis
print('Qual a sua idade?')
idade=int(input(''))

#condições
if idade<25 and 0<=idade<=125:
    print(idade)
    print('Quantos segundos são necessários para saber se um vídeo é bom?')
    vídeo=int(input(''))
    if vídeo<=5 and vídeo>=0:
        print(vídeo)
        print('RESULTADO')
        print('Você deveria estar no TikTok')
    elif vídeo>5:
        print(vídeo)
        print('RESULTADO')
        print('Sua página de memes é: @meltmemes')
    else: 
        print(vídeo)
        print('Erro: entrada inválida')


if 25<=idade<=40 and 0<=idade<=125:
    print(idade)
    print('Qual banda você gosta mais?')
    banda_favorita=str(input(''))
    if banda_favorita=='A':
        print('A) Matanza')
        print('RESULTADO')
        print('Sua página de memes é: @badrockistamemes')
    if banda_favorita=='B':
        print('B) Iron Maiden')
        print('RESULTADO')
        print('Sua página de memes é: @badrockistamemes')
    if banda_favorita=='C':
        print('C) Imagine Dragons')
        capivaras=str(input('São as capivaras os melhores animais da Terra?'))
        if capivaras=='Sim':
            print('')
            print(capivaras)
            print('RESULTADO')
            print('Sua página de memes é: @genteboamemes')
        if capivaras=='Não':
            print('')
            print(capivaras)
            print('RESULTADO')
            print('Sua página de memes é: @wrongchoicememes')
    if banda_favorita=='D':
        print('D) BlackPink')
        capivaras=str(input('São as capivaras os melhores animais da Terra?'))
        if capivaras=='Sim':
            print('')
            print(capivaras)
            print('RESULTADO')
            print('Sua página de memes é: @genteboamemes')
        if capivaras=='Não':
            print('')
            print(capivaras)
            print('RESULTADO')
            print('Sua página de memes é: @wrongchoicememes')
        else:
            print('')
            print(capivaras)
            print('Erro: entrada inválida')


if idade>40 and 0<=idade<=125:
    print(idade)
    grupo_fml=str(input('Que imagem de bom dia você manda no grupo da família?'))
    if grupo_fml=='A':
        print('')
        print('A) Bebê em roupa de flor')
        print('RESULTADO')
        print("Sua página de memes é: @bomdiabebe")
    elif grupo_fml=='B':
        print('')
        print('B) Gato')
        print('RESULTADO')
        print('Sua página de memes é: @kittykatmsgs')
    elif grupo_fml=='C':
        print('')
        print('C) Coração e rosas')
        print('RESULTADO')
        print("Sua página de memes é: @bomdiaflordodia")
    else:
        print('')
        print(grupo_fml)
        print('Erro: entrada inválida')


elif not 0<=idade<=125:
    print(idade)
    print('Erro: entrada inválida')
    