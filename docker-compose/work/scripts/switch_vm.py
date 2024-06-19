import paramiko
import sys
import os

# Define the relative path where the file will be saved, using `~`
local_path = '~/.kube/config'

def copy_file_from_remote(hostname, username, password, remote_path, local_path):
    # Expand `~` to the user's home directory
    local_path = os.path.expanduser(local_path)

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

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_err:
        print(f"SSH error occurred: {ssh_err}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SFTP session and SSH client
        if 'sftp' in locals():
            sftp.close()
        ssh_client.close()

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def main():
    vmSubIp = None

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
    remote_path = '/root/.kube/config'

    copy_file_from_remote(hostname, username, password, remote_path, local_path)

if __name__ == "__main__":
    main()
