CREATE TABLE IF NOT EXISTS traffic_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    junction INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    dayofweek INTEGER,
    predicted_traffic REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);