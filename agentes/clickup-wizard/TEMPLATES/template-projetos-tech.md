# Template: Gestão de Projectos Tech / Desenvolvimento
**Sector:** Software, IT, Desenvolvimento, SaaS, Startups Tech

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — Produto & Tech
│
├── Folder: Development
│   ├── List: Sprint Activo
│   ├── List: Backlog (Priorizado)
│   └── List: Ice Box (Futuro)
│
├── Folder: Quality & Releases
│   ├── List: Bugs & Issues
│   ├── List: Em QA / Testing
│   └── List: Releases & Deploy
│
├── Folder: Produto & Roadmap
│   ├── List: Features em Análise
│   ├── List: Roadmap Trimestral
│   └── List: Pedidos de Clientes
│
├── Folder: Infra & DevOps
│   ├── List: Servidores & Cloud
│   ├── List: Incidentes
│   └── List: Manutenção Planeada
│
└── Folder: Arquivo
    └── List: Sprints Anteriores
```

---

## Custom Fields por List

### Development / Sprint / Backlog
| Campo | Tipo | Valores |
|-------|------|---------|
| Tipo | Dropdown | Feature, Bug, Melhoria, Tech Debt, Infra, Documentação |
| Story Points | Number | 1, 2, 3, 5, 8, 13, 21 |
| Sprint | Dropdown | Sprint 1, Sprint 2, Sprint 3... |
| Épico | Dropdown | [personalizar por produto] |
| Ambiente | Dropdown | Dev, Staging, Production |
| Repositório | URL | — |
| PR Link | URL | — |
| Testado | Checkbox | — |
| Deploy | Dropdown | Não feito, Staging, Production |

### Bugs & Issues
| Campo | Tipo | Valores |
|-------|------|---------|
| Severidade | Dropdown | Crítico, Alto, Médio, Baixo |
| Reportado por | Text | — |
| Versão afectada | Text | — |
| Ambiente | Dropdown | Dev, Staging, Production |
| Reproduzível | Checkbox | — |
| Root Cause | Text | — |

---

## Views por List

### Sprint Activo
- **Board (Kanban):** por status (To Do → In Progress → In Review → Done)
- **List:** por Story Points (maior → menor)
- **Calendar:** por data de conclusão

### Backlog
- **List:** ordenado por prioridade
- **Table:** com Story Points + Épico + Sprint
- **Board:** por Épico

### Bugs & Issues
- **Board:** por Severidade
- **List:** filtrada por Ambiente (Production first)
- **Table:** completa para triagem

---

## Tags do Sector
`frontend` | `backend` | `database` | `api` | `ui-ux` | `performance` | `security` | `mobile` | `hotfix` | `breaking-change` | `nice-to-have` | `client-request` | `tech-debt` | `blocked`

---

## Status Sugeridos (configurar manualmente)

### Development
`Backlog` → `Ready` → `In Progress` → `In Review` → `In QA` → `Done ✅` | `Blocked ⚠️` | `Cancelled ❌`

### Bugs
`Reportado` → `Triagem` → `Em Desenvolvimento` → `Em QA` → `Resolvido ✅` | `Não Reproduzível` | `Won't Fix`

### Incidentes (P1/P2/P3)
`Detectado` → `Em Análise` → `Em Resolução` → `Resolvido` → `Post-mortem`

---

## Tasks de Exemplo

### Sprint Activo
1. "Implementar autenticação OAuth2 — LinkedIn" (Alta, 8 pts, data: +5 dias)
2. "Optimizar query relatórios — reduzir para <500ms" (Normal, 5 pts, data: +7 dias)
3. "Dashboard KPIs — componente gráfico barras" (Normal, 3 pts, data: +10 dias)

### Bugs & Issues
1. "CRÍTICO: Login falha em Safari iOS 17" (Urgente, Production)
2. "Exportação PDF — caracteres especiais cortados" (Alta, Staging)
3. "Timeout API após 30s em ligações lentas" (Médio, Production)

### Roadmap Trimestral
1. "Módulo de Relatórios Avançados — Q1 2026" (Alta, 21 pts)
2. "Integração Zapier — Q2 2026" (Normal, 13 pts)
3. "App Mobile iOS/Android — Q3 2026" (Normal, 21 pts)

---

## Automations Recomendadas (configurar manualmente)
1. Quando Severidade = "Crítico": atribuir a Tech Lead + prioridade Urgent + notificar Slack
2. Quando status → "Done": mover Story Points para velocity report automaticamente
3. Fim de Sprint (data): criar retrospectiva task + mover "In Progress" para próximo sprint
4. Quando PR Link preenchido: mover para "In Review" automaticamente
5. Deploy para Production: criar task de smoke test automaticamente
