from codigo4 import *
import requests
import pytest
import sqlite3
from bd4 import *


def test_get_data():
    # Fazendo uma requisição GET para o endpoint '/api/data'
    response = requests.get('http://127.0.0.1:5000/api/data')

    # Verificando o status code da resposta
    assert response.status_code == 200

    # Verificando se a resposta JSON contém a chave 'message'
    data = response.json()
    assert 'message' in data
    assert data['message'] == "Cuzinho!"

def test_post_data():
    # Dados que queremos enviar no corpo da requisição POST
    payload = {"name": "Jão", "age": 30}

    # Fazendo uma requisição POST para o endpoint '/api/data'
    response = requests.post('http://127.0.0.1:5000/api/data', json=payload)

    # Verificando o status code da resposta
    assert response.status_code == 201

    # Verificando se a resposta JSON contém os dados recebidos
    data = response.json()
    assert 'received' in data
    assert data['received'] == payload

@pytest.fixture
def db_connection():
    connection = create_connection()
    create_table(connection)
    yield connection
    connection.close()

# Testes que utilizam a fixture
def test_add_user(db_connection):
    add_user(db_connection, "Alice", 30)
    users = get_all_users(db_connection)
    assert len(users) == 1
    assert users[0]["name"] == "Alice"
    assert users[0]["age"] == 30

def test_update_user_age(db_connection):
    add_user(db_connection, "Bob", 25)
    users = get_all_users(db_connection)
    user_id = users[0]["id"]
    update_user_age(db_connection, user_id, 26)
    users = get_all_users(db_connection)
    assert users[0]["age"] == 26

def test_delete_user(db_connection):
    add_user(db_connection, "Charlie", 40)
    users = get_all_users(db_connection)
    user_id = users[0]["id"]
    delete_user(db_connection, user_id)
    users = get_all_users(db_connection)
    assert len(users) == 0

def test_get_all_users_empty(db_connection):
    users = get_all_users(db_connection)
    assert len(users) == 0