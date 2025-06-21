import socket
import time

class TL1Client:
    def __init__(self, host, port, timeout=10):
        """Initialize the TL1 client with host, port, and timeout."""
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None

    def connect(self):
        """Establish a connection to the TL1 server."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
        except socket.error as e:
            print(f"Connection failed: {e}")
            raise

    def send_command(self, command):
        """Send a TL1 command and return the response."""
        try:
            # Ensure command ends with semicolon as per TL1 convention
            if not command.endswith(";"):
                command += ";"
            # Send the command with newline
            self.socket.sendall((command + "\n").encode())
            print(f"Sent command: {command}")

            # Receive response
            response = ""
            start_time = time.time()
            while time.time() - start_time < self.timeout:
                data = self.socket.recv(4096).decode()
                response += data
                # Check for TL1 response termination (typically ends with ">")
                if ">" in data:
                    break
            return response
        except socket.error as e:
            print(f"Error sending command: {e}")
            raise

    def close(self):
        """Close the socket connection."""
        if self.socket:
            self.socket.close()
            print("Connection closed")
            self.socket = None

def main():
    # Example configuration
    HOST = "192.168.1.100"  # Replace with your device's IP
    PORT = 3083             # Common TL1 port, adjust as needed
    COMMANDS = [
        "RTRV-HDR:::1234;",  # Retrieve header
        "RTRV-ALM-ALL:::5678;",  # Retrieve all alarms
        "RTRV-INV:::9012;"   # Retrieve inventory
    ]

    # Initialize and connect the client
    client = TL1Client(HOST, PORT)
    try:
        client.connect()

        # Send each command and print the response
        for cmd in COMMANDS:
            response = client.send_command(cmd)
            print(f"Response for {cmd}:\n{response}\n")
            time.sleep(1)  # Brief pause between commands

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
