## ROUGE: Um Pacote para Avaliação Automática de Resumos

O ROUGE (Recall-Oriented Understudy for Gisting Evaluation) é um pacote desenvolvido para avaliar automaticamente a qualidade de resumos. Ele inclui várias medidas que comparam a semelhança entre os resumos, baseadas em estatísticas de coocorrência de n-gramas.

## Componentes e Arquitetura Técnica

O ROUGE consiste em quatro medidas principais:

1. **ROUGE-N:** Baseado em estatísticas de coocorrência de n-gramas, o ROUGE-N mede a semelhança entre um resumo candidato e um conjunto de resumos de referência.
2. **ROUGE-L:** Usa a subsequência comum mais longa (LCS) para avaliar a similaridade entre dois textos, levando em conta a ordem dos n-gramas.
3. **ROUGE-W:** Uma versão melhorada do ROUGE-L que considera a relação espacial entre os n-gramas na subsequência comum mais longa.
4. **ROUGE-S:** Usa o método de similaridade de sentença para comparar a semelhança entre dois textos, levando em conta a ordem dos n-gramas.

## Glossário de Entidades

* [[N-gram]]
* [[Subsequência Comum Mais Longa (LCS)]]
* [[Recall-Oriented Understudy for Gisting Evaluation (ROUGE)]]

## Metadados
- **Arquivo Original:** Lin.PDF - W04-1013 ROUGE A Package for Automatic Evaluation of Summaries.pdf
- **Data de Ingestão:** 2026-04-10