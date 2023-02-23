# definisco la classe ExamException()
class ExamException(Exception):
        pass
    
# definisco la classe CSVTimeSeriesFile()
class CSVTimeSeriesFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

        # per sapere se il file è leggibile 'True' oppure no 'False'
        self.leggibile=True

        # controlla se il nome del file è una stringa oppure no, in tal caso alza eccezione
        if type(self.name)!=str:
            # file non leggibile
            self.leggibile=False
            # alza eccezione
            raise Exception('Errore, nome file non valido')

        # provo a aprire il file
        try:                
            my_file=open(self.name,'r')
            # se lo apre provo a controllare se ha almeno una linea
            my_file.readline()

            # file leggibile
            self.leggibile=True
            
        # eccezione
        except Exception as e:
            # file non leggibile
            self.leggibile=False
            # stampa errore
            print(f'Errore : {e}')

            
    # definisco il metodo get_data()
    def get_data(self):

        # controllo se il file è leggibile
        if not self.leggibile:
            # stampa messaggio di errore
            raise Exception('Errore, file non leggibile')
            # restituisce None
            return None

        # altrimenti
        else:
            # apro il file
            my_file=open(self.name,'r')             

            # creo la lista vuota che conterrà gli elementi del file
            lista=[]
            # per ogni linea del file
            i=0
            for line in my_file:
                i+=1
                # divido gli elementi tramite split ','
                elementi=line.split(',')

                # l'ultimo elemento della lista contiene anche il carattere '\n', in questo modo
                # si posiziona sull'ultimo elemento e toglie il carattere '\n'
                elementi[-1]=elementi[-1].strip()
                
                # se non si trova sulla riga di intestazione può aggiungere elementi alla lista
                if elementi[0]!='date':
                    lista.append(elementi)

            # chiude il file
            my_file.close()

            # lista time_series che conterrà la lista appena creata ma con i valori dei passeggeri in intero
            time_series=[]

            # per ogni elemento della lista
            for item in lista:
                # conterrà elemento convertito di 
                item_convertito=[]

                # per ogni elemento di item, con indice per convertire il dato passeggeri
                for i, valore in enumerate(item):
                    # controlla se si trova sul primo valore, se così fosse lo aggiunge senza modifiche
                    # alla lista di appoggio item_convertito
                    if i==0:
                        item_convertito.append(valore)
                    elif i==1: # altrimenti 
                        try: #prova a convertire il secondo valore in intero
                            item_convertito.append(int(valore))
                        # eccetto
                        except Exception as e:
                            print(f"Errore :{e}")
                            # interrompo il ciclo e passo al prossimo item di lista
                            break
                            
                # controlla se item_convertito è composto da 2 valori
                if len(item_convertito)==2:
                    # se si, lo aggiunge a time_series
                    time_series.append(item_convertito)


            
                    
            # restituisce la lista time_series
            return time_series


file_name='data.csv'

my_file=CSVTimeSeriesFile(name='datacsv')
