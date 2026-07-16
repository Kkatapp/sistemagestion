import pandas as pd
import config

def load_arch(filename):
    path = config.RAW_DATA_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"El archivo {filename} no existe en la ruta {path}")
    
    return pd.read_csv(path)


    