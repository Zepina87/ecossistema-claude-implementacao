# KNOWLEDGE BASE — ClickUp Implementation Wizard

**Nota:** este ficheiro parte da metodologia de uma operação real de implementação ClickUp, com
nomes de clientes, colaboradores e tarifas removidos. A estrutura do processo, os tempos por fase
e as convenções ficaram — é o que interessa para operar o agente. Substitui os `[A PREENCHER]`
pela tua própria experiência à medida que fores implementando.

---

## 1. O PROCESSO DE IMPLEMENTAÇÃO

### Sequência de fases

```
FASE 0 — PRÉ-PROJECTO (comunicação inicial com o cliente)
    ↓
FASE 1 — REUNIÃO DIAGNÓSTICO (1h)
    ↓
FASE 2 — CRIAÇÃO DO PLANO DE IMPLEMENTAÇÃO (documento)
    ↓
FASE 3 — MODELAÇÃO DA ESTRUTURA BASE (Espaços + Pastas + Listas + Views)
    ↓
FASE 4 — CRIAÇÃO DOS KPIs
    ↓
FASE 5 — AJUSTES NA PRIMEIRA VERSÃO
    ↓
FASE 6 — VALIDAÇÃO COM O CLIENTE
    ↓
FASE 7 — IMPORTAÇÃO PARA CONTA DO CLIENTE
```

### Tempo típico por fase (referência de uma operação real; ajusta à tua)

| Fase | Estimado | Real (referência) |
|------|----------|------|
| Reunião Diagnóstico | 1h | 1h |
| Plano de Implementação | — | ~3h |
| Modelação estrutura base | 6h | ~3.75h |
| Criação de KPIs | 1.5h | 1.5h |
| Ajustes 1ª versão | 2.5h | 2.5h |
| **TOTAL TÍPICO** | **~11.5h** | **~8.75h** |

`[A PREENCHER: o teu custo/hora e se facturas por fase ou por pacote fechado]`

### Equipa de implementação (papéis, não pessoas)

Uma implementação tende a repartir-se por estes papéis — podem ser a mesma pessoa:
- **Modelação / Estrutura base** — quem desenha Espaços, Pastas e Listas
- **KPIs + Ajustes** — quem constrói dashboards e métricas
- **Validação + Import para conta do cliente** — quem fecha e entrega

---

## 2. JORNADA DO CLIENTE — COMUNICAÇÃO

### PRÉ-PROJECTO (mensagens WhatsApp/grupo)

**Mensagem 1 — Boas-vindas ao grupo:**
> "Boa tarde! Este grupo foi criado para o início do nosso projecto de implementação do ClickUp.
> Vai servir como o nosso meio de comunicação para todos os temas relacionados. Qualquer dúvida,
> resolvemos por aqui. Estamos ansiosos por começar!"

**Mensagem 2 — Marcação de reunião de diagnóstico:**
> "Gostaria de marcar uma reunião para discutirmos os tópicos necessários para o sucesso do vosso
> fluxo de trabalho. É importante para alinhar expectativas e optimizar os resultados. Sugere um
> horário conveniente?"

**Mensagem 3 — Pedido de materiais pré-reunião:**
Solicitar ao cliente:
- Esboço/ideia do processo de trabalho principal
- Modelos de mensagens ou emails que utilizam
- Documentos a associar ao ClickUp
- Lista de actividades para o ClickUp
- Lista de campos personalizados desejados
- Lista de métricas e KPIs essenciais
- Esquema de follow-up desejado

**Mensagem 4 — Follow-up após reunião:**
> "Passo para relembrar o envio dos pontos discutidos na nossa última reunião. Assim que
> recebermos o material, precisamos de cerca de 48 horas para verificar as informações e
> desenvolver o plano de implementação."

### PÓS-IMPLEMENTAÇÃO (período de suporte)

**Mensagem de encerramento (ajustar ao teu período de suporte):**
> "Com o encerramento do período de suporte, é com satisfação que concluímos esta fase do
> projecto. Obrigado pela confiança e pela colaboração durante todo o processo."
- Incluir sempre pedido de NPS
- Apresentar opções de suporte contínuo

---

## 3. CASOS — COMO REGISTAR OS TEUS

Mantém aqui os teus próprios casos reais, um por implementação, no mesmo formato:

```
### CASO: [sector, sem nome do cliente se preferires confidencialidade]
**Sector:**
**Tempo real:**
**Equipa do cliente mapeada:** [pessoa → responsabilidade]
**Funis/Espaços criados:**
**Etapas:**
**Status custom adicionados:**
**Nota de processo:** [algo que aprendeste nesta implementação e queres repetir/evitar]
```

Isto é o que dá ao Wizard "casos similares" para adaptar — sem isto preenchido, ele parte sempre
do zero.

---

## 4. INSIGHTS ESTRATÉGICOS

### A base de toda a modelação vem tipicamente de 2 fontes:
1. **Reunião de diagnóstico** (transcrição, se gravares — Fireflies ou equivalente)
2. **Estrutura do CRM do cliente** (Pipedrive ou outro, se já existir)

### Integração ClickUp ↔ CRM
Sincronizar listas do ClickUp com o pipeline comercial do CRM (Pipedrive ou outro) costuma ser um
deliverable recorrente e diferenciador — vale a pena oferecê-lo como upsell natural.

### Demos por vertical
O Wizard consegue gerar demos por sector com dados fictícios realistas — útil para mostrar antes
de uma reunião de venda, sem esperar pelo cliente real.

### Custom Fields de custo (opcional, se facturares por horas)
`[A PREENCHER: se quiseres rastrear custo/facturação dentro do próprio ClickUp — fórmula,
tarifa/hora, campo "Facturável?"]`

---

## 5. SECTORES E TEMPLATE BASE

| Sector | Template base a usar |
|--------|--------------------|
| Arquitectura & Decoração | `template-arquitectura-decoracao` |
| Construção / Obras | `template-operacoes` |
| Agência / Marketing | `template-agencia-marketing` |
| Tech / Software | `template-projetos-tech` |
| Venda Directa / Distribuição | `template-venda-direta` |
| Vendas / CRM | `template-vendas-crm` |
| `[A PREENCHER: outros sectores do teu portfólio]` | `template-custom` |

---

## 6. CHECKLIST PRÉ-MODELAÇÃO (correr sempre antes de modelar)

```
□ Lista de actividades/tarefas do negócio
□ Lista de campos personalizados desejados
□ Lista de métricas e KPIs essenciais
□ Esquema de follow-up desejado
□ Informações habitualmente pedidas aos clientes deles
□ Mapeamento equipa: pessoa → responsabilidades
□ Esboço do processo principal (funil)
□ Documentos a associar (propostas, orçamentos, etc.)
```

---

## 7. NOMENCLATURA PADRÃO (ajusta à tua)

### Nomenclatura de tasks de implementação:
- `Reunião Diagnóstico` (não "reunião inicial" ou "kickoff")
- `Modelação da estrutura Base` (não "criação" ou "setup")
- `Criação do Plano de Implementação` (documento separado)
- `Criação dos KPI'S`
- `Ajustes na primeira versão` (não "revisão" ou "fixes")
- `Validação da estrutura ClickUp com o cliente`
- `Importação para conta do cliente`

### Nomenclatura de clientes (escolhe uma convenção e mantém):
`[A PREENCHER: ex. "ClickUp [Nome Cliente]"]`

---

## 8. COMO O WIZARD DEVE USAR ESTA KNOWLEDGE BASE

### Ao iniciar uma implementação:
1. Identificar sector → consultar "Sectores e template base" (secção 5)
2. Verificar se há caso similar nos teus casos registados (secção 3) → adaptar estrutura
3. Usar o checklist pré-modelação (secção 6) para o intake
4. Seguir o processo real (secção 1) — não inventar fases

### Linguagem a usar (ajusta à tua):
- "Modelação" (não "configuração" ou "setup")
- "Espaços, Pastas e Listas" (por esta ordem)
- "Visualizações" (não "views" ao falar com clientes PT)
- "Plano de Implementação" (documento formal antes de executar)

### O que vale a pena manter da prática real:
- Documento de Plano ANTES de executar → o cliente valida
- Basear-se na reunião de diagnóstico + estrutura do CRM existente, quando houver
- Mapear sempre a equipa do cliente com responsabilidades
- Status custom claros (ex.: "Pendente", "Pronto para iniciar")
- Integração ClickUp ↔ CRM como upsell natural
