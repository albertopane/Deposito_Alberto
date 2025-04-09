class Libro():
    
    #costruttore con le 3 variabili da inizializzare
    def __init__(self, titolo, autore, nr_pag):
        self.titolo = titolo
        self.autore = autore
        self.nr_pag = nr_pag

    #metodo che stampa le info del libro
    def stampa(self):
        print(f"Il libro {self.titolo} e' stato scritto da {self.autore} e ha {self.nr_pag} pagine.")

#esempi
prontuario = Libro("Manuale di Nonna Papera","Nonna Papera", 5240)
prontuario.stampa()

class Biblioteca():

    #costruttore con catalogo vuoto su ciascuna biblioteca
    def __init__(self):
        self.catalogo = []

    #crea e aggiungi un libro al catalogo
    def aggiungiLibro(self, titolo, autore, nr_pag):
        nuovo_libro = Libro(titolo, autore, nr_pag)
        self.catalogo.append(nuovo_libro)
        return nuovo_libro
    
    #stampa la lista di libri dal catalogo attuale
    def stampaLibri(self):
        for x in self.catalogo:
            x.stampa()
        

biblio = Biblioteca()
libro2 = biblio.aggiungiLibro("1984", "George Orwell", 350)
libro3 = biblio.aggiungiLibro("500 Ricette Gustose al Microonde", "Papa Francesco", 900)
biblio.stampaLibri()