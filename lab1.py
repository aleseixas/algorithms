#variaveis
dia_mes=int(input(''))
dia_semana=str(input(''))
preço=float(input(''))
multiplo_7=dia_mes%7

#descobrindo o valor do produto
if multiplo_7==0 and dia_mes<preço:
    print(('{:.2f}'.format(preço/2)))
elif dia_semana=='sexta-feira':
        print(('{:.2f}'.format(preço-preço*0.25)))

#casos que podem dá valores menor que 0
elif dia_mes>=preço:
    print('{:.2f}'.format(0))
else:
    print(('{:.2f}'.format(preço-dia_mes)))

#frase que sera imprimida
if dia_semana=='segunda-feira':
    print('É um dia terrível, você não devia ter saído da cama.')
elif dia_semana=='sábado' or dia_semana=='domingo':
    print('Agradecemos a preferência, tenha um ótimo fim de semana!')
else:
    print('Agradecemos a preferência, tenha uma ótima {}!'.format(dia_semana))


