# Arquitetura e Estrutura do Projeto

## Visão Geral

O Knowledge Database é um **pipeline de ingestão + geração de Wiki** estruturado em camadas:

```
┌─────────────────────────────────────────────────┐
│        INPUT LAYER (Documentos)                │
│  [PDF] [DOCX] [PPTX] → sources/               │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────┐
│     PROCESSING LAYER (Transformação)          │
│  • Docling (Parsing)                           │
│  • Text Normalization                          │
│  • Chunk Creation                              │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────┐
│    STORAGE LAYER (Persistência)                │
│  • DuckDB (Metadados + Vetores)                │
│  • Hash validation (Idempotência)              │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────┐
│   AI LAYER (Extração de Conhecimento)          │
│  • Ollama + Mistral-Nemo                       │
│  • Entity Extraction                           │
│  • Content Summarization                       │
└────────────────┬────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────┐
│       OUTPUT LAYER (Wiki)                      │
│  wiki/entities/*.md (Markdown + Wikilinks)     │
└─────────────────────────────────────────────────┘
```

---

## Estrutura de Diretórios Detalhada

### `sources/` — Buffer de Entrada

Documentos originais (PDF, DOCX, PPTX) que serão processados.

```
sources/
├── GTC_NVIDIA/
│   ├── Agentic_AI_Security_Blueprint.pdf
│   ├── Architecting_Agentic_Systems.pdf
│   ├── Architecting_the_Intelligence_Age.pdf
│   ├── Enterprise_AI_Blueprint.pdf
│   ├── Neural_AI_Industrialization.pdf
│   ├── OCI_Zettascale_AI_Infrastructure.pdf
│   ├── The_AI_Blueprint.pdf
│   ├── The_Industrial_AI_Blueprint.pdf
│   └── The_Innovation_Prism.pdf
└── (adicione seus próprios documentos aqui)
```

**Bom para:**
- Organizar documentos por origem (ex: `GTC_NVIDIA/`, `Artigos_Técnicos/`, etc)
- Manter histórico de fontes

**Nota:** Arquivos `.pdf` não precisam ser commitados (use `.gitignore`). PDFs são grandes!

---

### `.knowledge-db/` — Banco de Dados Local

Armazena **metadados** e **vetores** em DuckDB (um arquivo único, sem servidor).

```
.knowledge-db/
└── metadata.db
    ├── TABLE: processed_files
    │   ├── hash (PK): SHA256 do arquivo
    │   ├── filename: Nome original
    │   └── ingested_at: Timestamp
    │
    └── (futuro: vectors, embeddings, chunks)
```

**Características:**
- Funciona offline
- Sem credenciais
- Arquivo único (`metadata.db`)
- Não commit no Git (adicione ao `.gitignore`)

**Para visualizar dados:**
```bash
# Abra o terminal DuckDB (interativo)
uv run duckdb .knowledge-db/metadata.db

# Dentro do DuckDB:
SELECT * FROM processed_files;
```

---

### `wiki/` — Base de Conhecimento

Contém as **páginas Markdown geradas** pelo pipeline.

#### `wiki/index.md`
**Mapa mental** do conhecimento — sumário das entidades principais.

```
# Índice de Conhecimento

## Domínios Técnicos
- [[RAG (Retrieval-Augmented Generation)]]
- [[LLMs (Large Language Models)]]
- [[Embeddings]]

## Arquiteturas
- [[NVIDIA H100]]
- [[Oracle Cloud Infrastructure]]

## Metodologias
- [[Evaluation Metrics]]
- [[Benchmarking]]
```

#### `wiki/log.md`

```markdown
# Log de Ingestas

## 2025-04-20
- Processado: `Architecting_Agentic_Systems.pdf` (12 entidades criadas)
- Processado: `RAG_Survey.pdf` (8 entidades, 5 atualizadas)

## 2025-04-19
- Processado: `BERT_Reranking.pdf` (3 entidades)
```

#### `wiki/entities/`
**Páginas geradas automaticamente** — uma por entidade.

```
wiki/entities/
├── Retrieval-Augmented_Generation.md
├── NVIDIA_H100.md
├── Mistral_Nemo.md
├── DuckDB.md
├── Ollama.md
└── (32+ outras entidades do seu dataset)
```

**Exemplo de página gerada:**

```yaml
---
title: "Retrieval-Augmented Generation"
aliases: ["RAG", "Augmented Generation"]
tags: ["nlp", "llm", "rag"]
origem: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf"
---

# Retrieval-Augmented Generation

## Resumo
RAG é uma técnica que combina [[Large Language Models|LLMs]] com 
sistemas de recuperação de informação para melhorar a qualidade 
das respostas geradas.

## Componentes Principais
1. **Retriever** — Busca documentos relevantes
2. **Generator** — LLM que sintetiza a resposta
3. **Index** — Base vetorial de conhecimento

## Aplicações
- [[Question Answering Systems]]
- [[Chatbots Corporativos]]
- [[Knowledge Management]]

## Origem
Documento original: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf](../../sources/...)

## Ver Também
- [[Embeddings]]
- [[Vector Databases]]
```

**Características das páginas:**

| Campo | Exemplo | Propósito |
|-------|---------|----------|
| YAML Frontmatter | `title`, `tags`, `aliases` | Metadados (Obsidian/Zettelkasten) |
| Wikilinks | `[[Entity Name]]` | Cross-referencing automático |
| Seção "Origem" | Link para PDF | Rastreabilidade (provenance) |
| Seções | `## Resumo`, `## Componentes` | Estrutura padronizada |

---

### `src/` — Código-Fonte

Organizado em **módulos temáticos**:

```
src/
├── __init__.py
│
├── core/
│   ├── __init__.py
│   ├── knowledge_engine.py      # 🎯 ORquestrador principal
│   ├── document_processor.py    # 📄 Processa PDF/DOCX/PPTX
│   └── wiki_generator.py        # 📖 Gera Markdown pages
│
├── db/
│   ├── __init__.py
│   ├── schemas.py               # 🗄️ Schemas DuckDB
│   └── queries.py               # 🔍 Helper queries
│
└── utils/
    ├── __init__.py
    ├── parsers.py               # 🔄 Docling + MarkItDown
    ├── hash.py                  # 🔐 SHA256 checksum
    └── wikilinks.py             # [[Link]] processor
```

**Fluxo do código (`main.py`):**

```python
# 1. Instancia o motor de conhecimento
engine = KnowledgeEngine()

# 2. Processa cada arquivo
for file in sources:
    engine.process_single_file(file)
    # Internamente:
    # - hash(file) → Evita re-processar
    # - docling.convert() → Markdown
    # - ollama.generate() → Extrai entidades
    # - wiki_generator.create_pages() → Cria .md
```

---

## Idempotência (Evitar Duplicatas)

O sistema usa **hash SHA256** para garantir que o mesmo arquivo não seja processado 2x:

```python
def process_single_file(self, file_path):
    f_hash = self.get_hash(file_path)  # SHA256
    
    # Verifica se já foi processado
    existing = self.db.execute(
        "SELECT * FROM processed_files WHERE hash = ?", [f_hash]
    ).fetchall()
    
    if existing:
        print(f"⏭️  Arquivo já processado, pulando...")
        return
    
    # Se novo, processa
    self.db.execute(
        "INSERT INTO processed_files VALUES (?, ?, NOW())",
        [f_hash, file_path.name]
    )
```

**Benefício:** Re-executar `./ingest.sh` é seguro — não cria duplicatas! ✅

---

## Variáveis de Ambiente

Crie um arquivo `.env` (não commitar):

```bash
# .env
HF_TOKEN=hf_xxxxxxxxxxxxx          # Hugging Face (opcional)
OLLAMA_MODEL=mistral-nemo          # Modelo LLM
OLLAMA_HOST=http://localhost:11434 # Endpoint Ollama
```

Carregue em `main.py`:

```python
from dotenv import load_dotenv
load_dotenv()  # Carrega .env
```

---

## Fluxo de Processamento (Detalhado)

```
main.py --execute--> ingest.sh
                        │
         find sources/ -name "*.pdf"
                        │
        for file in lista_de_arquivos:
                        │
                 KnowledgeEngine()
                    │    │    │
                    ├─ Calcula SHA256
                    ├─ Verifica se já processou (DuckDB)
                    └─ Se novo:
                            │
                     DocumentProcessor
                            │
                 Docling (PDF → Markdown)
                            │
               Chunk Creation (1000 tokens)
                            │
                     DuckDB Insert
                            │
                    Ollama LLM Call
                            │
              Entity Extraction + Summarization
                            │
                     WikiLinkGen
                            │
            Cria/Atualiza wiki/entities/*.md
                            │
                     Pronto!
```

---

## Próximas Camadas Planejadas

### Camada de RAG (Busca Semântica)
```
Query: "Quais são os chips de IA mais rápidos?"
          ↓
    Cria embedding → Busca no DuckDB
          ↓
    Retorna chunks relevantes
          ↓
    LLM sintetiza resposta com contexto
          ↓
    Resposta com citações
```

### Camada de API
```
POST /query
{
  "question": "Explicar RAG",
  "context": "wiki/entities/",
  "model": "mistral-nemo"
}
```

### Camada Web
Interface Streamlit/Gradio para explorar wiki sem terminal.

---

## Padrões de Código

### Logging

```python
import logging

logger = logging.getLogger(__name__)

logger.info("ℹ️ Processando arquivo...")
logger.warning("⚠️ Duplicado detectado")
logger.error("❌ Erro ao processar")
```

### Tratamento de Erros

```python
try:
    result = ollama.generate(...)
except Exception as e:
    logger.error(f"Falha no LLM: {e}")
    # Continuar com fallback
```

---

## Referências Rápidas

| Arquivo | Função |
|---------|--------|
| `main.py` | Entry point — processa um arquivo |
| `ingest.sh` | Loop de processamento — todos os arquivos |
| `.knowledge-db/metadata.db` | Base de dados persistente |
| `wiki/entities/` | Output final (Markdown) |
| `AGENTS.md` | Regras do agente LLM |
| `pyproject.toml` | Dependências |

---

**Última atualização:** 2025-04-20  
**Versão:** 0.1.0 MVP
