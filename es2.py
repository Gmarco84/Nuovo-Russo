# funzione sum_list a cui viene passato il marametro my_list
def sum_list(my_list):  
    # controllo se la lista è valida ...
    if my_list:
        # ... se è valida inizializzo somma=0 
        somma=0
        # per ogni elemento della lista
        for item in my_list:
            # provo a
            try:
                # sommare il valore della lista a somma
                somma+=item
            except:
                # altrimenti continua col prossimo elemento
                pass
        # restituisce la somma         
        return somma
        
    else:
        # ... se non è valida restituisce None
        return None

#lista=[]
#print(sum_list(lista))