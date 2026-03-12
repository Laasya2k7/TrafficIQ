import sqlite3

DB_PATH = "C:/Users/JAYARAM/Desktop/TrafficIQ/notebooks/traffic.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def insert_prediction(data, prediction):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO traffic_predictions 
    (junction, year, month, day, hour, dayofweek, predicted_traffic)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    cursor.execute(query, (
        data["Junction"],
        data["Year"],
        data["Month"],
        data["Day"],
        data["Hour"],
        data["Dayofweek"],
        prediction
    ))

    conn.commit()
    conn.close()