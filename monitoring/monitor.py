import psutil
import platform

def get_system_info():

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu < 70:
        status = "Healthy"
    elif cpu < 90:
        status = "Warning"
    else:
        status = "Critical"

    return {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "status": status,
 "os": platform.system(),

"processor": platform.processor(),

"machine": platform.machine(),

"python": platform.python_version(),
    }