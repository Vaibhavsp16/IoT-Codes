import socket
import pickle

# Custom class
class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

# Create object
obj = DataObject("Student", [10, 20, 30, 40])

# Serialize object
data = pickle.dumps(obj)

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5001))

# Send object
client.send(data)

# Receive response
response = client.recv(1024).decode()

print(response)

client.close()
