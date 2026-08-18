import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("localhost", 5000))

# Input numbers
message = input("Enter numbers separated by space: ")

# Send message
client.send(message.encode())

# Receive answer
result = client.recv(1024).decode()

print("Sum from server:", result)

# Close connection
client.close()
