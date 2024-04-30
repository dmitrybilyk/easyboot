import paramiko
import subprocess


def close_terminal_window_by_title(window_title, exclude_title='run-port-forward-all'):
    try:
        # Command to list all open windows and filter by title to get the window ID
        list_windows_cmd = f"wmctrl -l | grep '{window_title}'"

        if exclude_title:
            # Append a negative pattern match to exclude the specified title
            list_windows_cmd += f" | grep -v '{exclude_title}'"

        list_windows_cmd += " | awk '{print $1}'"

        window_ids = subprocess.check_output(list_windows_cmd, shell=True, text=True).strip().split('\n')

        for window_id in window_ids:
            # Command to close the window by ID
            subprocess.Popen(['wmctrl', '-ic', window_id])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_input(prompt, type_func):
    while True:
        try:
            user_input = type_func(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value of the specified type.")

def copy_file_from_remote(hostname, username, password, remote_path, local_path):
    # Create SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh_client.connect(hostname, username=username, password=password)

        # Create SFTP session
        sftp = ssh_client.open_sftp()

        # Download the file
        sftp.get(remote_path, local_path)

        print("File downloaded successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the SSH client
        ssh_client.close()

def port_forward_all():
    # Run kubectl get pods command
    get_pods_command = "kubectl get pods"
    get_pods_process = subprocess.Popen(get_pods_command, shell=True, stdout=subprocess.PIPE)
    get_pods_output = get_pods_process.communicate()[0].decode("utf-8")

    # Initialize command list for xfce4-terminal
    terminal_commands = []

    # Filter pods containing 'encourage-data'
    encourage_data_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-data' in line]

    # Port forward for encourage-data pods
    for index, pod in enumerate(encourage_data_pods):
        port_forward_command = f"kubectl port-forward {pod} 8300:8300"
        title = f"Data"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Filter pods containing 'encourage-conversations'
    encourage_conversations_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'encourage-conversations' in line]

    # Port forward for encourage-conversations pods
    for index, pod in enumerate(encourage_conversations_pods):
        port_forward_command = f"kubectl port-forward {pod} 8107:8107"
        title = f"Conversations"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

        # Filter pods containing 'interaction_service'
    interaction_service_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'interaction-service' in line]

    # Port forward for encourage-conversations pods
    for index, pod in enumerate(interaction_service_pods):
        port_forward_command = f"kubectl port-forward {pod} 8081:8081"
        title = f"InteractionService"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

        # Filter pods containing 'interaction_service'
    speech_service_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'speech' in line]

    # Port forward for speech pods
    for index, pod in enumerate(speech_service_pods):
        port_forward_command = f"kubectl port-forward {pod} 8080:8080"
        title = f"Speech"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

        # Filter pods containing 'interaction_service'
    speech_generative_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'generative' in line]

    # Port forward for speech pods
    for index, pod in enumerate(speech_generative_pods):
        port_forward_command = f"kubectl port-forward {pod} 8081:8080"
        title = f"Generative"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Filter pods containing 'rabbit'
    rabbit_podsUI = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-rabbitmq' in line]

    # Port forward for rabbit pods
    for index, pod in enumerate(rabbit_podsUI):
        port_forward_command = f"kubectl port-forward {pod} 15672:15672"
        title = f"Rabbit UI"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])


    # Filter pods containing 'rabbit'
    rabbit_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-rabbitmq' in line]

    # Port forward for rabbit pods
    for index, pod in enumerate(rabbit_pods):
        port_forward_command = f"kubectl port-forward {pod} 5672:5672"
        title = f"RabbitMQ"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Filter pods containing 'postgres'
    postgres_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-postgresql-0' in line]

    # Port forward for postgres pods
    for index, pod in enumerate(postgres_pods):
        port_forward_command = f"kubectl port-forward {pod} 5432:5432"
        title = f"Postgres"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Filter pods containing 'solr cloud'
    solrCloud_pods = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-solrcloud-0' in line]

    # Port forward for Solr Cloud pods
    for index, pod in enumerate(solrCloud_pods):
        port_forward_command = f"kubectl port-forward {pod} 8983:8983"
        title = f"SolrCloud"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Open terminals as tabs in the same window
    subprocess.Popen(["xfce4-terminal"] + terminal_commands)

    # Filter pods containing 'kubernetes-zookeeper'
    zoo_keeper = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-zookeeper' in line]

    # Port forward for Solr Cloud pods
    for index, pod in enumerate(zoo_keeper):
        port_forward_command = f"kubectl port-forward {pod} 9181:9181"
        title = f"ZooKeeper"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Open terminals as tabs in the same window
    subprocess.Popen(["xfce4-terminal"] + terminal_commands)

    # Filter pods containing 'kubernetes-solr-zookeeper'
    solr_zoo_keeper = [line.split()[0] for line in get_pods_output.split('\n') if 'kubernetes-solrcloud-zookeeper-0' in line]

    # Port forward for Solr Cloud pods
    for index, pod in enumerate(solr_zoo_keeper):
        port_forward_command = f"kubectl port-forward {pod} 9983:2181"
        title = f"SolrZooKeeper"
        terminal_commands.extend(["--tab", f"--title={title}", "--command", port_forward_command])

    # Open terminals as tabs in the same window
    subprocess.Popen(["xfce4-terminal"] + terminal_commands)


vmSubIp = get_input("Enter vm ip: ", str)

if not vmSubIp:
    hostname = "vm085.eng.cz.zoomint.com"
elif len(vmSubIp) == 2:
    hostname = "vm0%s.eng.cz.zoomint.com" % vmSubIp
else:
    hostname = vmSubIp

# Provide remote server details and paths
# hostname = 'vm085.eng.cz.zoomint.com'
username = 'root'
password = 'zoomcallrec'
remote_path = '.kube/config'
local_path = '/home/dmytro/.kube/config'

# Call the function to copy the file
copy_file_from_remote(hostname, username, password, remote_path, local_path)
# close_terminal_window_by_title('SolrZooKeeper')
port_forward_all()