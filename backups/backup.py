import shutil
import os
from datetime import datetime

def create_backup():

    source = "logs/system_log.csv"

    if os.path.exists(source):

        backup_name = (
            "backups/backup_"
            + datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".csv"
        )

        shutil.copy(source, backup_name)

        return backup_name

    return "No Log File Found"