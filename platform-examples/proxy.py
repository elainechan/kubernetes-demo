# TODO: refactor to functions
"""
Creates proxy for running pod.
Deletes proxy after running pod.

If a proxy is not set up, you will get MaxRetryError
when runing the pod creation scripts.
https://stackoverflow.com/questions/55742540/kubernetes-python-client-connection-issue
"""

import os
from subprocess import run, Popen, getoutput, PIPE, TimeoutExpired
from time import sleep


# Get sudo password from environment
SUDO_PASSWORD = os.getenv("SUDO_PASSWORD")
encoded_password = SUDO_PASSWORD.encode()

# Start proxy
def start_proxy():
    pass

create_process = Popen(["sudo", "-S", "kubectl", "proxy", "--port", "8001"],
                        stdin=PIPE, stdout=PIPE, stderr=PIPE)
try:
    outs, errs = create_process.communicate(encoded_password, timeout=15)
except TimeoutExpired:
    create_process.kill()
    create_process.communicate(encoded_password)

print("###### Proxy has been created ")

# https://www.unix.com/unix-for-dummies-questions-and-answers/38566-need-get-pid-process-have-store-pid-variable.html

# Inspect process to verify proxy has been started
process_info = getoutput("ps aux | grep 'kubectl proxy --port 8001'")
print(f"##### process: {process_info}")

# Get PIDs of proxy processes
# Note that running a proxy with sudo spawns two processes
# with two different PIDs
def get_pids():
    pass

sudo_pid = getoutput("ps aux | grep 'sudo -S kubectl proxy --port 8001' | grep -v grep | awk '{print $2}'")
second_pid = getoutput("ps aux | grep 'kubectl proxy --port 8001' | grep -v grep | awk '{print $2}'")

# Kill proxy
def kill_proxy():
    pass

kill_sudo_process = Popen(["sudo", "-S", "kill", "-9", sudo_pid], stdin=PIPE, stdout=PIPE,
                     stderr=PIPE)
try:
    outs, errs = kill_sudo_process.communicate(encoded_password, timeout=15)
except TimeoutExpired:
    kill_sudo_process.kill()
    outs, errs = kill_sudo_process.communicate(encoded_password)

kill_process = Popen(["sudo", "-S", "kill", "-9", second_pid], stdin=PIPE, stdout=PIPE,
                     stderr=PIPE)
try:
    outs, errs = kill_process.communicate(encoded_password, timeout=15)
except TimeoutExpired:
    kill_process.kill()
    outs, errs = kill_process.communicate(encoded_password)

print("#### Proxy has been killed")
create_process.terminate()
kill_sudo_process.terminate()
kill_process.terminate()
