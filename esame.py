# TOT. RIGHE CODICE : 157
#
#
# CLASSI :    - class ExamException(Exception) : estensione della classe Exception()
#
#             - class CSVTimeSeriesFile() : al suo interno, il metodo get_data() restituisce una lista time_series da valori letti da un
#                                           file 'data.csv'. time_series è una lista di liste formate da un valore stringa contenente 
#                                           la data 'YYYY-MM' ed un valore intero >0 che indica il numero di passeggeri
#
#
#
# FUNZIONI :  - controlla_anni_consecutivi(time_series) : controlla se time_series ha almeno un dato per ogni anno. 
#                                                         restituisce : -) (l'anno mancante)
#                                                                       -) -1 se è presente solamente il dato di un anno
#                                                                       -) -2 se sono presenti i dati di più di un anno
#
#              - controlla_ordine(time_series) : controlla se la lista time_series è ordinata. Restituisce: True = ord. / False = non ord.  
#
#              - controlla_data(data) : controlla la correttezza del formato della data. Se è nel formato 'YYYY-MM' restituisce True,
#                                       altrimenti restituisce False
#
#              - controlla_date_duplicate(time_series) : controlla se time_series ha valori duplicati. Restituisce False se non ha duplicati,
#                                                        altrimenti restituisce la data duplicata
# 
#              - detect_similar_monthly_variation(time_series,years): per il calcolo della variazione del numero mensile dei passeggeri.
#                                                                     alla funzione passeremo la time_series e gli anni su cui fare il 
#                                                                     confronto. Restituisce una lista di 11 elementi (True o False).
#                                                                     Essendo una funzione esterna a CSVTimeSeriesFile() ripeterà tutti i
#                                                                     controlli della validità dei valori passati come parametri

class ExamException(Exception):
    pass


def controlla_anni_consecutivi(time_series):
    
    conta_anni=-1  # per sapere se nella lista sono presenti i valori di un solo anno o più
    for i in range(len(time_series)-1):
        anno1=time_series[i][0]
        anno1=int(anno1[:4])

        anno2=time_series[i+1][0]
        anno2=int(anno2[:4])
        if anno1!=anno2:
            conta_anni=-2 # più di un anno
        # se non sono lo stesso anno o non sono consecutivi allora manca il dato di un anno
        if (anno2-anno1)!=0 and (anno2-anno1)!=1:
            return (anno1+1) # manca il dato dell'anno anno1+1
    return conta_anni



def controlla_ordine(time_series):
    
    for i in range(len(time_series)-1):
        # controlla una data con la successiva
        if time_series[i][0]>time_series[i+1][0]:
            return False # non ordinata
    return True  # ordinata



def controlla_data(data):
    # importo il modulo datetime per l'utilizzo di strptime()
    from datetime import datetime
    # controlla che data sia nel formato corretto
    try:
        datetime.strptime(data,'%Y-%m') 
        return True  # formato data corretto
    except:
        return False # formato data non corretto



def controlla_date_duplicate(time_series):
    
    for item in time_series:
        uguali=0        # conta elementi uguali, se = 1 non ci sono duplicati
        for elemento in time_series:
            if item[0]==elemento[0]:
                uguali+=1
            # esce dal ciclo se trova una data duplicata
            if uguali>1:
                break 
        # se ci sono duplicati restituisce il valore duplicato, altrimenti False
        if uguali>1:
            return item[0]   # restituisce il valore duplicato
        
    return False # non ci sono duplicati



class CSVTimeSeriesFile():
    # definisco il metodo __init__
    def __init__(self,name):
        self.name=name

    # definisco il metodo get_data()
    def get_data(self):
        # controllo se il file è leggibile:
        
        # se non è una stringa alza eccezione
        if not isinstance(self.name,str):
            raise ExamException("Errore, il nome file non è di tipo stringa")
        
        try:    # provo ad aprire il file in sola lettura
            my_file=open(self.name,'r')
            my_file.readline()    # se lo apre controlla che abbia almeno una linea
            my_file.close()    # chiudo il file
            
        except Exception as e:
            # file non leggibile, alza eccezione
            raise ExamException(f"Errore lettura file: {e}")

        # se il file è leggibile e contiene almeno una linea: apro il file in sola lettura
        my_file=open(self.name,'r')

        
        lista=[]    # creo lista vuota che conterrà gli elementi del file
        
        # scorro il file
        for line in my_file:
            
            elementi=line.split(',')             # divido gli elementi tramite split su ','
            elementi[-1]=elementi[-1].strip()    # elimino '\n' dall'ultimo elemento
            
            # se non si trova sulla riga di intestazione, può aggiungere elementi alla lista
            if elementi[0]!='date':
                lista.append(elementi)
        
        my_file.close()    # chiudo il file

        
        time_series=[]    # conterrà la lista appena creata ma con i valori dei passeggeri convertiti in int

        for item in lista:
            # item_convertito conterrà item con il numero passeggeri convertito in int
            item_convertito=[]
            # se il primo valore di item è una data in formato corretto, lo aggiunge a item_convertito
            if controlla_data(item[0]):
                item_convertito.append(item[0])
            else: 
                continue    # altrimenti non elabora item e va al successivo

            # se il formato della data è corretta, controlla se il secondo valore di item è convertibile in int
            try:
                passeggeri=int(item[1])
                
                if passeggeri<0:     # controlla che sia >=0
                    continue         # se il valore dei passeggeri è negativo non elabora item e 
                else:
                    item_convertito.append(passeggeri)
            except: 
                continue     # se non è convertibile in int non elabora item e va al successivo

            # se item_convertito è composto da due valori validi lo aggiunge a time_series
            time_series.append(item_convertito)

        # controlla se time_series ha delle date duplicate
        data=controlla_date_duplicate(time_series)
        if data!=False:
            raise ExamException("Errore serie, valore '{}' duplicato.".format(data))

        # controlla se time_series è ordinata, altrimenti alza eccezione
        if not controlla_ordine(time_series):
            raise ExamException("Time_series non ordinata")

        # controlla se time_serie ha almeno un valore per ogni anno
        serie=controlla_anni_consecutivi(time_series) # -1 o -2 se i dati sono corretti, altrimenti l'anno mancante
        if serie>0:
            raise ExamException("Manca almeno un dato dell'anno {}".format(serie))

        # se time_series ha valori validi...
        return time_series



def detect_similar_monthly_variation(time_series,years):
    
    # ----------controllo validità di time_series ----------
    if not time_series:
        raise ExamException("Lista time_series non valida")
    # se l'elemento non è una lista alza eccezione
    if not isinstance(time_series,list):
        raise ExamException("time_series non è una lista")
    # controlla che time_series abbia almeno due elementi
    if len(time_series)<2:
        raise ExamException("Valori time_series non sufficienti")
    
        # controlla se time_series ha valori validi
    for item in time_series:
        # se item non è una lista di due valori alza eccezione
        if not isinstance(item,list) or len(item)!=2:
            raise ExamException("Valori time_series non validi")
        # se è una lista e contiene due valori controlla che il primo sia una data nel formato corretto 
        # ed il seconto un int, altrimenti alza eccezione
        if not controlla_data(item[0]) or not isinstance(item[1],int):
            raise ExamException("Valori time_series non validi")
        # se il valore passeggeri è negativo alza eccezione
        if int(item[1])<0:
            raise ExamException("Valore passeggeri non valido :{}".format(item[1]))

    # controlla che time_Series sia ordinata
    if controlla_ordine(time_series)!=True:
        raise ExamException("lista non ordinata") 

    # controlla date duplicate
    if controlla_date_duplicate(time_series)!=False:
        raise ExamException("lista contiene valori duplicati")
            
    # controlla che time_series abbia almeno due anni consecutivi            
    if controlla_anni_consecutivi(time_series)!=-2: # la funzione restituisce -2 se trova due anni consecutivi
        raise ExamException("Non ci sono anni consecutivi nella lista")    
    
    # ---------- controllo dei valori di 'years' ----------        
        
    # se non è una lista e non contiene 2 valori alza eccezione
    if not isinstance(years,list):
        raise ExamException("'years' deve essere una lista di 2 interi")
    if len(years)!=2:
        raise ExamException("'years' deve essere una lista di 2 interi")
        
    # controlla se i valori di years sono di tipo intero
    anno1=years[0]
    anno2=years[1]
    if not isinstance(anno1,int) or not isinstance(anno2,int):
        raise ExamException("Valori di 'years' non di tipo intero")
    
    if (anno2-anno1)!=1:    # controlla che gli anni siano consecutivi
        raise ExamException("Valori di 'years' {} e {} non consecutivi o non inseriti correttamente".format(anno1,anno2))
        
    # controlla che i due anni siano presenti nella lista time_series. Due flag per controllare la presenza dei valori di years nella lista
    # flag = True anno presente, flag = False anno non presente
    # Se gli anni sono presenti, estrapola i dati per ogni mese

    # potremmo anche fare prima un ciclo per sapere se gli anni sono presenti nella time_series e poi un altro ciclo per estrapolare i dati
        
    flag_anno1=False
    flag_anno2=False
    
     # lista che contengono i 12 dati del primo e del secondo anno, impostati di default su False
    lista_anno1=[False,False,False,False,False,False,False,False,False,False,False,False]
    lista_anno2=[False,False,False,False,False,False,False,False,False,False,False,False]

    for item in time_series:
        # variabile che conterrà l'anno per ogni item[0] (primi 4 caratteri)
        # associa ad 'anno' il primo valore (cioè la data) di item
        anno=item[0]
        # converte l'anno in int (primi 4 caratteri)
        anno=int(anno[:4])
        
        # controlla se si trova sul primo o secondo anno
        if anno==anno1 or anno==anno2:
            # per capire su quale mese si trova
            mese=item[0]
            mese=int(mese[-2:])
            
            # associo il valore dei passeggeri di quest'anno e mese alla posizione corrispondente della
            # lista_anno e se anno = anno1 oppure anno = anno2 attivo il flag
            if anno==anno1:
                flag_anno1=True
                lista_anno1[mese-1]=item[1]
            elif anno==anno2:
                flag_anno2=True
            lista_anno2[mese-1]=item[1]

    # se uno dei flag = False , allora anno non trovato e alza eccezione
    if not flag_anno1:
        raise ExamException("Anno {} non presente nella lista".format(anno1))
    if not flag_anno2:
        raise ExamException("Anno {} non presente nella lista".format(anno2))

    # se tutto è andato a buon fine...
    # calcola, per ogni anno, la differenza dei valori dei mesi consecutivi se presenti, altrimenti 
    # assegna False di default
    for i in range(11):
        # controlla se è possibile fare la differenza dei valori
        
        # primo anno
        if lista_anno1[i+1]==False:
            lista_anno1[i]=False
        else:
            if lista_anno1[i]!=False:
                lista_anno1[i]=lista_anno1[i+1]-lista_anno1[i]
                
        # secondo anno
        if lista_anno2[i+1]==False:
            lista_anno2[i]=False
        else:
            if lista_anno2[i]!=False:
                lista_anno2[i]=lista_anno2[i+1]-lista_anno2[i]  
                
    # elimino l'ultimo elemento delle liste
    lista_anno1.pop(11)  # oppure lista_anno1[-1]=[]
    lista_anno2.pop(11)  # oppure lista_anno2[-1]=[]

    # controlla se la differenza sullo stesso mese dei due anni è simile +/- 2
    
    # lista che contiene le 11 variazioni
    variation=[]
    
    for i in range(11):
        
        val1=lista_anno1[i]     # val1 = valore mese i-esimo del primo anno
        val2=lista_anno2[i]     # val2 = valore mese i-esimo del secondo anno
        
        if val1==False or val2==False:
            variation.append(False)
            
        else: # controlla tolleranza
            if -2<=val1-val2<=2:
                variation.append(True)
            else:
                variation.append(False)
    return variation