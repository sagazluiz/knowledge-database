**Sentence-BERT: Embeddings de Frase usando Redes BERT-Siamese**

## Resumo Executivo

O Sentence-BERT é uma técnica para criar embeddings de frases usando redes BERT-Siamese. Ele utiliza a semelhança entre duas frases como critério de otimização, permitindo que as frases sejam comparadas e classificadas em tarefas específicas.

## Componentes e Arquitetura Técnica

A arquitetura do Sentence-BERT consiste em duas redes neurais BERT idênticas, uma para cada frase a ser comparada. As saídas das duas redes são concatenadas e passadas por uma camada fully connected (completa) para produzir um único vetor de saída.

O processo de treinamento envolve a otimização da semelhança entre as frases usando uma loss function específica, chamada de loss function de semelhança. Essa função mede a similaridade entre as duas frases e ajusta os parâmetros das redes para minimizar a diferença entre as saídas esperadas e obtidas.

## Glossário de Entidades

* BERT: Uma arquitetura de modelo de linguagem deep learning, baseada em transformadores.
* Embeddings: Vetores numéricos que representam palavras ou frases em um espaço vetorial.
* Semelhança: Uma medida da similaridade entre duas frases ou textos.

## Metadados
- **Arquivo Original:** Sentence-BERT\_Sentence\_Embeddings\_using\_Siamese\_BERT-Networks\_D19-1410.pdf
- **Data de Ingestão:** 2026-04-10