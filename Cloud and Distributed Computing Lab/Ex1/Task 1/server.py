import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind host and port
server.bind(("localhost", 5000))

# Listen for client
server.listen(1)

print("Server is waiting for connection...")

# Accept client
client, address = server.accept()
print("Connected to:", address)

# Receive message
message = client.recv(1024).decode()

print("Received:", message)

# Convert received numbers into list
numbers = list(map(int, message.split()))

# Find sum
total = sum(numbers)

# Send result back
client.send(str(total).encode())

# Close connection
client.close()
server.close()
