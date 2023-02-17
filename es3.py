# definisco la funzione sum_csv a cui passo come parametro
# il nome del file da utilizzare
def sum_csv(file_name):
    
    # provo ad aprire il file in lettura
    try:
        my_file=open(file_name,'r')
        
    except:
        # se non riesce ad aprire restituisce None
        return None

    # se è riuscito ad aprire il file

    # inizializzo somma=0
    somma=0.0
    # inizializzo conta=0 per contare gli elementi sommati
    # se conta=0 non ha contato nessun elemento
    conta=0

    # per ogni linea del file
    for line in my_file:
        # crea la lista elementi_riga a cui assegna i valori
        # della linea del file, splittati da ','
        elementi_riga=line.split(',')

        # se non si trova sulla riga di intestazione...
        if (elementi_riga[0]!='Date'):
            # prova a
            try:
                # sommare a somma il valore in float del
                # secondo elemento della riga
                somma+=float(elementi_riga[1])
                # incrementa conta di 1
                conta+=1
            # altrimenti va avanti
            except:
                pass

    # chiude il file
    my_file.close()

    # se ha sommato almeno un valore
    if conta>0:
        #r restituisce la somma
        return somma
    else:
        # altrimenti restituisce None
        return None

#file='shampoo_sales.csv'

#somma=sum_csv(file)

#print('Somma = ', somma)