# implemento la classe ExamException, estensione di Exception
# da richiamare in caso di eccezioni 
class ExamException(Exception):
    pass
    
# implemento la classe MovingAverage()
class MovingAverage():
    # definisco il metodo __init__()  ed inizializzo 
    # fin = lunghezza finiestra
    def __init__(self,fin):
        # conrolla validità del valore fin
        if fin==None: # se uguale a None
            raise ExamException("Valore finestra non valido")
        if type(fin)!=int: # se il valore non è intero
            raise ExamException("Valore finestra non valido")
        if fin<1: # se il valore è >=1
            raise ExamException("Valore finestra non valido")
            
        self.fin=fin    
 
    # definisco il metodo compute() che prende in input la lista 
    #di valori della serie e che ritorni la lista di valori 
    #corrispondente alla media mobile
    def compute(self,data):
        # controllo la correttezza di 'data'
        
        # controlla se la lista è vuota
        if not data:
            # se è vuota alza eccezione
            raise ExamException("Lista vuota")
        # controlla se è stata passata una lista
        if type(data)!=list:
            raise ExamException("Lista non valida")

        # controlla se la lista ha dimensione >= alla lunghezza
        # della finestra (fin)
        if len(data)<self.fin:
            # se non lo è alza eccezione
            raise ExamException("Valori lista non sufficienti")

        # controlla se tutti i valori della lista sono valori
        # numerici
        for i,item in enumerate(data):
            # controlla se il valore è None
            if item==None:
                raise ExamException("Vvalore lista non valido")
                
            # controlla se stringa e nel caso sanitizza
            if type(item)==str:
                raise ExamException("Valore lista non valido")

        # lista che contiene le medie mobili
        medie=[]

        # totale finestre da processare
        tot_fin=len(data)-self.fin+1
        # ciclo per il calcolo delle  medie
        for i in range(tot_fin):
            # per sommare valori
            somma=0
            # ciclo per calcolo media finestre
            for y in range(self.fin):
                somma+=data[i+y]

            # aggiungo la media calcolata alla lista medie[]
            medie.append(somma/self.fin)
            
        # restitusce le medie
        return medie

#moving_average=MovingAverage(2)
#result=moving_average.compute([1,'ciao',4,8,16])
#print(result)