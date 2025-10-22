import socket  # noqa: F401


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept() # wait for client

    connection.sendall(b"+PONG\r\n") # hard coding PONG response


if __name__ == "__main__":
    main()
