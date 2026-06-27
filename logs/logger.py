import csv
from datetime import datetime

def save_log(cpu, ram, disk, status):

    file_name = "logs/system_log.csv"

    current_time = datetime.now()

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            current_time.date(),
            current_time.time(),
            cpu,
            ram,
            disk,
            status
        ])