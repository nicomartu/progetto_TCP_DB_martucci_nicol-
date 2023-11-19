import socket

HOST = 'localhost'   
PORT = 50010    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    print('Received: ', data.decode())
    testo = input("\ninserisci qualcosa: ").encode()
    s.send(testo)


s.close()