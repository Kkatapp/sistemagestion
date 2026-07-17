from pipline.database import create_database
from pipline.extract import load_arch
from pipline.transform import (
    transform_patients,
    transform_services,
    transform_staff,
    transform_schedule,
)
from pipline.load import insert_data
import config


def run_pipeline():
    print("hello")
    try:
        print("Creando base de datos...")
        create_database()
        print("Base de datos creada exitosamente")

        print("Cargando y procesando pacientes...")
        patients = load_arch("patients.csv")
        patients = transform_patients(patients)
        insert_data(patients, "patients")
        
        print("Cargando y procesando staff...")
        staff = load_arch("staff.csv")
        staff = transform_staff(staff)
        insert_data(staff, "staff")

        print("Cargando y procesando servicios...")
        services = load_arch("services_weekly.csv")
        services = transform_services(services)
        insert_data(services, "shifts")

        print("Cargando y procesando horarios...")
        schedule = load_arch("staff_schedule.csv")
        schedule = transform_schedule(schedule)
        insert_data(schedule, "schedule")

        print("Pipeline completado exitosamente!")
    except Exception as e:
        print(f"Error en el pipeline: {e}")
    
