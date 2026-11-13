
from flask import Flask, render_template, request, redirect, url_for, flash
from task_manager import TaskManager

app = Flask(__name__)
app.secret_key = "techflow-dev"
manager = TaskManager("tasks.json")


@app.get("/")
def index():
    status = request.args.get("status", "all")
    tasks = manager.list_tasks(status)
    return render_template("index.html", tasks=tasks, status=status)


@app.post("/tasks")
def create_task():
    title = request.form.get("title", "")
    description = request.form.get("description", "")
    priority = request.form.get("priority", "Média")

    try:
        manager.add_task(title, description, priority)
        flash("Tarefa criada com sucesso!", "success")
    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/edit")
def edit_task(task_id):
    title = request.form.get("title", "")
    description = request.form.get("description", "")
    priority = request.form.get("priority", "Média")

    try:
        manager.update_task(task_id, title, description, priority)
        flash("Tarefa atualizada com sucesso!", "success")
    except (ValueError, KeyError) as error:
        flash(str(error), "error")

    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/toggle")
def toggle_task(task_id):
    try:
        manager.toggle_task(task_id)
    except KeyError:
        flash("Tarefa não encontrada.", "error")

    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/delete")
def delete_task(task_id):
    try:
        manager.delete_task(task_id)
        flash("Tarefa excluída com sucesso!", "success")
    except KeyError:
        flash("Tarefa não encontrada.", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
