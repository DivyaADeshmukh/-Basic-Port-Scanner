import socket

def scan_ports(ip, start_port, end_port):
    """Scans open ports on a given IP address within a specified range."""
    open_ports = []

    # Validate input port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Invalid port range. Please enter a valid range (1-65535).")
        return

    print(f"Scanning {ip} for open ports from {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Timeout for connection attempt
            result = sock.connect_ex((ip, port))  # Returns 0 if the port is open
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            return
        except socket.gaierror:
            print("Error: Invalid IP address.")
            return
        except socket.error:
            print("Error: Unable to connect to the target.")
            return

    # Display results
    if open_ports:
        print("\nOpen Ports Found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found in the given range.")

# User input
if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scan_ports(target_ip, start_port, end_port)
    except ValueError:
        print("Error: Please enter valid numeric port values.")
