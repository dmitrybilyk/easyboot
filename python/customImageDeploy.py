import subprocess

def execute_command(command):
    subprocess.run(command, shell=True)

def get_latest_image_id():
    # Run 'docker images' command and capture the output
    output = subprocess.check_output("docker images", shell=True, text=True)

    # Split the output by lines and get the second line (the latest built image)
    latest_image_info = output.strip().split('\n')[1]

    # Split the line by spaces and get the first element (the image ID)
    latest_image_id = latest_image_info.split()[0]

    return latest_image_id

def main():
    # Open xfce4-terminal
    execute_command("xfce4-terminal --minimize --maximize --geometry=80x24")

    # Navigate to the desired directory
    execute_command("cd /home/dmytro/dev/projects/data")

    # Build Maven project
    execute_command("mvn clean install -Pdocker-image")

    # Get the ID of the latest built image
    latest_image_id = get_latest_image_id()

    # Rename the Docker image tag
    execute_command(f"docker tag {latest_image_id} localhost:5000/custom:3.1.1")

    # Push the image to the Docker registry
    execute_command("docker push localhost:5000/custom:3.1.1")

if __name__ == "__main__":
    main()
