# ECOSYSTEM, o registo vivo

Este ficheiro é a lista do que existe. O Cérebro lê-o antes de forjar qualquer coisa, para não
criar um agente que já existe.

**Este repositório não vem vazio.** Já traz dois agentes reais, tirados de uma operação em
produção e adaptados para uso próprio: o Arquitecto (demos Pipedrive) e o ClickUp Implementation
Wizard (implementação ClickUp). Estão prontos a usar — só precisam das tuas credenciais em `.env`
e do preenchimento dos `[A PREENCHER]` nos ficheiros de memória de cada um. Outros agentes nascem
na Oficina, quando o uso os pedir: se ao fim de um mês esta tabela tiver mais linhas escritas por
ti, a entrega funcionou.

---

## Agentes activos

| Agente | Comando | Missão numa linha | SPAR | Criado por | Data |
|---|---|---|---|---|---|
| O Cérebro | `/cerebro` | Orquestrador principal: responde do método, forja agentes, afina os que existem, calibra o ambiente | 33/35 | de origem | 2026-07-28 |
| O Arquitecto | `/arquitecto` | Lê a reunião de diagnóstico no Fireflies e configura um trial Pipedrive personalizado, pronto para a demo de fecho | 33/35 | adaptado de agente real | 2026-09-18 |
| ClickUp Implementation Wizard | `/clickup-wizard` | Modela workspaces ClickUp completos por sector — Espaços, Pastas, Listas, Custom Fields, documentação e relatório de entrega | 32/35 | adaptado de agente real | 2026-09-18 |

Ficheiros de cada agente em `agentes/arquitecto/` e `agentes/clickup-wizard/` — master prompt,
skill, memória em 4 camadas, e no caso do Wizard também os 6 templates de sector.

---

## Gates de qualidade

Não são agentes. São filtros que correm por cima do que sai.

| Gate | Comando | Apanha |
|---|---|---|
| Fact check | `/fact-check` | Números sem fonte, nomes não confirmados, capacidades que não temos |
| Ghost check | `/ghost-check` | Texto que soa a máquina |
| Taste | `/taste` | Qualidade visual genérica |
| Deep research | `/deep-research` | Afirmar sobre o mundo sem verificar |

---

## Como registar um agente novo

A Oficina faz isto por ti, no passo 5 do processo descrito em `metodo/`. Se escreveres à mão, o
formato é o da tabela de cima, e as três colunas que as pessoas se esquecem de preencher são as
que interessam ao fim de seis meses: **SPAR** (para saberes se ele foi auditado), **criado por**
(para saberes a quem perguntar) e **data** (para saberes se ainda faz sentido).

Regra: um agente sem SPAR pontuado não entra nesta tabela. Fica em rascunho até ser pontuado.
