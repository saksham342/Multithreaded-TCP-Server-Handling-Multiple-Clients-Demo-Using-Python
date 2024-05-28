import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print(f'[*] Listening on {bind_ip}:{bind_port} ...... ' )

# This is a client side handling thread
def handle_client(client_socket):
    print(f"Accepted connection from {addr}") # we can also use client_socket.getpeername() to get client ip and port.

    while True:
        # Receive data from client
        request = client_socket.recv(1024).decode()
        if not request:
            break
        
        print(f"[*] Received message from {client_socket.getpeername()}: {request}")
        
        # Send back a response to the client
        message = f"Ack! The message received from you is: {request}"
        client_socket.send(message.encode())

    # Close the connection
    print(f"Closing connection with {client_socket.getpeername()}")
    client_socket.close()

while True:
    client, addr = server.accept()
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
