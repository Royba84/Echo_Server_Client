#Client for echo server, Roy Ben Avraham 23/02/2023, 18:40

#Client Side:

import socket
HOST="127.0.0.1" #Server's hostname or IP address
PORT=65432 #The port used by the server 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall("Hello comrade, it's Roy")
    data=s.recv(1024)

print(f"Received {data!r}")