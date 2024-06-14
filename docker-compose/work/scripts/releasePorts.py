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
        # 8300,
        8081,
        8107,
        8108,
        8201,
        8102,
        8207,
        8105,
        8080,
        8300,

        # 9983,
        # 8202,
        # 8301,
        # 15672,
        # 5672,
        # 5432,
        # 8983,
        # 9181
    ]
    release_ports(ports_to_release)