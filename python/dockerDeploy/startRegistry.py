import paramiko

hostname = "vm293.eng.cz.zoomint.com"
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

        # Restart the rke2-server service
        restart_command = "sudo systemctl restart rke2-server"
        stdin, stdout, stderr = client.exec_command(restart_command)

        # Check for any errors during the restart operation
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error: {stderr.read().decode('utf-8')}")
        else:
            print("rke2-server restarted successfully.")

    except paramiko.AuthenticationException:
        print(f"Failed to authenticate to {hostname}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

# Example usage
if __name__ == "__main__":

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
