import socket
import sys
import time

ME = int(sys.argv[1])

client = socket.socket()
client.connect(("localhost", 9000))

print("Process", ME, "connected")

try:
    while True:

        input("Press Enter to request Critical Section...")

        client.send(f"REQUEST {ME}".encode())
        print("REQUEST sent")

        reply = client.recv(1024).decode()

        if reply == "GRANT":
            print(">>> P%d ENTERED Critical Section" % ME)

            time.sleep(5)

            print("<<< P%d LEFT Critical Section" % ME)

            client.send(f"RELEASE {ME}".encode())

except KeyboardInterrupt:
    print("\nProcess stopped.")

finally:
    client.close()