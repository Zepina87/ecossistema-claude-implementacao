# Template: Operações / Logística
**Sector:** Operações, Supply Chain, Logística, Serviços, Processos Internos

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — Operações
│
├── Folder: Processos Operacionais
│   ├── List: Tarefas do Dia
│   ├── List: Processos Recorrentes
│   └── List: Incidents & Problemas
│
├── Folder: Fornecedores & Compras
│   ├── List: Fornecedores Activos
│   ├── List: Encomendas em Curso
│   └── List: Avaliação de Fornecedores
│
├── Folder: Equipa & Recursos
│   ├── List: Turnos & Disponibilidade
│   ├── List: Formação & Certificações
│   └── List: Equipamentos & Manutenção
│
├── Folder: KPIs & Relatórios
│   ├── List: Indicadores Mensais
│   ├── List: Auditorias Internas
│   └── List: Plano de Melhoria
│
└── Folder: Arquivo
    └── List: Histórico Operacional
```

---

## Custom Fields por List

### Tarefas Operacionais
| Campo | Tipo | Valores |
|-------|------|---------|
| Departamento | Dropdown | Produção, Logística, Qualidade, Administrativo, Manutenção |
| Tipo | Dropdown | Recorrente, Pontual, Emergência, Melhoria |
| Impacto | Dropdown | Crítico, Alto, Médio, Baixo |
| Custo Estimado € | Currency | — |
| Fornecedor | Text | — |
| Concluído por | People | — |
| Verificado por | People | — |

### Encomendas
| Campo | Tipo | Valores |
|-------|------|---------|
| Fornecedor | Text | — |
| Valor € | Currency | — |
| Data de Encomenda | Date | — |
| Data Prevista Entrega | Date | — |
| Número de Referência | Text | — |
| Status Pagamento | Dropdown | Pendente, Pago, Em Disputa |
| Recebido | Checkbox | — |

---

## Views por List

### Tarefas do Dia
- **List:** ordenada por prioridade + data
- **Board:** por departamento
- **Calendar:** visão semanal

### Encomendas em Curso
- **Table:** todos os campos visíveis
- **Calendar:** por Data Prevista Entrega
- **Board:** por status (Encomendado → Em Trânsito → Recebido → Verificado)

---

## Tags do Sector
`urgente` | `recorrente` | `em-curso` | `aguarda-fornecedor` | `bloqueado` | `qualidade` | `manutenção` | `auditoria` | `melhoria` | `custo-extra`

---

## Status Sugeridos (configurar manualmente)

### Processos Operacionais
`A Fazer` → `Em Curso` → `Aguarda Aprovação` → `Concluído ✅` | `Cancelado ❌` | `Bloqueado ⚠️`

### Encomendas
`Solicitado` → `Aprovado` → `Encomendado` → `Em Trânsito` → `Recebido` → `Verificado ✅`

---

## Tasks de Exemplo

### Tarefas do Dia
1. "Verificar stock armazém Norte — Turno Manhã" (Urgente, recorrente diária)
2. "Manutenção preventiva — Empilhador #3" (Alta, data: +3 dias)
3. "Actualizar inventário após recepção Fornecedor XYZ" (Normal, data: hoje)

### Encomendas em Curso
1. "Encomenda material embalagem — Papel Pack Lda" (Alta, entrega: +7 dias)
2. "Reposição stock produto A — Distribuidora Norte" (Normal, entrega: +14 dias)
3. "Peças sobressalentes — Técnica Industrial" (Baixa, entrega: +30 dias)

---

## Automations Recomendadas (configurar manualmente)
1. Quando Data Prevista Entrega = hoje + status ≠ "Recebido": criar alerta automático
2. Quando status → "Bloqueado": notificar gestor operacional imediatamente
3. Processos Recorrentes: criar tasks automaticamente (diária/semanal/mensal)
4. Quando Impacto = "Crítico": mudar prioridade para "Urgent" automaticamente
