**Retrieval-Augmented Generation**

## Resumo Executivo

O Retrieval-Augmented Generation (RAG) é uma abordagem para tarefas de linguagem natural que utiliza grandes modelos de linguagem com ferramentas externas para aumentar a precisão, correção e compreensão contextual. Este artigo revisa os conceitos-chave do RAG, como ele difere dos sistemas anteriores que recuperavam ou geravam conteúdo, sua utilização em questionamento, gestão de conhecimento e geração de conteúdo, bem como suas limitações, incluindo a qualidade da recuperação, o requisito para computadores de alto desempenho, integração complicada e problemas de privacidade de dados. O artigo também explora novas abordagens para endereçar essas limitações.

## Componentes e Arquitetura Técnica

O RAG consiste em dois componentes principais: um recuperador e um gerador. Os recuperadores podem ser densos (como os modelos dual-encoder, como DPR [19] e Atlas [20]), esparsos (como BM25 [22]) ou uma combinação desses tipos [3], [4]. Os geradores são tipicamente modelos seq2seq LLMs (por exemplo, BART [8] e T5 [15]). Há três estratégias principais para a fusão dos passagens recuperados: marginalização no nível da sequência (RAG-Sequence), integração no nível do token (RAG-Token) [17] ou atenção cruzada com concatenação (FiD) [8]. Algumas abordagens, como Self-RAG, melhoram o desempenho gerando críticas e obtendo mais evidências [10].

## Glossário de Entidades

* **Retrieval-Augmented Generation (RAG):** Uma abordagem para tarefas de linguagem natural que utiliza grandes modelos de linguagem com ferramentas externas.
* **Dual-encoder models:** Modelos que consistem em dois encoders, um para as consultas e outro para os documentos.
* **BM25:** Um algoritmo de busca de informação esparsa baseado em estatísticas de frequência de palavras.
* **LLMs (Large Language Models):** Modelos de linguagem grandes treinados em grandes conjuntos de dados de texto.

## Metadados

* **Arquivo Original:** Retrieval-Augmented Generation: A Comprehensive Survey of Foundations, Evolution, Applications, Limitations, and Future Directions.pdf
* **Data de Ingestão:** 2026-04-10