import sqlite3

def create_table():
    conn = sqlite3.connect("database/system.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpu REAL,
        ram REAL,
        disk REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_to_db(cpu, ram, disk, status):
    conn = sqlite3.connect("database/system.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO system_logs(cpu, ram, disk, status) VALUES (?, ?, ?, ?)",
        (cpu, ram, disk, status)
    )

    conn.commit()
    conn.close()