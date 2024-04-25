import subprocess

def get_latest_image_id():
    # Run 'docker images' command and capture the output
    output = subprocess.check_output("docker images", shell=True, text=True)

    # Split the output by lines and get the second line (the latest built image)
    latest_image_info = output.strip().split('\n')[1]

    # Split the line by spaces and get the first element (the image ID)
    latest_image_id = latest_image_info.split()[0]

    return latest_image_id

def main():
    path = "/home/dmytro/dev/projects/data"
    directory_name = "Your_Directory_Name"
    command = "mvn clean install -Pdocker-image"

    # Open xfce4-terminal with the specified working directory, title, and command
    subprocess.Popen(["xfce4-terminal", "--working-directory", path, "--title", directory_name, "--command", command])

    # Wait for the command to complete
    subprocess.wait()

    # Get the ID of the latest built image
    latest_image_id = get_latest_image_id()

    # Rename the Docker image tag
    subprocess.run(f"docker tag {latest_image_id} localhost:5000/custom:3.1.1", shell=True)

    # Push the image to the Docker registry
    subprocess.run("docker push localhost:5000/custom:3.1.1", shell=True)

if __name__ == "__main__":
    main()
