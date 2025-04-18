CREATE TABLE IF NOT EXISTS transport (
    route TEXT NOT NULL,            
    driver_name TEXT NOT NULL,     
    departure_date TEXT NOT NULL,
    arrival_date TEXT NOT NULL, 
    cargo_weight REAL NOT NULL
)