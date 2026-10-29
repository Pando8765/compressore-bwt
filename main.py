#variabile stringa
stringa= input("inserisci la stringa: ")
stringa=stringa+"$"


#creazione della lista di stringhe 
listaStringhe=[]
listaStringhe.append(stringa)
i=0
for a in stringa:
    a=listaStringhe[i]
    listaStringhe.append(a[1:]+a[0])
    i=i+1  

listaStringhe.pop()
print("la lista della stringhe non ordinata è: \n",listaStringhe)



#riordinamento alfabetico
listaStringhe.sort()
print("la lista della stringhe ordinata è: \n", listaStringhe)    