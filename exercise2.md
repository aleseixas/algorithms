# MC102QR - Algoritmos e Programação de Computadores

## Lab 2 - Condicionais Encadeados

**Prazo da atividade**: 10 de Abril de 2022  
**Peso na nota**: 1

Além de gostar de programação, você provavelmente se interessa pelas profundezas da natureza humana. Como todos nós sabemos, a melhor forma de entender o ser humano é através dos testes do BuzzFeed. Por isso neste laboratório iremos desenvolver o que seria um teste do BuzzFeed intitulado "Que página de meme do Instagram você é?" (todas serão fictícias, pois nenhuma quis pagar a publicidade dos labs de MC102). Vamos às perguntas.

A primeira pergunta será "Qual a sua idade?". Se a resposta for menor que vinte e cinco será feita a pergunta "Quantos segundos são necessários para saber se um vídeo é bom?". Já se a resposta da idade for 25 ≤ x ≤ 40 a pergunta deve ser "Qual banda você gosta mais?". Caso a idade for x > 40, a próxima pergunta deve ser "Que imagem de bom dia você manda no grupo da família?". 

Para a pergunta "Quantos segundos são necessários para saber se um vídeo é bom?" se a resposta for x <= 5 o resultado do teste é "Você deveria estar no TikTok", caso contrário o resultado do teste é "@meltmemes". 

A pergunta "Qual banda você gosta mais?" tem as seguintes opções: A) Matanza, B) Iron Maiden, C) Imagine Dragons, D) BlackPink. Se a resposta for "A" ou "B" o resultado do teste é "@badrockistamemes", já se a resposta for "C" ou "D" a pergunta "São as capivaras os melhores animais da Terra?" deve ser respondida.

Para a pergunta da imagem de bom dia, as opções são: A) Bebê em roupa de flor, B) Gato, C) Coração e rosas. Se a resposta for "A" o resultado do teste é "@bomdiabebe", se for "B" a resposta o resultado do teste é "@kittykatmsgs", no caso de resposta "C" o resultado é "@bomdiaflordodia". 

Por fim, para a pergunta se capivaras são os melhores animais da Terra, as respostas podem ser "Sim", o resultado será "@genteboamemes", e "Não", onde o resultado é "@wrongchoicememes". Com isso você terá criado um teste inovador para compartilhar por aí.

### Entrada
A entrada é composta simplesmente pelos números correspondentes às opções escolhidas.

### Restrições
- O programa não deve aceitar opções de resposta que não foram oferecidas ao usuário.
- A idade é no mínimo 0 e no máximo 125 anos.
- Não existe tempo negativo.

### Saída
Seu programa deve imprimir como saída o nome do teste, as perguntas feitas e suas respectivas respostas, e por fim o resultado do teste. Caso tenha entradas que se enquadrem em uma das restrições acima a mensagem "Erro: entrada inválida" deve ser impressa. Ao divulgar o resultado do teste deve ser escrito na tela "RESULTADO" e na linha seguinte para indicar a página do resultado a mensagem "Sua página de memes é: X", onde X é o resultado do teste. Os exemplos abaixo especificam como seriam a entrada e saída de um programa correto.  
**Observação:** Para o seu programa passar nos testes automáticos use exatamente a mesma grafia do enunciado no que for a saída do programa.

### Exemplos

#### Exemplo 1:
**Entrada**
20
3


**Saída**
Que página de meme do Instagram você é?
Qual a sua idade?
20
Quantos segundos são necessários para saber se um vídeo é bom?
3
RESULTADO
Você deveria estar no TikTok

#### Exemplo 2:
**Entrada**
-10

**Saída**
Que página de meme do Instagram você é?
Qual a sua idade?
-10
Erro: entrada inválida

#### Exemplo 3:
**Entrada**
28
D
Sim

**Saída**
Que página de meme do Instagram você é?
Qual a sua idade?
28
Qual banda você gosta mais?
D) BlackPink
São as capivaras os melhores animais da Terra?
Sim
RESULTADO
Sua página de memes é: @genteboamemes


### Submissão
Você deverá submeter no CodePost, na tarefa Lab 2, um arquivo com o nome `lab2.py`, contendo todo o seu programa. Após o prazo estabelecido para a atividade, será aberta uma tarefa Lab 2 - Segunda Chance, com prazo de entrega até o fim do semestre.
