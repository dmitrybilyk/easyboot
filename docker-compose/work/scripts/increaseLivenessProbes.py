import os
import paramiko
import subprocess
import sys

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def get_user_home():
    return os.path.expanduser("~")

def ssh_download_file(hostname, username, password, remote_path, local_path):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        sftp = ssh_client.open_sftp()
        sftp.get(remote_path, local_path)
        print(f"File downloaded successfully from {hostname}.")

    except Exception as e:
        print(f"Error downloading file: {e}")

    finally:
        ssh_client.close()

def main():
    vmSubIp = ''
    if len(sys.argv) > 1:
        vmSubIp = sys.argv[1]
    else:
        vmSubIp = get_input("Enter vm IP: ", str)

    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 3:
        hostname = f"vm{vmSubIp}.eng.cz.zoomint.com"
    else:
        hostname = vmSubIp

    username = 'root'
    password = 'zoomcallrec'
    remote_path = '.kube/config'
    local_path = os.path.join(get_user_home(), ".kube/config")

    ssh_download_file(hostname, username, password, remote_path, local_path)

    resources = [
        "encourage-data",
        "automated-qm",
        "interaction-player",
        "encourage-integrations",
        "scorecard"
    ]

    for resource in resources:
        command = [
            "kubectl", "patch", "deployment", resource,
            "--type", "json",
            "-p", '[{"op": "replace", "path": "/spec/template/spec/containers/0/livenessProbe/failureThreshold", "value": 80000}]'
        ]
        subprocess.run(command)

if __name__ == "__main__":
    main()
