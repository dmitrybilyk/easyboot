import subprocess
import platform
import time

def close_terminal_window_by_title(window_title, exclude_title='run-port-forward-5000'):
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

def open_ssh_tunnel(vmSubIp):
    # SSH command with password
    if not vmSubIp:
        hostname = "vm085.eng.cz.zoomint.com"
    elif len(vmSubIp) == 2:
        hostname = "vm0%s.eng.cz.zoomint.com" % vmSubIp
    else:
        hostname = vmSubIp

    host = hostname
    port = 5000
    ssh_command = f'sshpass -p zoomcallrec ssh -L {port}:127.0.0.1:{port} root@%s' % host

    # Command to open a new terminal and run the SSH command
    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', (f'{port} %s' % vmSubIp)])
    else:
        print("Unsupported platform for xfce4-terminal.")

if __name__ == "__main__":
    close_terminal_window_by_title('5000')
    time.sleep(1)
    vmSubIp = get_input("Enter vm ip: ", str)
    open_ssh_tunnel(vmSubIp)
