import paramiko
import subprocess

def establish_ssh_tunnel(remote_host, remote_port, local_port, ssh_username, ssh_password):
    try:
        # Create SSH client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        ssh_client.connect(remote_host, username=ssh_username, password=ssh_password)

        # Open an SSH tunnel (local_port -> remote_host:remote_port)
        ssh_tunnel_command = f"ssh -L {local_port}:127.0.0.1:{remote_port} {ssh_username}@{remote_host}"
        ssh_client.exec_command(ssh_tunnel_command)

        print(f"SSH tunnel established: localhost:{local_port} -> {remote_host}:{remote_port}")

        # Keep the SSH session open (you can add additional commands here)

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {ssh_username}@{remote_host}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh_client.close()

# Example usage: Establish SSH tunnel to vm029.eng.cz.zoomint.com
remote_host = "vm029.eng.cz.zoomint.com"
remote_port = 5000
local_port = 5000
ssh_username = "root"
ssh_password = "zoomcallrec"

# Establish SSH tunnel
establish_ssh_tunnel(remote_host, remote_port, local_port, ssh_username, ssh_password)
