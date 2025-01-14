# Gerenciador de Tarefas CLI

Este é um aplicativo simples de linha de comando (CLI) para gerenciar tarefas. Você pode adicionar, atualizar, excluir e listar tarefas, além de alterar seus status para "em andamento" ou "concluído". As tarefas são salvas em um arquivo JSON no diretório atual.

# Recursos Principais

Adicionar, atualizar e excluir tarefas.

Alterar o status para "pendente", "em andamento" ou "concluído".

Listar tarefas filtrando por status ou exibir todas.

# Como Usar

Comandos Básicos

Adicionar Tarefa:

python task_cli.py add "Descrição da tarefa"

# Exemplo:

python task_cli.py add "Comprar pão"

# Atualizar Tarefa:

python task_cli.py update <ID> "Nova descrição"

# Excluir Tarefa:

python task_cli.py delete <ID>

# Alterar Status:

Em andamento:

python task_cli.py mark-in-progress <ID>

Concluído:

python task_cli.py mark-done <ID>

# Listar Tarefas:

Todas:

python task_cli.py list

Por status:

python task_cli.py list <status>

Substitua <status> por todo, in-progress ou done.

# Detalhes Técnicos

Estrutura de Dados

Cada tarefa segue este formato no arquivo tasks.json:

{
    "id": 1,
    "description": "Descrição da tarefa",
    "status": "todo",
    "createdAt": "2025-01-13T10:00:00",
    "updatedAt": "2025-01-13T10:00:00"
}

# Gerenciamento de Arquivo

O arquivo tasks.json será criado automaticamente no diretório atual.

Caso o arquivo seja corrompido, exclua-o para que um novo seja gerado.
