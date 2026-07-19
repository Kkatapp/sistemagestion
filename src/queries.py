import sqlite3
import config as config
import pandas as pd

# Consultas básicas

def get_patient(patient_id):
    query = "SELECT * FROM patients WHERE patient_id = ?"
    
    with sqlite3.connect(config.DB_DIR / "database.db") as conn:
        df = pd.read_sql_query(query, conn, params=(patient_id,))

    return df

