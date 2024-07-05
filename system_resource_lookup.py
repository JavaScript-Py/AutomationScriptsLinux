import psutil


def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_info.percent}%")
    print(f"Disk Usage: {disk_info.percent}%")


if __name__ == "__main__":
    monitor_system()
