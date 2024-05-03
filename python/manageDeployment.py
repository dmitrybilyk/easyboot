import subprocess
import sys

deployment_name = "encourage-scheduler"
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
    "speechrec"
]

def execute(command, resource):
    global deployment_name, default_command

    if command:
        default_command = command
    if resource:
        deployment_name = find_deployment_name(resource)

    # Construct the kubectl command

    if default_command == 'stop':
        kubectl_command = f"kubectl scale --replicas=0 deployment {deployment_name}"
    elif default_command == 'start':
        kubectl_command = f"kubectl scale --replicas=1 deployment {deployment_name}"
    elif default_command == 'status':
        kubectl_command = f"kubectl get deployments | grep {deployment_name}"
    else:
        kubectl_command = f"kubectl rollout restart deployment {deployment_name}"

    # Run the command using subprocess
    try:
        subprocess.run(kubectl_command, shell=True, check=True)
        print(f"Rollout {default_command} for deployment {deployment_name} successful.")
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
