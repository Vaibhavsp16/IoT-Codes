import socket
import pickle

# Custom class
class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5001))
server.listen(1)

print("Server waiting...")

client, address = server.accept()
print("Connected to:", address)

# Receive serialized object
data = client.recv(4096)

# Deserialize object
obj = pickle.loads(data)

print("Name:", obj.name)
print("Values:", obj.values)

# Calculate sum
total = sum(obj.values)

# Send response
response = f"Sum of values = {total}"
client.send(response.encode())

client.close()
server.close()
