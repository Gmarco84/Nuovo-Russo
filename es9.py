class Model():
    
    def fit(self,data):
        # Fit non implementato nella classe base
        raise NotImplementedError("Metodo non implementato")

    def predict(self,data):
        # Predict non implementato nella classe base
        raise NotImplementedError("Metodo non implementato")

class IncrementModel(Model):
    # definisco metodo per calcolo incremento medio 
    # di una lista generica
    def incremento_medio(self,lista):
        # contrlla che la lista passata sia effettivamente
        # una lista
        if type(lista)!=list:
            # alza eccezione
            raise TypeError("Lista non valida")

        # continua con il procedimento
        # prev_value memorizza il valore precedente nella lista
        prev_value=None
        # s per sommare gli incrementi
        s=0
        # i per tener conto dei valori validi nella lista
        i=0
        # per ogni elemento della lista
        for item in lista:
            # controlla se item è un valore valido
            if item==None:
                raise TypeError("Valore non valido")
            # altrimenti
            else:
                # controlla se item è una stringa e nel caso 
                # la sanitizza
                if type(item)==str:
                    item=stem.strip()
                # prova a convertire il valore in float
                try:
                    item=float(item)
                # eccezione
                except TypeError:
                    print("Valore non valido")
                    # passa al successivo
                    continue 

                # se è riuscito a convertire
                # controlla se non è il primo valore elaborato
                if prev_value!=None:
                    s+=item-prev_value

                # assegna a prev_value il valore di item
                prev_value=item
                # aggiorno il contatore dei valori
                i+=1
        
        # controlla se ha processato valori validi
        if i==0:
            raise Exception("Nessun valore valido nella lista")
        if i==1:
            raise Exception("Elementi insufficienti nella lista")

        # restituisce il valore calcolato
        return int(( s / (i-1) ))
                
    # definisce metodo predict()
    def predict(self,data):
        inc_m=self.incremento_medio(data)
        
        return data[-1]+inc_m

# estendo IncrementModel()
class FitIncrementModel(IncrementModel):
    # variabile che contiene incremento medio di tutto il dataset
    global_agv_increment=None
    # definisco il metodo fit()
    def fit(self,data):
        # calcola incremento medio di tutti il dataset
        self.global_agv_increment=self.incremento_medio(data)
        
    # definisco il metodo predict()
    def predict(self,dati):
        incremento=self.incremento_medio(dati)
 
        valore=(self.global_agv_increment + incremento)/2
   
        if incremento<0:
            valore=-valore
  
        return dati[-1]+valore
      
        

f=FitIncrementModel()
dati=[8,19,31,41]
f.fit(dati)
print(f.predict([60,55,50]))

#data=[50,52,60]
#l=dati+data
#prediction=f.predict(data)


#from matplotlib import pyplot
#pyplot.plot(l+[prediction], color='tab:red')
#pyplot.plot(l,color='tab:blue')
#pyplot.show()