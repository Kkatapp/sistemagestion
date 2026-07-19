import pandas as pd

# Quitar -PAT de patients y convertir arraviel_date y deperture_date a tipo DATE

def correction_patient_type(patients):
    patients['patient_id'] = patients['patient_id'].str.replace('PAT-', '', regex=False)
    patients['arrival_date'] = pd.to_datetime(patients['arrival_date'])
    patients['departure_date'] = pd.to_datetime(patients['departure_date'])
    patients.info()
    return patients

# Quitar -STF de staff
def correction_staff_type(staff):
    staff['staff_id'] = staff['staff_id'].str.replace('STAF-', '')
    staff.info()
    return staff

# Crear del table de departaments
def create_table_departments(staff):
    departaments = pd.DataFrame({
    "departament": staff["service"].unique()  
    })
    departaments.insert(0, 'service_id', range(1, len(departaments) + 1))
    departaments.info()
    return departaments

# Crear la tabla de ingreso_pacientes
def create_table_ingreso(patients, maps_id):
    ingreso_paciente = patients.copy()
    ingreso_paciente.drop(columns=["name","age"], inplace=True)
    ingreso_paciente.insert(0, 'ingreso_id', range(1, len(ingreso_paciente) + 1))
    ingreso_paciente["service"] = ingreso_paciente["service"].map(maps_id)
    ingreso_paciente.rename(columns={"service":"service_id"}, inplace=True)
    ingreso_paciente.info()
    return ingreso_paciente

# Corregir la tabla patients
def correction_patients(patients):
    patients[["name_patient", "last_name_patient"]] = patients["name"].str.split(" ", n=1, expand=True)
    patients.drop(columns=["name"], inplace=True)
    patients.drop(columns=["arrival_date"], inplace=True)
    patients.drop(columns=["departure_date"], inplace=True)
    patients.drop(columns=["service"], inplace=True)
    patients.drop(columns=["satisfaction"], inplace=True)
    mes_fijado = "-04-10"
    nacimiento = (2025 - patients["age"]).astype(str) + mes_fijado
    patients["birth_date"] = pd.to_datetime(nacimiento)
    patients.drop(columns=["age"], inplace=True)
    patients.info()
    return patients
    
# Corregior la tabla service -> operational_shift 
def correction_service(maps_id,service):
    operational_shift = service.copy()
    operational_shift.insert(0, 'shift_id', range(1, len(operational_shift) + 1))
    operational_shift["service"] = operational_shift["service"].map(maps_id)
    operational_shift.rename(columns={"service":"service_id"}, inplace=True)
    operational_shift.drop(columns=["month"], inplace=True)
    operational_shift.info()
    return operational_shift

# Corregir la tabla de shudele ->Staff_attandance 
def correction_schudele(maps_id, schedule):
    # 5. Utilizar la tabla de schudele como "Staff_attendence" con asistencia_id, week, staff:id, departament_id y present. Dejar staff solamente con Staff_id, staff_name, staff_last_name, role
    staff_attendance = schedule.copy()
    staff_attendance['staff_id'] = staff_attendance['staff_id'].str.replace('STF-', '', regex=False)
    staff_attendance["service"] = staff_attendance["service"].map(maps_id)
    staff_attendance.rename(columns={"service":"service_id"}, inplace=True)
    staff_attendance.drop(columns=["staff_name", "role"], inplace=True)
    staff_attendance.insert(0, 'attendance_id', range(1, len(staff_attendance) + 1))
    staff_attendance.info()
    return staff_attendance

# Corregir Staff
def correction_staff(staff):
    staff['staff_id'] = staff['staff_id'].str.replace('STF-', '', regex=False)
    staff.drop(columns=["service"], inplace=True)
    staff[["staff_name", "last_name_staff"]] = staff["staff_name"].str.split(" ", n=1, expand=True)
    staff.info()
    return staff








