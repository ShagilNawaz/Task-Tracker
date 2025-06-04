from flask import Blueprint, request, jsonify
from .models import Task, db

main = Blueprint("main", __name__)

@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks])

@main.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"id": new_task.id})