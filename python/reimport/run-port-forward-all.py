import subprocess

def port_forward_all():
    # Run kubectl get pods command
    get_pods_command = "kubectl get pods"
    get_pods_process = subprocess.Popen(get_pods_command, shell=True, stdout=subprocess.PIPE)
    get_pods_output = get_pods_process.communicate()[0].decode("utf-8")

    # Filter pods containing 'encourage-data'
    encourage_data_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-data' in line]

    # Port forward for encourage-data pods
    for index, pod in enumerate(encourage_data_pods):
        port_forward_command = f"kubectl port-forward {pod} 8300:8300"
        title = f"Encourage Data - {index+1}"
        subprocess.Popen(["xfce4-terminal", "--hold", "--title", title, "--command", port_forward_command])

    # Filter pods containing 'encourage-conversations'
    encourage_conversations_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-conversations' in line]

    # Port forward for encourage-conversations pods
    for index, pod in enumerate(encourage_conversations_pods):
        port_forward_command = f"kubectl port-forward {pod} 8107:8107"
        title = f"Encourage Conversations - {index+1}"
        subprocess.Popen(["xfce4-terminal", "--hold", "--title", title, "--command", port_forward_command])

if __name__ == "__main__":
    port_forward_all()
