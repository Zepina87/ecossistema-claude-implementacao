# Template: Arquitectura & Decoração de Interiores
**Sector:** Ateliers de Arquitectura, Decoração, Design de Interiores, Reabilitação

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — Projectos & Atelier
│
├── Folder: Projectos Arquitectura
│   ├── List: Novos Pedidos
│   ├── List: Em Desenvolvimento
│   ├── List: Em Aprovação / Licenciamento
│   └── List: Concluídos
│
├── Folder: Projectos Decoração & Interiores
│   ├── List: Em Briefing
│   ├── List: Em Produção (3D / Fornecimentos)
│   ├── List: Montagem & Instalação
│   └── List: Pós-venda & Acompanhamento
│
├── Folder: Comercial & Propostas
│   ├── List: Leads & Primeiros Contactos
│   ├── List: Orçamentos Enviados
│   └── List: Negociação
│
├── Folder: Fornecedores & Compras
│   ├── List: Encomendas em Curso
│   ├── List: Fornecedores Activos
│   └── List: Artigos & Catálogo
│
├── Folder: Equipa & Gestão
│   ├── List: Reuniões & Follow-ups
│   └── List: Tarefas Internas
│
└── Folder: Arquivo
    └── List: Projectos Entregues
```

---

## Custom Fields por List

### Projectos Arquitectura
| Campo | Tipo | Valores |
|-------|------|---------|
| Tipo de Projecto | Dropdown | Habitação, Comercial, Industrial, Reabilitação, Ampliação, Outro |
| Valor Honorários € | Currency | — |
| Fase | Dropdown | Honorários → Levantamento → Estudo Prévio → Projecto Execução → Licenciamento → Obra |
| Responsável Projecto | People | — |
| Cliente | Text | — |
| Área Intervenção m² | Number | — |
| Data Entrega Estimada | Date | — |
| Licenciamento Necessário | Checkbox | — |
| Câmara Municipal | Text | — |

### Projectos Decoração & Interiores
| Campo | Tipo | Valores |
|-------|------|---------|
| Tipo | Dropdown | Decoração Completa, FF&E, Consultoria, 3D Renders, Montagem |
| Orçamento Total € | Currency | — |
| Fase | Dropdown | Conceito → Apresentação → Aprovado → Encomendado → Montagem → Pós-venda |
| Fornecedor Principal | Text | — |
| Responsável 3D | People | — |
| Data Entrega | Date | — |
| Montagem Incluída | Checkbox | — |
| Aprovação Cliente | Checkbox | — |

### Comercial & Propostas
| Campo | Tipo | Valores |
|-------|------|---------|
| Tipo de Pedido | Dropdown | Arquitectura, Decoração, Misto, Consultoria |
| Valor Estimado € | Currency | — |
| Fonte do Contacto | Dropdown | Referência, Website, Redes Sociais, Evento, Outro |
| Probabilidade % | Number | — |
| Data Fecho Estimada | Date | — |
| Sector do Cliente | Dropdown | Habitação Privada, Empresa, Hotelaria, Comércio, Saúde, Outro |

### Encomendas em Curso
| Campo | Tipo | Valores |
|-------|------|---------|
| Fornecedor | Text | — |
| Valor € | Currency | — |
| Data de Encomenda | Date | — |
| Data Prevista Entrega | Date | — |
| Projecto Associado | Text | — |
| Status Pagamento | Dropdown | Pendente, Pago, Em Disputa |
| Recebido | Checkbox | — |

---

## Views por List

### Projectos Arquitectura — Em Desenvolvimento
- **Board (Kanban):** por Fase (Levantamento → Estudo Prévio → Projecto Execução)
- **Calendar:** por Data Entrega Estimada
- **Table:** com Valor Honorários + Área m² + Responsável

### Projectos Decoração — Em Produção
- **Board:** por Fase (Conceito → Encomendado → Montagem)
- **Calendar:** por Data Entrega
- **Table:** com Orçamento + Fornecedor + Responsável

### Comercial — Orçamentos Enviados
- **Board:** por probabilidade (Quente / Morno / Frio)
- **Table:** Valor Estimado + Data Fecho + Tipo de Pedido

---

## Tags do Sector
`urgente` | `licenciamento` | `3D-renders` | `orçamento-pendente` | `aguarda-cliente` | `obra-activa` | `importado` | `pós-venda` | `habitação` | `comercial` | `reabilitação` | `referência`

---

## Status Sugeridos (configurar manualmente)

### Projectos Arquitectura
`Lead` → `Proposta` → `Honorários` → `Levantamento` → `Estudo Prévio` → `Projecto Execução` → `Licenciamento` → `Concluído ✅` | `Em Pausa ⏸️` | `Cancelado ❌`

### Projectos Decoração
`Briefing` → `Proposta` → `Conceito Aprovado` → `Em Produção` → `Encomendado` → `Montagem` → `Pós-venda` → `Concluído ✅`

### Comercial
`Contacto Inicial` → `Reunião Marcada` → `Orçamento Enviado` → `Em Negociação` → `Ganho ✅` | `Perdido ❌`

---

## Tasks de Exemplo

### Em Desenvolvimento (Arquitectura)
1. "Moradia Unifamiliar — Família Costa — Projecto Execução" (Alta, data: +21 dias, Área: 180m²)
2. "Ampliação Clínica Dr. Rodrigues — Estudo Prévio" (Normal, data: +14 dias)
3. "Reabilitação Apartamento — Lisboa Chiado — Levantamento" (Urgente, data: +5 dias)
   - Subtask: "Visita ao local com medições"
   - Subtask: "Fotografias de estado actual"

### Em Produção (Decoração)
1. "Sala Principal — Vila Cascais — Conceito 3D" (Alta, data: +7 dias)
2. "Escritório Empresa ABC — FF&E Selecção" (Normal, data: +14 dias)
3. "Quarto Criança — Apartamento Porto — Montagem" (Urgente, data: +3 dias)

### Orçamentos Enviados
1. "Proposta Vivenda — Sintra — Decoração Completa" (Alta, Valor: €15.000)
2. "Proposta Restaurante — Baixa Lisboa — Interiores" (Normal, Valor: €28.000)
3. "Proposta T3 — Cascais — Consultoria" (Baixa, Valor: €3.500)

---

## Modelo de 6 Fases (Projectos Complexos)

```
PHASE 1 — DESIGN CONCEPT
  → Briefing cliente, referências, moodboard, conceito inicial

PHASE 2 — INTERIOR ARCHITECTURE DRAWINGS
  → Plantas, cortes, alçados, layouts definitivos

PHASE 3 — FF&E (Furniture, Fixtures & Equipment)
  → Selecção de mobiliário, materiais, acabamentos

PHASE 4 — QUOTATION
  → Orçamentos fornecedores, proposta final ao cliente

PHASE 5 — SUPPLY & DELIVERY
  → Encomendas, acompanhamento entregas, controlo qualidade

PHASE 6 — INSTALLATION & HANDOVER
  → Montagem, inspecção final, entrega ao cliente
```

---

## Automations Recomendadas (configurar manualmente)
1. Quando Fase → "Licenciamento": notificar responsável + criar subtask "Submeter processo câmara"
2. Quando Data Prevista Entrega encomenda < +3 dias: alerta equipa (controlo montagem)
3. Quando status → "Pós-venda": criar task de follow-up automático em 30 dias
4. Quando Aprovação Cliente = true: mover para fase seguinte automaticamente
5. Quando Probabilidade < 20% + 14 dias sem actividade: alertar gestor comercial

---

## Integração ClickUp ↔ Pipedrive
*(Upsell natural)*

- Pipeline comercial no Pipedrive → sincronizar com List "Orçamentos Enviados" no ClickUp
- Lead fechado no Pipedrive → criar projecto automaticamente no ClickUp
- Nota Pipedrive → visível como comentário na task ClickUp

*Nota de processo: a modelação parte tipicamente da estrutura já existente no Pipedrive do
cliente, quando existir.*
