# definisco la classe CSVFile()
class CSVFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

        # variabile per capire se il file è leggibile o no
        self.leggibile=True

        # controlla se il nome del file è una stringa
        # oppure no, in tal caso alza eccezione
        if type(self.name)!=str:
            self.leggibile=False
            raise Exception('Errore, nome file non valido')
            return None
        # provo a aprire il file
        try:                
            my_file=open(self.name,'r')
            # se lo apre provo a controllare se ha almeno
            # una linea
            my_file.readline()
            self.leggibile=True
            
        # eccezione
        except Exception as e:
            print('Errore : {}'.format(e))
            self.leggibile=False
            return None
            
    # definisco il metodo get_data()
    def get_data(self, start=None, end=None):

        # controllo se il file è leggibile
        if not self.leggibile:
            # stampa messaggio di errore
            raise Exception('Errore, file non leggibile')
            # restituisce niente
            return None

        # altrimenti
        else:

            # apro il file
            my_file=open(self.name,'r')
            
            # contatore righe file
            tot_righe=0
            
            # ciclo per contare linee del file
            for line in my_file:
                tot_righe+=1

            # chiude il file
            my_file.close()
            
            # e lo riapre
            my_file=open(self.name,'r')

            # controlla i valori di START e END
            # controlla se START è una stringa
            if type(start)==str:
                # sanitizza 
                start=start.strip()
                # se è convertibile in intero
                if int(start):
                    # converte in inter
                    start=int(start)
                else:
                    # altrimenti alza eccezione
                    raise Exception('Errore conversione START')
              
            # controlla se START <1 oppure =None, in tal caso
            # assegna di default 1
            if start==None:
                print('Valore di START non valido')
                print('Assegno di default il valore 1')
                start=1

            # se START<1 oppure >tot_righe alza eccezione
            if start<1 or start>tot_righe:
                raise ValueError('Valore non valido di START')

            # controlla se END è una stringa
            if type(end)==str:
                # sanitizza
                end=end.strip()
                # controlla se è convertibile
                if int(end):
                    # e lo converte
                    end=int(end)
                else:
                    # altrimenti alza eccezione
                    raise Exception('Valore di END non valido')
            # controlla se END <1 oppure =None, in tal caso
            # assegna di default tot_righe
            if end==None or end<1:
                print('Valore di END non valido')
                print('Assegno di default il n. di righe del file : {}'.format(tot_righe))
                end=tot_righe

            # se END_tot_righe alza eccezione
            if end>tot_righe:
                raise ValueError('END > tot_righe')
                
            # controlla se START>END, nel caso inverte
            if start>end:
                raise ValueError('Errore : Start > End')                   

            # creo la lista vuota che conterrà gli elementi
            # del file
            lista=[]
            # per ogni linea del file
            i=0
            for line in my_file:
                i+=1
                # divido gli elementi tramite split ','
                elementi=line.split(',')

                # l'ultimo elemento della lista contiene 
                # anche il carattere '\n', in questo modo
                # si posiziona sull'ultimo elemento e 
                # toglie il carattere '\n'
                elementi[-1]=elementi[-1].strip()
                
                
                # se non si trova sulla riga di
                # intestazione può aggiungere elementi
                # alla lista
                #if elementi[0]!='Date' and start<=i and end>=i:
                if start<=i and end>=i:
                    # aggiunge alla lista igli elementi 
                    # trovati
                    if elementi[0]!='Date':
                        lista.append(elementi)


            # chiude il file
            my_file.close()

            return lista

           

                
# estendo l'oggetto CSVFile
class NumericalCSVFile(CSVFile):

    # definisco il metodo get_data()
    def get_data(self, *args, **kvargs):

        # creo variabile a cui assegno la lista restituita
        # da super().get_data()
        lista=super().get_data(*args,**kvargs)
        # creo lista vuota

        lista_num=[]

        # per ogni elemento della lista
        for item in lista:
                
            # creo lista vuota per inserire i valori
            # convertiti di ogni riga
            item_convertito=[]

            # per ogni valore di item, in più creo
            # un indice
            for i,valore in enumerate(item):

                # controlla se si trova sul primo
                # valore, se così fosse lo aggiunge
                # alla lista conv_item senza modifiche
                if i==0:
                    item_convertito.append(valore)

                # altrimenti
                else:
                    # prova a convertire il valore ed
                    # aggiungerlo alla lista conv_item
                    try:
                        item_convertito.append(float(valore))

                    # eccetto
                    except Exception as e:
                        # stampa errore
                        print('Errore : {}'.format(e))

                        # interrompe il ciclo for
                        break
           
            # controlla se la lunghezza di 
            #item = item_convertito,
            # se uguale è riuscito a convertire tutti i 
            # valori e quindi lo aggiunge alla lista_num,
            # altrimenti salta la riga
            if len(item)==len(item_convertito):
                lista_num.append(item_convertito)

        # restituisce la lista_num
        return lista_num

#f='shampoo_sales.csv'
#l=CSVFile(f)
#print('---------------------------')
#for item in l.get_data('ciao','2r'):
#   print(item)