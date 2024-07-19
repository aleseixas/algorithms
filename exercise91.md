MC102QR - Algoritmos e
Programação de Computadores

Lab 9 - Objetos Multidimensionais

Prazo da atividade: 04 de Julho de 2022
Peso na nota: 3 (7,32%)
Um pixel é o menor elemento em um dispositivo de exibição (por exemplo, um
monitor) ao qual se pode atribuir uma cor. Assim, uma imagem pode ser
representada como uma matriz de pixels. Um editor de imagens é um programa que
manipula essa matriz de forma a gerar os efeitos desejados.
Tarefa
Você deve implementar um editor de imagens simples com as seguintes operações:
espelhamento (horizontal ou vertical), rotação de 90o graus no sentido horário,
seleção retangular, recorte e cópia. Considera-se a princípio que toda a imagem
está selecionada até que outra seleção seja feita.
A operação de espelhamento deve agir apenas na região selecionada. A operação
de rotação deve rotacionar a área selecionada, sobrepondo pixels da imagem
original caso necessário, e zerando pixels que foram movidos sem reposição. A
operação de recorte deve zerar a área selecionada, e sobrepor outra região da
imagem com os pixels antigos da seleção. A operação de cópia sobrepõe uma
região com os pixels da seleção da mesma forma, porém não zera a área
selecionada. Nenhuma operação altera as dimensões originais da imagem, nem
tenta selecionar ou alterar índices inválidos (isto é, além das dimensões da
imagem).
Nota: você deve implementar explicitamente todas as operações de matriz
descritas, sem o uso de módulos python que tenham essas funções prontas.
As imagens a seguir mostram exemplos das operações:

Figura 1: Rotação aplicada à toda a imagem. Note que esse caso só ocorrerá se a imagem for
quadrada, do contrário tentaria mover pixels para além das dimensões originais da imagem.

Figura 2: Rotação aplicada à uma região selecionada. Note a região preta (pixels de valor zero)
formada no processo, e note também que a seleção continua a mesma, sem rotacionar com a

imagem.

Figura 3: Espelhamento vertical aplicado à toda a imagem.

Figura 4: Espelhamento horizontal aplicado à uma região selecionada.

Figura 6: Cópia de uma região selecionada. Note que a seleção continua na posição em que estava,

não muda para a posição da cópia.

Figura 8: Recorte de uma região selecionada.

Entrada
A primeira linha da entrada consiste da largura l e altura a da imagem original. A
segunda linha consiste da quantidade n de operações a serem feitas. As próximas a
linhas contém a matriz de pixels da imagem (por simplicidade, seu editor deve
considerar apenas imagens em tons de cinza, onde cada pixel é representado por
um único número com três dígitos, de 000 a 255, indicando sua luminosidade). As
últimas n linhas da entrada listam as operações que serão realizadas.
A operação “espelhamento” é seguida do caractere “v” ou “h”, indicando se o
espelhamento é vertical ou horizontal. A operação “selecao” é seguida de quatro

inteiros, os dois primeiros indicam as coordenadas do canto superior esquerdo da
seleção, e os dois últimos indicam a largura e altura da seleção, respectivamente.
As operações “recorte” e “copia” são seguidas de dois inteiros, indicando as
coordenadas do canto superior esquerdo da região em que os pixels da seleção
serão colados.
Nota: É recomendado o uso da função string.strip() ao ler palavras da
entrada, para evitar que espaços em branco atrapalhem comparações entre strings
no código.
Saída
A saída deverá ser a matriz de pixels da imagem após realizadas todas as
operações, onde o valor de cada pixel deve ser impresso com três dígitos.
