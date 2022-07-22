from codecs import utf_8_decode
from encodings import utf_8, utf_8_sig
from socket import *

serverPort = 12000
sock = socket(AF_INET, SOCK_STREAM)

sock.bind(('', serverPort))
sock.listen(1)

while True:
    print('Pronto para servir!')
    connectionSocket, addr = sock.accept()
    if connectionSocket:
        print(f'Solicitacao recebida de {addr}')
    try:
        req = connectionSocket.recv(1024)
        print(req)
        filename = req.split()[1]
        if filename == b'/':
            filename = b'/index.html'
        f = open(filename[1:])
        output = f.read()
        f.close()

        connectionSocket.send(b'HTTP/1.0 200 OK\r\n\r\n')
        for i in range(0, len(output)):
            connectionSocket.send(output[i].encode())
        connectionSocket.close()
    except IOError:
        string404 = '404 Not Found'
        print(string404)
        connectionSocket.send(string404.encode())
        connectionSocket.close()
    print('...')

    connectionSocket.close()

