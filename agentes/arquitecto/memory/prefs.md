# O Arquitecto — Preferences & Templates
**Camada 2 de 4 | Templates de Sector + Fluxo de Demo**

---

## FLUXO COMPLETO (modo padrão)

### PASSO 1 — Identificar Reunião (Fireflies)
- Meeting ID dado → usar directamente
- "última reunião" → `fireflies_get_transcripts` → mais recente
- Nome empresa → `fireflies_search`

### PASSO 2 — Analisar R1 (extrair obrigatoriamente)
```
EMPRESA | SECTOR | DECISORES | EQUIPA DE VENDAS | PROCESSO ACTUAL
DORES TOP 3 | OBJECÇÕES | VOLUME DE NEGÓCIO | BUDGET HINTS
PRÓXIMOS PASSOS ACORDADOS | LINGUAGEM DO CLIENTE
```

### PASSO 3 — Seleccionar Template de Sector (ver abaixo)

### PASSO 4 — Gerar Configuração JSON Completa
- 4-6 Organizações fictícias mas realistas do mesmo sector/zona
- 4-6 Persons com nomes portugueses reais
- 5-8 Deals distribuídos pelos stages com valores realistas
- 3-5 Actividades (calls e reuniões próximos dias)
- **Regra de ouro:** dados fictícios que parecem REAIS e do SECTOR

### PASSO 5 — Executar Configuração
```bash
python "agentes/arquitecto/scripts/configurar-trial.py" \
  --token [TOKEN_DO_TRIAL] \
  --config "outputs/config-[empresa]-[data].json" \
  --reset
```

### PASSO 6 — Briefing R2 para o Closer
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRIEFING R2 — [EMPRESA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACESSO: Login | Password | URL

O QUE MOSTRAR (por ordem de impacto):
1. [dor mais forte R1 → feature que resolve]
2. [segunda dor → feature]
3. [custom fields do sector]

SCRIPT DE ABERTURA R2:
"[Nome], preparámos uma demo que reflecte exactamente o vosso processo de [sector]..."

DORES A FOCAR + como Pipedrive resolve
OBJECÇÕES ESPERADAS + respostas
O QUE NÃO MOSTRAR

CTA FINAL R2:
"Faz sentido avançarmos? Posso deixar este trial para a equipa 14 dias."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## TEMPLATES DE SECTOR (JSON completos)

### IMOBILIÁRIO
```json
{
  "pipeline_nome": "Processo de Vendas — [EMPRESA]",
  "stages": [
    {"name": "Lead Qualificada", "probabilidade": 10},
    {"name": "Visita Agendada", "probabilidade": 25},
    {"name": "Visita Realizada", "probabilidade": 40},
    {"name": "Proposta Enviada", "probabilidade": 60},
    {"name": "Em Negociação", "probabilidade": 75},
    {"name": "Escritura / Fecho", "probabilidade": 90}
  ],
  "custom_fields": [
    {"name": "Tipologia do Imóvel", "tipo": "varchar_options", "opcoes": ["T1","T2","T3","T4","T5+","Moradia","Comercial","Terreno"]},
    {"name": "Zona / Localização", "tipo": "varchar"},
    {"name": "Orçamento do Cliente (€)", "tipo": "double"},
    {"name": "Financiamento", "tipo": "varchar_options", "opcoes": ["Sim — banco aprovado","Sim — em processo","Não — capitais próprios","Não definido"]},
    {"name": "Prazo de Compra", "tipo": "varchar_options", "opcoes": ["Urgente (<1 mês)","Curto (1-3 meses)","Médio (3-6 meses)","Longo (+6 meses)"]},
    {"name": "Canal de Origem", "tipo": "varchar_options", "opcoes": ["Idealista","Imovirtual","Referência","Site próprio","Redes Sociais","Outro"]}
  ],
  "prova_social": "Parceiro Gonçalo Pinheirinho / Novo Imobiliário. Clientes: Life Plane Resort, KW, Remax, Century 21."
}
```

### SAÚDE / CLÍNICAS
```json
{
  "pipeline_nome": "Pipeline Comercial — [EMPRESA]",
  "stages": [
    {"name": "Contacto Inicial", "probabilidade": 10},
    {"name": "Necessidades Levantadas", "probabilidade": 25},
    {"name": "Demo Agendada", "probabilidade": 45},
    {"name": "Proposta Enviada", "probabilidade": 65},
    {"name": "Decisão Interna", "probabilidade": 80},
    {"name": "Contrato Assinado", "probabilidade": 95}
  ],
  "custom_fields": [
    {"name": "Especialidade Clínica", "tipo": "varchar_options", "opcoes": ["Medicina Geral","Dentária","Dermatologia","Ortopedia","Psicologia","Nutrição","Fisioterapia","Multi-especialidade"]},
    {"name": "Nº de Médicos / Especialistas", "tipo": "double"},
    {"name": "Nº de Consultas / Dia", "tipo": "double"},
    {"name": "Software Actual", "tipo": "varchar"},
    {"name": "Principal Dor", "tipo": "varchar_options", "opcoes": ["Agendamentos perdidos","Follow-up pós consulta","Gestão de leads privados","Falta de pipeline","Sem CRM"]}
  ],
  "prova_social": "Clínica Lusíadas. NUNCA mencionar 'Grupo Zidas' — não existe."
}
```

### SEGUROS
```json
{
  "pipeline_nome": "Carteira Comercial — [EMPRESA]",
  "stages": [
    {"name": "Lead Recebida", "probabilidade": 10},
    {"name": "Levantamento de Necessidades", "probabilidade": 20},
    {"name": "Proposta Elaborada", "probabilidade": 40},
    {"name": "Proposta Apresentada", "probabilidade": 60},
    {"name": "Em Negociação / Renovação", "probabilidade": 75},
    {"name": "Apólice Emitida", "probabilidade": 95}
  ],
  "custom_fields": [
    {"name": "Ramo do Seguro", "tipo": "varchar_options", "opcoes": ["Automóvel","Saúde","Vida","Habitação","Empresarial","Acidentes Trabalho","Responsabilidade Civil","Multi-risco"]},
    {"name": "Seguradora Actual", "tipo": "varchar"},
    {"name": "Prémio Actual (€/ano)", "tipo": "double"},
    {"name": "Data de Renovação", "tipo": "date"},
    {"name": "Nº de Apólices do Cliente", "tipo": "double"},
    {"name": "Canal de Captação", "tipo": "varchar_options", "opcoes": ["Referência","Prospecção directa","Digital","Balcão","Corretor parceiro"]}
  ],
  "prova_social": "Tranquilidade de Seguros, MAPFRE."
}
```

### AGÊNCIA / MARKETING
```json
{
  "pipeline_nome": "Pipeline de Novos Clientes — [EMPRESA]",
  "stages": [
    {"name": "Prospecção", "probabilidade": 10},
    {"name": "Qualificação", "probabilidade": 20},
    {"name": "Brief Recebido", "probabilidade": 40},
    {"name": "Proposta Enviada", "probabilidade": 55},
    {"name": "Aprovação Interna", "probabilidade": 75},
    {"name": "Contrato Assinado", "probabilidade": 90}
  ],
  "custom_fields": [
    {"name": "Tipo de Serviço", "tipo": "varchar_options", "opcoes": ["Social Media","SEO/SEM","Paid Ads","Branding","Web","Email Marketing","CRM","Full Service"]},
    {"name": "Budget Mensal (€)", "tipo": "double"},
    {"name": "Canal Principal", "tipo": "varchar_options", "opcoes": ["Instagram","LinkedIn","Google Ads","Meta Ads","Email","Multi-canal"]},
    {"name": "Duração do Contrato", "tipo": "varchar_options", "opcoes": ["Projecto pontual","3 meses","6 meses","12 meses","Contínuo"]},
    {"name": "Decisor", "tipo": "varchar"}
  ],
  "prova_social": "CloudTalk (parceiro directo — NÃO cliente)."
}
```

### CONSTRUÇÃO / PROMOTOR
```json
{
  "pipeline_nome": "Gestão Comercial Obras — [EMPRESA]",
  "stages": [
    {"name": "Pedido de Orçamento", "probabilidade": 15},
    {"name": "Visita / Medição", "probabilidade": 30},
    {"name": "Orçamento Elaborado", "probabilidade": 45},
    {"name": "Proposta Apresentada", "probabilidade": 60},
    {"name": "Negociação", "probabilidade": 75},
    {"name": "Adjudicação / Contrato", "probabilidade": 90}
  ],
  "custom_fields": [
    {"name": "Tipo de Obra", "tipo": "varchar_options", "opcoes": ["Remodelação","Construção nova","Ampliação","Manutenção","Reabilitação","Industrial","Comercial"]},
    {"name": "Localização da Obra", "tipo": "varchar"},
    {"name": "Valor Estimado (€)", "tipo": "double"},
    {"name": "Prazo de Execução", "tipo": "varchar_options", "opcoes": ["<1 mês","1-3 meses","3-6 meses","6-12 meses","+12 meses"]},
    {"name": "Subempreiteiro Necessário", "tipo": "varchar_options", "opcoes": ["Sim","Não","A avaliar"]},
    {"name": "Origem do Lead", "tipo": "varchar_options", "opcoes": ["Referência","Concurso público","Arquitecto","Promotor","Plataforma","Directo"]}
  ]
}
```

### PME GENÉRICA (fallback)
```json
{
  "pipeline_nome": "Pipeline Comercial — [EMPRESA]",
  "stages": [
    {"name": "Lead Qualificada", "probabilidade": 10},
    {"name": "1ª Reunião Realizada", "probabilidade": 25},
    {"name": "Proposta Enviada", "probabilidade": 50},
    {"name": "Em Negociação", "probabilidade": 70},
    {"name": "Fecho", "probabilidade": 90}
  ],
  "custom_fields": [
    {"name": "Sector", "tipo": "varchar"},
    {"name": "Dimensão da Equipa de Vendas", "tipo": "double"},
    {"name": "CRM Actual", "tipo": "varchar_options", "opcoes": ["Excel","Nenhum","HubSpot","Salesforce","Outro"]},
    {"name": "Principal Dor", "tipo": "varchar"},
    {"name": "Canal de Captação", "tipo": "varchar_options", "opcoes": ["Inbound","Outbound","Referência","Parceiro","Misto"]}
  ],
  "prova_social": "Platinum Partner Pipedrive. Caso do sector mais próximo disponível."
}
```
