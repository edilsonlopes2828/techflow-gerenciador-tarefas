# Diagrama UML de Casos de Uso — TechFlow

## Objetivo

Representar as funcionalidades disponíveis no sistema de gerenciamento de tarefas TechFlow e a interação do usuário com a aplicação.

## Diagrama

```mermaid
flowchart LR
    U["👤 Usuário"]

    subgraph Sistema["Sistema TechFlow"]
        A(["Cadastrar tarefa"])
        B(["Visualizar tarefas"])
        C(["Editar tarefa"])
        D(["Concluir tarefa"])
        E(["Excluir tarefa"])
        F(["Filtrar tarefas"])
    end

    U --- A
    U --- B
    U --- C
    U --- D
    U --- E
    U --- F