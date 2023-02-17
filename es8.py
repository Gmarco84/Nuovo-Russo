class Model():
    
    def fit(self,data):
        # Fit non implementato nella classe base
        raise NotImplementedError("Metodo non implementato")

    def predict(self,data):
        # Predict non implementato nella classe base
        raise NotImplementedError("Metodo non implementato")

class IncrementModel(Model):
    # definisce metodo predict()
    def predict(self,data):
        # controlla se data è una lista
        if type(data)!=list:
            raise TypeError("Lista non valida")
        # prev_value memorizza il valore della lista precedente
        prev_value=None
        # s per sommare gli incremente
        s=0
        # i per tener conto dei valori della lista letti e validi
        i=0
        # per ogni elemento della lista
        for item in data:
            # Logica per la predizione
            # controlla se il valore di item è corretto
            if item==None:
                # altrimenti alza eccezione
                raise TypeError("Valore non valido")
            # prova a capire se è corretto il valore della lista
            # controlla se item è na stringa
            if type(item)==str:
                # nel caso sanitizza
                item=item.strip()
     
            # prova   
                # converte il valore della lista in float e
                # lo assegna ad n
            
            try:    
                n=float(item)
          
            # eccezione
            except TypeError:
                # stampa messaggio di errore
                print(f"valore della lista '{item }' non corretto")
               
                # passa al prossimo item della lista
                continue

            # se conversione è andata a buon fine 
            # controlla se si trova sul primo valore della lista
            # in tal caso non succede nulla e lo associa 
            # a prev_ value
            if prev_value==None:
                prev_value=n
            # altrimenti
            else:
                # ad s aggiunge la differenza tra il valore letto
                # ed il valore precedente
                s+=n-prev_value
                # a prev_value assegna il valore di item
                prev_value=n

            # incremente il contatore dei valori corretti
            i+=1
                    

        print(f"prev = {prev_value} - i = {i} - s = {s}")
        # se non ci sono valori validi nella lista
        # alza eccezione
        if i==0:
            raise Exception("Nessun valore valido nella lista")

        # se la lista è composta da un solo valore 
        # alza eccezione
        if i==1:
            raise Exception("Numero valori nella lista non validi")

        # calcoclo di predicttion
        prediction=prev_value+(s/(i-1))

        # restituisce prediction
        return prediction

#f=IncrementModel()
#dati=[None,2,3]
#print(f.predict(dati))