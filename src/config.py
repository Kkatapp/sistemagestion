#Configuración del proyecto

import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DB_DIR = PROJECT_ROOT / "db"
SCHEMA_PATH = PROJECT_ROOT / "db" / "scheme.sql"
