import subprocess
import platform

subHost = '85'
hostname = "vm0%s.eng.cz.zoomint.com" % subHost
def open_ssh_tunnel():
    # SSH command with password

    host = hostname
    port = 5000
    ssh_command = f'sshpass -p zoomcallrec ssh -L {port}:127.0.0.1:{port} root@%s' % host

    # Command to open a new terminal and run the SSH command
    if platform.system() == "Linux":
        subprocess.Popen(['xfce4-terminal', '--command', ssh_command, '--title', (f'{port} %s' % subHost)])
    else:
        print("Unsupported platform for xfce4-terminal.")

if __name__ == "__main__":
    open_ssh_tunnel()
