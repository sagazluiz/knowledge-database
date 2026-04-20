import sys
import hashlib
import logging
import duckdb
import re
from pathlib import Path
from datetime import datetime
from docling.document_converter import DocumentConverter
import ollama

# --- CONFIGURAÇÕES ---
# Voltamos ao Nemo para estabilidade e velocidade no M4
COMPLETION_MODEL = "mistral-nemo" 
BASE_DIR = Path(__file__).parent
WIKI_DIR = BASE_DIR / "wiki"
DB_DIR = BASE_DIR / ".knowledge-db"

class KnowledgeEngine:
    def __init__(self):
        # Garante que as pastas existam
        WIKI_DIR.mkdir(parents=True, exist_ok=True)
        (WIKI_DIR / "entities").mkdir(parents=True, exist_ok=True)
        DB_DIR.mkdir(parents=True, exist_ok=True)
        
        self.db = duckdb.connect(str(DB_DIR / "metadata.db"))
        self.converter = DocumentConverter()
        self._bootstrap_db()

    def _bootstrap_db(self):
        self.db.execute("CREATE TABLE IF NOT EXISTS processed_files (hash TEXT PRIMARY KEY, filename TEXT, ingested_at TIMESTAMP)")

    def get_hash(self, path):
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192): hasher.update(chunk)
        return hasher.hexdigest()

    def process_single_file(self, file_path):
        f_hash = self.get_hash(file_path)
        
        # GATEKEEPER: Verifica se já existe
        exists = self.db.execute("SELECT 1 FROM processed_files WHERE hash = ?", [f_hash]).fetchone()
        if exists:
            print(f"⏭️  Ignorado (Hash já processado): {file_path.name}")
            return

        print(f"🚀 Iniciando: {file_path.name}")
        
        # Conversão de PPTX para Markdown
        result = self.converter.convert(file_path)
        raw_md = result.document.export_to_markdown()

        # LLM Synthesis com Feedback Visual (Streaming)
        client = ollama.Client(timeout=300.0) # 5 minutos é mais que suficiente para o Nemo
        rules = (BASE_DIR / "AGENTS.md").read_text()
        
        prompt = f"### ARQUIVO: {file_path.name}\n<CONTENT>\n{raw_md[:15000]}\n</CONTENT>\n\nRegras: {rules}"
        
        print(f"🧠 {COMPLETION_MODEL} sintetizando: ", end="", flush=True)
        
        try:
            response_stream = client.chat(
                model=COMPLETION_MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={
                    "temperature": 0.1, 
                    "num_ctx": 8192,  # Reduzido para evitar pressão excessiva na VRAM
                    "num_thread": 8    # Foco nos cores de performance do M4
                },
                stream=True
            )
            
            wiki_output = ""
            for chunk in response_stream:
                content = chunk['message']['content']
                wiki_output += content
                # Imprime um ponto para cada pedaço gerado
                print("·", end="", flush=True)
            
            print(" ✅")

        except Exception as e:
            print(f"\n❌ Erro na LLM: {e}")
            return
        
        # Salvamento determinístico para evitar colisões
        safe_output_name = file_path.stem  
        output_path = WIKI_DIR / "entities" / f"{safe_output_name}.md"

        output_path.write_text(wiki_output)

        # COMMIT: Só salva no banco se chegar aqui
        self.db.execute("INSERT INTO processed_files VALUES (?, ?, ?)", [f_hash, file_path.name, datetime.now()])
        print(f"✨ Salvo em: {output_path.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro: Forneça o caminho do arquivo.")
        sys.exit(1)
    
    engine = KnowledgeEngine()
    engine.process_single_file(Path(sys.argv[1]))