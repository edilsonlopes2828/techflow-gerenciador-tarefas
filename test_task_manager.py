
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


def test_editar_tarefa(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    tarefa = manager.add_task("Estudar Python")

    atualizada = manager.update_task(
        tarefa["id"],
        "Estudar Flask",
        "Aprender rotas e formulários",
        "Alta"
    )

    assert atualizada["title"] == "Estudar Flask"
    assert atualizada["description"] == "Aprender rotas e formulários"
    assert atualizada["priority"] == "Alta"


def test_impedir_edicao_com_titulo_vazio(tmp_path):
    manager = TaskManager(tmp_path / "tasks.json")
    tarefa = manager.add_task("Estudar Python")

    with pytest.raises(ValueError):
        manager.update_task(tarefa["id"], "   ")


def test_edicao_salva_no_arquivo(tmp_path):
    arquivo = tmp_path / "tasks.json"
    manager = TaskManager(arquivo)
    tarefa = manager.add_task("Tarefa original")

    manager.update_task(tarefa["id"], "Tarefa modificada")

    novo_manager = TaskManager(arquivo)

    assert novo_manager.list_tasks()[0]["title"] == "Tarefa modificada"
