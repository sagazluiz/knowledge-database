# Contribuindo com o Knowledge Database

Obrigado por considerar contribuir! Este projeto é ["Build in Public"](https://x.com/karpathy/status/2039805659525644595) — contribuições são bem-vindas e apreciadas.

---

## Como Contribuir

### 1. Reportar Bugs

Se encontrou um bug:

1. **Verifique** se já não foi reportado em [Issues](issues)
2. **Descreva** o problema claramente:
   - O que você tentou fazer?
   - Qual foi o erro?
   - Qual sistema/versão Python?
3. **Inclua** exemplos ou logs se possível

**Template:**
```markdown
## Bug: [Título curto]

### Ambiente
- macOS/Linux/Windows: [seu SO]
- Python 3.x: [versão]
- Ollama: [versão]

### Passos para Reproduzir
1. Executei `[comando]`
2. Com arquivo `[nome]`
3. Resultado: [erro exato]

### Esperado
Deveria ter...

### Atual
Mas acontece...

### Logs
[Cole logs/erros]
```

---

### 2. Sugerir Melhorias

Quer uma nova feature? Abra uma **Discussion** ou **Issue** descrevendo:

- Qual é a necessidade?
- Como isso ajudaria?
- Há alternativas?

**Exemplos:**
- "Adicionar suporte a busca semântica (RAG Query)"
- "Interface Web com Streamlit"
- "Export para Obsidian"

---

### 3. Submeter Code (Pull Request)

#### Setup Inicial

```bash
# Fork o repositório no GitHub
# Clone sua fork
git clone https://github.com/seu-usuario/knowledge-database.git
cd knowledge-database

# Crie uma branch
git checkout -b feature/novo-recurso
# ou: git checkout -b fix/correcao-bug

# Configure o ambiente
uv sync
```

#### Desenvolvimento

1. **Código limpo**
   ```bash
   # Siga PEP 8
   # Use type hints quando possível
   def process_file(file_path: Path) -> str:
       """Processa arquivo e retorna Markdown."""
       ...
   ```

2. **Teste localmente**
   ```bash
   # Se modificar main.py:
   uv run python main.py sources/teste.pdf
   
   # Confira o output
   cat wiki/entities/resultado.md
   ```

3. **Commit semântico**
   ```bash
   git add .
   git commit -m "Add: Novo recurso de busca semântica"
   # ou: "Fix: Corrige hash duplicado em chunks"
   # ou: "Docs: Atualiza README com exemplos"
   ```

   **Prefixos recomendados:**
   - `Add:` — Nova feature
   - `Fix:` — Bugfix
   - `Docs:` — Documentação
   - `Refactor:` — Limpar código
   - `Test:` — Testes

4. **Push e PR**
   ```bash
   git push origin feature/novo-recurso
   ```
   Depois abra um PR no GitHub com descrição clara.

---

## Padrões de Código

### Python Style

```python
# Bom
def extract_entities(text: str, model: str = "mistral-nemo") -> list[str]:
    """
    Extrai entidades de um texto usando LLM.
    
    Args:
        text: Texto a processar
        model: Modelo Ollama a usar
        
    Returns:
        Lista de entidades encontradas
    """
    entities = []
    try:
        response = ollama.generate(prompt=text, model=model)
        entities = parse_entities(response)
    except Exception as e:
        logger.error(f"Erro na extração: {e}")
        return []
    
    return entities


# Evitar
def extract_entities(t, m="mistral-nemo"):
    try:
        r = ollama.generate(prompt=t, model=m)
        return parse_entities(r)
    except:
        return []
```

### Documentação (Docstrings)

```python
class KnowledgeEngine:
    """
    Orquestrador principal do pipeline de ingestão.
    
    Responsabilidades:
    - Detectar arquivos novos
    - Iniciar processamento
    - Gerenciar DuckDB
    
    Atributos:
        db (DuckDB): Conexão com banco de metadados
        converter (DocumentConverter): Parser do Docling
    """
    
    def __init__(self):
        """Inicializa o engine e configura diretórios."""
        pass
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)

# Use logging
logger.info("Iniciando ingestão de arquivo")
logger.warning("Arquivo pode estar corrompido")
logger.error("Falha na conexão com Ollama")

# Evite prints
print("Debug info")  # Não faça isso em código commits
```

---

## Testando Antes de Submeter

```bash
# 1. Verifique imports
uv run python -m py_compile src/core/*.py

# 2. Teste com um arquivo pequeno
uv run python main.py sources/test.pdf

# 3. Valide o output
ls -la wiki/entities/
head -20 wiki/entities/algo.md

# 4. Verifique se não quebrou nada
./ingest.sh  # Se não der erro, ótimo!
```

---

## Estrutura de PRs Esperada

```markdown
## Descrição
O que essa PR faz? Por que?

## Tipo de Mudança
- [ ] Bug fix (mudança que corrige um issue)
- [ ] Nova feature (adiciona funcionalidade)
- [ ] Breaking change (altera comportamento existente)
- [ ] Atualização de docs

## Como Testar?
Passos para validar sua mudança

## Checklist
- [ ] Meu código segue o style deste projeto
- [ ] Atualizei a documentação relevante
- [ ] Meus testes passam localmente
- [ ] Não adicionei warnings
```

---

## Onde Contribuir

### Bom para Iniciantes

- [ ] Melhorar documentação (README, ARCHITECTURE.md)
- [ ] Adicionar comentários explicativos
- [ ] Corrigir typos
- [ ] Adicionar exemplos

### Intermediário

- [ ] Adicionar testes unitários
- [ ] Melhorar tratamento de erros
- [ ] Otimizar performance
- [ ] Adicionar suporte a novos formatos

### Avançado

- [ ] RAG Query implementation
- [ ] API REST (FastAPI)
- [ ] Interface Web (Streamlit)
- [ ] Versionamento automático

---

## Discussões & Questions

Dúvidas? Abra uma **Discussion** em vez de Issue.

---

## Referências Úteis

- [PEP 8 — Python Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Docling Documentation](https://ds2-oss.github.io/docling/)

---

## Reconhecimento

Contribuidores serão creditados em:
- README.md (Seção "Contributors")
- Release notes

---

**Obrigado por contribuir!**

Construir em público é melhor juntos.
