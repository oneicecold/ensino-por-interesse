import sys
import json
import random

def generate_lesson(topic, interest):
    """
    Gera uma aula baseada em IBL.
    Nota: Em produção, isso chamaria uma LLM (Gemini, GPT, etc).
    Aqui usamos templates para demonstrar a arquitetura.
    """
    
    titles = [
        f"Domine {topic} através do {interest}",
        f"O Segredo de {topic} escondido no {interest}",
        f"{topic}: Muito mais fácil quando pensamos em {interest}"
    ]
    
    # Simulação de "Inteligência"
    lesson = {
        "title": random.choice(titles),
        "content": f"""
## O Jogo Começa

Imagine que você está vivendo o auge do **{interest}**. É exatamente aí que **{topic}** entra em cena, mesmo que você não perceba.

### A Conexão

No mundo do {interest}, cada movimento tem uma razão. 
> "Pensar em {topic} é como planejar a jogada perfeita no {interest}."

Quando olhamos para **{topic}**, a regra é clara: interagir com os elementos. Assim como no {interest}, se você não domina os fundamentos, o jogo não flui.

### A Teoria na Prática

1. **Fundamento 1**: Observe como {topic} se comporta sob pressão.
2. **Fundamento 2**: A estratégia do {interest} se aplica aqui para resolver o problema.

### Desafio Rápido

Pense na última vez que viu algo incrível em {interest}. Consegue ver **{topic}** acontecendo ali?

*Essa aula foi gerada automaticamente pelo Agente IBL.*
        """
    }
    
    return lesson

def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Uso: python ibl_generator.py <topico> <interesse>"}))
        sys.exit(1)
        
    topic = sys.argv[1]
    interest = " ".join(sys.argv[2:]) # Pega o resto como interesse
    
    result = generate_lesson(topic, interest)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
