import psutil
import platform

print("System:", platform.system())
print("CPU cores:", psutil.cpu_count())

ram = psutil.virtual_memory().total / (1024**3)
print("RAM:", round(ram, 2), "GB")

disk = psutil.disk_usage('C:/').percent
print("Disk:", disk, "% used")