import subprocess
import platform
import time
import paramiko
import sys


local_kube_path = '/home/dmytro/.kube/config'
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

vmSubIp = '085'

if len(sys.argv) > 1:
    vmSubIp = sys.argv[1]
else:
    vmSubIp = get_input("Enter vm ip: ", str)

hostname = 'vm085.eng.cz.zoomint.com'

# SSH command with password
if not vmSubIp:
    hostname = "vm085.eng.cz.zoomint.com"
elif len(vmSubIp) == 3:
    hostname = "vm%s.eng.cz.zoomint.com" % vmSubIp
else:
    hostname = vmSubIp

host = hostname
port = 5000

username = 'root'
password = 'zoomcallrec'
local_host = '127.0.0.1'

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

def close_terminal_window_by_title(window_title, exclude_title='thenRunPortForward5000'):
    try:
        # Command to list all open windows and filter by title to get the window ID
        list_windows_cmd = f"wmctrl -l | grep '{window_title}'"

        if exclude_title:
            # Append a negative pattern match to exclude the specified title
            list_windows_cmd += f" | grep -v '{exclude_title}'"

        list_windows_cmd += " | awk '{print $1}'"

        window_ids = subprocess.check_output(list_windows_cmd, shell=True, text=True).strip().split('\n')

        for window_id in window_ids:
            # Command to close the window by ID
            if window_id:
                subprocess.Popen(['wmctrl', '-ic', window_id])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def open_ssh_tunnel(vmSubIp):
    # Command to remove the specified host entry from known_hosts file
    command = 'ssh-keygen -f "/home/dmytro/.ssh/known_hosts" -R %s' % host

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print("Host entry removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Command to fetch the SSH key and add it to known_hosts
    command = f'echo "yes" | ssh-keyscan {hostname} >> ~/.ssh/known_hosts'

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"SSH key for {hostname} added to known_hosts.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


    ssh_command = f'sshpass -p {password} ssh -L {port}:{local_host}:{port} {username}@%s' % host

    # Command to open a new terminal and run the SSH command
    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', (f'{port} %s' % vmSubIp)])
    else:
        print("Unsupported platform for xfce4-terminal.")

if __name__ == "__main__":
    # Check if at least one argument (excluding script name) is passed
    close_terminal_window_by_title(5000)
    copy_file_from_remote(hostname, username, password, '.kube/config', local_kube_path)
    time.sleep(1)
    open_ssh_tunnel(vmSubIp)
