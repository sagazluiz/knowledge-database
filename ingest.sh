#!/bin/zsh

# Garante a existência da pasta de saída
mkdir -p wiki/entities

echo "🎬 Iniciando Pipeline Atômico..."

# Usamos o find para evitar o erro 'no matches found' do ZSH
# Ele busca de forma recursiva e ignora erros se uma extensão não existir
files=$(find ./sources -type f \( -name "*.pptx" -o -name "*.pdf" -o -name "*.docx" \))

if [[ -z "$files" ]]; then
    echo "⚠️  Nenhum arquivo encontrado na pasta ./sources"
    exit 0
fi

# Itera sobre a lista de arquivos encontrados
echo "$files" | while read -r file; do
    echo "------------------------------------------"
    # Chama o python de forma isolada para cada arquivo
    uv run python main.py "$file"
    
    # Pequena pausa para garantir que o Ollama liberou a sessão de chat
    sleep 1
done

echo "🏁 Ingestão concluída."