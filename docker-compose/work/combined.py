import paramiko
import subprocess

def copy_file_from_remote(hostname, username, password, remote_path, local_path):
    # Create SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh_client.connect(hostname, username=username, password=password)

        # Create SFTP session
        sftp = ssh_client.open_sftp()

        # Download the file
        sftp.get(remote_path, local_path)

        print("File downloaded successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SSH client
        ssh_client.close()

def port_forward_all():
    # Run kubectl get pods command
    get_pods_command = "kubectl get pods"
    get_pods_process = subprocess.Popen(get_pods_command, shell=True, stdout=subprocess.PIPE)
    get_pods_output = get_pods_process.communicate()[0].decode("utf-8")

    # Initialize command list for xfce4-terminal
    terminal_commands = []

    # Filter pods containing 'encourage-data'
    encourage_data_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-data' in line]

    # Port forward for encourage-data pods
    for index, pod in enumerate(encourage_data_pods):
        port_forward_command = f"kubectl port-forward {pod} 8300:8300"
        title = f"Encourage Data - {index+1}"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Filter pods containing 'encourage-conversations'
    encourage_conversations_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-conversations' in line]

    # Port forward for encourage-conversations pods
    for index, pod in enumerate(encourage_conversations_pods):
        port_forward_command = f"kubectl port-forward {pod} 8107:8107"
        title = f"Encourage Conversations - {index+1}"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Open terminals as tabs in the same window
    subprocess.Popen(["xfce4-terminal"] + terminal_commands)


# Provide remote server details and paths
hostname = 'vm085.eng.cz.zoomint.com'
username = 'root'
password = 'zoomcallrec'
remote_path = '.kube/config'
local_path = '/home/dmytro/.kube/config'

# Call the function to copy the file
copy_file_from_remote(hostname, username, password, remote_path, local_path)
port_forward_all()