import paramiko
import subprocess
import sys

def run_command(command):
    """Helper function to run shell commands."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode().strip(), error.decode().strip()

# Function to prompt user for input of a specific type
def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def ssh_download_file(hostname, username, password, remote_path, local_path):
    """Download a file from a remote server via SSH."""
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        sftp = ssh_client.open_sftp()
        sftp.get(remote_path, local_path)
        print(f"File downloaded successfully from {hostname}.")

    except Exception as e:
        print(f"Error downloading file: {e}")

    finally:
        ssh_client.close()

def kubectl_get_pods():
    """Execute 'kubectl get pods' and return the output."""
    return run_command("kubectl get pods")

def filter_pods_by_name(pods_output, keyword):
    """Filter pods by name based on a keyword."""
    return [line.split()[0] for line in pods_output.split('\n') if keyword in line]

def port_forward(pod_name, local_port, remote_port, title):
    """Create a port forwarding command for a specific pod."""
    return f"kubectl port-forward {pod_name} {local_port}:{remote_port}"

def open_terminal_with_tabs(terminal_commands):
    """Open a terminal with multiple tabs for port forwarding."""
    command = ["xfce4-terminal"] + terminal_commands
    subprocess.Popen(command)

def main():

    vmSubIp = '085'
    # Check if at least one argument (excluding script name) is passed
    if len(sys.argv) > 1:
        vmSubIp = sys.argv[1]
    else:
        # Provide remote server details and paths
        vmSubIp = get_input("Enter vm IP: ", str)

    # print("You entered:", vmIp)
    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 3:
        hostname = "vm%s.eng.cz.zoomint.com" % vmSubIp
    else:
        hostname = vmSubIp

    username = 'root'
    password = 'zoomcallrec'
    remote_path = '.kube/config'
    local_path = '/home/dmytro/.kube/config'

    # Download Kubernetes config file from the remote server
    ssh_download_file(hostname, username, password, remote_path, local_path)

    # Get pods information
    pods_output, _ = kubectl_get_pods()

    # Define port forwarding mappings based on pod names
    port_mappings = [
        ("automated-qm", 8207, 8207, "Automated QM"),
        ("encourage-data", 8300, 8300, "Data"),
        ("encourage-scheduler", 8105, 8105, "Scheduler"),
        # ("encourage-conversations", 8107, 8107, "Conversations"),
        ("encourage-correlation", 8108, 8108, "Correlation"),
        ("encourage-zqm-connector", 8201, 8201, "ZQM"),
        ("encourage-integrations", 8202, 8202, "Integrations"),
        ("encourage-framework", 8102, 8102, "Framework"),
        ("interaction-service", 8081, 8081, "InteractionService"),
        ("speech", 8080, 8080, "Speech"),
        ("generative", 8301, 8301, "Generative"),
        ("kubernetes-rabbitmq", 15672, 15672, "Rabbit UI"),
        ("kubernetes-rabbitmq", 5672, 5672, "RabbitMQ"),
        ("kubernetes-postgresql-0", 5432, 5432, "Postgres"),
        ("kubernetes-solrcloud-0", 8983, 8983, "SolrCloud"),
        ("kubernetes-zookeeper", 9181, 9181, "ZooKeeper"),
        ("kubernetes-solrcloud-zookeeper-0", 9983, 2181, "SolrZooKeeper")
    ]

    # Prepare terminal commands for port forwarding
    terminal_commands = []

    for pod_keyword, local_port, remote_port, title in port_mappings:
        filtered_pods = filter_pods_by_name(pods_output, pod_keyword)
        for pod in filtered_pods:
            port_forward_command = port_forward(pod, local_port, remote_port, title)
            terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Open xfce4-terminal with tabs for port forwarding
    open_terminal_with_tabs(terminal_commands)

if __name__ == "__main__":
    main()
