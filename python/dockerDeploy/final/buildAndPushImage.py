import subprocess
import os
import docker
import paramiko
import platform

# Function to prompt user for input of a specific type
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")
vmSubIp = get_input("Enter vm IP: ", str)

paths = [
    ("/home/dmytro/dev/projects/data/service"),
    ("/home/dmytro/dev/projects/interaction-service"),
    ("/home/dmytro/dev/projects/conversations/service"),
    ("/home/dmytro/dev/projects/correlation/service"),
    ("/home/dmytro/dev/projects/zqm-connector/service"),
    ("/home/dmytro/dev/projects/scheduler/service"),
    ("/home/dmytro/dev/projects/framework/service"),
    ("/home/dmytro/dev/projects/automatedqm"),
    ("/home/dmytro/dev/projects/interaction-player/webapp"),
    ("/home/dmytro/dev/projects/speechrec/core")
]

mvn_apps = [
    ("/home/dmytro/dev/projects/data/service"),
    ("/home/dmytro/dev/projects/conversations/service"),
    ("/home/dmytro/dev/projects/correlation/service"),
    ("/home/dmytro/dev/projects/zqm-connector/service"),
    ("/home/dmytro/dev/projects/scheduler/service"),
    ("/home/dmytro/dev/projects/framework/service"),
    ("/home/dmytro/dev/projects/interaction-player/webapp")
]

names = [
    ("data"),
    ("interaction-service"),
    ("conversations"),
    ("correlation"),
    ("zqm-connector"),
    ("scheduler"),
    ("framework"),
    ("automatedqm"),
    ("interaction-player"),
    ("speechrec")
]

resources_names = [
    ("encourage-data"),
    ("interaction-service"),
    ("encourage-conversations"),
    ("encourage-correlation"),
    ("encourage-zqm-connector"),
    ("encourage-scheduler"),
    ("encourage-framework"),
    ("automated-qm"),
    ("interaction-player"),
    ("speechrec")
]

# Define the new tag for the Docker image
new_tag = 'data:3.1.17'





# vmSubIp = "85"

service_name = get_input("Enter service name: ", str)

resource_name = [name for name in resources_names if service_name in name][0]

image_repository = "eleveo/encourage/%s" % resource_name
if resource_name.__contains__("auto"):
    image_repository = "artifactory.zoomint.com/eleveo/encourage/%s" % resource_name

service_path = [name for name in paths if service_name in name][0]

# Define the directory path for the Maven project
service_directory_path = service_path

service = [name for name in names if service_name in name]

tagPathVersion = get_input("Enter Patch Version: ", int)

new_tag = f'{service_name}:8.1.{tagPathVersion}'

hostname = "vm0%s.eng.cz.zoomint.com" % vmSubIp

# def run_maven_build(directory, image_repository, image_tag):
def run_maven_build(directory, image_repository, image_tag):
    try:
        # Change directory to the specified path
        os.chdir(directory)
        if mvn_apps.__contains__(directory):
            # Define the Maven command to be executed
            maven_command = [
                "mvn",
                "clean",
                "install",
                "-Dmaven.test.skip",
                "-Pdocker-image",
                f"-Ddocker.image.repository={image_repository}",
                f"-Ddocker.image.tag={image_tag}"
            ]

            # Execute the Maven command using subprocess
            subprocess.run(maven_command, check=True)
            print("Maven build completed successfully.")
            return True

        else:
            # Change directory to the specified path
            os.chdir(directory)
            # Define the Gradle command as a list of strings
            gradle_command = ['./gradlew', 'clean', 'build', '-x', 'test', '-x', 'jib']

            # Execute the Gradle command
            try:
                # Run the command and capture the output
                result = subprocess.run(gradle_command, capture_output=True, text=True, check=True)
                # Print the command output (stdout and stderr)
                print(result.stdout)
                print(result.stderr)
            except subprocess.CalledProcessError as e:
                # Handle any errors that occur during command execution
                print(f"Error: {e}")

            # Define the Gradle command as a list of strings
            gradle_command = ['./gradlew', ':jibDockerBuild', '-x', 'test']

            # Execute the Gradle command
            try:
                # Run the command and capture the output
                result = subprocess.run(gradle_command, capture_output=True, text=True, check=True)
                # Print the command output (stdout and stderr)
                print(result.stdout)
                print(result.stderr)
                return True
            except subprocess.CalledProcessError as e:
                # Handle any errors that occur during command execution
                print(f"Error: {e}")
    finally:
        print("image build and re-named")


# Example usage:
directory_path = "eleveo/"
repository_name = "/encourage/encourage-integrations-api"
image_tag = "latest"

def find_latest_image():
    try:
        client = docker.from_env()
        images = client.images.list()

        # Sort images by creation date to get the latest one
        images.sort(key=lambda img: img.attrs['Created'], reverse=True)

        if images:
            latest_image = images[0]
            return latest_image
        else:
            return None

    except docker.errors.APIError as e:
        print(f"Error: {e}")
        return None

def tag_latest_image_with_new_tag(latest_image, new_tag):
    try:
        # Define the Docker command to tag the image
        docker_command = [
            "docker",
            "tag",
            latest_image.tags[0],
            f"localhost:5000/{new_tag}"
        ]

        # Execute the Docker command using subprocess
        subprocess.run(docker_command, check=True)
        print("Tagging of the Docker image completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while tagging the Docker image: {e}")
        return False

def get_last_5_image_tags():
    try:
        # Initialize Docker client
        client = docker.from_env()

        # Get a list of all Docker images
        images = client.images.list()

        # Sort images by creation date in descending order
        images.sort(key=lambda img: img.attrs['Created'], reverse=True)

        # Extract tags of the last 5 images (if available)
        last_5_tags = []
        for image in images[:5]:
            tags = image.tags
            if tags:
                last_5_tags.extend(tags)

        return last_5_tags

    except docker.errors.APIError as e:
        print(f"Error: {e}")
        return []

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


def push_docker_image(image_tag):
    try:
        # Execute docker push command
        subprocess.run(["docker", "push", image_tag], check=True)
        print(f"Successfully pushed Docker image: {image_tag}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while pushing Docker image: {e}")
        return False

def remove_unused_images():
    try:
        # Command to list images with "none" tag
        cmd_list_images = f"docker image ls --format '{{{{.ID}}}}\t{{{{.Repository}}}}' | awk '$2 ~ /{service_name}/ {{print $1}}'"

        # Run the command to get image IDs
        result = subprocess.run(cmd_list_images, shell=True, capture_output=True, text=True)
        image_ids = result.stdout.strip().split()  # Split output into a list of image IDs

        if image_ids:
            # Command to remove images by IDs
            cmd_remove_images = f"docker image rm {' '.join(image_ids)} -f"

            # Run the command to remove images
            subprocess.run(cmd_remove_images, shell=True, check=True)
            print("Unused Docker images removed successfully.")
        else:
            print("No unused Docker images found.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Handle error if the subprocess command fails

if __name__ == "__main__":
    remove_unused_images()
    # Run Maven build
    if run_maven_build(service_directory_path, image_repository, "latest"):
        # Find the latest Docker image
        latest_image = find_latest_image()

        if latest_image:
            # Tag the latest image with the defined new tag
            if tag_latest_image_with_new_tag(latest_image, new_tag):
                print(f"Successfully tagged the latest image with: localhost:5000/{new_tag}")
            else:
                print("Failed to tag the latest image.")
        else:
            print("No images found.")

        # Get and display the last 5 Docker image tags
        last_5_tags = get_last_5_image_tags()

        if last_5_tags:
            print("\nLast 5 Docker image tags:")
            for tag in last_5_tags:
                print(tag)
        else:
            print("Failed to retrieve last 5 Docker image tags.")
    else:
        print("Maven build failed. Cannot proceed with Docker image operations.")

if not vmSubIp:
    hostname = "vm085.eng.cz.zoomint.com"
elif len(vmSubIp) == 2:
    hostname = "vm0%s.eng.cz.zoomint.com" % vmSubIp
else:
    hostname = vmSubIp

# hostname = f'vm0{vmSubIp}.eng.cz.zoomint.com'
username = 'root'
password = 'zoomcallrec'
remote_path = '.kube/config'
local_path = '/home/dmytro/.kube/config'

remote_port = 5000
local_port = 5000

def establish_ssh_tunnel():

    host = hostname
    port = 5000
    ssh_command = f'sshpass -p zoomcallrec ssh -L {port}:127.0.0.1:{port} root@%s' % host

    # Command to open a new terminal and run the SSH command
    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', (f'{port} %s' % vmSubIp)])
    else:
        print("Unsupported platform for xfce4-terminal.")

kubectl_command = f"kubectl set image deployment/%s {resource_name}=localhost:5000/{new_tag}" % resource_name

def execute_kubectl_command(hostname, username, password, kubectl_command):
    try:
        # Create SSH client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        ssh_client.connect(hostname, username=username, password=password)

        # Execute kubectl command remotely
        stdin, stdout, stderr = ssh_client.exec_command(kubectl_command)

        # Check for any errors during command execution
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error executing kubectl command: {stderr.read().decode('utf-8')}")
        else:
            print("kubectl command executed successfully.")

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {username}@{hostname}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh_client.close()


# Call the function to copy the file
copy_file_from_remote(hostname, username, password, remote_path, local_path)



# hostname = "vm085.eng.cz.zoomint.com"
# username = "root"
# password = "zoomcallrec"

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
# update_registries_and_restart(hostname, username, password, yaml_content)

# establish_ssh_tunnel()

push_docker_image(f"localhost:5000/{new_tag}")

execute_kubectl_command(hostname, username, password, kubectl_command)