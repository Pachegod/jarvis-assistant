# Jarvis Assistant

Um assistente inteligente que integra Gmail, Google Calendar e Claude Code para automatizar gerenciamento de tarefas e calendário, com notificações via Slack.

## Funcionalidades

- Sincronização de tarefas do Gmail
- Integração com Google Calendar
- Busca de tasks do Claude Code
- Notificações diárias no Slack
- Agendamento automático (8:30 AM)

## Requisitos

- Python 3.8+
- Docker e Docker Compose (opcional)
- Credenciais de API para:
  - Google Workspace (Gmail, Calendar)
  - Slack
  - Claude Code (API)

## Instalação

### Setup Local

1. Clone o repositório:
```bash
git clone <repo-url>
cd jarvis-assistant
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
make install
# ou manualmente: pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite .env com suas credenciais
```

5. Setup inicial:
```bash
make setup
```

### Setup com Docker

```bash
docker-compose up -d
```

## Uso

### Executar uma vez:
```bash
make run
```

### Iniciar scheduler (executa diariamente às 8:30 AM):
```bash
make schedule
```

### Comandos disponíveis:

```bash
make install     # Instala dependências
make run         # Executa uma vez
make schedule    # Inicia scheduler
make setup       # Setup inicial
make clean       # Remove cache e arquivos temporários
```

## Estrutura do Projeto

```
jarvis-assistant/
├── src/
│   ├── main.py                 # Script principal
│   ├── scheduler.py            # Configuração de agendamento
│   └── integrations/
│       ├── __init__.py
│       ├── gmail.py            # Integração Gmail
│       ├── calendar.py         # Integração Google Calendar
│       ├── claude_code.py      # Integração Claude Code
│       └── slack.py            # Integração Slack
├── requirements.txt            # Dependências Python
├── .env.example               # Template de variáveis de ambiente
├── .gitignore                 # Arquivos ignorados
├── Makefile                   # Comandos úteis
├── docker-compose.yml         # Configuração Docker
└── README.md                  # Este arquivo
```

## Configuração de Variáveis de Ambiente

Crie um arquivo `.env` baseado em `.env.example` com:

```env
# Google Workspace
GOOGLE_CREDENTIALS_PATH=credentials.json
GOOGLE_TOKEN_PATH=token.pickle

# Gmail
GMAIL_USER_EMAIL=seu-email@gmail.com
GMAIL_TASK_LABEL=Tarefas

# Google Calendar
CALENDAR_ID=seu-calendar-id@gmail.com

# Claude Code
CLAUDE_CODE_API_KEY=sua-api-key
CLAUDE_CODE_USER_ID=seu-user-id

# Slack
SLACK_BOT_TOKEN=xoxb-seu-token
SLACK_CHANNEL=C123456789

# Agendamento
SCHEDULE_TIME=08:30
```

## Fluxo de Funcionamento

1. **Carregamento de Credenciais**: Lê variáveis de ambiente
2. **Sincronização Gmail**: Busca tarefas com label específico
3. **Integração Calendar**: Consulta compromissos do dia
4. **Busca Claude Code**: Recupera tasks e PRs em progresso
5. **Montagem de Mensagem**: Formata informações em um resumo
6. **Envio Slack**: Publica no canal configurado

## Autenticação Google

Veja a [documentação de autenticação Google](https://developers.google.com/identity/protocols/oauth2) para gerar credenciais de API.

## Desenvolvimento

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Instalar em modo desenvolvimento
pip install -e .

# Executar testes (quando disponíveis)
pytest
```

## Troubleshooting

### Erro de autenticação Google
- Verifique se as credenciais estão no arquivo correto
- Confirme se as APIs estão habilitadas no Google Cloud Console

### Mensagens não chegam ao Slack
- Verifique o token do bot
- Confirme se o bot tem permissão no canal

### Scheduler não inicia
- Verifique se todas as variáveis de ambiente estão configuradas
- Confira os logs: `python -m src.scheduler`

## Contribuindo

1. Crie uma branch: `git checkout -b feature/sua-feature`
2. Faça suas alterações
3. Commit: `git commit -m "Descrição clara"`
4. Push: `git push origin feature/sua-feature`
5. Abra um Pull Request

## Licença

Este projeto é privado e confidencial.

## Contato

Para dúvidas ou sugestões, entre em contato com a equipe.
