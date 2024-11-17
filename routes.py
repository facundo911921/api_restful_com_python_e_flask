"""Define as rotas da API"""
from flask import Blueprint, request, jsonify
from models import db, Task
from schemas import TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Blueprint serve para modularizar rotas, facilitando a organização e reutilização
routes = Blueprint('routes', __name__)

@routes.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    description = request.json.get('description', '')
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return task_schema.jsonify(task), 201

@routes.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return tasks_schema.jsonify(tasks), 200

@routes.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return task_schema.jsonify(task), 200

@routes.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    db.session.commit()
    return task_schema.jsonify(task), 200

@routes.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
