### RAG: Arquitetura de Geração Aumentada por Recuperação e Integração com LLMs

Büşra Tural, Zeynep Örpek e Zeynep Destan
Centro de Pesquisa e Desenvolvimento, Vakif Participation Istanbul, Turquia

busra.tural@vakifkatilim.com.tr, zeynep.orpek@vakifkatilim.com.tr, zeynep.destan@vakifkatilim.com.tr

## Resumo Executivo

O avanço da Processamento de Linguagem Natural (PLN) levou ao surgimento de estruturas complexas como os grandes modelos de linguagem (LLMs). Os LLMs são altamente eficazes em entender as sutilezas da linguagem e processar contexto sendo treinados em grandes conjuntos de dados. No entanto, as dificuldades encontradas nos processos de Recuperação de Informação (RI) criaram uma conscientização de que esses modelos não são suficientes por si só. Os métodos tradicionais de RI geralmente foram insuficientes em entender a complexidade da linguagem natural na resposta a consultas específicas e recuperar informações apropriadas dos documentos ou bancos de dados. Como esse processo é baseado apenas em palavras-chave, não pode capturar completamente o significado semântico da linguagem. Por essa razão, foi necessário ir além dos métodos tradicionais de RI para criar informações mais precisas com base no contexto e no significado. Como resultado dessas necessidades, a arquitetura de Geração Aumentada por Recuperação (RAG) veio à tona. A RAG oferece a capacidade de criar respostas mais ricas e contextualizadas às consultas dos usuários integrando LLMs com sistemas de RI. Esta arquitetura permite que o modelo de linguagem acesse instantaneamente fontes de informações externas, gerando assim respostas mais precisas e contextuais apoiadas em informações existentes. Essas características da RAG proporcionam soluções apropriadas às demandas dos usuários por informações ao entender melhor a complexidade da linguagem natural. Neste estudo, enfatiza-se que a integração da arquitetura RAG com sistemas de RI e LLMs proporciona soluções mais sensíveis e precisas em tarefas intensivas em informações. Este estudo destaca que a capacidade da arquitetura RAG de informação por meio do uso dinâmico das fontes de dados obtidas dos grandes conjuntos de treinamento dos LLMs fortalece as aplicações de dados utilizados para o treinamento do modelo se tornam menos significativos com o tempo, levando a uma queda no desempenho do modelo. Como uma solução preliminar, foi proposto que os modelos fossem retreinados com novos dados. No entanto, retreinar os modelos com cada novo conjunto de dados não é viável.

## Componentes e Arquitetura Técnica

A arquitetura RAG é baseada na integração de modelos de geração de texto com sistemas de RI. Antes de responder a uma pergunta, esses sistemas recuperam documentos relevantes e usam essa informação para criar respostas. Isso proporciona uma grande vantagem, especialmente na prestação de informações precisas e atualizadas. A RAG é um sistema avançado com modelos como o T5 do Google e oferece processos de criação de informações mais eficientes.

## Glossário de Entidades

* Large Language Models (LLMs)
* Information Retrieval (IR)
* Natural Language Processing (NLP)
* Transformer-based models
* BERT (Bidirectional Encoder Representations from Transformers)
* GPT (Generative Pre-trained Transformer)
* Vector Space Model (-SM)
* Dense Retrieval Model (DRM)

## Metadados

* **Arquivo Original:** Sci-Net: Retrieval-Augmented Generation (RAG) and LLM Integration.pdf
* **Data de Ingestão:** 2026-04-10