
# Projeto: Knowledge Database

## 1. Requisitos de Engenharia

### Funcionais (RF)

- **RF01 - Ingestão Multi-formato:** Suportar `.pptx`, `.pdf` e `.docx` via normalização para Markdown.
- **RF02 - Persistência Híbrida:** Armazenar metadados e vetores no DuckDB e a síntese em arquivos `.md` (Obsidian-ready).
- **RF03 - Identificação de Entidades:** O sistema deve extrair e vincular tecnologias (ex: "H100", "InfiniBand") entre diferentes arquivos.
- **RF04 - Interface de Consulta:** Permitir busca semântica (RAG) sobre a base consolidada.

### Não-Funcionais (RNF)

- **RNF01 - Privacidade (Local-First):** Todo processamento deve ser local (Mac M4 + Ollama) para garantir o sigilo dos dados da diretoria.
- **RNF02 - Rastreabilidade:** Cada insight na Wiki deve ter um link de volta para o arquivo fonte original (provenance).
- **RNF03 - Idempotência:** Re-processar o mesmo arquivo não deve duplicar entradas no banco ou na Wiki.

---

## 2. Arquitetura e Governança de Dados

A governança aqui foca em **Integridade** e **Auditabilidade**.

- **Versionamento de Conhecimento:** A pasta da Wiki deve ser um repositório Git. Isso permite auditar como a inteligência da POC evoluiu a cada novo slide inserido.

### Esquema de Dados (DuckDB)

| Tabela             | Descrição                                                    |
|--------------------|--------------------------------------------------------------|
| `raw_sources`      | Hash do arquivo, path original, data de ingestão.           |
| `knowledge_chunks` | Texto normalizado, metadados de página/slide.               |
| `vectors`          | Embeddings associados aos chunks (usando a extensão `vss`). |

---

## 3. Plano de Qualidade (QA)

Como medir se a LLM Wiki é "boa"?

- **Fidelidade da Extração — Teste de "Round-Trip":** Pegar um insight gerado e pedir para o sistema localizar o slide exato de onde ele veio.
- **Sanidade dos Links:** Um "Linter" automático que verifica se as entidades criadas na Wiki (`[[Re-ranking]]`) realmente possuem uma página correspondente ou se são links órfãos.
- **Benchmarking Local:** Monitorar o uso de memória e CPU no M4 durante a ingestão de apresentações grandes (ex: +50 slides) para garantir que o processo é sustentável.

---

## 4. Plano de Testes

| Caso de Teste         | Descrição                                              | Resultado Esperado                                                        |
|-----------------------|--------------------------------------------------------|---------------------------------------------------------------------------|
| **TC01 - Ingestão**   | Inserir um `.pptx` com tabelas e imagens.             | Conversão fiel para Markdown preservando a hierarquia de títulos.         |
| **TC02 - Cross-Link** | Inserir dois arquivos diferentes que citam "CUDA".    | A Wiki deve atualizar a página `CUDA.md` com insights de ambas as fontes. |
| **TC03 - RAG Query**  | Perguntar "Quais as datas de lançamento?"             | Resposta sintetizada com citações diretas aos arquivos fonte.             |
| **TC04 - Segurança**  | Tentar rodar o script sem conexão à internet.         | O sistema deve funcionar 100% offline.                                    |

---

## 5. Estrutura do Projeto

```
knowledge-database/
├── .knowledge-db/          # DuckDB database files (local-only)
├── wiki/                   # A "Wiki" viva (Arquivos .md)
│   ├── index.md            # Mapa de conteúdo e conceitos
│   ├── log.md              # Registro cronológico de ingestas
│   └── entities/           # Páginas sobre chips, arquiteturas, etc.
├── sources/                # Buffer para PPTX/PDFs de entrada
├── src/
│   ├── core/               # Lógica de extração e RAG
│   ├── db/                 # Schemas e queries DuckDB
│   └── utils/              # Parsers (Docling/MarkItDown)
├── AGENTS.md               # Governança e regras do agente LLM
├── pyproject.toml          # Dependências gerenciadas via uv
└── README.md               # Este documento
```


Rests

# Remova o banco e as entidades antigas
rm .knowledge-db/metadata.db
rm -rf wiki/entities/*

# Resete o índice para um estado neutro
echo "# 📚 Index de Conhecimento" > wiki/index.md