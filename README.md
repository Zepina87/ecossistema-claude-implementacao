# O teu ecossistema de IA — foco em implementação

**Para:** quem implementa Pipedrive e ClickUp em clientes

Não é um pacote de ferramentas genérico. É uma oficina (o Cérebro, que constrói e afina agentes
novos quando precisares) **com dois agentes reais já instalados e prontos a trabalhar**:

- **O Arquitecto** — lê a reunião de diagnóstico (Fireflies) e configura um trial Pipedrive
  personalizado, pronto para a demo de fecho.
- **ClickUp Implementation Wizard** — modela um workspace ClickUp completo por sector, do intake
  à documentação e ao relatório de entrega, sem pedir confirmação a cada passo.

Os dois vêm de agentes reais em produção, adaptados para uso próprio: sem nomes de clientes, sem
tokens, sem marca de ninguém. O que ficou é a doutrina que interessa — o fluxo, as regras, os
templates de sector.

---

## Arranque, cerca de dez minutos

### 1. Instalar o Claude Code

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

Precisas de Node 18 ou superior e de uma conta Claude. Documentação: https://docs.claude.com/claude-code

### 2. Abrir esta pasta

```bash
cd ecossistema-claude-implementacao
claude
```

### 3. Instalar os comandos

```bash
./scripts/instalar.sh
```

Ficas com `/cerebro` e as ferramentas de ofício. Se já tiveres um comando com o mesmo nome, o
antigo é guardado numa cópia antes de ser substituído, e o instalador diz onde.

### 4. Ligar as tuas credenciais

```bash
cp .env.example .env
```

Preenche o `.env` com os teus tokens (Pipedrive, Fireflies se usares). O ClickUp fica à parte: o
MCP nativo e o Enhanced MCP guardam o token no `settings.json` do Claude Code, não neste
repositório — ver `agentes/clickup-wizard/SKILL.md`.

### 5. Preencher a identidade de cada agente

Três ficheiros têm `[A PREENCHER]` à espera de ti:
- `CLAUDE.md.template` → copia para `CLAUDE.md` (quem és, as tuas regras absolutas)
- `agentes/arquitecto/memory/core.md` → a tua prova social real, os teus sectores
- `agentes/clickup-wizard/memory/core.md` → o teu nome, a tua lista interna de acompanhamento

Nada disto é obrigatório para o primeiro teste — os agentes funcionam com os defaults e avisam-te
quando faltar algo em vez de inventar. Mas vale a pena fazê-lo antes de usar a sério.

### 6. Primeiro uso a sério

```
/arquitecto prepara demo para [empresa] — última reunião
```
ou
```
/clickup-wizard [cliente] [sector]
```

---

## O que está aqui

| Pasta | O que contém |
|---|---|
| `cerebro/` | O Cérebro — orquestrador, forja agentes novos quando precisares, já sabe que o Arquitecto e o ClickUp Wizard existem |
| `agentes/arquitecto/` | Master prompt, skill, memória em 4 camadas, script de configuração do trial (`configurar-trial.py`), pool de trials |
| `agentes/clickup-wizard/` | Master prompt, skill, memória em 4 camadas, knowledge base do processo, 6 templates de sector |
| `metodo/` | Nove documentos: anatomia, memória, SPAR, autonomia, orquestração, loops, qualidade, custo, erros |
| `seguranca/` | Cinco documentos e uma checklist. Segredos, repositórios de fora, injecção de prompt, permissões, dados pessoais |
| `skills/` | Ferramentas de ofício: gates de qualidade, design, memória, pensamento |
| `templates/` `scripts/` | Moldes para agentes novos e o instalador |

---

## Uma diferença face ao ponto de partida genérico

Um agente forjado do zero pela Oficina começa read-only por desenho: lê, analisa, propõe — a
escrita fica do lado de quem opera. **O Arquitecto e o ClickUp Wizard não seguem essa regra**,
porque é literalmente o que fazem: o Arquitecto escreve no trial Pipedrive do prospect, o Wizard
escreve no workspace ClickUp do cliente. Isso é intencional e é o valor deles — mas por isso trazem
os próprios travões: o Arquitecto nunca activa nada sem confirmação explícita e faz sempre reset
antes de uma demo nova; o Wizard verifica duplicados antes de criar um Space e nunca apaga
estrutura existente sem confirmação. Qualquer agente novo que forjares a seguir volta ao default
read-only, a não ser que decidas explicitamente o contrário.

**Nada sai sem passar pelos gates.** Um número sem origem, um nome não confirmado, um texto que soa
a máquina. Quem assina és tu, portanto o custo do erro é teu.

---

## Quando algo não funcionar

Pergunta directamente: *"porque é que fizeste assim"* ou *"o que precisas para isto funcionar"*.
Se faltar um acesso, o agente diz qual em vez de inventar o resultado.

---

## Ler a seguir

**[COMECAR-AQUI.md](COMECAR-AQUI.md)**, uma página, com o dia 1, o dia 7 e o dia 30.
