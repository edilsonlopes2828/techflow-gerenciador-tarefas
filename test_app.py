import pytest
import app as app_module
from task_manager import TaskManager


@pytest.fixture
def client(tmp_path):
    app_module.manager = TaskManager(tmp_path / "tasks.json")
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    response = client.get("/")

    assert response.status_code == 200


def test_cadastrar_tarefa_pela_rota(client):
    response = client.post(
        "/tasks",
        data={
            "title": "Estudar Flask",
            "description": "Praticar testes",
            "priority": "Média"
        }
    )

    assert response.status_code == 302
    assert len(app_module.manager.list_tasks()) == 1
    assert app_module.manager.list_tasks()[0]["title"] == "Estudar Flask"


def test_editar_tarefa_pela_rota(client):
    tarefa = app_module.manager.add_task("Tarefa antiga")

    response = client.post(
        f"/tasks/{tarefa['id']}/edit",
        data={
            "title": "Tarefa atualizada",
            "description": "Descrição nova",
            "priority": "Média"
        }
    )

    assert response.status_code == 302
    assert app_module.manager.list_tasks()[0]["title"] == "Tarefa atualizada"


def test_concluir_tarefa_pela_rota(client):
    tarefa = app_module.manager.add_task("Concluir atividade")

    response = client.post(f"/tasks/{tarefa['id']}/toggle")

    assert response.status_code == 302
    assert len(app_module.manager.list_tasks("completed")) == 1


def test_excluir_tarefa_pela_rota(client):
    tarefa = app_module.manager.add_task("Excluir atividade")

    response = client.post(f"/tasks/{tarefa['id']}/delete")

    assert response.status_code == 302
    assert app_module.manager.list_tasks() == []