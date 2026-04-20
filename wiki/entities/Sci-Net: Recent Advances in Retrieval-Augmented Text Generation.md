### Recent Advances in Retrieval-Augmented Text Generation

#### Resumo Executivo

Este tutorial visa apresentar os avanços recentes na geração de texto auxiliada por recuperação de forma abrangente e comparativa. Primeiramente, destaca-se o paradigma genérico da geração de texto auxiliada por recuperação, em seguida revisam-se trabalhos notáveis para diferentes tarefas de geração de texto, incluindo a geração de diálogo, tradução de máquina e outras tarefas de geração. Por fim, apontam-se algumas limitações e falhas para facilitar futuras pesquisas.

#### Componentes e Arquitetura Técnica

O tutorial é organizado da seguinte forma:

- Introdução (15 minutos): Contexto da geração de texto, limitações dos modelos existentes e motivação do paradigma de geração de texto auxiliada por recuperação.
- Um novo paradigma: Geração de texto auxiliada por recuperação (20 minutos)
  - Fontes de recuperação: corpus de treinamento, conjuntos de dados externos e corpus não supervisionado.
  - Métricas de recuperação: recuperação vetorial esparsa, recuperação vetorial densa e recuperação específica da tarefa.
  - Integração: como combinar a recuperação e a geração.
- Geração de resposta em diálogo (40 minutos)
  - Contexto: sistemas de diálogo baseados em recuperação e geração.
  - Integração rasa: resultados de recuperação como entrada auxiliar.
  - Integração profunda: resultados de recuperação como esqueleto ou protótipo de resposta.
- Tradução de máquina (40 minutos)
  - Contexto: definições de memória de tradução em tradução estatística de máquina (SMT) e tradução de máquina neural (NMT).
  - Integração de memória de tradução na fase de inferência.
  - Integração de memória de tradução na fase de treinamento.
- Um breve intervalo (10 minutos)
- Geração exemplificada: Transferência de estilo, resumo e geração de paraphrase.
- Outras tarefas de geração (40 minutos)
  - Geração baseada em fatos: modelagem de linguagem e geração de dados para texto.
- Discussão sobre os principais problemas e conclusão (30 minutos)
  - Sensibilidade à recuperação: como tornar o desempenho da geração de texto auxiliada por recuperação menos sensível à qualidade da recuperação?
  - Eficiência de recuperação: como equilibrar a troca entre o tamanho da memória de recuperação e a eficiência de recuperação?
  - Multi-modais: é possível estender a memória de recuperação para outras modalidades?

#### Glossário de Entidades

- [[Text Generation]]
- [[Retrieval-Augmented Learning]]
- [[Dialogue Systems]]
- [[Machine Translation]]
- [[Knowledge Graphs]]

#### Metadados

- **Arquivo Original:** Sci-Net: Recent Advances in Retrieval-Augmented Text Generation.pdf
- **Data de Ingestão:** 2026-04-10