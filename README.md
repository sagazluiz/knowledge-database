# Knowledge Database - AI-Powered Wiki Generator

Um pipeline local de ingestão de documentos que transforma PDFs, PPTXs e DOCXs em uma **Wiki técnica estruturada**, alimentada por LLM local e RAG (Retrieval-Augmented Generation). Sem APIs externas. Sem custos. 100% privado.

**Filosofia:** Seguindo a abordagem ["Build in Public"](https://x.com/karpathy/status/2039805659525644595) de Andrej Karpathy — construindo conhecimento técnico de forma reproduzível e transparente.

---

## O Projeto

Este repositório contém um sistema **local-first** que:

- Ingeres documentos em múltiplos formatos (PDF, PPTX, DOCX)
- Extrai conhecimento usando `docling` + LLM local (`mistral-nemo`)
- Gera páginas Wiki em Markdown com estrutura de Wikilinks (`[[Entidade]]`)
- Armazena metadados num banco de dados local (DuckDB)
- Funciona offline — sem dependências externas
- Rastreável — cada página Wiki tem referência ao arquivo fonte (provenance)

### Case de Uso
Perfeito para:
- Engenheiros construindo **bases de conhecimento técnico** sobre arquiteturas, papers, blueprints
- Pesquisadores criando **hubs de referência** sobre um domínio específico
- Equipes que querem **governança de dados** com auditabilidade completa

---

## Quick Start

### 1. Pré-requisitos

- **Python 3.13+**
- **uv** (gerenciador de pacotes) — [Instale aqui](https://astral.sh/uv/install.sh)
- **Ollama** — [Instale aqui](https://ollama.com)
- **LibreOffice** (opcional, para converter PPTXs para PDF)

### 2. Setup Inicial

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/knowledge-database.git
cd knowledge-database

# Configure o ambiente Python
uv sync

# Baixe o modelo LLM
ollama pull mistral-nemo

# Inicie o Ollama (em outro terminal, rode em background)
ollama serve
```

### 3. Rode o Pipeline

```bash
# Coloque seus PDFs/DOCXs em sources/
ls sources/
# sources/seu-documento-1.pdf
# sources/seu-documento-2.pdf

# Execute o pipeline
./ingest.sh

# Confira os resultados
ls wiki/entities/
# Suas entidades em Markdown estarão aqui!
```

---

## Estrutura do Projeto

```
knowledge-database/
├── .knowledge-db/              # DuckDB (metadados + vetores)
│   └── metadata.db
│
├── wiki/                       # Base de conhecimento (Obsidian-ready)
│   ├── index.md               # Mapa mental do conhecimento
│   ├── log.md                 # Registro cronológico de ingestas
│   └── entities/              # Páginas geradas (Arquiteturas, Embeddings, RAG, etc)
│
├── sources/                    # Buffer de entrada (PDFs, DOCXs)
│   └── GTC_NVIDIA/            # Exemplo: conferência técnica
│
├── src/                        # Código-fonte
│   ├── __init__.py
│   ├── core/                  # Lógica do pipeline
│   ├── db/                    # Schemas DuckDB
│   └── utils/                 # Parsers e helpers
│
├── main.py                     # Script principal de ingestão
├── ingest.sh                   # Pipeline automático
├── pyproject.toml             # Dependências (uv)
├── AGENTS.md                  # Regras de governança do LLM
└── README.md                  # Este arquivo
```

### Saiba mais sobre cada pasta:

| Pasta | Função | Você Edita? |
|-------|--------|-------------|
| `.knowledge-db/` | Banco de dados local (DuckDB) | Raramente |
| `wiki/entities/` | Páginas Markdown geradas | Não (gerado pelo pipeline) |
| `sources/` | Seus documentos de entrada | ✅ Sim |
| `src/` | Código do pipeline | ✅ Sim (para customizar) |

---

## Como Funciona o Pipeline

```
[PDF/DOCX] 
    ↓
[Docling] → Normaliza para Markdown
    ↓
[DuckDB] → Armazena chunks + metadados
    ↓
[Ollama + Mistral-Nemo] → Extrai entidades + síntese
    ↓
[Wiki Generator] → Cria páginas com Wikilinks
    ↓
[/wiki/entities/*.md] ✅ Pronto para ler/versionar
```

### O que cada etapa faz:

1. **Ingestão** (`docling`)
   - Converte PDF/DOCX para Markdown estruturado
   - Preserva títulos, tabelas, links

2. **Armazenamento** (`DuckDB`)
   - Calcula hash SHA256 do arquivo (evita re-processar duplicatas)
   - Armazena chunks e metadados

3. **Extração de Conhecimento** (`Ollama + Mistral-Nemo`)
   - Resume cada documento
   - Identifica ENTIDADES (ex: `NVIDIA H100`, `Retrieval-Augmented Generation`)
   
4. **Geração de Wiki** 
   - Cria arquivo `.md` por entidade
   - Insere Wikilinks (`[[Entity Name]]`) para cross-referencing
   - Adiciona seção "Origem" com link para arquivo fonte

---

## Banco de Dados

O DuckDB armazena:

```sql
-- Rastreamento de arquivos
CREATE TABLE processed_files (
  hash TEXT PRIMARY KEY,        -- SHA256 do arquivo
  filename TEXT,                -- Nome original
  ingested_at TIMESTAMP         -- Data/hora da ingestão
);
```

Você **não precisa interagir diretamente** — o sistema gerencia automaticamente.

---

## Customização

### Trocar o Modelo LLM

Edit [main.py](main.py#L11):

```python
COMPLETION_MODEL = "ollama"  # Mude para outro modelo
# Opciones: "mistral", "neural-chat", "dolphin-mixtral", etc.
```

Depois baixe:
```bash
ollama pull seu-modelo
```

### Adicionar Campos Customizados

Edit `src/core/` para modificar o template de geração de páginas Wiki.

### Mudar Diretório de Saída

Edit [main.py](main.py#L15):
```python
WIKI_DIR = Path("/seu/caminho/customizado/wiki")
```

---

## Validação & QA

### Testar com um Único Documento

```bash
# Processa apenas um arquivo
uv run python main.py sources/seu-arquivo.pdf

# Confira o resultado
cat wiki/entities/seu-arquivo.md
```

### Limpar Cache (Reset Completo)

```bash
# Remove banco de dados e entidades
rm -rf .knowledge-db/metadata.db wiki/entities/*

# Próxima execução fará re-ingestão completa
./ingest.sh
```

### Performance (M1/M2/M3/M4)

- **Ingestão**: ~10-30s por documento (depende do tamanho)
- **Memória**: ~1-2 GB (pipeline local)
- **Disco**: ~100MB para base com 30 documentos

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| `ollama: command not found` | Instale Ollama: https://ollama.com |
| `ModuleNotFoundError: docling` | Execute `uv sync` |
| `Connection refused` (Ollama) | Certifique-se que `ollama serve` está rodando em outro terminal |
| `Warning: HF_TOKEN not set` | Opcional — veja [.env.example](.env.example) |
| Arquivo não processa | Confirme formato (PDF, DOCX, PPTX) e que não está corrompido |

---

## Navegação com Obsidian

A pasta `wiki/` está **pronta para usar como um Obsidian Vault**! As páginas geradas contêm **Wikilinks** (`[[Entity Name]]`) que permitem navegação visual e conexões entre conceitos.

### Abrir no Obsidian

1. **Instale Obsidian** → https://obsidian.md
2. **Abra como Vault**:
   - Abra Obsidian
   - Clique "Open folder as vault"
   - Selecione a pasta `/Users/fbda/knowledge-database/wiki`

3. **Explore o Grafo**:
   - Clique na aba **Graph view** (canto superior direito)
   - Veja as conexões entre entidades
   - Clique em um nó para navegar

### Recursos Disponíveis

| Recurso | Descrição |
|---------|-----------|
| Graph View | Visualiza todas as entidades e suas conexões |
| Local Graph | Vê conexões de uma página específica |
| Wikilinks | Navegação com `[[Entity]]` — clique para ir para página |
| Backlinks | Veja quais entidades linkam para a página atual |
| Search | Busca full-text em toda a Wiki |
| Quick Switcher | `Cmd+O` para pular entre páginas |

### Exemplo de Navegação

```
1. Abre wiki/entities/Retrieval-Augmented_Generation.md
2. Vê link [[Large Language Models]]
3. Clica → vai para essa página
4. Vê "Backlinks" mostrando todas as páginas que linkam aqui
5. Graph View mostra RAG conectado a LLMs, Embeddings, etc
```

### Customização Obsidian (Opcional)

Adicione um `.obsidian/` folder customizado (arquivo `vault.json`) para:
- Temas
- Configurações de plugins
- Aparência do grafo

**Dica:** Use plugins como:
- **Graph Analysis** — Destaca clusters de conhecimento
- **Tag Wrangler** — Organiza tags das entidades
- **Dataview** — Query as entidades via SQL-like syntax

---

## Próximas Evoluções

- [ ] API REST para consultas (FastAPI)
- [ ] Interface Web (Streamlit/Gradio)
- [ ] Suporte a embeddings customizados
- [ ] Cross-linking automático entre entidades
- [ ] Versionamento de mudanças na Wiki
- [ ] Export automático para Obsidian Vault
- [ ] Benchmarking contra outros sistemas RAG
- [ ] Visualização de relacionamentos em tempo real

---

## Licença

MIT — Use livremente para fins educacionais e comerciais.

---

## Contribuindo

Este é um projeto "Build in Public"! Contribuições, issues e PRs são bem-vindos.

```bash
# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/sua-feature
git commit -m "Add: Nova feature"
git push origin feature/sua-feature
```

---

## Contato & Créditos

- **Inspiração:** [Andrej Karpathy - Build in Public](https://x.com/karpathy/status/2039805659525644595)
- **Stack:** `docling` | `DuckDB` | `Ollama` | `Mistral-Nemo`

---

**Construído como exercício de Machine Learning em Produção**
