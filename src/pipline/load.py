# Subir los datos de un dataframe a una base de datos

import sqlite3
import config as config

def insert_data(dataframe, table_name):
    try:
        with sqlite3.connect(config.DB_DIR / "database.db") as conn:
            dataframe.to_sql(table_name, conn, if_exists="append", index=False)
            conn.commit()
            
    except Exception as e:
        print(f"Error al insertar en {table_name}: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise