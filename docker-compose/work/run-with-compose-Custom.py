import subprocess
import os

def execute_commands_in_terminals(path_and_commands, custom_names=None):
    for (path, command), custom_name in zip(path_and_commands, custom_names or []):
        # Get the directory name from the path
        directory_name = custom_name if custom_name else os.path.basename(os.path.normpath(path)) if path else "Default"
        # Launch command in a new terminal window
        if path:
            subprocess.Popen(["xfce4-terminal", "--working-directory", path, "--title", directory_name, "--command", command])
        else:
            subprocess.Popen(["xfce4-terminal", "--title", directory_name, "--command", command])

if __name__ == "__main__":
    paths_and_commands = [
        # ("/home/dmytro/dev/projects/data/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        # ("/home/dmytro/dev/projects/interaction-service", "./gradlew bootRun --args='--spring.profiles.active=run-with-compose'"),
        # ("/home/dmytro/dev/projects/conversations/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        # ("/home/dmytro/dev/projects/correlation/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        # ("/home/dmytro/dev/projects/zqm-connector/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        ("/home/dmytro/dev/projects/scheduler/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        # ("/home/dmytro/dev/projects/framework/service", "mvn spring-boot:run -Dspring-boot.run.profiles=run-with-compose"),
        # ("/home/dmytro/dev/projects/automatedqm", "./gradlew bootRun --args='--spring.profiles.active=run-with-compose'"),
        # ("/home/dmytro/dev/projects/speechrec/core", ".././gradlew bootRun --args='--spring.profiles.active=run-with-compose'")
    ]
    custom_names = [
        # "Data",
        # "Interaction",
        # "Conversations",
        # "Correlation",
        # "ZQM Connector",
        "Scheduler",
        # "Framework",
        # "AutomatedQM"
        # "SpeechRec",
    ]
    execute_commands_in_terminals(paths_and_commands, custom_names)
