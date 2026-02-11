from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import subprocess
import json
import os
import sys

app = FastAPI()

# Modelo de dados para a requisição
class LessonRequest(BaseModel):
    topic: str
    interest: str

# Endpoint da API
@app.post("/api/generate")
async def generate_lesson_endpoint(request: LessonRequest):
    try:
        # Chama o script de execução (Camada 3)
        # Isso mantém a arquitetura: Server (Orquestração) chama Script (Execução)
        script_path = os.path.join("execution", "ibl_generator.py")
        
        # Executa o script Python como um sub-processo
        result = subprocess.run(
            [sys.executable, script_path, request.topic, request.interest],
            capture_output=True,
            text=True,
            encoding='utf-8' # Forçar UTF-8 para evitar erros de acentuação
        )
        
        if result.returncode != 0:
            raise Exception(f"Erro no script: {result.stderr}")
            
        return json.loads(result.stdout)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Monta a pasta 'web' na raiz '/'
app.mount("/", StaticFiles(directory="web", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    print("Iniciando servidor IBL em http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
