import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, address = server_socket.accept() # wait for client

    while True:
        data = conn.recv(1024)
        
        if not data:
            break

        if data == b"*1\r\n$4\r\nPING\r\n":
            conn.sendall(b"+PONG\r\n")

    conn.close()

if __name__ == "__main__":
    main()
