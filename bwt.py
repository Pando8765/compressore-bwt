def bwt(stringa): 
    #variabile stringa
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

    #ordinamento a bolle
    n=len(listaStringhe)
    for i in range(n):
        for j in range(0,n-i-1):
            if listaStringhe[j]>listaStringhe[j+1]:
                temp=listaStringhe[j]
                listaStringhe[j]=listaStringhe[j+1]
                listaStringhe[j+1]=temp
    
    print("la lista della stringhe ordinata è: \n", listaStringhe)    

    #creazione stringa ordinata 
    stringaOrdinata=""
    for a in listaStringhe:
        stringaOrdinata=stringaOrdinata + str(a[-1])
        
    return (stringaOrdinata) 