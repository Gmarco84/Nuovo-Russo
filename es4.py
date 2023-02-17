# definisco la classe CSVFile()
class CSVFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

    # definisco il metodo get_data()
    def get_data(self):
        # prova ad aprire il file
        try:
            my_file=open(self.name,'r')
        # se non  riesce ad aprire restituisce None
        except:
            return None

        # se è riuscito ad aprire il file
        # crea una lista vuota
        lista=[]

        # per ogni linea del file
        for line in my_file:
            # prova
            try:
                # divide ogni elemento della riga dal 
                # carattere '\n'
                riga=line.split('\n')

                # splitta la prima parte della riga dal 
                # carattere ','
                elementi_riga=riga[0].split(',')

                # se non si trova sulla riga di intestazione
                if elementi_riga[0]!='Date':
                    # aggiunge alla lista gli elementi
                    # della riga
                    lista.append(elementi_riga)
            # altrimenti va avanti
            except:
                pass

        # restituisce la lista creata
        return lista


# file='shampoo_sales.csv'
# prova=CSVFile(file)
# l=prova.get_data()
# if l:
#     for item in l:
#         print(item)
# else:
#     print("Vuota")