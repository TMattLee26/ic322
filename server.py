"""
Author: MIDN 3/C Tristan Lee
Project: Build a Server
Description: A simple HTTP server to serve HTML and Image (jpg/png) Files
Usage: python3 server.py
"""
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

server_port = 12000
server_socket.bind(('', server_port))
server_socket.listen(1)
print('The server is ready to receive')

while True:
    conn_socket, addr = server_socket.accept()
    print('Connected to:', addr)

    try:
        request = conn_socket.recv(1024).decode()

        # Get the filename from the HTTP request
        request_parts = request.split()
        if len(request_parts) >= 2:
            filename = request_parts[1][1:]
        else:
            pass

        # Extract file extension
        extension = filename.split(".")[-1]

        response = "HTTP/1.1 200 OK\r\n"

        try:
            if extension in ["png", "jpg", "jpeg"]:
                # Add Content-type header field for images
                response += f"Content-type: image/{extension}\r\n\r\n"
                mode = "rb"
            else:
                # Add Content-type header field for other file types
                response += "Content-type: text/html\r\n\r\n"
                mode = "r"

            with open(filename, mode) as file:
                fcontents = file.read()

            # Send the HTTP response message header
            conn_socket.send(response.encode())

            # Send the HTTP response message entity body
            conn_socket.sendall(fcontents.encode() if mode == "r" else fcontents)

        except FileNotFoundError:
            # Send 404 status code and serve the 404 HTML page
            response = "HTTP/1.1 404 Not Found\r\n\r\n"
            with open("404.html", "r") as file:
                fcontents = file.read()
                
            conn_socket.send(response.encode())
            conn_socket.sendall(fcontents.encode())

    finally:
        # Close client socket
        conn_socket.close()

# Close the server socket
server_socket.close()
