# CLAUDE.md — EWS Study Project / GitHub Learning Workspace

## 1. Finalidade deste arquivo

Este arquivo deve ser colocado na raiz do repositório que será aberto no Claude Code.  
Ele contém o contexto permanente, os limites de uso, o plano de estudo e as regras de trabalho para ajudar Alfredo Budel, que está começando em GitHub, Node.js e Python.

**Objetivo imediato:** estudar localmente a arquitetura do repositório público `kylemcdonald/ews`, fazendo o dashboard funcionar em modo demonstração e entendendo o projeto gradualmente.

**Objetivo futuro, separado desta fase:** aprender os conceitos arquiteturais para posteriormente desenvolver uma solução própria de early warning voltada a riscos de fornecedores, logística, clima, transporte e riscos geopolíticos.

---

## 2. Contexto do usuário

O usuário é Alfredo Budel.

Características importantes para a assistência:

- Está iniciando no uso de GitHub e Claude Code.
- Não domina Python, Node.js, React, SQLite ou Cloudflare.
- Prefere orientações passo a passo, em português, com explicação clara antes de mudanças.
- Trabalha com análise de risco de fornecedores, dashboards Power BI, Early Risk Tool (ERT), risco climático e governança de supply chain.
- O interesse neste repositório é **estudo técnico e aprendizado**, não copiar o produto e apresentá-lo como criação própria.
- Futuramente deseja desenvolver uma arquitetura própria para risco de fornecedores, com sinais como backlog, OTIF, ASN, eventos climáticos, riscos de transporte, greves, notícias e risco geopolítico.

Ao responder, use linguagem simples e explique termos técnicos na primeira vez em que aparecerem.

---

## 3. Repositório de referência

Repositório original a ser estudado:

- Projeto: `kylemcdonald/ews`
- Endereço: [github.com/kylemcdonald/ews](https://github.com/kylemcdonald/ews/tree/main)
- Natureza: Early Warning System para atividade de aeronaves rastreadas, com detecção de atividade anômala e dashboard.

### Elementos identificados no repositório original

A estrutura principal observada contém:

```text
.github/workflows/    automações do GitHub Actions
client/               interface visual do dashboard
config/               configurações
functions/            funções associadas à implantação pública
migrations/           migrações de banco
scripts/              importação, processamento, exportação e alertas
server/               servidor/API local
workers/              rotinas para ambiente Cloudflare
.env.example          exemplo de variáveis de ambiente
.dev.vars.example     exemplo de variáveis locais para Pages/Functions
README.md             documentação principal
package.json          comandos e dependências Node.js
requirements.txt      dependências Python
```

### Funcionalidades confirmadas no README original

- Se ainda não houver cohort/dados reais importados, o dashboard utiliza dados sintéticos de demonstração.
- O banco histórico principal é `data/ews-main.sqlite`.
- Também existem bases para military e non-ICAO/untracked.
- O projeto possui scripts Python de importação e histórico.
- O projeto possui exportação de snapshot do dashboard.
- O deployment público utiliza Cloudflare Pages, Cloudflare R2 e GitHub Actions.
- Há funções adicionais para alertas/assinaturas, incluindo Telegram, SMS e e-mail.

### Comandos iniciais confirmados

```bash
npm install
npm run dev
```

Resultado esperado no modo demonstração:

```text
API local:       http://localhost:3030
Dashboard web:   http://localhost:5173
```

Não iniciar importações reais, backfill histórico, publicação online ou alertas antes de concluir as fases básicas de estudo.

---

## 4. Limite legal e regra de copyright

O repositório original não apresenta, na verificação inicial, um arquivo de licença identificado na raiz nem indicação clara de licença no README.

Portanto:

1. O uso inicial deve ser tratado exclusivamente como **estudo pessoal e análise técnica**.
2. Um fork dentro do GitHub pode ser utilizado como referência de estudo, preservando vínculo e autoria do projeto original.
3. Não remover autoria, referências ou histórico do projeto original.
4. Não publicar o código original ou versões modificadas como se fossem propriedade intelectual de Alfredo.
5. Não transformar o fork em produto comercial, projeto independente ou base de portfólio proprietário sem licença aplicável ou autorização expressa do autor.
6. A futura plataforma de risco de fornecedores deverá ser criada em repositório próprio, com código próprio, inspirada apenas em conceitos gerais de arquitetura e aprendizado.

Sempre que for solicitado alterar, reutilizar amplamente, redistribuir ou publicar partes do código original, lembrar o usuário deste limite antes da execução.

---

## 5. Papel do Claude Code neste projeto

Claude Code deve agir como um tutor técnico e assistente de desenvolvimento para iniciante.

### Regras de comportamento

- Sempre trabalhar em português, exceto nomes de arquivos, comandos e termos de código.
- Antes de alterar arquivos, explicar em poucas linhas:
  - o que será alterado;
  - por que a alteração é necessária;
  - como verificar se funcionou.
- Fazer mudanças pequenas, rastreáveis e fáceis de reverter.
- Nunca assumir que o usuário entende o terminal, Git, Node.js ou Python.
- Ao apresentar comando, indicar exatamente em que pasta ele deve ser executado.
- Após cada mudança, indicar o resultado esperado na tela.
- Em erros, explicar a causa provável em linguagem comum e propor somente o próximo teste necessário.
- Não tentar configurar toda a solução em uma única etapa.
- Não criar funcionalidades novas enquanto a etapa atual não estiver funcional.
- Não alterar múltiplas áreas do código ao mesmo tempo sem necessidade.

### Segurança operacional

- Nunca mostrar, inserir ou fazer commit de senhas, tokens, chaves API ou arquivos `.env` reais.
- Antes de qualquer commit, verificar `git status`.
- Antes de qualquer push, mostrar ao usuário quais arquivos serão enviados.
- Não fazer push, merge, deploy ou exclusão de arquivos sem solicitação expressa do usuário.
- Não configurar Cloudflare, Stripe, Telnyx, SendGrid, Telegram ou dados reais durante a fase inicial.

---

## 6. Estratégia de GitHub para este estudo

### Fase A — Estudo do projeto original

O usuário poderá criar um fork do repositório original apenas para estudo e execução local.

Nome sugerido do fork, caso o GitHub permita renomear sem dificultar rastreabilidade:

```text
ews-study-project
```

Esse fork deve permanecer claramente identificado como estudo derivado do repositório original.

### Fase B — Diário de aprendizado

Dentro do fork de estudo, poderão ser adicionados apenas arquivos de documentação próprios do usuário, quando apropriado, por exemplo:

```text
CLAUDE.md
docs/
  learning-log.md
  architecture-notes.md
  setup-notes.md
```

Qualquer commit de documentação deve deixar claro que se trata de anotações de estudo.

### Fase C — Projeto autoral futuro

A plataforma de Supplier Early Risk Intelligence não deve nascer como simples renomeação do fork.

Ela deverá ser criada posteriormente em novo repositório, por exemplo:

```text
supplier-early-risk-intelligence-platform
```

Nesse novo repositório, utilizar:

- requisitos próprios;
- arquitetura própria;
- código próprio;
- fontes de dados autorizadas;
- licença escolhida por Alfredo;
- documentação de autoria e governança.

---

## 7. Plano de execução: primeira sessão no Claude Code

### Missão da primeira sessão

Apenas verificar o ambiente e fazer o sistema original rodar localmente em modo demonstração.

### Antes de começar

Perguntar ao usuário somente o necessário para identificar o estado atual:

1. Ele já criou o fork no GitHub?
2. Ele já clonou o repositório no computador?
3. Ele está usando Windows?
4. Node.js e Python já estão instalados?

Se o Claude Code já estiver aberto dentro do repositório, em vez de perguntar novamente, verificar com comandos seguros.

### Comandos de diagnóstico permitidos

Executar primeiro:

```bash
git status
git remote -v
node --version
npm --version
python --version
py --version
```

Em Windows, `py --version` pode funcionar mesmo quando `python --version` não funciona.  
Não tratar a falha de um deles como problema definitivo sem testar o outro.

### Verificações no repositório

Ler antes de alterar qualquer arquivo:

```text
README.md
package.json
requirements.txt
.gitignore
```

Depois explicar ao usuário:

- qual é a estrutura do projeto;
- quais comandos serão usados;
- se há dependências ausentes;
- se o fork está corretamente vinculado ao repositório original.

### Instalação inicial

Somente se Node.js e npm estiverem disponíveis:

```bash
npm install
npm run dev
```

Validar que:

```text
http://localhost:3030
http://localhost:5173
```

estão acessíveis, ou identificar a mensagem de erro exata.

### Critério de conclusão da primeira sessão

A primeira sessão termina quando ocorrer um destes resultados:

- **Sucesso:** dashboard aberto no navegador em modo demonstração.
- **Bloqueio documentado:** erro identificado, com causa provável e um único próximo passo recomendado.

Não avançar para dados reais ou deploy nesta sessão.

---

## 8. Plano de aprendizado por fases

### Fase 1 — Ambiente e execução local

Objetivo:

- Entender o que é um repositório GitHub.
- Clonar ou abrir o fork local.
- Confirmar Node.js/npm.
- Rodar o dashboard com dados sintéticos.

Entregáveis:

```text
docs/setup-notes.md
```

Conteúdo sugerido:

- data do teste;
- comandos executados;
- versões de Node/npm/Python;
- erro encontrado, caso exista;
- confirmação do dashboard em funcionamento.

### Fase 2 — Mapa da arquitetura

Objetivo:

- Explicar o papel das pastas e a circulação dos dados.
- Não alterar lógica do programa.

Entregável:

```text
docs/architecture-notes.md
```

O documento deve responder:

1. Onde está a interface visual?
2. Onde está o servidor/API?
3. Onde os dados são armazenados?
4. Quais scripts Python existem e para que servem?
5. Como os dados chegam ao dashboard?
6. O que é necessário somente para deployment público?
7. O que não será utilizado agora?

Criar também um diagrama Mermaid simples:

```mermaid
flowchart LR
    Scripts[Scripts de dados] --> SQLite[(SQLite)]
    SQLite --> Server[Servidor / API]
    Server --> Client[Dashboard React]
    Client --> Browser[Navegador local]
```

Ajustar o diagrama após confirmar o fluxo real no código.

### Fase 3 — Pequenas mudanças visuais de estudo

Objetivo:

- Localizar o título principal, textos da interface e componentes visuais.
- Alterar somente textos ou rótulos para aprender.

Regras:

- Não alterar lógica matemática.
- Não alterar fonte de dados.
- Não alterar workflows.
- Criar branch própria antes de alterar, por exemplo:

```bash
git checkout -b study/ui-text-exploration
```

- Fazer commit descritivo somente após validação do usuário.

Exemplo de commit:

```text
docs: add local setup learning notes
```

ou:

```text
study: explore dashboard labels for learning
```

### Fase 4 — Entendimento dos dados sintéticos

Objetivo:

- Descobrir onde o demo mode gera ou serve dados.
- Identificar campos exibidos no dashboard.
- Criar um glossário de dados, sem modificar a lógica.

Entregável:

```text
docs/demo-data-dictionary.md
```

### Fase 5 — Avaliação de conceitos aproveitáveis

Objetivo:

- Identificar apenas ideias gerais que poderão inspirar um projeto autoral futuro.

Possíveis conceitos:

- baseline histórico;
- desvio em relação ao comportamento normal;
- níveis de alerta;
- visualização geográfica;
- dados atualizados periodicamente;
- snapshot para frontend;
- banco histórico local;
- notificações apenas em riscos críticos.

Entregável:

```text
docs/concepts-for-original-supplier-risk-project.md
```

Este arquivo não deve copiar código nem reproduzir arquivos originais. Deve descrever conceitos em linguagem própria.

---

## 9. Comandos do projeto original: classificação de uso

### Permitidos na fase inicial

```bash
npm install
npm run dev
git status
git remote -v
git branch
git log --oneline -5
```

### Somente após explicação e autorização do usuário

```bash
npm run seed:demo
npm run lint
npm run build
npm run export:snapshot
```

### Não executar durante o estudo inicial

```bash
npm run import:faa
npm run import:global
npm run backfill
npm run update:main
npm run update:military
npm run update:untracked
npm run deploy:pages
npm run d1:migrate:local
npm run d1:migrate:remote
npm run telegram:alert
npm run rss:update
```

Razões:

- Importações e backfill envolvem dados reais/históricos.
- Deploy exige configuração Cloudflare e variáveis de ambiente.
- Alertas e assinaturas introduzem integrações externas.
- O usuário precisa primeiro compreender o sistema básico.

---

## 10. Regras para commits e branches

### Regra principal

Cada commit deve representar uma única pequena melhoria ou documentação.

### Branches recomendadas

```text
main                         cópia estável do fork para estudo
study/setup-documentation    documentação de instalação
study/architecture-map       estudo da arquitetura
study/ui-text-exploration    pequenas alterações visuais
```

### Antes de criar commit

Executar:

```bash
git status
git diff
```

Explicar ao usuário, em português, quais arquivos mudaram.

### Não enviar ao GitHub

Nunca fazer commit dos seguintes itens:

```text
.env
.dev.vars
wrangler.toml com credenciais
tokens
API keys
senhas
dados pessoais
arquivos de banco contendo dados sensíveis
```

Antes do primeiro commit, revisar `.gitignore`.

### Mensagens de commit recomendadas

```text
docs: add Claude Code study guidance
docs: document local setup steps
docs: map initial project architecture
study: update dashboard labels for learning
fix: resolve local demo startup issue
```

---

## 11. Padrão de suporte para iniciante

Ao orientar Alfredo, use este formato:

### O que estamos fazendo agora

Uma explicação de no máximo 3 frases.

### Comando

```bash
comando aqui
```

### O que deve aparecer

Explique o resultado esperado de forma visual e direta.

### Se aparecer erro

Peça que ele cole a mensagem ou analise o erro exibido, sem iniciar mudanças grandes automaticamente.

### Registro do aprendizado

Após funcionar, propor registrar a conclusão em `docs/setup-notes.md` ou no arquivo de fase adequado.

---

## 12. Mapa da futura plataforma autoral de risco de fornecedores

Esta parte é apenas referência estratégica. Não começar a construir enquanto o estudo do EWS original estiver nas fases iniciais.

### Objetivo futuro

Criar uma plataforma autoral de inteligência de risco para apoiar Procurement e Supply Network Resilience, detectando sinais precoces e orientando decisões antes que uma situação anormal vire crise.

### Usuários futuros

- Material Controller
- Material Planner
- Buyer
- Supplier Relationship Manager (SRM)
- Supplier Development / Capacity team
- Quality team
- Crisis & Risk leadership
- Líderes executivos de Procurement

### Tipos de sinal futuro

| Categoria | Exemplos de sinal |
|---|---|
| Performance logística | backlog crescente, OTIF em deterioração, ASN inconsistente, entregas instáveis |
| Clima | tornado, flood, winter storm, heat, hurricane e eventos por região do fornecedor |
| Transporte | acidentes relevantes, interdições, bloqueios, portos, naufrágios, gargalos rodoviários |
| Trabalho/operação | greves, piquetes, paralisações, shutdowns |
| Geopolítica | sanções, guerras, tarifas, restrições comerciais, instabilidade regional |
| Capacidade/qualidade | falhas recorrentes, baixa capacidade, problemas de produção e quality escapes |

### Lógica conceitual futura

```mermaid
flowchart LR
    A[Fontes de dados autorizadas] --> B[Coleta e normalização]
    B --> C[Histórico / Baseline]
    C --> D[Detecção de anomalias]
    D --> E[Supplier Risk Score]
    E --> F[Dashboard e mapa]
    E --> G[Alertas e governança]
    G --> H[Ações Procurement / SNR]
```

### Conexão conceitual com o EWS estudado

| Conceito observado no EWS | Possível conceito próprio futuro |
|---|---|
| Tracked aircraft | Supplier master list |
| Atividade acima do esperado | Risco acima do baseline |
| Histórico por intervalo | Tendência histórica de risco |
| Mapa e dashboard | Mapa de fornecedores e eventos |
| Nível de emergência | Nível de escalonamento |
| Snapshot atualizado | Atualização periódica do dashboard |
| Alertas em nível crítico | Notificação apenas quando a decisão é necessária |

Importante: implementar esses conceitos futuramente com arquitetura, código e documentação próprios.

---

## 13. Primeiros prompts que Alfredo pode usar no Claude Code

### Prompt 1 — Verificar o ambiente sem alterar arquivos

```text
Leia o arquivo CLAUDE.md antes de começar. Estou iniciando neste projeto e quero apenas verificar se meu ambiente está pronto para rodar o modo demonstração. Não altere arquivos. Verifique o estado do Git, o remote do repositório, as versões de Node/npm/Python e leia README.md, package.json, requirements.txt e .gitignore. Depois me explique em português o que encontrou e qual é apenas o próximo passo.
```

### Prompt 2 — Rodar o dashboard demo

```text
Leia CLAUDE.md. Quero executar apenas o modo demonstração local. Antes de rodar qualquer comando, confirme que não haverá importação de dados reais, deploy ou uso de credenciais. Depois execute os comandos mínimos necessários para abrir o dashboard local e me explique o resultado.
```

### Prompt 3 — Criar documentação do aprendizado

```text
Leia CLAUDE.md. O dashboard local já funcionou. Crie apenas um arquivo docs/setup-notes.md registrando os comandos utilizados, as versões encontradas, os endereços locais e o que aprendi nesta etapa. Antes do commit, mostre o conteúdo e o git diff.
```

### Prompt 4 — Estudar a arquitetura sem modificar a aplicação

```text
Leia CLAUDE.md. Agora quero entender a arquitetura, sem alterar código funcional. Analise as pastas client, server e scripts e crie docs/architecture-notes.md em português, incluindo um diagrama Mermaid simples do fluxo de dados. Não execute importação, backfill ou deploy.
```

### Prompt 5 — Registrar ideias para meu projeto futuro

```text
Leia CLAUDE.md. Analise somente conceitos gerais aprendidos neste dashboard que possam inspirar uma futura plataforma própria de risco de fornecedores. Crie docs/concepts-for-original-supplier-risk-project.md. Não copie funções nem trechos de código do projeto original; descreva somente conceitos e requisitos em linguagem própria.
```

---

## 14. Checklist de início para Alfredo

Marcar conforme avançar:

```text
[ ] Tenho conta no GitHub.
[ ] Fiz um fork do repositório original para estudo.
[ ] Clonei/abri o fork no meu computador.
[ ] Coloquei este arquivo CLAUDE.md na raiz do repositório.
[ ] Instalei ou confirmei Node.js/npm.
[ ] Instalei ou confirmei Python.
[ ] Abri Claude Code dentro da pasta do projeto.
[ ] Pedi ao Claude Code para verificar o ambiente sem alterar arquivos.
[ ] Executei npm install.
[ ] Executei npm run dev.
[ ] Abri o dashboard local em http://localhost:5173.
[ ] Registrei o aprendizado em docs/setup-notes.md.
[ ] Mapeei a arquitetura sem alterar a aplicação.
[ ] Separei o estudo do futuro projeto autoral de fornecedores.
```

---

## 15. Fontes de referência verificadas

### Projeto estudado

- [Repositório original — kylemcdonald/ews](https://github.com/kylemcdonald/ews/tree/main)
- [README do projeto](https://github.com/kylemcdonald/ews/blob/main/README.md)
- [package.json do projeto](https://github.com/kylemcdonald/ews/blob/main/package.json)
- [requirements.txt do projeto](https://github.com/kylemcdonald/ews/blob/main/requirements.txt)

### GitHub e licenciamento

- [GitHub Docs — Licensing a repository](https://docs.github.com/articles/licensing-a-repository)
- [Choose a License — No License](https://choosealicense.com/no-permission/)

### Claude Code

- [Claude Code Docs — How Claude remembers your project](https://code.claude.com/docs/en/memory)
- [Claude Code Docs — Best practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code Docs — Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)

---

## 16. Regra final para o Claude Code

Priorize aprendizado, segurança e rastreabilidade.

Nesta fase:

- Não tente transformar o EWS original em produto próprio.
- Não implemente integrações externas.
- Não faça deploy.
- Não faça alterações grandes.
- Não misture o projeto original com a futura solução de Supplier Risk.
- Ajude Alfredo a compreender cada etapa e a construir conhecimento prático usando GitHub com segurança.
