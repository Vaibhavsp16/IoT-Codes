import socket
import threading

clients = {}
queue = []
busy = False

def grant(pid):
    clients[pid].send(b"GRANT")
    print("GRANT -> P%d" % pid)

def handle(conn):
    global busy

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            cmd, pid = msg.split()
            pid = int(pid)

            clients[pid] = conn

            if cmd == "REQUEST":
                print("REQUEST from P%d" % pid)

                if busy:
                    queue.append(pid)
                else:
                    busy = True
                    grant(pid)

            elif cmd == "RELEASE":
                print("RELEASE from P%d" % pid)

                if queue:
                    grant(queue.pop(0))
                else:
                    busy = False

        except:
            break

    conn.close()

server = socket.socket()
server.bind(("localhost", 9000))
server.listen(5)
server.settimeout(1)

print("Coordinator started...")

try:
    while True:
        try:
            conn, addr = server.accept()
            print("Process connected:", addr)
            threading.Thread(target=handle, args=(conn,), daemon=True).start()
        except socket.timeout:
            pass

except KeyboardInterrupt:
    print("\nCoordinator stopped.")

finally:
    for c in clients.values():
        c.close()
    server.close()