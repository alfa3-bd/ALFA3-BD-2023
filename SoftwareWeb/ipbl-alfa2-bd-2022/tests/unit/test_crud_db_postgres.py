import pytest
import psycopg2
from psycopg2 import Error


def create_connection():
    """Cria uma conexão com o banco de dados PostgreSQL"""
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="core",
            user="root",
            password="root"
        )
        print("Conexão com o PostgreSQL estabelecida com sucesso")
        return connection
    except Error as e:
        print(f"Ocorreu um erro ao conectar-se ao PostgreSQL: {e}")


def close_connection(connection):
    """Fecha a conexão com o banco de dados"""
    if connection:
        connection.close()
        print("Conexão com o PostgreSQL fechada com sucesso")

print(f"Ocorreu um erro ao criar a tabela")


def insert_frase(connection, frase, tipo):
    """Insere uma nova frase no banco de dados"""
    insert_query = "INSERT INTO frase (fra_frase, tip_frase) VALUES (%s, %s);"
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, (frase, tipo))
        connection.commit()
        print("Frase inserida com sucesso")
    except Error as e:
        print(f"Ocorreu um erro ao inserir a frase: {e}")


def get_all_frases(connection):
    """Retorna todas as frases cadastradas no banco de dados"""
    select_query = "SELECT * FROM frase;"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Frase: {row[1]}, Tipo: {row[2]}")
    except Error as e:
        print(f"Ocorreu um erro ao buscar as frases: {e}")


def update_frase(connection, fra_id, nova_frase):
    """Atualiza a frase de uma determinada ID"""
    update_query = "UPDATE frase SET fra_frase = %s WHERE fra_id = %s;"
    try:
        cursor = connection.cursor()
        cursor.execute(update_query, (nova_frase, fra_id))
        connection.commit()
        print("Frase atualizada com sucesso")
    except Error as e:
        print(f"Ocorreu um erro ao atualizar a frase: {e}")


def delete_frase(connection, fra_id):
    """Deleta uma frase pelo ID"""
    delete_query = "DELETE FROM frase WHERE fra_id = %s;"
    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, (fra_id,))
        connection.commit()
        print("Frase deletada com sucesso")
    except Error as e:
        print(f"Ocorreu um erro ao deletar a frase: {e}")


# Exemplo de uso
connection = create_connection()
@pytest.fixture(scope="module")
def test_connection():
    """Cria e retorna uma conexão com o banco de dados para os testes"""
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="core",
            user="root",
            password="root"
        )
        print("Conexão com o PostgreSQL estabelecida com sucesso")
        yield connection
    finally:
        if connection:
            connection.close()
            print("Conexão com o PostgreSQL fechada com sucesso")

def test_insert_frase(test_connection):
    """Testa a inserção de frases"""
    insert_frase(test_connection, "Exemplo de frase 1", 1)
    insert_frase(test_connection, "Exemplo de frase 2", 2)


def test_get_all_frases(test_connection):
    """Testa a obtenção de todas as frases"""
    get_all_frases(test_connection)


def test_update_frase(test_connection):
    """Testa a atualização de uma frase"""
    update_frase(test_connection, 1, "Nova frase")


def test_delete_frase(test_connection):
    """Testa a exclusão de uma frase"""
    delete_frase(test_connection, 2)