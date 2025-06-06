# Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
# содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
# водителя, даты отправки и прибытия, масса груза.

import sqlite3

conn = sqlite3.connect("transport.db")
cursor = conn.cursor()

data = """
CREATE TABLE IF NOT EXISTS transport (
    route TEXT NOT NULL,            
    driver_name TEXT NOT NULL,     
    departure_date TEXT NOT NULL,
    arrival_date TEXT NOT NULL, 
    cargo_weight REAL NOT NULL
)
"""

cursor.execute(data)
conn.commit()

# cursor.execute("sql запрос")
# в конце conn.commit() для сохранения изменений после выполненного запроса

def add():
    cursor.execute("INSERT INTO transport VALUES (?, ?, ?, ?, ?)", (V1, V2, V3, V4, V5))
    conn.commit()
def edit():
    cursor.execute("INSERT INTO transport VALUES (?, ?, ?, ?, ?)", (V1, V2, V3, V4, V5))
    conn.commit()
def delete():
    cursor.execute("INSERT INTO transport VALUES (?, ?, ?, ?, ?)", (V1, V2, V3, V4, V5))
    conn.commit()

print(cursor.execute("SELECT * FROM transport").fetchall())

conn.close()