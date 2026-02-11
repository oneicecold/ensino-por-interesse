# Estrutura do Agente

Este projeto segue uma arquitetura de 3 camadas para separar responsabilidades e maximizar a confiabilidade.

## Arquitetura de 3 Camadas

**Camada 1: Diretiva (O que fazer)**
- Procedimentos Operacionais Padrão (SOPs) em Markdown na pasta `directives/`.
- Definem objetivos, entradas, ferramentas a usar e saídas esperadas.

**Camada 2: Orquestração (Tomada de Decisão)**
- O Agente (IA) lê as diretivas e orquestra a execução.
- Chama ferramentas de execução, lida com erros e atualiza diretivas.

**Camada 3: Execução (Como fazer)**
- Scripts Python determinísticos na pasta `execution/`.
- Realizam o trabalho pesado (chamadas de API, processamento de dados, etc.).
- Robustos, testáveis e rápidos.

## Organização de Arquivos

- `directives/`: SOPs (Instruções).
- `execution/`: Scripts Python (Ferramentas).
- `.tmp/`: Arquivos temporários e intermediários (não commitados).
- `.env`: Variáveis de ambiente (não commitado).

## Princípios Operacionais

1. **Verificar ferramentas primeiro**: Antes de pedir um novo script, verifique se já existe um em `execution/`.
2. **Auto-correção**: Se um script falhar, analise o erro, corrija e tente novamente.
3. **Atualizar diretivas**: Melhore as diretivas conforme aprende sobre limitações ou melhores práticas.
