import subprocess
import sys
import psycopg2

# List of shell commands to execute
allCommands = [
    "curl -X DELETE http://localhost:8108/api/correlation-range/",
    "curl -X DELETE http://localhost:8107/api/v3/conversations/",
    "curl -X DELETE http://0.0.0.0:8300/api/v3/events/",
    "curl -X DELETE http://0.0.0.0:8300/api/v3/tasks/",
    "kubectl rollout restart deployment encourage-scheduler"
]
justRestartSchedulerCommand = [
    "kubectl rollout restart deployment encourage-scheduler"
]


def execute_commands(callId):
    if callId:
        try:
            # Establish a connection to the PostgreSQL database
            connection = psycopg2.connect(
                user="postgres",
                password="postgres",
                host="localhost",
                port="5432",
                database="eleveo_default_db"
            )

            # Create a cursor object using the connection
            cursor = connection.cursor()

            # Define the update query
            update_query = """
                UPDATE callrec.couples
                SET dirty = true
                WHERE callid = %s
            """

            # Specify the callid to update
            callid_value = callId

            # Execute the update query with parameter binding
            cursor.execute(update_query, (callid_value,))

            # Commit the transaction
            connection.commit()

            for cmd in justRestartSchedulerCommand:
                print(f"Executing command: {cmd}")
                try:
                    # Execute the command and capture the output
                    result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    # Print the command output
                    if result.stdout:
                        print("Output:")
                        print(result.stdout)
                    if result.stderr:
                        print("Error:")
                        print(result.stderr)

                except subprocess.CalledProcessError as e:
                    # Handle if the command returns a non-zero exit status
                    print(f"Command '{cmd}' failed with error code {e.returncode}")
                    print("Error output:")
                    print(e.stderr)

                print("=" * 50)  # Separator between commands


                print(f"Updated just call {callId}")
        finally:
            print("success")
    else:
        # Iterate over each command and execute them one by one
        for cmd in allCommands:
            print(f"Executing command: {cmd}")
            try:
                # Execute the command and capture the output
                result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Print the command output
                if result.stdout:
                    print("Output:")
                    print(result.stdout)
                if result.stderr:
                    print("Error:")
                    print(result.stderr)

            except subprocess.CalledProcessError as e:
                # Handle if the command returns a non-zero exit status
                print(f"Command '{cmd}' failed with error code {e.returncode}")
                print("Error output:")
                print(e.stderr)

            print("=" * 50)  # Separator between commands

def main():
    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 1:
        # The first command-line argument (sys.argv[0]) is the script name
        # Subsequent arguments are the values passed
        values = sys.argv[1:]
        for value in values:
            execute_commands(value)
    else:
        execute_commands(None)
        # execute_commands(133007)
        print("No values passed.")

    # Execute the specified commands


if __name__ == "__main__":
    main()
