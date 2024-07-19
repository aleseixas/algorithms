# MC102QR - Algoritmos e Programação de Computadores

## Lab 1 - Condicionais Simples

**Prazo da atividade**: 03 de Abril de 2022  
**Peso na nota**: 1 (2,44%)

Edgar Field é um excêntrico dono de loja que decidiu oferecer descontos aos clientes de acordo com o dia em que a compra é feita. Se o dia do mês em que a compra foi feita é múltiplo de 7, o cliente recebe 50% de desconto. Senão, se é sexta-feira o cliente recebe 25% de desconto. Se nenhuma dessas condições ocorre, então o número do dia do mês é descontado do valor da compra. Por exemplo, para uma compra de valor R$ 50,00 no dia 20 o cliente paga apenas R$ 30,00, e para uma compra de R$ 4,00 no dia 10 o cliente paga R$ 0,00.

Edgar contratou você para implementar um programa que calcule o quanto cada cliente irá pagar após receber esses descontos. O programa também deve imprimir uma mensagem de despedida ao cliente, de acordo com o dia da semana. De terça a sexta-feira, a mensagem de despedida é “Agradecemos a preferência, tenha uma ótima XXX!”, onde XXX deve ser substituído pelo dia da semana em questão. Aos sábados e domingos, a mensagem é “Agradecemos a preferência, tenha um ótimo fim de semana!” Por fim, nas segundas-feiras a mensagem é simplesmente “É um dia terrível, você não devia ter saído da cama.” pois o dono da loja odeia segundas-feiras.

### Tarefa
Seu programa deve receber o dia do mês e o dia da semana em que uma compra foi realizada, seu valor em reais, e imprimir como saída o valor final que será pago após aplicado o desconto conforme as regras da loja, além da mensagem de despedida apropriada.

### Entrada
A entrada do programa consiste do dia do mês em que a compra foi realizada (um inteiro de 1 a 31), o dia da semana em que a compra foi realizada (uma string com os possíveis valores: “segunda-feira”, “terça-feira”, “quarta-feira”, “quinta-feira”, “sexta-feira”, “sábado” ou “domingo”), e o valor da compra (um número decimal com dois dígitos após a vírgula) antes de aplicado o desconto.

### Saída
Seu programa deve imprimir como saída o valor final da compra como um número decimal não-negativo com exatamente dois dígitos após a vírgula, e na linha seguinte a mensagem de despedida, formatada exatamente como no enunciado.

### Exemplos

#### Exemplo 1:
**Entrada**
14
sábado
52.00

**Saída**
26.00
Agradecemos a preferência, tenha um ótimo fim de semana!

#### Exemplo 2:
**Entrada**
15
sexta-feira
44.00


**Saída**
33.00
Agradecemos a preferência, tenha uma ótima sexta-feira!


#### Exemplo 3:
**Entrada**
26
segunda-feira
27.00



**Saída**
1.00
É um dia terrível, você não devia ter saído da cama.




### Submissão
Você deverá submeter no CodePost, na tarefa Lab 1, um arquivo com o nome `lab1.py`, contendo todo o seu programa. Após o prazo estabelecido para a atividade, será aberta uma tarefa Lab 1 - Segunda Chance, com prazo de entrega até o fim do semestre.
