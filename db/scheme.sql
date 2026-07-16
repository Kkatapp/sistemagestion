CREATE TABLE IF NOT EXISTS staff (
    staff_id TEXT PRIMARY KEY,
    staff_name TEXT,
    role TEXT,
    service TEXT
);

CREATE TABLE IF NOT EXISTS schedule (
    week INTEGER,
    staff_id TEXT,
    present INTEGER,
    PRIMARY KEY (week, staff_id)
);

CREATE TABLE IF NOT EXISTS patients (
    patient_id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    arrival_date DATE,
    departure_date DATE,
    service TEXT,
    satisfaction INTEGER,
    arrival_week INTEGER,
    departure_week INTEGER
);

CREATE TABLE IF NOT EXISTS shifts (
    shift_id TEXT PRIMARY KEY,
    week INTEGER,
    month INTEGER,
    service TEXT,
    event TEXT,
    available_beds INTEGER,
    patients_request INTEGER,
    patients_admitted INTEGER,
    patients_refused INTEGER,
    patient_satisfaction INTEGER,
    staff_morale INTEGER
);