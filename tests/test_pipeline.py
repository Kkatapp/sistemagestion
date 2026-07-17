import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from pipline.database import create_database
from config import DB_DIR, SCHEMA_PATH


def test_create_database_creates_sqlite_db_and_schema():
    create_database()
    assert DB_DIR.exists(), 'El directorio de la base de datos no se creó'
    db_path = DB_DIR / 'database.db'
    assert db_path.exists(), 'El archivo de la base de datos no se creó'
    assert SCHEMA_PATH.exists(), 'La ruta del esquema no existe'
