# Creación y administración del SQLite
import sqlite3
from pathlib import Path
import config


def get_connection():
    config.DB_DIR.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(config.DB_DIR / "database.db")


def delete_database():
    db_path = config.DB_DIR / "database.db"
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
    execute_script(config.SCHEMA_PATH)

    with sqlite3.connect(config.DB_DIR / "database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA table_info(patients)")
        print(cursor.fetchall())

