
from socket import *

serverName = 'localhost'
serverPort = 12000

sentence = ''
while(sentence != '0'):
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((serverName, serverPort))
    sentence = input('Input lowercase sentence:')
    clientSock.send(sentence.encode())
    modifiedSentence = clientSock.recv(1024)
    print('From Server:', modifiedSentence.decode())
clientSock.close()
