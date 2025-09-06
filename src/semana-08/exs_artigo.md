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

> O campo receptivo local é a parte da imagem à qual um único neurônio está conectado.
> A importância do campo receptivo local nas CNNs está em reduzir o número de conexões e permitir que a rede encontre padrões locais, que são mais robustos a pequenas variações e deslocamentos.

- Como funciona o compartilhamento de pesos? Por que ele é vantajoso?

> O compartilhamento de pesos faz com que todas as unidades de um feature map usam o mesmo conjuntos de pesos no processamento de diferentes partes da imagem.
> É vantajoso porque reduz bastante o número de parâmetros, e ainda introduz invariância a deslocamentos. 

- Qual é a função das camadas de subamostragem?

> As camadas de subamostragem realizam uma redução da resolução dos feature maps, por meio de média local e subamostragem. Além disso, essa camada introduz certo nível de invariância a distorções e translações.  

### Resultados (Seção 5)

Observe como os resultados são apresentados e avaliados pelos autores.

**Pontos de atenção:**

- Métricas utilizadas para avaliar o desempenho.
- Critério para rejeição de classificações duvidosas.

**Questões que você deve responder:**

- Quais foram os resultados principais obtidos?

> Após 30 passagens de treinamento, a taxa de erro foi de 1.1% no conjunto de treinamento e o erro quadrático médio(MSE) FOI 0.017.
> No conjunto de testes, a taxa de erro foi de 3.4% e o MSE foi 0.024.
> Todos os erros de classificação ocorreram em caracteres manuscritos. 

- Qual a importância prática do critério de rejeição?

> Em aplicações realistas, o usuário não tem muito interesse na taxa bruta de erro, mas sim no números de rejeições necessárias para atingir um nível de precisão aceitável. 
> Nesse caso, para obter 1% de erro, foi necessário rejeitar 5.7% dos padrões no conjunto completo de testes, já no subconjunto de dígitos manuscritos foram 9%.

### Conclusão (Seção 6)

Reflita sobre as conclusões finais tiradas pelos autores com base nos resultados obtidos.

**Pontos de atenção:**

- Principais contribuições do artigo para o avanço das CNNs.
- Importância da arquitetura específica utilizada pelos autores.

**Questões que você deve responder:**

- Quais vantagens os autores identificaram ao usar CNNs com aprendizado via backpropagation?

> Permite treinar com dados pouco processados, reduz o tempo de aprendizado, escala bem para tarefas maiores, pode ser implementado em hardware comercial de processamento de digital de sinais ("Our results appear to be at the state of the art in handwritten digit recognition").


- Por que é importante ter restrições na arquitetura e nos pesos da rede?

> Para incorporar reconhecimento da tarefa, melhorar a generalização, reduzir o tempo de treinamento e reduzir o pré-processamento.