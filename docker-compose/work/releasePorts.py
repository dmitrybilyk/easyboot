# import psutil
#
# # List of terminal names to close
# # terminals = ["Data", "Interaction", "Conversations", "Correlation",
# #              "ZQM Connector", "Scheduler", "Framework", "AutomatedQM", "PLAYER", "Speechrec"]
# terminals = ["mvn"]
#
# # Iterate through the list of terminal names
# for term_name in terminals:
#     # Search for processes containing the terminal name
#     for proc in psutil.process_iter(['pid', 'name']):
#         if term_name in proc.info['name']:
#             # Terminate the process
#             proc.kill()
#             print(f"Closed {term_name}")
#             break
#     else:
#         print(f"{term_name} not found")
#
#
# sudo fuser -k 8300/tcp
# sudo fuser -k 8081/tcp
# sudo fuser -k 8107/tcp
# sudo fuser -k 8108/tcp
# sudo fuser -k 8201/tcp
# sudo fuser -k 8207/tcp
# sudo fuser -k 8102/tcp
# sudo fuser -k 8105/tcp
# sudo fuser -k 8080/tcp

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
        8300,
        8081,
        8107,
        8108,
        8201,
        8102,
        8207,
        8105,
        8080]
    release_ports(ports_to_release)