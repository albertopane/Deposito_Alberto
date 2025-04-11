import sqlite3  
import numpy as np

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.vendite = np.random.randint(10, 1000)

    def tupla(self):
        return (self.titolo, self.autore, self.vendite)

conn = sqlite3.connect('libreria.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT,
        autore TEXT,
        vendite INTEGER
    )
''')

#inserisco 3 libri

libro1 = Libro("Il piccolo principe", "Antoine de Saint-Exupery")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("500 ricette gustose al Microonde", "Umberto Eco")

#creo una lista di tuple ricavate da tutti i libri
libri_da_inserire = [libro1, libro2, libro3]
dati = [libro.tupla() for libro in libri_da_inserire]

cur.executemany("INSERT INTO libri (titolo, autore, vendite) VALUES (?, ?, ?)", (dati))
conn.commit()

#seleziono tutti i nomi e li stampo
cur.execute("SELECT * FROM libri")
righe = cur.fetchall()

for r in righe:
    print(r)

conn.close()