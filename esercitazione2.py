# implemento la classe ExamException, estensione di Exception
# da richiamare in caso di eccezioni 
class ExamException(Exception):
    pass

# implemento della classe Diff()
class Diff():
    # definisco il metodo __init__
    def __init__(self,ratio=1):
        # controllo correttezza valore di ratio
        
        if ratio==None: # se = None imposta dafeult=1
            raise ExamException("Valore ratio non valido") 
        if type(ratio)==str:
            raise ExamException("Valore ratio non valido")
        if not float(ratio): # controlla se ratio è intero
            raise ExamException("Valore ratio non valido")
        if ratio<1:# controlla se è un valore <1
            raise ExamException("Valore ratio non valido") 

        self.ratio=ratio

    # definisco il metodo compute() che prenda in input una lista 
    # di valori numerici e che ritorni in output la lista 
    # corrispondente alle loro differenze.
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
        if len(data)<2:
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

        # lista che contiene le differenza
        diff=[]

        # totale finestre da processare
        tot_valori=len(data)-1
        # ciclo per il calcolo delle differenze
        for i in range(tot_valori):
            # calcolo differenza e divido per ratio
            val=(data[i+1] - data[i]) / self.ratio
            # aggiungo il valore calcolato alla lista diff[]
            diff.append(val)
            
        # restitusce le differenze
        return diff

#diff=Diff()
#result=diff.compute([2,4,8,16])
#print(result)            