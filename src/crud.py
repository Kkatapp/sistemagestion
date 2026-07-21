import sqlite3
import config as config
import pandas as pd
import random
from pipline import database
import queries

def generate_id():
    while True:
        patient_id = f"PAT-{random.randint(10000000, 99999999)}"

        if patient_id not in queries.get_all_id_patients():
            return patient_id

def add_patient(patient_id, name_patient, last_name_patient, birth_date):
    query = "INSERT INTO patients (patient_id, name_patient, last_name_patient, birth_date) VALUES (?, ?, ?, ?)"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(patient_id, name_patient, last_name_patient, birth_date))
        conn.commit()


def add_ingreso_paciente(patient_id, service_id, arrival_date, departure_date, satisfaction):
    query = "INSERT INTO patients (patient_id, service_id, arrival_date, departure_date, satisfaction) VALUES (?, ?, ?, ?, ?)"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(patient_id, service_id, arrival_date, departure_date, satisfaction))
        conn.commit()
    

def update_patient(dato, valor):
    query = "UPDATE patients SET ? = ?"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(dato, valor))
        conn.commit()

def delete_patient(patient_id):
    query = "DELETE FROM patients WHERE patient_id = ? "
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(patient_id))
        conn.commit()

# Staff

def add_staff(staff_name, last_name_staff, role):
    query = "INSERT INTO patients (staff_id, staff_name, last_name_staff, role) VALUES (?, ?, ?, ?)"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(staff_name, last_name_staff, role))
        conn.commit()


def add_staff_attendance(staff_id, service_id, week, present, patient_satisfaction):
    query = "INSERT INTO patients (attendance_id, staff_id, service_id, week, present, patient_satisfaction) VALUES (?, ?, ?, ?, ?, ?)"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(staff_id, service_id, week, present, patient_satisfaction))
        conn.commit()
    

def update_staff(dato, valor):
    query = "UPDATE staff SET ? = ?"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(dato, valor))
        conn.commit()

def delete_staff(staff_id):
    query = "DELETE FROM staff WHERE patient_id = ? "
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(staff_id))
        conn.commit()

def update_staff_attendance(dato, valor):
    query = "UPDATE staff_attendance SET ? = ?"
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(dato, valor))
        conn.commit()

def delete_staff_attendance(staff_id):
    query = "DELETE FROM attandance WHERE patient_id = ? "
    with database.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query,(staff_id))
        conn.commit()

