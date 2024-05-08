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

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)
        exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <db_dump_suffix>")
        exit(1)

    db_dump_suffix = sys.argv[1]

    # Change directory
    run_command("cd /home/dmytro/dev/projects/easyboot/docker-compose/work")

    # Database dump
    dump_file = f"/home/dmytro/eleveo_default_db_dump_{db_dump_suffix}.sql"
    dump_command = f"/usr/bin/pg_dump --dbname=postgresql://postgres:postgres@10.17.50.85:5432/eleveo_default_db --file={dump_file} --host=10.17.50.85"
    run_command(dump_command)

    # Stop Docker containers
    run_command("docker-compose down")

    # Remove Docker volumes
    run_command("docker volume prune -f")

    # Start Docker containers in detached mode
    run_command("docker-compose up -d")

    # Wait for 10 seconds
    time.sleep(10)

    # Restore database dump
    restore_command = f'/usr/bin/psql --host=localhost --port=5432 dbname=eleveo_default_db --username=postgres --file="{dump_file}"'
    run_command(restore_command)

    # Stop Docker containers again
    run_command("docker-compose down")

    # Start Docker containers
    run_command("docker-compose up")

if __name__ == "__main__":
    main()
