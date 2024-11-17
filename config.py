"""Configuração do Banco de dados"""
import os

# Definir o local do arquivo
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Definir a classe responsável pela configuração do Banco de dados
class Config:
    # Define o local/URL de conexão com o Banco de dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    # Desativa o sistema de notificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
Separando a configuração do Banco de dados em um arquivo individual, facilita a troca para o outro Banco de dados.
Se quiser trocar para PostgreSQL, por exemplo, basta usar o código:
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
"""