import subprocess
import platform

def open_ssh_tunnel():
    # SSH command with password
    ssh_command = 'sshpass -p zoomcallrec ssh -L 5000:127.0.0.1:5000 root@vm085.eng.cz.zoomint.com'

    # Command to open a new terminal and run the SSH command
    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', '5000 85'])
    else:
        print("Unsupported platform for xfce4-terminal.")

if __name__ == "__main__":
    open_ssh_tunnel()
