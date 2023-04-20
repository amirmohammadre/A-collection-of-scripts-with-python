import platform
import psutil


def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor



# print System Information
print("System Information".center(100, "="))

uname = platform.uname()

print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")



# print CPU information
print("CPU Info".center(100, "="))

print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

print(f"Total CPU Usage: {psutil.cpu_percent()}%")



# print Memory Information
print("Memory Information".center(100, "="))

svmem = psutil.virtual_memory()

print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")



