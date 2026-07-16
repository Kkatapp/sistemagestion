# transformar los datos
import pandas as pd
import config


def transform_patients(data):
    df = data.copy()
    df["arrival_date"] = pd.to_datetime(df["arrival_date"], format="%Y-%m-%d")
    df["departure_date"] = pd.to_datetime(df["departure_date"], format="%Y-%m-%d")
    df["arrival_week"] = df["arrival_date"].dt.isocalendar().week.astype(int)
    df["departure_week"] = df["departure_date"].dt.isocalendar().week.astype(int)
    df = df[["patient_id", "name", "arrival_date", "departure_date", "service", "satisfaction", "arrival_week", "departure_week"]]
    return df


def transform_services(data):
    df = data.copy()
    df["shift_id"] = range(1, len(df) + 1)
    df["shift_id"] = df["shift_id"].astype(str)
    return df


def transform_staff(data):
    df = data.copy()
    return df


def transform_schedule(data):
    df = data.copy()
    df = df[["week", "staff_id", "present"]]
    df.head()
    return df

