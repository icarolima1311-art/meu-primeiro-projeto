# simple_task_manager/database.py
import sqlite3

DATABASE_NAME = "tasks.db"

def init_db():
    """
    Inicializa o banco de dados e cria a tabela 'tasks' se ela não existir.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    print("Banco de dados inicializado ou já existe.")

def create_task(description: str):
    """
    Cria uma nova tarefa no banco de dados.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "description": description, "completed": False}

def get_tasks():
    """
    Retorna todas as tarefas do banco de dados.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks ORDER BY id DESC")
    tasks = []
    for row in cursor.fetchall():
        tasks.append({"id": row[0], "description": row[1], "completed": bool(row[2])})
    conn.close()
    return tasks

def update_task_status(task_id: int, completed: bool):
    """
    Atualiza o status 'completed' de uma tarefa específica.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (1 if completed else 0, task_id))
    conn.commit()
    conn.close()
    
def delete_task(task_id: int):
    """
    Exclui uma tarefa do banco de dados.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
init_db()