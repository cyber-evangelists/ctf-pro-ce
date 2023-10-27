import subprocess
import sys
import os
    
def ping_me(host):
    if sys.platform.startswith("linux"):
        command = f"ping -c 3 {host}"
    elif os.name == "nt":
        command = f"ping -n 3 {host}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.stdout:
        output = result.stdout
        return output
    else:
        error_message = result.stderr
        return error_message

# x = ping_me("google.com")
# print(x)