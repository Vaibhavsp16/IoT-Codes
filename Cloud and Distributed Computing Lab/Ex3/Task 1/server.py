import socket
import threading

clients = []

def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_client(conn, addr):
    name = conn.recv(1024).decode()
    print(name, "joined")

    broadcast(name + " joined the chat", conn)

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            print(name + ":", msg)
            broadcast(name + ": " + msg, conn)

        except:
            break

    if conn in clients:
        clients.remove(conn)

    conn.close()
    print(name, "left")
    broadcast(name + " left the chat")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6000))
server.listen()
server.settimeout(1)      # Check every 1 second

print("Server started... Press Ctrl+C to stop.")

try:
    while True:
        try:
            conn, addr = server.accept()
            clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\nStopping server...")

finally:
    for client in clients:
        client.close()
    server.close()
    print("Server stopped.")