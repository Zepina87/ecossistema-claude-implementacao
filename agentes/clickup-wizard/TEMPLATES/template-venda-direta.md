# Template: Venda Directa / Distribuição / Equipamentos
**Sector:** Venda directa B2B, distribuidores, tratamento de água, equipamentos industriais, venda de campo

---

## Perfil do Cliente Típico
- Empresa com força de vendas em campo (comerciais + técnicos)
- Processo: prospecção → demonstração/visita → proposta → instalação/entrega → suporte pós-venda
- Dores: seguimento de visitas disperso, propostas enviadas sem controlo, equipa técnica desalinhada do comercial

---

## Estrutura de Folders & Lists

```
Space: [Empresa] — Vendas & Operações
│
├── Folder: Funil Comercial
│   ├── List: Prospecção & Qualificação
│   ├── List: Demonstrações & Visitas
│   ├── List: Propostas Enviadas
│   └── List: Negociação & Fecho
│
├── Folder: Clientes & Pós-Venda
│   ├── List: Clientes Activos
│   ├── List: Instalações em Curso
│   ├── List: Suporte & Manutenção
│   └── List: Renovações & Recambios
│
├── Folder: Equipa de Campo
│   ├── List: Visitas da Semana
│   ├── List: Relatórios de Visita
│   └── List: Formação & Produto
│
├── Folder: Operações & Stock
│   ├── List: Encomendas a Fornecedores
│   ├── List: Stock & Inventário
│   └── List: Entregas Pendentes
│
└── Folder: Arquivo
    └── List: Negócios Concluídos
```

---

## Custom Fields por List

### Funil Comercial (todas as lists)
| Campo | Tipo | Valores |
|-------|------|---------|
| Valor Estimado € | Currency | — |
| Probabilidade % | Number | 0-100 |
| Data Visita/Demo | Date | — |
| Comercial Responsável | People | — |
| Produto/Equipamento | Dropdown | [personalizar por linha de produto] |
| Canal de Origem | Dropdown | Prospecção directa, Referência, LinkedIn, Feira/Evento, Website, Parceiro |
| Decisor | Text | — |
| Empresa | Text | — |
| Telefone | Phone | — |
| Sector do Cliente | Dropdown | Restauração, Hotelaria, Indústria, Saúde, Habitação, Outro |

### Instalações em Curso
| Campo | Tipo | Valores |
|-------|------|---------|
| Técnico Responsável | People | — |
| Data Instalação | Date | — |
| Morada | Text | — |
| Equipamento | Dropdown | [linha de produto] |
| Número de Série | Text | — |
| Status Técnico | Dropdown | Agendado, Em Instalação, Concluído, Aguarda Peça |
| Assinatura Cliente | Checkbox | — |

### Suporte & Manutenção
| Campo | Tipo | Valores |
|-------|------|---------|
| Tipo de Ocorrência | Dropdown | Avaria, Manutenção Preventiva, Reclamação, Upgrade |
| Urgência | Dropdown | Crítica (24h), Alta (48h), Normal (7 dias), Programada |
| Técnico | People | — |
| Data de Resolução | Date | — |
| Custo Intervenção € | Currency | — |
| Garantia Activa | Checkbox | — |

---

## Views por List

### Prospecção & Qualificação
- **Board (Kanban):** por status (Novo → Contactado → Qualificado → Demo Agendada)
- **List:** ordenada por prioridade + comercial
- **Calendar:** por Data Visita/Demo

### Visitas da Semana
- **Calendar:** visão semanal por comercial
- **Board:** por comercial responsável
- **List:** ordenada por data

### Instalações em Curso
- **Table:** todos os campos visíveis
- **Board:** por status técnico
- **Calendar:** por Data Instalação

---

## Tags do Sector
`demo-agendada` | `proposta-enviada` | `follow-up` | `instalação-pendente` | `manutenção` | `avaria` | `hot-lead` | `renovação` | `recambio` | `em-formação` | `parceiro`

---

## Status Sugeridos (configurar manualmente)

### Funil Comercial
`Novo Lead` → `Contactado` → `Demo Agendada` → `Proposta Enviada` → `Em Negociação` → `Ganho ✅` | `Perdido ❌` | `Em Pausa`

### Instalações
`Agendada` → `Em Curso` → `Aguarda Peça` → `Concluída ✅` | `Cancelada ❌`

### Suporte
`Reportado` → `Em Diagnóstico` → `Aguarda Peça` → `Em Resolução` → `Resolvido ✅` | `Escalado ⚠️`

---

## Tasks de Exemplo

### Prospecção & Qualificação
1. "Contactar Restaurante O Forno — Demo purificador de água" (Urgente, data: +2 dias)
2. "Qualificar lead — Hotel Miramar Lisboa" (Alta, data: +5 dias)
3. "Visita prospecção — Clínica Dental Cascais" (Normal, data: +7 dias)

### Demonstrações & Visitas
1. "Demo equipamento — Fábrica Têxtil Guimarães — João Costa" (Alta, data: +3 dias)
2. "Visita follow-up — Padaria Central Porto" (Normal, data: +4 dias)
3. "Apresentação linha premium — Grupo Hoteleiro Norte" (Alta, data: +6 dias)

### Instalações em Curso
1. "Instalação sistema osmose — Restaurante Tágide Lisboa" (Urgente, data: +1 dia)
2. "Setup equipamento industrial — Fábrica Moldes Marinha Grande" (Alta, data: +5 dias)
3. "Entrega + instalação — Clínica Dr. Santos Setúbal" (Normal, data: +8 dias)

---

## Automations Recomendadas (configurar manualmente)
1. Quando demo concluída → criar task "Enviar proposta em 24h" automaticamente
2. Quando instalação concluída → criar task "Check-in 30 dias pós-instalação"
3. Quando task Suporte urgente criada → notificar técnico responsável imediatamente
4. Quando status → "Ganho ✅" → mover para "Clientes Activos" + criar task "Agendar instalação"
5. Quando data visita passou + status ≠ "Concluído" → criar alerta para gestor

---

## Integração ClickUp ↔ Pipedrive (upsell natural)

Este sector beneficia especialmente da integração:
- Deals Pipedrive → tasks instalação ClickUp (automático via integração)
- Notas de visita Pipedrive → visíveis no ClickUp pela equipa técnica
- Proposta ganha → triggers instalação sem intervenção manual

Mencionar sempre ao fechar implementação: *"A integração ClickUp ↔ Pipedrive elimina a comunicação manual entre comercial e técnico — é o passo seguinte natural."*
