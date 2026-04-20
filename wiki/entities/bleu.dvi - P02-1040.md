# BLEU : um Método para Avaliação Automática de Tradução de Máquina

## Resumo Executivo

A avaliação humana de tradução de máquina é extensa, mas cara. Ela pode levar meses para ser concluída e envolve trabalho humano que não pode ser reutilizado. Propondo um método de avaliação automática de tradução de máquina que é rápido, barato e independente de linguagem, que correlaciona altamente com a avaliação humana e tem pouco custo marginal por execução. Apresentamos esse método como uma subestuda automatizada para juízes humanos qualificados, que substitui-os quando há necessidade de avaliações rápidas ou frequentes.

## Componentes e Arquitetura Técnica

O BLEU (Bilingual Evaluation Understudy) é um método de avaliação automática de tradução de máquina que se baseia em uma métrica de 'proximidade de tradução' modificada, inspirada no índice de erro de palavras usado pela comunidade de reconhecimento de fala. A métrica BLEU compara n-gramas do texto traduzido com os n-gramas das traduções de referência e conta o número de correspondências. Quanto mais correspondências, melhor a tradução.

A principal tarefa para um implementador do BLEU é comparar os n-gramas do texto traduzido com os n-gramas da tradução de referência e contar o número de correspondências. Essas correspondências são independentes de posição. A métrica BLEU também considera a exaustão das palavras de referência após uma palavra correspondente ser identificada, garantindo que as traduções não sejam penalizadas por gerar excessivamente 'palavras razoáveis'.

## Glossário de Entidades

- **BLEU**: Bilingual Evaluation Understudy
- **MT**: Machine Translation (Tradução de Máquina)
- **n-gramas**: Sequências de n palavras em um texto.

## Metadados

- **Arquivo Original:** bleu.dvi - P02-1040.pdf
- **Data de Ingestão:** 2026-04-10