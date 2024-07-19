# MC102QR - Algoritmos e Programação de Computadores

## Lab 6 - Objetos e Modelagem

**Prazo da atividade:** 15 de Maio de 2022  
**Peso na nota:** 2 (4,88%)

### Descrição da Atividade

Nesta tarefa, você continuará a história de Sarah, mas a empresa de jogos em que você trabalha resolveu mudar todo o estilo do jogo a ser desenvolvido. A empresa quer apostar na volta dos jogos de aventura baseados em texto, comuns nos anos 70 e 80.

Nesta versão do jogo, Sarah deverá encontrar a espada das fadas para derrotar seu clone maligno. Para encontrar a espada, Sarah deve andar pelas salas do castelo até encontrar o baú de sua família. Como herdeira do reino das fadas, Sarah pode abrir o baú sem receber nenhuma maldição. Neste baú está a espada que permitirá que o clone seja derrotado.

O elemento básico para o novo jogo será um mapa (o castelo) constituído de diferentes salas. Nessas salas existem vários itens que Sarah pode coletar em um inventário de tamanho limitado. Apesar de bastar ter a espada das fadas para derrotar o clone, há algumas condições em que Sarah pode perder para o clone:
- A primeira é: ao explorar o mapa Sarah encontrar o seu clone sem a espada das fadas em seu inventário.
- A segunda é: Sarah coletar o item de poção letal ao seu inventário.

Além de construir o mapa seguindo os requisitos do jogo, você deve testar o jogo construindo um bot para simular as ações possíveis do jogador (texto correspondente às ações que o jogador tomou) que viverá as aventuras de Sarah.

### Tarefa

Nesta tarefa você deve utilizar seus conhecimentos de orientação a objeto para criar o jogo de Sarah. Os elementos principais que você deve implementar são o mapa, que é composto de salas, e as salas devem conter os itens que podem ser coletados por Sarah. Além disso, você deve implementar o bot para simular um jogador. Esse bot não é muito inteligente, logo apenas faz um passeio pelo mapa e coleta todo item disponível na sala. As salas têm exatamente um item e, caso o bot pegue o item da sala e adicione ao seu inventário, a sala fica sem o item.

**Obs1:** Você pode criar novas classes de acordo com o que você achar que é a melhor forma de modelar a solução do problema.

### Entrada

A entrada do programa é composta por:
1. O número de salas do mapa (n)
2. Em seguida, uma lista de inicialização do mapa onde cada linha é o número da sala a ser adicionada no mapa (em ordem crescente de 0 a n-1) e as outras salas conectadas a ela. Uma sala terá obrigatoriamente conexão com 4 outras salas, as salas são numeradas, logo você não precisa se preocupar com a orientação das conexões.
3. O número de itens a serem distribuídos no mapa.
4. Uma lista de itens a serem distribuídos no mapa seguindo o padrão "numero_sala nome_item" (o nome dos itens são sempre uma palavra).
5. O número da sala onde o clone está.
6. O número da sala onde o bot inicia o jogo.
7. A quantidade de itens que a personagem pode carregar no seu inventário.
8. A lista das salas por onde o bot deve passar, em sequência.

### Saída

A saída deve ser a mensagem inicial do jogo, uma mensagem de debug indicando em que sala está o clone, a sala atual onde se encontra o bot, a indicação do item que a sala contém, para quais outras salas o jogador pode ir, a ação do jogador, a mensagem de derrota e a mensagem de vitória. Abaixo as saídas que devem ser mostradas nas situações adequadas.

#### Mensagens de Saída

**Mensagem inicial:**
Bem-vindo às Aventuras de Sarah 2.0
Sarah acorda no saguão do antigo castelo de sua família, ela
tem a oportunidade única de derrotar o seu clone maligno que
se apoderou do reino.
Para isso ela deve encontrar o baú da sua família que contém a
espada mágica que apenas a verdadeira herdeira pode utilizar.
Na sala onde está, Sarah vê várias portas. Qual é a sua próxima
ação?

bash
Copiar código

**Mensagem de debug indicando a sala do clone:**
DEBUG - O clone está na sala: X

markdown
Copiar código

**Mensagem de indicação da sala:**
Você está na sala de número X, ela contém um baú com ITEM e dela você pode ir para as salas LISTA_DE_SALAS

css
Copiar código

**Caso a sala não tenha nenhum item:**
Você está na sala de número X e dela você pode ir para as salas LISTA_DE_SALAS

arduino
Copiar código

**Ações do jogador:**
Mover para sala X
Pegar ITEM

css
Copiar código

**Mensagens para a ação pegar:**
ITEM adicionado ao inventário
Inventário cheio!

markdown
Copiar código

**Mensagens de derrota:**
Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...

Copiar código
Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...

markdown
Copiar código

**Mensagem de vitória:**
Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.
PARABÉNS!
