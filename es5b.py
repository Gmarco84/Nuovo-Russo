# definisco la classe CSVFile()
class CSVFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

        # variabile per capire se il file è leggibile o no
        self.leggibile=True

        # provo a aprire il file
        try:
            my_file=open(self.name,'r')
            # se lo apre provo a controllare se ha almeno
            # una linea
            my_file.readline()
            
        # eccezione
        except Exception as e:
            # stampa messaggio di errore con l'Exception
            print('Errore file : {}'.format(e))

            # file non leggibile, variabile impostata
            # su False
            self.leggibile=False

    # definisco il metodo get_data()
    def get_data(self):

        # controllo se il file è leggibile
        if not self.leggibile:
            # stampa messaggio di errore
            print('Errore, file non leggibile')
            # restituisce niente
            return None

        # altrimenti
        else:

            # apro il file
            my_file=open(self.name,'r')

            # creo la lista vuota che conterrà gli elementi
            # del file
            lista=[]

            # per ogni linea del file
            for line in my_file:
                # divido gli elementi tramite split ','
                elementi=line.split(',')

                # l'ultimo elemento della lista contiene 
                # anche il carattere '\n', in questo modo
                # si posiziona sull'ultimo elemento e 
                # toglie il carattere '\n'
                elementi[-1]=elementi[-1].strip()
                print(elementi)
                
                # se non si trova sulla riga di
                # intestazione può aggiungere elementi
                # alla lista
                if elementi[0]!='Date':
                    # aggiunge alla lista igli elementi 
                    # trovati
                    lista.append(elementi)


            # chiude il file
            my_file.close()

            # restituisce la lista di valori creata
            return lista

# estendo l'oggetto CSVFile
class NumericalCSVFile(CSVFile):

    # definisco il metodo get_data()
    def get_data(self):

        # creo variabile a cui assegno la lista restituita
        # da super().get_data()
        lista=super().get_data()
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
