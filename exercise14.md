# MC102QR - Algoritmos e Programação de Computadores

## Lab 14 - Recursão Avançada

**Prazo:** 17 de Julho de 2022  
**Peso na nota:** 5 (12,20%)

### Descrição da Atividade

Maria, uma animadora 3D que também é apaixonada por matemática, precisa calcular o quanto o volume de um objeto 3D muda após uma série de transformações lineares. As transformações lineares podem ser representadas por matrizes, e a mudança no volume do objeto é dada pelo determinante da matriz resultante da multiplicação das matrizes de transformação.

Você precisa implementar o cálculo do determinante de uma matriz utilizando a Expansão de Laplace e aplicar a propriedade multiplicativa dos determinantes para encontrar o determinante da multiplicação de várias matrizes.

### Fórmulas e Conceitos

1. **Determinante de uma matriz 2x2:**

   Para uma matriz \( A \) de ordem 2:
   \[
   A = \begin{pmatrix}
   a & b \\
   c & d
   \end{pmatrix}
   \]
   O determinante é:
   \[
   \text{det}(A) = ad - bc
   \]

2. **Expansão de Laplace:**

   Para calcular o determinante de uma matriz \( n \times n \) usando a Expansão de Laplace:
   \[
   \text{det}(B) = \sum_{j=1}^n (-1)^{i+j} B_{i,j} \cdot \text{det}(M_{i,j})
   \]
   onde \( B_{i,j} \) é o elemento da matriz na \( i \)-ésima linha e \( j \)-ésima coluna, e \( M_{i,j} \) é a submatriz obtida removendo a \( i \)-ésima linha e a \( j \)-ésima coluna.

3. **Propriedade Multiplicativa dos Determinantes:**

   Se \( A \) e \( B \) são matrizes, então:
   \[
   \text{det}(AB) = \text{det}(A) \times \text{det}(B)
   \]

### Tarefa

Você deve:

1. **Implementar o cálculo do determinante usando a Expansão de Laplace.**
2. **Multiplicar as matrizes e calcular o determinante da matriz resultante utilizando a propriedade multiplicativa dos determinantes.**

### Entrada

A entrada será fornecida no formato:

- **Primeira linha:** Quantidade \( m \) de matrizes.
- **Segunda linha:** Valor \( n \), a dimensão das matrizes \( n \times n \).
- **Seguintes \( m \times n \) linhas:** Valores das matrizes, seguindo o padrão de \( n \) linhas com os valores das colunas para cada matriz.

### Saída

A saída deve seguir o formato:

Após as m transformações, o objeto n-dimensional teve o volume multiplicado no valor d.

scss
Copiar código

onde \( m \) é a quantidade de matrizes, \( n \) é a dimensão das matrizes, e \( d \) é o valor da determinante após as transformações.

### Exemplo

**Entrada:**
2
2
1 2
3 4
5 6
7 8

makefile
Copiar código

**Saída:**
Após as 2 transformações, o objeto 2-dimensional teve o volume multiplicado no valor -2.

css
Copiar código

### Observações

- É proibido usar bibliotecas que já calculam determinantes ou operações de matrizes.
- A solução deve ser implementada utilizando a recursão para calcular o determinante e a multiplicação das matriz
