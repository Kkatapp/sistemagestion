import sqlite3
import config as config
import pandas as pd
from pipline import database

# Queries de visualización

def get_patient(patient_id):
    print(patient_id)
    query = "SELECT * FROM patients WHERE patient_id = ?"
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(patient_id,))
    return df

def get_all_patients():
    query = "SELECT * FROM patients"
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_all_id_patients():
    query = "SELECT patient_id FROM patients"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df
    
def search_patient(name_patient,last_name_patient):
    query = "SELECT * FROM patients WHERE name_patient = ? AND last_name_patient = ? "
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(name_patient,last_name_patient))
    return df

def get_current_patients():
    query = "SELECT * FROM patients INNER JOIN ingreso_paciente ON patients.patient_id=ingreso_paciente.patient_id WHERE ingreso_paciente.departure_date IS NULL"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_discharged_patients():
    query = "SELECT * FROM patients INNER JOIN ingreso_paciente ON patients.patient_id=ingreso_paciente.patient_id WHERE ingreso_paciente.departure_date IS NOT NULL"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_patients_by_department(service_id):
    query = "SELECT * FROM patients INNER JOIN ingreso_paciente ON patients.patient_id=ingreso_paciente.patient_id WHERE service_id = ?"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(service_id))
    return df

def get_patients_this_week(start_date, end_date):
    query = "SELECT * FROM patients INNER JOIN ingreso_paciente ON patients.patient_id = ingreso_paciente.patient_id WHERE ingreso_paciente.arrival_date <= ? AND ( ingreso_paciente.departure_date >= ? OR ingreso_paciente.departure_date IS NULL)"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    return df

def count_patients():
    query = "SELECT COUNT(patient_id) AS [Número de pacientes] FROM patients "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

# Para staff
def get_staff(staff_id):
    query = "SELECT * FROM staff WHERE staff_id = ?"
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(staff_id))
    return df

def get_all_staff():
    query = "SELECT * FROM staff"
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def search_staff(staff_name, last_name_staff):
    query = "SELECT * FROM staff WHERE staff_name = ? AND last_name_staff = ? "
    
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(staff_name,last_name_staff))
    return df

def get_staff_by_departament(service_id):
    query = "SELECT * FROM staff INNER JOIN staff_attendance ON staff.staff_id=staff_attendance.staff_id WHERE service_id = ? "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(service_id))
    return df

def get_doctors():
    query = "SELECT * FROM staff WHERE role = doctor "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_nurses():
    query = "SELECT * FROM staff WHERE role = nurse "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def count_staff():
    query = "SELECT staff, COUNT(staff_id) AS [Número de staff] FROM staff "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def count_staff_this_week(week):
    query = "SELECT COUNT(staff_id) AS [Número de staff está semana] FROM staff INNER JOIN staff_attendance ON staff.staff_id=staff_attendance.staff_id WHERE week = ?"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(week))
    return df

# Sobre los horarios de los empleados
def get_staff_schedule(staff_id):
    query = "SELECT * FROM staff_attendance WHERE staff_id =? "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(staff_id))
    return df

def get_attendance_by_week(week):
    query = "SELECT * FROM staff INNER JOIN staff_attendance ON staff.staff_id=staff_attendance.staff_id WHERE week = ?"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(week))
    return df

def get_absent_staff():
    query = "SELECT * FROM staff INNER JOIN staff_attendance ON staff.staff_id=staff_attendance.staff_id WHERE present = 0 ORDER BY week ASC"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_low_attendance():
    query = " SELECT TOP 3 staff.staff_name, staff.last_name_staff, COUNT(staff_name) FROM staff INNER JOIN staff_attendance ON staff.staff_id=staff_attendance.staff_id WHERE present = 0 ORDER BY COUNT(staff_name) ASC "
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def get_schedule_by_department(service_id):
    query = "SELECT * FROM staff_attendance WHERE service_id =?"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn, params=(service_id))
    return df

# Para los departamentos

def get_departments():
    query = "SELECT departament FROM departament"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def patients_per_department():
    query = "SELECT department.department, COUNT(ingreso_paciente.patient_id) FROM department INNER JOIN ingreso_paciente ON ingreso_paciente.service_id = department.service_id"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df

def staff_per_departament():
    query = "SELECT department.department, COUNT(staff_attendance.staff_id) FROM department INNER JOIN staff_attendance ON staff_attendance.service_id = department.service_id"
    with database.get_connection() as conn:
        df = pd.read_sql_query(query, conn)
    return df