import psutil
import platform
import socket
import time
import sys

def bar(percent):
    length = 20
    filled = int(length * percent / 100)
    return "█" * filled + "░" * (length - filled)

system = platform.system()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("===== SYSTEM MONITOR =====\n")

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:/').percent

    output = f"""
System: {system}
Host: {hostname}
IP: {ip}

CPU :  {bar(cpu)} {cpu}%
RAM :  {bar(ram)} {ram}%
DISK:  {bar(disk)} {disk}%
"""

    sys.stdout.write("\033[H\033[J")  # очищає екран
    sys.stdout.write("===== SYSTEM MONITOR =====")
    sys.stdout.write(output)
    sys.stdout.flush()

    time.sleep(1)