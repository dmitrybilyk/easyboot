import subprocess
import platform
import time
import paramiko
import sys
import os

local_kube_path = os.path.expanduser('~/.kube/config')
known_hosts_path = os.path.expanduser('~/.ssh/known_hosts')

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def main():
    vmSubIp = '085'

    if len(sys.argv) > 1:
        vmSubIp = sys.argv[1]
    else:
        vmSubIp = get_input("Enter VM IP: ", str)

    hostname = determine_hostname(vmSubIp)
    username = 'root'
    password = 'zoomcallrec'
    local_host = '127.0.0.1'
    port = 5000

    copy_file_from_remote(hostname, username, password, '.kube/config', local_kube_path)
    time.sleep(1)
    open_ssh_tunnel(hostname, vmSubIp, username, password, local_host, port)

def determine_hostname(vmSubIp):
    if not vmSubIp:
        return "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 3:
        return f"vm{vmSubIp}.eng.cz.zoomint.com"
    else:
        return vmSubIp

def copy_file_from_remote(hostname, username, password, remote_path, local_path):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        sftp = ssh_client.open_sftp()
        sftp.get(remote_path, local_path)
        print("File downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        ssh_client.close()

def open_ssh_tunnel(hostname, vmSubIp, username, password, local_host, port):
    command = f'ssh-keygen -f "{known_hosts_path}" -R {hostname}'
    try:
        subprocess.run(command, shell=True, check=True)
        print("Host entry removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    command = f'echo "yes" | ssh-keyscan {hostname} >> {known_hosts_path}'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"SSH key for {hostname} added to known_hosts.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    ssh_command = f'sshpass -p {password} ssh -L {port}:{local_host}:{port} {username}@{hostname}'

    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', f'{port} {vmSubIp}'])
    else:
        print("Unsupported platform for xfce4-terminal.")

if __name__ == "__main__":
    main()
