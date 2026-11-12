import socket
from main import bwt

#creazione del socket server
socket_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(("127.0.0.1", 5000))

#ascolto del server
socket_server.listen()

#creazione di conn
conn, addr =socket_server.accept()

#ricezione
stringa_originale=conn.recv(1024)
stringa_originale=stringa_originale.decode()

#modifica
stringa_modificata=bwt(stringa_originale)

#invio stringa modificata
conn.sendall(stringa_modificata)