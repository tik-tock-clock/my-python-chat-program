import socket
import threading

HOST = ""
PORT = 1511
ADDR = (HOST, PORT)

clients = {}

def broadcast(msg):
    for sock in clients:
        sock.send(msg.encode())
    print(msg)

def recieve(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if data.decode() != "/quit":
                broadcast(f"{clients[conn]}: {data.decode()}")
            else:
                broadcast(f"{clients[conn]} has left the chat.")
                del clients[conn]
                break

        except OSError:
            break

def accept_connection():
    while True:
        new_name = False
        conn, addr = s.accept()
        conn.send("Please enter a display name:".encode())
        data = conn.recv(1024).decode()
        clients[conn] = data
        broadcast(f"{clients[conn]} has joined.")
        threading.Thread(target=recieve, args=(conn, addr)).start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

if __name__ == "__main__":
    s.listen(6)
    print(f"Server listening on {socket.gethostname()}:{PORT}")
    accept_thread = threading.Thread(target=accept_connection)
    accept_thread.start()
    accept_thread.join()
    s.close()