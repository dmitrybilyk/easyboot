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

# Function to prompt user for input of a specific type
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")


# Provide remote server details and paths
vmSubIp = get_input("Enter vm IP: ", str)
# print("You entered:", vmIp)
if not vmSubIp:
    hostname = "vm085.eng.cz.zoomint.com"
elif len(vmSubIp) == 3:
    hostname = "vm%s.eng.cz.zoomint.com" % vmSubIp
else:
    hostname = vmSubIp
hostname = f'vm{vmSubIp}.eng.cz.zoomint.com'
username = 'root'
password = 'zoomcallrec'
remote_path = '.kube/config'
local_path = '/home/dmytro/.kube/config'

# Call the function to copy the file
copy_file_from_remote(hostname, username, password, remote_path, local_path)

