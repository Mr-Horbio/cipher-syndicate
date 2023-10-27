import requests
import socket
import pyfiglet

text = "syndicate"
ascii_banner = pyfiglet.figlet_format(text)
print(ascii_banner)
Domain = input("Enter your domain: ")

def subfinder():
    sub_domain = "word.txt"

    with open(sub_domain, "r") as file:
        file1 = file.read().splitlines()  # Split the lines in the file into a list

    for sub in file1:
        url = f"https://{sub}.{Domain}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
            if response.status_code == 200:
                print(f"Found: {url}")
        except requests.RequestException as e:
            print(f"Error with {url}: {e}")

def scnni(domain):
    open_ports = []

    for port in range(1, 1025):  # Scan common ports (1-1024)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Adjust the timeout as needed
            result = sock.connect_ex((domain, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
            sock.close()
        except (socket.timeout, ConnectionRefusedError):
            pass

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    subfinder()
    scnni(Domain)
