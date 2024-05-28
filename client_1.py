import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost",9999))

while True:
    send_data = input("Enter data to send to server: ")
    client.send(send_data.encode())
    received = client.recv(1024).decode()
    print(received)