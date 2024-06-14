import subprocess
import sys
import argparse

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
    "audit-log",
    "interaction-player",
    "speechrec",
    "speech-generative-ai",
    "scorecard"
]

def execute(pod_name=None, since_minutes=10, to_follow=False):
    follow_flag = '--follow=true' if to_follow else '--follow=false'
    since_flag = f"--since={since_minutes}m"

    try:
        if pod_name:
            command = (
                f"clear && kubectl get pods | grep {pod_name} | awk '{{print $1}}' | "
                f"xargs -I {{}} kubectl logs {{}} {follow_flag} {since_flag}"
            )
        else:
            command = "kubectl get pods"

        print(f"Executing command: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def find_deployment_name(resource):
    for name in resource_names:
        if resource in name:
            return name
    return None

def main():
    parser = argparse.ArgumentParser(description="Fetch Kubernetes pod logs.")
    parser.add_argument('pod_name', type=str, nargs='?', help='Name of the pod to fetch logs for.')
    parser.add_argument('since_minutes', type=int, nargs='?', default=10, help='Number of minutes to look back for logs.')
    parser.add_argument('to_follow', type=bool, nargs='?', default=False, help='Set to True to follow the logs.')
    args = parser.parse_args()

    execute(args.pod_name, args.since_minutes, args.to_follow)

if __name__ == "__main__":
    main()
