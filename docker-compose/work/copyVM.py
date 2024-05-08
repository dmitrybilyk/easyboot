# sudo apt-get install postgresql-client

# 1. cd /home/dmytro/dev/projects/easyboot/docker-compose/work
# 2. /usr/bin/pg_dump --dbname=postgresql://postgres:postgres@10.17.50.85:5432/eleveo_default_db --file=/home/dmytro/eleveo_default_db_dump_085.sql --host=10.17.50.85
# 3. docker-compose down
# 4. docker volume prune -f
# 5. docker-compose up -d
# 6. Wait for 10 seconds
# 7. /usr/bin/psql --host=localhost --port=5432 dbname=eleveo_default_db --username=postgres --file="/home/dmytro/eleveo_default_db_dump_085.sql"
# 8. docker-compose down
# 9. docker-compose up

import subprocess
import time
import sys
import os


def create_pgpass_file():
    # Define the file path
    file_path = '/home/dmytro/.pgpass'

    # Define the content to be written to the file
    content = 'localhost:5432:eleveo_default_db:postgres:postgres\n'

    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write the content to the file
            file.write(content)

        # Change the file permissions to 600 (read/write by owner only)
        os.chmod(file_path, 0o600)

        print(f".pgpass file successfully created at {file_path} with permissions set to 600.")

    except OSError as e:
        print(f"Error occurred: {e}")


def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")


def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)
        exit(1)


def main():
    if len(sys.argv) > 1:
        vmSubIp = sys.argv[1]
    else:
        vmSubIp = get_input("Enter vm ip: ", str)

    # hostname = 'vm085.eng.cz.zoomint.com'

    # SSH command with password
    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 3:
        hostname = "vm%s.eng.cz.zoomint.com" % vmSubIp
    else:
        hostname = vmSubIp

    db_dump_suffix = hostname

    create_pgpass_file()

    # Change directory
    os.chdir("/home/dmytro/dev/projects/easyboot/docker-compose/work")
    # run_command("cd /home/dmytro/dev/projects/easyboot/docker-compose/work")

    # Database dump
    dump_file = f"/home/dmytro/eleveo_default_db_dump_{db_dump_suffix}.sql"
    dump_command = f"/usr/bin/pg_dump --dbname=postgresql://postgres:postgres@{hostname}:5432/eleveo_default_db --file={dump_file} --host={hostname}"
    run_command(dump_command)

    # Stop Docker containers
    run_command("docker-compose down")
    time.sleep(10)
    # Remove Docker volumes
    run_command("docker volume rm work_pgdata_correct")
    run_command("docker volume prune -f")

    # Start Docker containers in detached mode
    run_command("docker-compose up -d")

    # Wait for 10 seconds
    time.sleep(10)

    # Restore database dump
    restore_command = f'/usr/bin/psql --host=localhost --port=5432 dbname=eleveo_default_db --username=postgres --file="{dump_file}"'
    run_command(restore_command)

    time.sleep(10)

    # Stop Docker containers again
    run_command("docker-compose down")

    time.sleep(10)

    # Start Docker containers
    run_command("docker-compose up -d")


if __name__ == "__main__":
    main()
