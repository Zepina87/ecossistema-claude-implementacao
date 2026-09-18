# Template: Vendas / CRM
**Sector:** Comercial, Vendas B2B/B2C, CRM interno

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — CRM & Vendas
│
├── Folder: Pipeline Comercial
│   ├── List: Prospecção Activa
│   ├── List: Propostas Enviadas
│   ├── List: Em Negociação
│   └── List: Fechados (Won/Lost)
│
├── Folder: Gestão de Clientes
│   ├── List: Clientes Activos
│   ├── List: Onboarding Clientes
│   └── List: Renovações & Upsell
│
├── Folder: Actividades Comerciais
│   ├── List: Reuniões & Chamadas
│   ├── List: Follow-ups Pendentes
│   └── List: Eventos & Feiras
│
└── Folder: Arquivo
    └── List: Histórico de Negócios
```

---

## Custom Fields por List

### Pipeline Comercial (todas as lists)
| Campo | Tipo | Valores |
|-------|------|---------|
| Valor Estimado € | Currency | — |
| Probabilidade % | Number | 0-100 |
| Data Fecho Estimada | Date | — |
| Fonte do Lead | Dropdown | LinkedIn, Referência, Website, Cold Call, Evento, Parceiro |
| Produto/Serviço | Dropdown | [personalizar por cliente] |
| Empresa | Text | — |
| Decisor | Text | — |
| Contacto | Email | — |
| Telefone | Phone | — |

### Clientes Activos
| Campo | Tipo | Valores |
|-------|------|---------|
| Sector | Dropdown | [por mercado do cliente] |
| NIF | Text | — |
| Valor Contrato € | Currency | — |
| Data Início | Date | — |
| Data Renovação | Date | — |
| Plano/Produto | Dropdown | — |
| NPS Score | Number | 0-10 |
| Account Manager | People | — |

---

## Views por List

### Prospecção Activa
- **Board (Kanban):** por status (Novo → Contactado → Qualificado → Proposta)
- **List:** ordenada por prioridade
- **Calendar:** por Data de Follow-up

### Clientes Activos
- **Table:** visão completa com todos os campos
- **List:** filtrada por Account Manager
- **Calendar:** por Data de Renovação

---

## Tags do Sector
`hot-lead` | `cold-lead` | `follow-up` | `proposta-enviada` | `demo-agendada` | `decisor-contactado` | `upsell` | `renovação` | `inativo` | `parceiro`

---

## Status Sugeridos (configurar manualmente)

### Pipeline
`Novo Lead` → `Contactado` → `Qualificado` → `Proposta Enviada` → `Em Negociação` → `Ganho ✅` | `Perdido ❌`

### Clientes
`Onboarding` → `Activo` → `Em Risco` → `Pausado` → `Churned`

---

## Tasks de Exemplo (criar 3 por list principal)

### Prospecção Activa
1. "Contactar Empresa ABC Lda — Demo Pipedrive" (Urgente, data: +3 dias)
2. "Qualificar Lead — Construtora XYZ" (Alta, data: +7 dias)
3. "Enviar proposta — Clínica Dental Lisboa" (Normal, data: +10 dias)

### Clientes Activos
1. "Check-in mensal — Cliente Farmácias Portugal" (Normal, recorrente)
2. "Renovação contrato — Empresa BETA Lda" (Alta, data: +30 dias)
3. "Upsell módulo relatórios — TechStart PT" (Normal, data: +45 dias)

---

## Automations Recomendadas (configurar manualmente)
1. Quando status → "Ganho ✅": mover para "Clientes Activos" + notificar gestor
2. Quando Data de Renovação = hoje + 60 dias: criar task "Iniciar renovação"
3. Quando task sem update há 7 dias: notificar responsável
4. Quando Probabilidade > 70%: adicionar tag "hot-lead"
