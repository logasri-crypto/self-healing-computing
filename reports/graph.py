import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("database/system.db")

query = "SELECT * FROM system_logs"
df = pd.read_sql_query(query, conn)

conn.close()

print(df)

plt.figure(figsize=(10,5))
plt.plot(df["cpu"], label="CPU Usage")
plt.plot(df["ram"], label="RAM Usage")
plt.plot(df["disk"], label="Disk Usage")

plt.title("System Resource Usage")
plt.xlabel("Records")
plt.ylabel("Usage (%)")
plt.legend()

plt.savefig("reports/system_graph.png")
plt.savefig("reports/system_graph.png")