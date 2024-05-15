import sys
import socket

def scan_port(ip, port, timeout):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        # Try to connect to the port
        s.connect((ip, port))
        return True
    except:
        return False
    finally:
        s.close()

def main(ip):
    # Ports to scan
    ports = [80, 443, 22, 25, 53]
    # Timeout in seconds
    timeout = 0.1

    for port in ports:
        if scan_port(ip, port, timeout):
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")

if __name__ == "__main__":
    # Check if a parameter was provided
    if len(sys.argv) > 1:
        # Extract the ipAddress from the command line arguments
        ip = sys.argv[1]
        # Call the main function with the ipAddress
        main(ip)
    else:
        print("No ip address provided.")

# Should be able to pass an IP address as a command-line argument. (1.5 marks) - DONE

# Scan only ports 80,443, 22,25 and 53. (1.5 marks)

# Set a default timeout for port response to be 0.1 second (100ms). (1.5 marks)

# A port is considered to be open when the connection is established, else an exception is raise. Use try...catch to catch the exception. (1.5 marks)

# Print the open ports for the given IP address. (4 marks)