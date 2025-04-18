# Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
# содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
# водителя, даты отправки и прибытия, масса груза.

import sqlite3

conn = sqlite3.connect("transport.db")

def execute_sql_from_file(conn, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        cursor = conn.cursor()
        cursor.execute(sql_script)
        conn.commit()

execute_sql_from_file(conn, 'code.sql')
conn.close()