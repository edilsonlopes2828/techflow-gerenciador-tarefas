
import pytest
from task_manager import TaskManager


def test_adicionar_tarefa(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")

    tarefa = manager.add_task(
        "Estudar Python",
        "Revisar os fundamentos",
        "Alta"
    )

    assert tarefa["title"] == "Estudar Python"
    assert tarefa["priority"] == "Alta"
    assert tarefa["completed"] is False


def test_impedir_titulo_vazio(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")

    with pytest.raises(ValueError):
        manager.add_task("   ")


def test_concluir_tarefa(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    tarefa = manager.add_task("Fazer atividade")

    manager.toggle_task(tarefa["id"])

    assert manager.list_tasks("completed")[0]["title"] == "Fazer atividade"


def test_excluir_tarefa(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    tarefa = manager.add_task("Tarefa temporária")

    manager.delete_task(tarefa["id"])

    assert manager.list_tasks() == []
