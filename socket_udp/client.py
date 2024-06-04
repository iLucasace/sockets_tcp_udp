import socket

# Server IP address and port
SERVER_IP = '127.0.0.1'             
SERVER_PORT = 5000                  

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Destination (IP + port) of the server
DESTINATION = (SERVER_IP, SERVER_PORT)

# Input message from user
message = input("Enter the message to send (type 'exit' to close connection): ")
        
# Convert message to bytes and send it to the destination
udp_socket.sendto(bytes(message, "utf8"), DESTINATION)

# Close the socket
udp_socket.close()
