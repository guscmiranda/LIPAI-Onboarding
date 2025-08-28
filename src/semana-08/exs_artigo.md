# Questôes relacionadas ao artigo científico "Handwritten Digit Recognition with a Back-Propagation Network", publicado por LeCun e colaboradores em 1989.


### **Introdução (Seções 1 e 2)**

Nesta seção, concentre-se em entender qual problema está sendo resolvido e por que ele é importante.

**Pontos de atenção:**

- Motivação da escolha dos dígitos manuscritos.
- Diferença deste método em relação a trabalhos anteriores.

**Questões que você deve responder:**

- Por que os autores escolheram dígitos manuscritos como aplicação?

> Os autores escolheram dígitos manuscritos como aplicação porque é uma tarefa relativamente simples, já que a entrada consiste apenas de pixels brancos e pretos, em geral os dígitos são bem sepradados do plano de fundo e existem apenas 10 categorias de output.

- O que diferencia o método deste artigo dos métodos anteriores?

> Diferentemente de métodos anteriores, a rede é diretamente alimentada com imagens, em vez de características extraídas manualmente, demonstrando a habilidade das redes treinadas com backpropagation de lidar com grandes volumes de informação de baixo nível.

### Preprocessamento (Seção 3)

Entenda quais passos foram necessários antes que os dados fossem utilizados para treinamento.

**Pontos de atenção:**

- Normalização das imagens e padronização dos dados.

**Questões que você deve responder:**

- Por que as imagens precisam ser redimensionadas?

> Como o input de uma rede treinada com backpropagation tem tamanho fixo, faz-se necessário normalizar o tamanho das imagens. 

- Por que a normalização das imagens é importante?

> A normalização é importante para garantir a uniformização das dimensões de entrada. Além disso, a aplicação de uma transformação linear ajusta os valores dos pixels para a faixa entre -1 e 1, facilitando o aprendizado da rede ao tornar o processo mais estável e eficiente.

### Arquitetura da Rede (Seção 4)

Explore como foi estruturada a rede neural convolucional proposta pelos autores.

**Pontos de atenção:**

- Camadas convolucionais e o conceito de campo receptivo local.
- Compartilhamento de pesos (weight sharing).
- Camadas de subamostragem (subsampling).

**Questões que você deve responder:**

- O que é campo receptivo local e qual sua importância em CNNs?
- Como funciona o compartilhamento de pesos? Por que ele é vantajoso?
- Qual é a função das camadas de subamostragem?

### Resultados (Seção 5)

Observe como os resultados são apresentados e avaliados pelos autores.

**Pontos de atenção:**

- Métricas utilizadas para avaliar o desempenho.
- Critério para rejeição de classificações duvidosas.

**Questões que você deve responder:**

- Quais foram os resultados principais obtidos?
- Qual a importância prática do critério de rejeição?

### Conclusão (Seção 6)

Reflita sobre as conclusões finais tiradas pelos autores com base nos resultados obtidos.

**Pontos de atenção:**

- Principais contribuições do artigo para o avanço das CNNs.
- Importância da arquitetura específica utilizada pelos autores.

**Questões que você deve responder:**

- Quais vantagens os autores identificaram ao usar CNNs com aprendizado via backpropagation?
- Por que é importante ter restrições na arquitetura e nos pesos da rede?

## Após a leitura

Prepare-se para discutir os seguintes pontos: 

- Qual foi a importância histórica e prática deste artigo para o desenvolvimento das CNNs?
- Quais são as diferenças entre as dificuldades enfrentadas pelos autores na época e as que enfrentamos hoje?
- Como você acha que a arquitetura proposta evoluiu até os dias atuais?