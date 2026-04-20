# TREC-8 Question Answering Track Report

## Resumo Executivo

O relatório do TREC-8 Question Answering Track descreve a primeira grande avaliação de sistemas de resposta a perguntas independentes de domínio. O objetivo da tarefa era recuperar pequenos trechos de texto que contivessem a resposta exata para uma pergunta, em vez de listas de documentos tradicionalmente retornadas por sistemas de recuperação de texto. Os resultados mostram que abordagens simples baseadas em "saco de palavras" eram adequadas para encontrar respostas quando as respostas podiam ter até 250 bytes, mas processamento mais sofisticado era necessário para respostas mais diretas (50 bytes).

## Componentes e Arquitetura Técnica

Os participantes usaram uma variedade de abordagens para resolver o problema da resposta a perguntas. A maioria dos sistemas tentou classificar uma pergunta de acordo com o tipo da resposta, como sugerido pela palavra-chave da pergunta. Em seguida, eles recuperaram uma pequena porção da coleção de documentos usando tecnologia padrão de recuperação de texto e a pergunta como consulta. O sistema então realizou um parse superficial dos documentos retornados para detectar entidades do mesmo tipo que a resposta. Se uma entidade do tipo apropriado fosse encontrada suficientemente próxima às palavras da pergunta, o sistema retornava essa entidade como resposta.

## Glossário de Entidades

- TREC (Text REtrieval Conference)
- QA (Question Answering)
- IBM Research
- AT&T Labs Research
- CL Research
- Cymfony, Inc.
- GE/U. of Pennsylvania
- LIMSI-CNRS
- MITRE Corporation
- New Mexico State U.
- NTT Data Corp.
- Southern Methodist U.
- University of Maryland
- University of Ottawa/NCR
- University of Sheffield
- Xerox Research Centre Europe

## Metadados

- **Arquivo Original:** G2000-2691 Voorhees The TREC-8 Question Answering Track Report.pdf
- **Data de Ingestão:** 2026-04-10