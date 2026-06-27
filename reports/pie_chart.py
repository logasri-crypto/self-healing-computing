import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("database/system.db")

df = pd.read_sql_query(
    "SELECT * FROM system_logs ORDER BY id DESC LIMIT 1",
    conn
)

cpu = df["cpu"][0]
ram = df["ram"][0]
disk = df["disk"][0]

values = [cpu, ram, disk]
labels = ["CPU", "RAM", "Disk"]

plt.figure(figsize=(6,6))

plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("System Resource Usage")

plt.savefig("reports/pie_chart.png")

plt.show()