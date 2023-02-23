# definisco la classe ExamException() estensione di Exception()
class ExamException(Exception):
        pass
    
# definisco la classe CSVTimeSeriesFile()
class CSVTimeSeriesFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

            
    # definisco il metodo get_data()
    def get_data(self):

        # controllo se il file è leggibile

        # controlla se il nome del file è una stringa oppure no, se != stringa alza eccezione
        if type(self.name)!=str:
            # file non leggibile
            raise ExamException('Errore, nome file non valido')

        # provo ad aprire il file
        try:                
            my_file=open(self.name,'r')
            # se lo apre controlla che abbia almeno una linea
            my_file.readline()  
            # chiudo file
            my_file.close()
        # eccezione
        except Exception as e:
            # file non leggibile alza eccezione
            raise ExamException("Errore lettura file: {}".format(e))
            

        # apro il file
        my_file=open(self.name,'r')             

        # creo la lista vuota che conterrà gli elementi del file
        lista=[]
        # per ogni linea del file
        for line in my_file:
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

        # importo il modulo datetime per il controllo della correttezza del formato della data
        from datetime import datetime

        # per ogni elemento della lista
        for item in lista:
            # conterrà elemento convertito di 
            item_convertito=[]

            # per ogni elemento di item, con indice per convertire il dato passeggeri
            for i, valore in enumerate(item):
                # se si trova sul primo valore controlla che sia una data corretta
                if i==0:
                    try:    # prova a convertire in oggetto datetime, se la conversione riesce il formato data è corretto
                        datetime.strptime(valore,'%Y-%m')
                        # aggiunge la data alla lista di appoggio
                        item_convertito.append(valore)
    
                    except Exception:
                        # interrompe il ciclo e passa al prossimo elemento della lista
                        break
                        
                elif i==1: # altrimenti, se si trova sul secondo valore
                    try: #prova a convertire il secondo valore in intero
                        item_convertito.append(int(valore))
                 
                    except Exception as e:
                        print(f"Errore : {e}")
                        # interrompo il ciclo e passo al prossimo item di lista
                        break
                            
            # controlla se item_convertito è composto da 2 valori ['YYYY-MM',int]
            if len(item_convertito)==2:
                # se si, lo aggiunge a time_series
                time_series.append(item_convertito)


        # controlla se ci sono duplicati nella time_series
        for item in time_series:
            # conta elementi uguali, se = 1 non ci sono duplicati
            uguali=0
            for elemento in time_series:
                if item[0]==elemento[0]:
                    uguali+=1
                # esce dal ciclo se trova data duplicata
                if uguali>1:
                    break
            # se ha trovato più di un elemento uguale
            if uguali>1:
                # alza eccezione
                raise ExamException("Errore serie, valore '{}' duplicato.".format(elemento[0]))

        # controlla se time_series è ordinata
        for i in range(len(time_series)-1):
            # controlla una data con la succesiva
            if time_series[i][0]>time_series[i+1][0]:
                # alza eccezione
                raise ExamException(f"Errore, serie non ordinata '{time_series[i][0]}' > '{time_series[i+1][0]}'")
            
        # controlla che time_series abbia almeno un dato per ogni anno
        for i in range(len(time_series)-1):
            
            anno1=time_series[i][0]
            anno1=int(anno1[:4])
            
            anno2=time_series[i+1][0]
            anno2=int(anno2[:4])
            # se non sono lo stesso anno e se non sono successivi
            if (anno2-anno1)!=0 and (anno2-anno1)!=1:
                # allora manca il dato di un anno
                raise ExamException(f"Errore, manca il dato dell'anno {anno1+1}")

                
        # restituisce la lista time_series
        return time_series


# definisco la funzione per il calcolo della variazione del numero mensile dei passeggeri
# alla funzione passeremo la time_series e gli anni su cui fare il confronto
def detect_similar_monthly_variations(time_series,years):

# ---------------------------------- controllo correttezza valori time_series ----------------------------------
    # controllo se time_series è un valore valido
    if not time_series:
        raise ExamException("Lista time_series non valida")
    # controlla che time_series abbia almeno due anni consecutivi ed i valori siano nel formato valido
    if len(time_series)<2:
        raise ExamException("Valori time_series non sufficienti")

    # importo il modulo datetime per il controllo della correttezza del valore data nella lista time_series
    from datetime import datetime

    # per ogni elemento di time_series
    for item in time_series:
        # se l'elemento non è una lista alza eccezione
        if not isinstance(item,list):
            raise ExamException("Valori time_series non validi")
        # se è una lista deve avere almeno due valori altrimenti alza eccezione
        if len(item)!=2:
            raise ExamException("Valori time_series non validi")
        # se contiene due valori controlla che il primo sia una data nel formato corretto 
        # ed il secondo un int altrimenti alza eccezione
        if not datetime.strptime(item[0],'%Y-%m') or not isinstance(item[1],int):
            raise ExamException("Valori time_series non validi")

    # controllo che time_series abbia almeno due anni consecutivi
    # flag che segnala la presenza di due anni consecutivi
    flag=False
    for i in range(len(time_series)-1):
        
        anno1=time_series[i][0]
        anno1=int(anno1[:4])
        
        anno2=time_series[i+1][0]
        anno2=int(anno2[:4])
        # confronto tra i due anni
        if anno2==anno1+1:
            flag=True
    # se non trova anni consecutivi alza eccezione
    if not flag:
        raise ExamException("Non ci sono anni consecutivi nella lista")


    
# ---------------------------------- controllo correttezza valori di years ----------------------------------
    
    # controllo della correttezza di years, deve contenere due anni (interi) consecutivi e presenti nella lista
    # se non contiene 2 valori alza eccezione
    if len(years)!=2:
        raise ExamException("Valori di YEARS' non corretti")

    # controlla che gli anni siano di tipo intero
    anno1=years[0]
    anno2=years[1]
    # se non sono di tipo intero alza eccezione
    if not isinstance(anno1,int) or not isinstance(anno2,int):
        raise ExamException("Formato per lista YEARS non valido")

    # controlla che gli anni siano due valori successivi
    if (anno2-anno1)!=1:
        raise ExamException(f"Valori nella lista YEARS ({anno1} - {anno2}) non consecutivi")
        

    # controlla che gli anni siano presenti nella lista time_series
    
    # flag per controllare la presenza dei valori di years nella lista time_series
    # flag=True anno presente flag=False anno non presente
    flag_anno1=False
    flag_anno2=False

    # per ogni elemento della lista time_series
    for item in time_series:
        # variabile che conterrà l'anno per ogni item (primi 4 caratteri)
        # associa a year il primo valore (data) di item
        year=item[0]
        # converte la data in int
        year=int(year[:4])
      
        # se year = anno1 o year = anno2 attivo il flag
        if year==anno1:
            flag_anno1=True
           
        elif year==anno2:
            flag_anno2=True

    # se uno dei flag = False , allora anno non trovato e alza eccezione
    if not flag_anno1:
        raise ExamException(f"Anno : {anno1} non presente nella lista")
    if not flag_anno2:
        raise ExamException(f"Anno : {anno2} non presente nella lista")
            
    # lista che contiene i dati del primo anno, impostati di dafault su False
    lista_anno1=[False,False,False,False,False,False,False,False,False,False,False,False]
    # lista che contiene i dati del secondo anno, impostati di default su False
    lista_anno2=[False,False,False,False,False,False,False,False,False,False,False,False]

    
    # ciclo per estrapolare i dati riferiti agli anni scelti dalla lista time_series

    for item in time_series:
        # per capire l'anno elaborato durante il ciclo for
        anno=item[0]
        anno=int(anno[:4])
        # controlla se si trova sul primo o secondo anno
        if anno1==anno or anno2==anno:
            # per capire su quale mese mi trovo
            mese=item[0]
            mese=int(mese[-2:])
        # associo il valore di passeggeri di quest'anno e mese alla posizione corrispondente della lista_anno corrispondente
        if anno1==anno:
            lista_anno1[mese-1]=item[1]
        elif anno2==anno:
            lista_anno2[mese-1]=item[1]

            
    for i in range(12):
        print(f"{i+1} = {lista_anno1[i]} - {lista_anno2[i]} ")

        # calcola, per ogni anno la differenza dei valori dei mesi consecutivi, se presenti
    for i in range(11):
        if lista_anno1[i+1]==False:
            lista_anno1[i]=False
        else:
            if lista_anno1[i]!=False:
                lista_anno1[i]=lista_anno1[i+1]-lista_anno1[i]
                
        if lista_anno2[i+1]==False:
            lista_anno2[i]=False
        else:
            if lista_anno2[i]!=False:
                lista_anno2[i]=lista_anno2[i+1]-lista_anno2[i]        
            
        

    # elimino ultimo elemento della lista
    lista_anno1.pop(11) # oppure lista_anno1[-1]=[]
    lista_anno2.pop(11) # oppure lista_anno2[-1]=[]
  
    
    print("---------------------------------")

    for i in range(11):
        print(f"{i+1} = {lista_anno1[i]} - {lista_anno2[i]}")    

    # controlla se la differenza del mese dei due anni è simile +/- 2%
    # lista per contenere le 11 variazioni
    variation=[] 
    for i in range(11):
        val1=lista_anno1[i]
        val2=lista_anno2[i]
        # calcolo della percentuale della differenza tra lo stesso mese dei due anni
        if val1==False or val2==False:
            variation.append(False)
        else:
            # controlla tolleranza
            if val1>val2:
                if val1-val2<=2:
                    variation.append(True)
                else:
                    variation.append(False)
            else:
                if val2-val1<=2:
                    variation.append(True)
                else:
                    variation.append(False)
            

    print("---------------------------------------")
    for i in range(11):
        print(f"{i+1} - {variation[i]}")

    return variation

    

nome='data.csv'
my_file=CSVTimeSeriesFile(nome)
l=my_file.get_data()
years=[1957,1958]

lista=detect_similar_monthly_variations(l,years)

