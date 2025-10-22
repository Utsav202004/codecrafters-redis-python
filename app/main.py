import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept() # wait for client

    while connection.recv(1024):
        data = connection.recv(1024)
        if data == b"*1\r\n$4\r\nPING\r\n":
            connection.sendall(b"+PONG\r\n")


if __name__ == "__main__":
    main()
