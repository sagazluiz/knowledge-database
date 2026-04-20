### ARQUIVO: Evaluating Accuracy in Large Language Models: Benchmarking Corrective Rag Vs. Naive Retrieval Augmented Generation Approach.pdf

<CONTENT>
## Resumo Executivo
Este documento apresenta uma comparação entre duas abordagens de Retrieval-Augmented Generation (RAG): a RAG simples e a Corrective Retrieval-Augmented Generation (CRAG). A CRAG é uma extensão da RAG que visa melhorar o processo de recuperação e utilização de documentos para tarefas que exigem conhecimento. A CRAG introduz um avaliador de recuperação, integração de busca na web e um algoritmo decompor-então-recompor.

## Componentes e Arquitetura Técnica

### RAG Simples
A RAG simples consiste em dois componentes principais: um recuperador e um gerador. O recuperador é um índice vetorial denso de um corpus de conhecimento externo, enquanto o gerador é um modelo de seqüência pré-treinado que gera tokens condicionados à entrada, ao documento recuperado e aos tokens anteriormente gerados.

### CRAG
A CRAG estende a RAG simples com três principais componentes:

1. **Avaliador de Recuperação:** Um modelo neural leve que avalia a qualidade e relevância dos documentos recuperados para uma consulta dada.
2. **Integração de Busca na Web:** Usa resultados de busca na web para expandir o escopo e diversidade das informações recuperadas quando os documentos não são suficientes ou ambíguos.
3. **Algoritmo Decompor-Então-Recompor:** Refina os documentos recuperados ao extrair as passagens mais relevantes e descartar conteúdo não essencial.

### Uso com LLMs
A CRAG pode ser integrada a modelos de linguagem grandes (LLMs) para melhorar seu desempenho em tarefas que exigem acesso a conhecimento externo. A integração da CRAG no pipeline do LLM permite ao modelo acessar e utilizar knowledge específico da organização ou do usuário.

## Glossário de Entidades

- **RAG:** Retrieval-Augmented Generation (Geração Augmentada por Recuperação)
- **CRAG:** Corrective Retrieval-Augmented Generation (Geração Augmentada por Recuperação Corretiva)
- **LLMs:** Large Language Models (Modelos de Linguagem Grandes)

## Metadados
- **Arquivo Original:** Evaluating Accuracy in Large Language Models: Benchmarking Corrective Rag Vs. Naive Retrieval Augmented Generation Approach.pdf
- **Data de Ingestão:** 2026-04-10