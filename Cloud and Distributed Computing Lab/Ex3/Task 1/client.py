import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 6000))

name = input("Enter your name: ")
client.send(name.encode())

def receive():
    while True:
        try:
            print(client.recv(1024).decode())
        except:
            break

threading.Thread(target=receive, daemon=True).start()

print("Type messages (type 'exit' to quit)")

while True:
    msg = input()

    if msg == "exit":
        break

    client.send(msg.encode())

client.close()