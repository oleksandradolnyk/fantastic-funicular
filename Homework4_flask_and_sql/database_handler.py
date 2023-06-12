import sqlite3

def execute_query(query):
    with sqlite3.connect('database/chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    return data

def formatting_data(keys, data):
    formatted_data = [dict(zip(keys, item)) for item in data]
    return formatted_data