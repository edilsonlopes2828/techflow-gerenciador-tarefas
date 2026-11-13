# Registro de Alteração de Escopo — TechFlow

## 1. Descrição da alteração

Durante o desenvolvimento do sistema TechFlow, foi identificada a necessidade de permitir que os usuários editassem tarefas já cadastradas.

Inicialmente, o escopo previa o cadastro, a visualização, a conclusão e a exclusão de tarefas. Após analisar o funcionamento da aplicação, foi decidido ampliar o sistema com a funcionalidade de edição.

## 2. Justificativa

A alteração foi proposta para melhorar a experiência do usuário e oferecer maior flexibilidade na organização das tarefas.

Sem essa funcionalidade, caso uma tarefa fosse cadastrada com informações incorretas, seria necessário excluí-la e cadastrá-la novamente.

Com a edição, o usuário pode corrigir o título, a descrição e a prioridade sem perder o registro original da tarefa.

## 3. Impactos no projeto

A mudança exigiu:

- Implementação do método `update_task()` na classe `TaskManager`.
- Criação de uma rota para edição de tarefas no Flask.
- Adaptação da interface HTML.
- Criação de testes automatizados para validar a edição.
- Atualização da documentação do projeto.

## 4. Validação

A funcionalidade foi validada por meio de testes automatizados, incluindo a edição de tarefas, a rejeição de títulos vazios e a persistência das alterações no arquivo JSON.

Os sete testes automatizados existentes foram executados com sucesso.

## 5. Conclusão

A alteração de escopo contribuiu para tornar o TechFlow mais completo e funcional. A decisão demonstra a importância da adaptação durante o desenvolvimento ágil, permitindo incorporar melhorias identificadas ao longo do projeto.