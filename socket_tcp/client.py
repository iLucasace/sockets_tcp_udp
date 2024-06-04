import socket

# Define server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000

# Create TCP socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
DESTINATION = (SERVER_IP, SERVER_PORT)
tcp.connect(DESTINATION)

try:
    while True:
        # Get user input for message
        message = input("Enter the message to send (or 'exit' to quit): ")
        
        # Check if user wants to quit
        if message.lower() == 'exit':
            break
        
        # Send the message to the server
        tcp.sendall(bytes(message, "utf8"))
  
finally:
    # Close the connection
    tcp.close()
