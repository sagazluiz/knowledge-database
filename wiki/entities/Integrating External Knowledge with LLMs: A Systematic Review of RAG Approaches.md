# Integrando Conhecimento Externo com LLMs: Uma Revisão Sistemática dos Aproximações RAG

Ivan Mikulić, Marin Vlačić, Goran Delać, Marin Šilić, Klemo Vladimir
Universidade de Zagreb, Faculdade de Engenharia Elétrica e Computação, Zagreb, Croácia {ivan.mikulic2, marin.vlaic, goran.delac, marin.silic, klemo.vladimir}@fer.hr

## Resumo Executivo

Modelos de linguagem grandes (LLMs) têm demonstrado capacidades notáveis em compreensão e geração de linguagem natural, exibindo habilidades excepcionais de aprendizado em contexto sem a necessidade de ajustamento extensivo. No entanto, esses modelos frequentemente sofrem com limitações significativas, incluindo alucinações onde informações fabricadas ou incorretas são apresentadas como fatos, e a necessidade constante de retreinamento para integrar novo conhecimento. A aproximação de geração auxiliada por recuperação (RAG) emergiu como uma promessa atraente para endereçar esses desafios ao combinar LLMs com técnicas de recuperação de informações (IR). Ao explorar bancos de conhecimentos externos, os pipelines RAG recuperam e incorporam informações relevantes dinamicamente, aprimorando a precisão factual e adaptabilidade dos LLMs. Este artigo fornece uma visão geral dos métodos mais avançados para implementar RAG em LLMs, examinando os componentes-chave do pipeline RAG, incluindo preparação de dados, recuperação, reranking e técnicas pós-recuperação. Nosso objetivo é destacar como esses componentes coletivamente permitem que LLMs alcancem maior confiabilidade e flexibilidade, pavimentando o caminho para aplicações de IA mais robustas.

Palavras-chave: RAG, Recuperação, IR, LLM

## Componentes e Arquitetura Técnica

### II. PREPARAÇÃO DE DADOS

O primeiro passo em um pipeline RAG é preparar a coleção de conhecimentos para recuperação. Uma vez que os LLMs têm uma janela de contexto limitada, e pesquisas indicam que conteúdos irrelevantes dentro dessa janela degradam o desempenho em tarefas subsequentes [13], documentos devem ser divididos em menores pedaços estruturados - um processo conhecido como chunking.

Uma abordagem básica envolve dividir texto em chunks de tamanho fixo de caracteres. Um método mais eficaz é o chunking recursivo, que respeita a estrutura do documento ao iterar através de separadores de prioridade (por exemplo, seções, parágrafos, sentenças) até que todos os chunks caibam dentro do tamanho alvo.

Além do chunking estrutural, o chunking semântico usa embeddings e similaridade para detectar mudanças de conteúdo. Singh et al. [14] empregam embeddings densos e similaridade de produto escalar para identificar as melhores bordas de chunk. No entanto, Qu et al. [15] argumentam que o chunking semântico é benéfico apenas quando os dados exibem transições temáticas nítidas.

Estratégias alternativas incluem chunking baseado em proposições, onde Chen et al. [16] ajustam um modelo T5 para extrair fatos atômicos e auto-contidos. O chunking assistido por LLM, como proposto por Duarte et al. [17], precede IDs de sentença e promove um LLM para identificar mudanças de contexto, enquanto DStar [18] aprimora isso ao classificar chunks com base na similaridade da consulta, preservando a relevância contextual durante a recuperação.

Para tabelas, convertê-las em JSON antes do chunking previne a perda estrutural. Imagens e gráficos podem ser processados com modelos de imagem para texto para gerar descrições textuais, assegurando que informações multimodais sejam preservadas.

### III. RECUPERAÇÃO

A recuperação é o componente mais crítico do pipeline RAG. Nessa etapa, a consulta do usuário deve ser combinada com documentos ou chunks contendo conteúdo relevante. No campo da recuperação de informações (IR), isso é conhecido como pergunta e resposta em domínio aberto (ODQA) [19], e muitos avanços de pesquisa na ODQA podem ser aplicados diretamente aos pipelines RAG.

### A. Estratégias de Recuperação

Várias estratégias de recuperação podem ser empregadas para identificar e recuperar documentos relevantes a uma consulta dada. Esta seção fornece uma visão geral ampla das estratégias de recuperação mais amplamente utilizadas no RAG.

1. Recuperação esparsa: Métodos de recuperação esparsa, como TF-IDF e BM25 [20], são técnicas tradicionais que representam documentos como vetores esparsos em um espaço de alta dimensionalidade, com cada dimensão correspondendo a um termo no vocabulário. Esses métodos são altamente eficazes para corresponder termos exatos, sendo adequados para cenários onde o sobreposição de palavras-chave é crucial. No entanto, eles enfrentam limitações como o problema de