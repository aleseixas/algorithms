# MC102QR - Algoritmos e Programação de Computadores

## Lab 10 - Combinando Estruturas de Dados

**Prazo:** 12 de Junho de 2022  
**Peso na nota:** 3 (7,32%)

### Descrição da Atividade

Neste laboratório, você utilizará seus conhecimentos de programação para ajudar na construção de diagramas de filogenia, especificamente o Cladograma, que mostra a relação de ancestralidade entre grupos de animais. O Cladograma é representado em forma de árvore, agrupando espécies com base em características evolutivas.

Você será responsável por construir um cladograma a partir de um conjunto de amostras de DNA de espécies alienígenas. A tarefa é contar o número de mutações ocorridas desde o DNA mais ancestral, organizando as características e as espécies de acordo com sua ancestralidade. 

### Tarefa

Seu programa deve:

1. **Agrupar as espécies de acordo com a ancestralidade** e imprimir as características mais ancestrais e as espécies definidas por essas características.
    - Encontre a ordem das características e conte o número de mutações em relação ao DNA ancestral.
    - Identifique quais espécies são caracterizadas por cada característica e imprima em ordem decrescente de ancestralidade.

**Aspectos do DNAA:**

1. O DNAA é formado por pares de proteínas base que se ligam.
2. Existem 5 proteínas: "B", "C", "D", "E", "F". Cada base se liga com qualquer outra base.
3. As mutações são contadas pela diferença e pela ordem dos pares. Pares menores lexicograficamente não são considerados mutações.

### Entrada

A entrada para a formação do cladograma será formada pelos seguintes componentes:

- **Quantidade de espécies** a serem utilizadas no cladograma.
- **Lista de espécies e suas características**:
  - Formato: `id nome_espécie nome_científico | carac_1, carac_2, ..., carac_n`
- **Quantidade de características** a serem levadas em conta.
- **Nome da característica** e duas sequências de letras (de mesmo tamanho) representando cada fita de DNAA na linha seguinte. Cada par é formado por uma letra da primeira linha e a outra letra na mesma posição da linha seguinte.

### Saída

A saída do programa deve ser a estrutura de grupos do cladograma:

- Nome da característica e o nome das espécies que contêm exclusivamente essa característica como a mais ancestral.
- Grupos devem ser ordenados por ordem decrescente de ancestralidade. As espécies são ordenadas ascendentemente por id.

**Formato da saída:**

CARACTERÍSTICA: X
id1 nome_espécie1 nome_científico1
id2 nome_espécie2 nome_científico2
...

==========
CARACTERÍSTICA: Y
id3 nome_espécie3 nome_científico3
id4 nome_espécie4 nome_científico4
...

==========

kotlin
Copiar código

### Observações

- A partir do Python 3.7, a ordem de inserção em dicionário é garantida. Caso esteja usando versões anteriores, utilize `OrderedDict` da biblioteca `collections`.
- Use a função `sorted()` para ordenar listas.
