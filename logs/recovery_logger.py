import csv
from datetime import datetime

def save_recovery(action):

    file_name = "logs/recovery_log.csv"

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            action
        ])