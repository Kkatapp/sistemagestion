CREATE TABLE IF NOT EXISTS departament (
    service_id VARCHAR(50) PRIMARY KEY,
    departament TEXT
);

CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR(50) PRIMARY KEY,
    name_patient TEXT,
    last_name_patient TEXT,
    birth_date DATE
);

CREATE TABLE IF NOT EXISTS ingreso_paciente (
    ingreso_id VARCHAR(50) PRIMARY KEY AUTO_INCREMENT,
    patient_id TEXT,
    service_id TEXT,
    arrival_date DATE,
    departure_date DATE,
    satisfaction INTEGER CHECK (satisfaction >= 0 AND satisfaction <= 100),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id VARCHAR(50) PRIMARY KEY,
    staff_name TEXT,
    last_name_staff TEXT,
    role TEXT
);

CREATE TABLE IF NOT EXISTS staff_attendance (
    attendance_id VARCHAR(50) PRIMARY KEY AUTO_INCREMENT,
    staff_id TEXT,
    service_id TEXT,
    week INTEGER,
    present BOOLEAN,
    patient_satisfaction INTEGER,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);

CREATE TABLE IF NOT EXISTS operational_shift (
    shift_id VARCHAR(50) PRIMARY KEY AUTO_INCREMENT,
    service_id TEXT,
    week INTEGER,
    available_beds INTEGER,
    patients_request INTEGER,
    patients_admitted INTEGER,
    patients_refused INTEGER,
    patient_satisfaction INTEGER,
    staff_morale INTEGER,
    event TEXT,
    FOREIGN KEY (service_id) REFERENCES departament(service_id)
);