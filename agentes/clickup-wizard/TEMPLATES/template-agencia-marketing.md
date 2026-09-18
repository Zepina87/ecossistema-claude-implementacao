# Template: Agência Criativa / Marketing
**Sector:** Agências, Marketing, Comunicação, Design, PR

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — Projectos & Clientes
│
├── Folder: Projectos Activos
│   ├── List: Em Produção
│   ├── List: Em Revisão / Aprovação
│   └── List: Entregues este Mês
│
├── Folder: Clientes
│   ├── List: Clientes Retainer (mensais)
│   ├── List: Clientes Pontual
│   └── List: Leads & Propostas
│
├── Folder: Conteúdo & Campanhas
│   ├── List: Calendário Editorial
│   ├── List: Campanhas Pagas (Ads)
│   └── List: Relatórios & Métricas
│
├── Folder: Equipa Interna
│   ├── List: Capacidade da Equipa
│   ├── List: Reuniões & Briefings
│   └── List: Formação & Recursos
│
└── Folder: Arquivo
    └── List: Projectos Concluídos
```

---

## Custom Fields por List

### Projectos (todas as lists de projecto)
| Campo | Tipo | Valores |
|-------|------|---------|
| Cliente | Text | — |
| Tipo de Projecto | Dropdown | Website, Campanha, Redes Sociais, Branding, Vídeo, Copywriting, SEO, Outro |
| Valor do Projecto € | Currency | — |
| Data de Entrega | Date | — |
| Fase | Dropdown | Briefing → Proposta → Produção → Revisão → Aprovação → Entregue |
| Horas Estimadas | Number | — |
| Horas Reais | Number | — |
| Designer Responsável | People | — |
| Aprovação Cliente | Checkbox | — |

### Calendário Editorial
| Campo | Tipo | Valores |
|-------|------|---------|
| Canal | Dropdown | Instagram, LinkedIn, Facebook, TikTok, Email, Blog, Google Ads |
| Formato | Dropdown | Post, Story, Reel, Artigo, Newsletter, Vídeo |
| Cliente | Text | — |
| Data de Publicação | Date | — |
| Copy aprovado | Checkbox | — |
| Visual aprovado | Checkbox | — |

---

## Views por List

### Em Produção
- **Board (Kanban):** por fase (Briefing → Produção → Revisão → Entregue)
- **Calendar:** por Data de Entrega
- **Table:** com horas estimadas vs reais

### Calendário Editorial
- **Calendar:** visão mensal de publicações
- **Board:** por canal
- **List:** filtrada por cliente

---

## Tags do Sector
`urgente` | `aguarda-aprovação` | `revisão` | `entregue` | `retainer` | `pontual` | `redes-sociais` | `paid-media` | `branding` | `website` | `atrasado` | `em-pausa`

---

## Status Sugeridos (configurar manualmente)

### Projectos
`Briefing` → `Proposta` → `Em Produção` → `Em Revisão` → `Aguarda Aprovação` → `Entregue ✅` | `Cancelado ❌`

### Editorial
`Ideia` → `A Criar` → `Em Revisão` → `Aprovado` → `Publicado ✅`

---

## Tasks de Exemplo

### Em Produção
1. "Website Clínica Dr. Silva — Desenvolvimento" (Urgente, data: +5 dias)
2. "Campanha Redes Sociais — Abril — Café Lisboa" (Alta, data: +7 dias)
3. "Branding — Nova Identidade — StartupX" (Normal, data: +14 dias)

### Calendário Editorial
1. "Post Instagram — Promoção Primavera — Cliente ABC" (data: +2 dias)
2. "Newsletter Abril — Clínica Dental" (data: +5 dias)
3. "Reel LinkedIn — Case Study — Empresa XYZ" (data: +8 dias)

---

## Automations Recomendadas (configurar manualmente)
1. Quando status → "Aguarda Aprovação": notificar account manager + enviar email ao cliente
2. Quando Data de Entrega = amanhã + status ≠ "Entregue": notificar equipa (urgente)
3. Quando "Copy aprovado" + "Visual aprovado" = true: mover para "Aprovado" automaticamente
4. Quando Horas Reais > Horas Estimadas: notificar gestor de projecto
