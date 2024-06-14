import subprocess
import sys
import os

def docker_compose_up(detached=True, compose_directory='/home/dmytro/dev/projects/easyboot/docker-compose/work/'):
    try:
        # Change the working directory
        os.chdir(compose_directory)

        # Prepare the docker-compose up command
        command = ['docker-compose', 'up']
        if detached:
            command.append('-d')  # Run in detached mode

        # Run the docker-compose up command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check the result and print the output
        if result.returncode == 0:
            print("Docker Compose up executed successfully.")
            print(result.stdout)
        else:
            print("Error executing Docker Compose up.")
            print(result.stderr)
            sys.exit(result.returncode)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    docker_compose_up()
