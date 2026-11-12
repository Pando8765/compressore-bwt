import socket

#creazione socket del client
client_sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sock.connect(("127.0.0.1", 5000))

#input della stringa
stringa_originale=input("inserisci la stringa: ")


#invio stringa
client_sock.sendall(stringa_originale.encode())

#ricezione stringa modificata
stringa_modificata=client_sock.recv(1024)
stringa_modificata=stringa_modificata.decode()

#print 
print (stringa_modificata)



client_sock.close()