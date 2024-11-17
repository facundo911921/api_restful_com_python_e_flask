"""Arquivo principal"""
from flask import Flask
from models import db
from schemas import ma
from routes import routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
app.register_blueprint(routes)

# Inicializar o banco de dados
@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
