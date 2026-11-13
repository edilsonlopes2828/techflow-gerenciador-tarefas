# TechFlow — Gerenciador de Tarefas

Sistema web de gerenciamento de tarefas desenvolvido em Python com Flask, como parte de um projeto acadêmico de gestão ágil e controle de qualidade.

## Sobre o projeto

O TechFlow é uma aplicação que permite organizar tarefas de maneira simples e prática, acompanhando suas prioridades e seu andamento.

## Funcionalidades

- Cadastrar novas tarefas.
- Listar tarefas cadastradas.
- Editar título, descrição e prioridade.
- Excluir tarefas.
- Marcar tarefas como concluídas ou pendentes.
- Filtrar tarefas.
- Armazenar dados em arquivo JSON.
- Executar testes automatizados com Pytest.

## Tecnologias utilizadas

- Python
- Flask
- HTML
- CSS
- Pytest
- Git e GitHub
- GitHub Actions

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/edilsonlopes2828/techflow-gerenciador-tarefas.git
```

### 2. Entrar na pasta

```bash
cd techflow-gerenciador-tarefas
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

Acesse no navegador:

http://127.0.0.1:5000

## Como executar os testes

Com o projeto aberto no terminal, execute:

```bash
pytest
```

Os testes verificam operações de cadastro, edição, exclusão e atualização de tarefas.

## Estrutura do projeto

```text
techflow-gerenciador-tarefas/
│
├── app.py
├── task_manager.py
├── test_task_manager.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── .github/
    └── workflows/
        └── tests.yml
```

## Qualidade e integração contínua

O projeto possui testes automatizados utilizando Pytest e configuração de integração contínua por meio do GitHub Actions.

## Objetivo acadêmico

Aplicar conceitos de metodologia ágil, gerenciamento de tarefas, controle de versão, testes automatizados e melhoria contínua no desenvolvimento de software.