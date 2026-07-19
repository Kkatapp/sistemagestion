from . import database
from . import extract
from . import load
from . import transform

import config

def run_pipeline():
    print("Iniciando proceso de pipline")
    #base de datos
    try:
        print("Creando base de datos")
        database.create_database()
        print("Base de datos creada exitosamente")
    except Exception as e:
        print ("Falló la creación de la base de datos {e}")
        
    # Correción de formato
    print("Iniciar la correción del formato de datos")
    
    try:
        print("Corrigiendo patients")
        patients = extract.load_arch("patients.csv")
        patients = transform.correction_patient_type(patients)
        print("Corrigiendo staff")
        staff = extract.load_arch("staff.csv")
        staff = transform.correction_staff_type(staff)
        print("Correción terminada")
    except Exception as e:
        print(f"No de logró hacer las correciones {e}")
    
    
    # Creación de la tabla de departametnos
    try:
        departaments = transform.create_table_departments(staff)
        load.insert_data(departaments, "departament")
    except Exception as e:
        print(f"No se pudo crear Departaments {e}")
    
    # Mapeo de departamentos
    maps_id = departaments.set_index("departament")["service_id"]
        
    # Creación de la tabla de infreso_pacientes
    try:
        ingreso_paciente = transform.create_table_ingreso(patients, maps_id) 
        load.insert_data(ingreso_paciente, "ingreso_paciente")
    except Exception as e:
        print(f"No se pudo crear la tabla ingreso de pacientes {e}")
        
    # Corrección de tabla de pacientes 
    try:
        correction_patients = transform.correction_patients(patients)
        load.insert_data(correction_patients, "patients")
    except Exception as e:
        print(f"No se puede hacer la correción de la tabla de paciente {e}")
    
    # Convertir tabla de service a operational_shift
    try:
        operational_shift = extract.load_arch("services_weekly.csv")
        operational_shift = transform.correction_service(maps_id,operational_shift)
        load.insert_data(operational_shift, "operational_shift")
    except Exception as e:
        print(f"No se puede convertir operational_shift {e}")
        
    # Convertir la tabla de schedule
    try:
        staff_attendence = extract.load_arch("staff_schedule.csv")
        staff_attedence = transform.correction_schudele(maps_id, staff_attendence)
        load.insert_data(staff_attedence, "staff_attendance")
    except Exception as e:
        print(f"No de puese convertir la tabla de schedule {e}")
    
    # Corregir staff
    try: 
        staff = transform.correction_staff(staff)
        load.insert_data(staff, "staff")
    except Exception as e:
        print(f"No se puede convertir la tabal de staff {e}")
    
    print("Se logro hacer el pipline")