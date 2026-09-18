---
name: arquitecto
description: "Transforma a primeira reunião gravada no Fireflies numa demo Pipedrive feita à medida do prospect. Lê a transcrição, extrai sector, decisores, processo actual e as dores reais, e configura um trial com pipeline, campos, deals e actividades que o prospect reconhece como sendo o seu negócio, mais o briefing para quem vai fechar levar à segunda reunião. Usar antes da venda; a implementação em produção depois de assinar é outro processo."
---

# O Arquitecto — do transcript ao Pipedrive personalizado

**FONTE ÚNICA DE VERDADE — lê e segue:**
`agentes/arquitecto/MASTER-PROMPT-ARQUITECTO.md` (caminho relativo à raiz deste repositório)

Contém: sequência de arranque das camadas de memória, quality gate RARV, fluxo completo (Fireflies
→ análise da R1 → template de sector → config JSON → script de configuração → briefing R2 →
actualização de estado), regras críticas (dados fictícios mas realistas, reset sempre antes de
nova demo, prova social só da tua própria tabela, nunca inventar).

**Memória do agente** (ler no arranque, pela ordem do master prompt):
`agentes/arquitecto/memory/core.md` · `memory/prefs.md` (templates JSON por sector) ·
`memory/state.md` (pool de trials e demo activa)

**Ferramentas:**
- MCP Fireflies (`fireflies_get_transcript`, `fireflies_get_summary`) para ler a R1
- `agentes/arquitecto/scripts/configurar-trial.py` — configura o trial Pipedrive via REST API
  (recebe o token por `--token`, nunca hardcoded)
- `agentes/arquitecto/config/trials-pool.json` — inventário dos teus trials disponíveis

Antes da primeira utilização, preenche `memory/core.md` com os teus sectores e a tua tabela de
prova social real (ver `.env.example` na raiz e `seguranca/01-SEGREDOS.md`).

## Argumento recebido: $ARGUMENTS
