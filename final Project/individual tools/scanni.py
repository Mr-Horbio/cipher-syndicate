import socket
url = input("Enter the url:")
def scnni():
 def scan_port(host, port):
     try:
         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         sock.settimeout(1)  # Adjust the timeout as needed
         sock.connect((host, port))
         sock.close()
         return True
     except (socket.timeout, ConnectionRefusedError):
         return False

 def main():
    target_host = url # Replace with the target hostname or IP address
    open_ports = []

    for port in range(1, 1025):  # Scan common ports (1-1024)
        if scan_port(target_host, port):
            print(f"Port {port} is open")
            open_ports.append(port)

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

 if __name__ == "__main__":
    main()

scnni()
