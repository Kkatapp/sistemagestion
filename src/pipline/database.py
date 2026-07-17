# Creación y administración del SQLite
import sqlite3
from pathlib import Path
from config import DB_DIR, SCHEMA_PATH


def get_connection():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_DIR / "database.db")


def delete_database():
    print("buenas")
    db_path = DB_DIR / "database.db"
    if db_path.exists():
        db_path.unlink()


def execute_script(script_path):
    with get_connection() as conn:
        with open(script_path, "r", encoding="utf-8") as f:
            script = f.read()
        conn.executescript(script)
        conn.commit()


def create_database():
    delete_database()
    execute_script(SCHEMA_PATH)

    with sqlite3.connect(DB_DIR / "database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(patients)")
        print(cursor.fetchall())

