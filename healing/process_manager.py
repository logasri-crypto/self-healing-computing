import psutil

def manage_processes():
    processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            if process.cpu_percent(interval=0.1) > 0:
                processes.append(process.info['name'])
        except:
            pass

    return processes