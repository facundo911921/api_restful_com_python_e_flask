"""Definição do banco de dados"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável pela criação e estrutura do Banco de dados. SQLAlchemy permite representar Bancos de dados como classes
# Cada classe representa uma tabela no Banco de dados
class Task(db.Model):
    # Cada atributo da classe representa uma coluna na tabela
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    done = db.Column(db.Boolean, default=False)

