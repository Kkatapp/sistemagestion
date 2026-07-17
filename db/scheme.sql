CREATE TABLE IF NOT EXISTS departament (
    service_id VARCHAR(50) PRIMARY KEY,
    service_name TEXT
);

CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR(50) PRIMARY KEY,
    name_patient TEXT,
    last_name_patient TEXT,
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS ingreso_paciente (
    ingreso_id VARCHAR(50) PRIMARY KEY,
    patient_id TEXT,
    service_id TEXT,
    arrivale_date DATE,
    depature_date DATE,
    satisfaction INTEGER CHECK (satisfaction >= 0 AND satisfaction <= 100),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id VARCHAR(50) PRIMARY KEY,
    name_staff TEXT,
    last_name_staff TEXT,
    role TEXT
);

CREATE TABLE IF NOT EXISTS staff_attendance (
    attendance_id VARCHAR(50) PRIMARY KEY,
    staff_id TEXT,
    service_id TEXT,
    week INTEGER,
    present BOOLEAN,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);

CREATE TABLE IF NOT EXISTS operational_shift (
    shift_id VARCHAR(50) PRIMARY KEY,
    service_id TEXT,
    week INTEGER,
    available_beds INTEGER,
    patients_request INTEGER,
    patients_admitted INTEGER,
    patients_refused INTEGER,
    patients_satisfaction INTEGER,
    staff_morale INTEGER,
    event TEXT,
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);