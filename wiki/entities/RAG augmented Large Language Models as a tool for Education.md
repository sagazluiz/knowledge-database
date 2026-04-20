# RAG Augmented Large Language Models as a Tool for Education

## Resumo Executivo

Este documento explora o uso do Retrieval-Augmented Generation (RAG) como uma ferramenta para aprimorar os grandes modelos de linguagem (LLMs) no contexto educacional. O RAG é uma abordagem híbrida que combina sistemas de recuperação de informações com modelos gerativos, permitindo que os LLMs tenham acesso a informações atualizadas e relevantes não presentes em seu treinamento original.

## Componentes e Arquitetura Técnica

### A. Bases de Dados Vetoriais

As bases de dados vetoriais são essenciais para o funcionamento do RAG, pois armazenam e recuperam documentos ou trechos de texto como vetores de alta dimensionalidade. Algumas das principais opções de bases de dados vetoriais incluem PgVector, WeaviateCloud, QdrantCloud, ZillizCloud, ElasticCloud, Milvus e Pinecone.

Um estudo comparativo [18] avaliou o desempenho dessas bases de dados em diferentes critérios, como taxa de consultas por segundo (QPS), taxa de acerto, latência, duração do carregamento e contagem de carga máxima. Os resultados indicaram que Milvus apresentou o maior QPS e a maior contagem de carga, enquanto ZillizCloud teve a menor latência. Pinecone mostrou um bom desempenho geral, exceto pela taxa de acerto. WeaviateCloud e QdrantCloud demonstraram sólido desempenho em vários critérios.

Outro estudo [19] comparou cinco bases de dados vetoriais (Qdrant, Milvus, Weaviate, ElasticSearch e Redis) usando diferentes conjuntos de dados e o algoritmo Approximate Nearest Neighbor (ANN). Qdrant apresentou o melhor desempenho geral em termos de RPS e latência em quase todas as situações de teste.

## Glossário de Entidades

- **RAG (Retrieval-Augmented Generation):** Uma abordagem híbrida que combina sistemas de recuperação de informações com modelos gerativos.
- **LLMs (Large Language Models):** Modelos de linguagem treinados em grandes quantidades de dados, capazes de gerar texto coerente e contextualizado.
- **ANN (Approximate Nearest Neighbor):** Um algoritmo utilizado para encontrar pontos de dados próximos ao ponto de dado de consulta.

## Metadados

- **Arquivo Original:** RAG augmented Large Language Models as a tool for Education.pdf
- **Data de Ingestão:** 2026-04-10