import subprocess
import os
import time

def execute_commands_in_terminals(path_and_commands):
    for path, command, custom_name in path_and_commands:
        # Get the directory name from the path
        directory_name = custom_name if custom_name else os.path.basename(os.path.normpath(path)) if path else "Default"

        # Expand home directory in path if provided
        if path:
            expanded_path = os.path.expanduser(path)
        else:
            expanded_path = None

        # Launch command in a new terminal window
        time.sleep(2)
        if expanded_path:
            subprocess.Popen(["xfce4-terminal", "--working-directory", expanded_path, "--title", directory_name, "--command", command])
        else:
            subprocess.Popen(["xfce4-terminal", "--title", directory_name, "--command", command])

if __name__ == "__main__":
    paths_and_commands = [
        # ("~/dev/projects/data/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Data"),
        # ("~/dev/projects/interaction-service", "./gradlew bootRun --args='--spring.profiles.active=run-with-compose'", "Interactions"),
        # ("~/dev/projects/conversations/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Conversations"),
        # ("~/dev/projects/correlation/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Correlation"),
        # ("~/dev/projects/zqm-connector/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "ZQM"),
        ("~/dev/projects/scheduler/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Scheduler"),
        # ("~/dev/projects/framework/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Framework"),
        # ("~/dev/projects/automatedqm", "./gradlew bootRun --args='--spring.profiles.active=run-with-compose'", "AutoQM"),
        # ("~/dev/projects/interaction-player/webapp", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose", "Player"),
        # ("~/dev/projects/speech-generative-ai/service", ".././gradlew bootRun --args='--spring.profiles.active=run-with-compose'", "GAI"),
        # ("~/dev/projects/speechrec/core", ".././gradlew bootRun --args='--spring.profiles.active=run-with-compose'", "Speech")
    ]
    execute_commands_in_terminals(paths_and_commands)
