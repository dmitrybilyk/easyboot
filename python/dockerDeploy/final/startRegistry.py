import paramiko

hostname = "vm085.eng.cz.zoomint.com"

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def update_registries_and_restart(hostname, username, password, yaml_content):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=password)

        # Create a temporary file on the remote server to store the YAML content
        temp_file = "/tmp/registries.yaml"
        with client.open_sftp() as sftp:
            with sftp.file(temp_file, "w") as f:
                f.write(yaml_content)

        # Move the temporary file to the desired location
        move_command = f"sudo mv {temp_file} /etc/rancher/rke2/registries.yaml"
        stdin, stdout, stderr = client.exec_command(move_command)

        # Check for any errors during the move operation
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error: {stderr.read().decode('utf-8')}")
        else:
            print("Registries configuration updated successfully.")
        # Define the command to start the docker-registry service
        command = "sudo systemctl start docker-registry"

        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the SSH server
            ssh_client.connect(hostname, port=22, username=username, password=password)

            # Execute the command over SSH
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # Check command execution status
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print("Docker registry service started successfully.")
            else:
                print(f"Error occurred: {stderr.read().decode()}")

        finally:
            # Close the SSH connection
            ssh_client.close()

    except paramiko.AuthenticationException:
        print(f"Failed to authenticate to {hostname}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

def restartRegistries(hostname, username, password, yaml_content):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, password=password)

        # Define the command to start the docker-registry service
        command = "systemctl restart rke2-server"

        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the SSH server
            ssh_client.connect(hostname, port=22, username=username, password=password)

        # Execute systemctl command to check service status
        # stdin, stdout, stderr = ssh_client.exec_command(f'systemctl is-active {service_name}')
        # output = stdout.read().decode().strip()
        #
        # # Check the output to determine service status
        # if output == 'active':
        #     print(f"The service '{service_name}' is active.")
        # else:
        #     print(f"The service '{service_name}' is not active.")

            # Execute the command over SSH
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # Check command execution status
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                print("Docker registries restarted successfully.")
            else:
                print(f"Error occurred: {stderr.read().decode()}")

        finally:
            # Close the SSH connection
            ssh_client.close()

    except paramiko.AuthenticationException:
        print(f"Failed to authenticate to {hostname}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()


# Example usage
if __name__ == "__main__":

    vmSubIp = get_input("Enter vm ip: ", str)

    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 2:
        hostname = "vm0%s.eng.cz.zoomint.com" % vmSubIp
    else:
        hostname = vmSubIp

    username = "root"
    password = "zoomcallrec"

    # YAML content to replace /etc/rancher/rke2/registries.yaml
    yaml_content = """\
mirrors:
  "docker.io":
    endpoint:
      - "https://artifactory.zoomint.com"
  "artifactory.zoomint.com":
    endpoint:
      - "https://artifactory.zoomint.com"
  "localhost:5000":
    endpoint:
      - "https://localhost:5000"
configs:
  "docker.io":
    tls:
      insecure_skip_verify: true
  "artifactory.zoomint.com":
    tls:
      insecure_skip_verify: true
  "localhost:5000":
    tls:
      insecure_skip_verify: true
"""

    # Update /etc/rancher/rke2/registries.yaml and restart rke2-server on the remote server
    update_registries_and_restart(hostname, username, password, yaml_content)
    restartRegistries(hostname, username, password, yaml_content)
