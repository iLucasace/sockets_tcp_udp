import socket

# Server IP address and port
IP = ''                                
# Server IP address, '' means it will listen on all interfaces

PORT = 5000
# Port that the server will listen on
                                

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP and port to start listening
MY_SERVER = (IP, PORT) 
udp_socket.bind(MY_SERVER) 

try:
    # Receive data from the socket
    message_received, client_address = udp_socket.recvfrom(1024)
    # recvfrom returns a tuple (string, address) where string is the received data and address is the address of the socket that sent the data

    print("Received:", message_received, "from client:", client_address)
    # client_address is the address of the socket that sent the data.

finally:
    # Close the socket
    udp_socket.close()