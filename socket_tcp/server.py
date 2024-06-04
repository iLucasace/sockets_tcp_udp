import socket

# Define constants
IP = ''
PORT = 8000  

# Create TCP socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
SERVER = (IP, PORT) 
tcp.bind(SERVER)

# Listen for incoming connections
tcp.listen(1) 

# Accept a connection
conection, client = tcp.accept()
print("Client", client, "conected.")

try:
    while True:
        # Receive data from the client
        message = conection.recv(1024)
        
        if not message:
            break
        
        # Print received message
        print("Message received from the client", client, ":", message.decode())

finally:
    # Close the connection
    conection.close()
