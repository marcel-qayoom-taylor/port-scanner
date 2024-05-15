import sys
import socket

def scan_port(ipAddress, port, timeout=0.1):
    # Create a socket object
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Apply timeout
    socket.settimeout(timeout)

    try:
        # Try to connect to the port
        socket.connect((ipAddress, port))
        return True
    except:
        return False
    finally:
        socket.close()

def main(ipAddress):
    # Ports to scan
    ports = [80, 443, 22, 25, 53]
    # Timeout in seconds
    timeout = 0.1

    for port in ports:
        if scan_port(ipAddress, port, timeout):
            print(f"Port {port} is open on {ipAddress}")

if __name__ == "__main__":
    # Check if a parameter was provided
    if len(sys.argv) > 1:
        # Extract the ipAddress from the command line arguments
        ipAddress = sys.argv[1]
        # Call the main function with the ipAddress
        main(ipAddress)
    else:
        print("No ip address address provided.")
