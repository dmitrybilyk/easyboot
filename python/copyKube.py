import paramiko

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

# Provide remote server details and paths
hostname = 'vm085.eng.cz.zoomint.com'
username = 'root'
password = 'zoomcallrec'
remote_path = '.kube/config'
local_path = '/home/dmytro/.kube/config'

# Call the function to copy the file
copy_file_from_remote(hostname, username, password, remote_path, local_path)
