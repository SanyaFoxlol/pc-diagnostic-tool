import psutil
import platform
import time
import os

print("System:", platform.system())
print("CPU cores:", psutil.cpu_count())

while True:
    os.system("cls")  # очищає консоль (Windows)

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = ram.percent

    disk = psutil.disk_usage('C:/').percent

    print("=== SYSTEM MONITOR ===\n")

    print("CPU usage:", cpu, "%")
    print("RAM usage:", ram_used, "%")
    print("Disk usage:", disk, "%")

    print("\nUpdating every second...")