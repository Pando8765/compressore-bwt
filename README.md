BWT client-server

Programma in Python che calcola la trasformata di Burrows-Wheeler (BWT) di una stringa usando i socket. Il client invia una stringa al server, il server calcola la BWT e rimanda indietro il risultato.

File: main.py contiene la funzione bwt server.py e' il server, riceve la stringa e risponde con la BWT client.py e' il client, invia la stringa e stampa il risultato

Come si usa: Prima si avvia server.py, poi in un secondo terminale si avvia client.py e si inserisce la stringa. Il server ascolta su 127.0.0.1, porta 5000.

Esempio: input banana, output annb$aa