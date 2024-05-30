import subprocess
import sys

deployment_name = "zqm"
default_command = "restart"

resource_names = [
    "encourage-data",
    "interaction-service",
    "encourage-conversations",
    "encourage-correlation",
    "encourage-zqm-connector",
    "encourage-integrations",
    "automated-qm",
    "encourage-scheduler",
    "encourage-framework",
    "automated-qm",
    "interaction-player",
    "speechrec",
    "speech-generative-ai",
    "scorecard"
]

def execute(pod_name, toFollow):
    global deployment_name, default_command

    # if resource:
    #     deployment_name = find_deployment_name(resource)

    if toFollow:
        toFollow = 'true'
    else:
        toFollow = 'false'

    command = (
        f"clear && kubectl get pods | grep {pod_name} | awk '{print $1}' | xargs -I {} kubectl logs {} --follow={toFollow} --since=5m"
    )

    # Run the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def find_deployment_name(resource):
    for name in resource_names:
        if resource in name:
            return name
    return None

def main():
    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 2:
        execute(sys.argv[1], sys.argv[2])
    else:
        execute(None, None)
        print("No values passed.")

if __name__ == "__main__":
    main()
