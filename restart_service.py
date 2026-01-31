import subprocess

service = "httpd"

status = subprocess.run(
    ["systemctl", "is-active", service], 
    capture_output=True,
    text=True
    ).stdout.strip()

if status != "active":
    subprocess.run(["systemctl", "restart", service])
