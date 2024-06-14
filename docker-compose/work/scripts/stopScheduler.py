import psutil

def release_ports(ports):
    for port in ports:
        # Find process using the port
        for conn in psutil.net_connections():
            if conn.laddr.port == port:
                process = psutil.Process(conn.pid)
                print(f"Port {port} is in use by process {process.pid}. Releasing...")
                # Terminate the process
                process.terminate()
                print(f"Port {port} released.")
                break
        else:
            print(f"Port {port} is not in use.")

if __name__ == "__main__":
    # List of ports to release
    ports_to_release = [
        8105
    ]
    release_ports(ports_to_release)