import subprocess
import os

# Define the directory path
directory_path = "/home/dmytro/dev/projects/integrations"

# Change directory to the specified path
os.chdir(directory_path)

# Define the Maven command to be executed
maven_command = ["mvn", "clean", "install", "-Dmaven.test.skip", "-Pdocker-image"]

# Execute the Maven command using subprocess
try:
    subprocess.run(maven_command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running Maven command: {e}")
else:
    print("Maven build completed successfully.")
