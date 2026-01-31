import shutil

threshold = 10
total, used, free = shutil.disk_usage("/")

usage = int((used / total) * 100)

if usage > threshold:
    print(f"Disk usage high: {usage}%")