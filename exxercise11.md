# MC102QR - Algoritmos e Programação de Computadores

## Lab 11 - Homem-aranha sem casa - O retorno

**Prazo:** 19 de Junho de 2022  
**Peso na nota:** 4 (9,76%)

### Descrição da Atividade

Peter Parker enfrenta novos desafios ao tentar equilibrar sua vida universitária, suas atividades como herói e seu trabalho como fotógrafo para o Clarim Diário. Para conseguir um aumento, ele precisa organizar e extrair informações de arquivos de texto com notícias lançadas, gerando relatórios a partir desses dados.

Cada arquivo de notícia contém informações estruturadas que devem ser extraídas e utilizadas para criar relatórios individuais e um relatório final.

### Estrutura dos Arquivos de Notícia

Cada arquivo `.txt` de uma notícia contém as seguintes informações na ordem:

1. **Número identificador da notícia:** `[nId:]`
2. **Título da notícia:** `[titulo:]`
3. **Quantidade de leitores total:** `[qtdLeitores:]`
4. **Quantidade de leitores que foram até o final da notícia:** `[qtdLeitoresFinal:]`
5. **Quantidade de cliques em anúncios:** `[qtdCliques:]`
6. **Tempo médio que os leitores ficaram na página:** `[tempo:]`
7. **Conteúdo da notícia** (em várias linhas): `[noticia:]`

### Tarefas

1. **Gerar um arquivo de relatório para cada notícia:**
   - O nome do arquivo deve ser `relatorio_[numero_identificador_da_noticia].txt`.
   - Formato do relatório:
     ```
     nId: [numero_identificador]
     qtdLeitores: [quantidade_de_leitores_total]
     qtdLeitoresFinal: [quantidade_de_leitores_que_foram_ate_o_final]
     qtdCliques: [quantidade_de_cliques]
     tempo: [tempo_medio_em_segundos]
     ```

2. **Gerar um arquivo final de relatório com base nas informações extraídas das notícias:**
   - Nome do arquivo: `relatorio_final.txt`
   - Informações a serem incluídas:
     1. Média de leitores totais (valor inteiro)
     2. Título da notícia com mais leitores totais (entre aspas duplas), seguido da quantidade de leitores totais
     3. Título da notícia com mais leitores que foram até o final da notícia (entre aspas duplas), seguido da quantidade de leitores que foram até o final
     4. Média de cliques em anúncios (valor inteiro)
     5. Maior tempo médio dentre todas as notícias
     6. Média de quantidade de parágrafos em cada notícia (valor inteiro)

### Entrada

A entrada será fornecida no terminal da seguinte forma:

- **Primeira linha:** Quantidade de arquivos a serem analisados (`n`).
- **Linhas subsequentes:** Nomes dos arquivos a serem analisados.

Os arquivos estarão divididos em pastas de teste, e cada pasta conterá um arquivo com as entradas para serem inseridas no terminal. Exemplo de estrutura de arquivos:

- **Pasta:** `teste_1`
  - **Arquivos de notícias:** `noticia_1.txt`, `noticia_2.txt`, etc.
  - **Arquivo de entrada:** `t1_in.txt`

### Observações

1. **Número de arquivos de saída:** Se houver `n` notícias, serão gerados `n+1` arquivos (um para cada notícia + o relatório final).
2. **Formato das saídas:** Siga o formato especificado para os relatórios individuais e o relatório final.
3. **Testes:** Realize testes localmente para garantir que seu código funcione corretamente com os arquivos fornecidos.

### Exemplo de Formato de Arquivo de Relatório

**relatorio_54.txt**
nId: 54
qtdLeitores: 1054
qtdLeitoresFinal: 541
qtdCliques: 645
tempo: 126

Copiar código

**relatorio_final.txt**
574
“HOMEM-ARANHA FORAGIDO” 5410
“NOVA SUBSTÂNCIA PRODUZIDA PELA OSCORP” 1428
246
1054
