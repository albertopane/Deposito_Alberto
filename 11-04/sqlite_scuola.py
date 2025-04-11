import sqlite3  

conn = sqlite3.connect('scuola.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

#inserisco 3 studenti
for i in range(3):
    stud = input("Inserisci il nome di uno studente: \n")
    cur.execute("INSERT INTO studenti (nome) VALUES (?)", (stud,))

while True:

    scelta = input("Vuoi continuare?\n" \
        "Puoi scrivere: nome di un nuovo studente; 'modifica' per modificare uno studente; " \
        "'elimina' per eliminare uno studente; 'esci' per uscire: ")
    
    if scelta == "esci":  #esco dal menu studenti
        break

    elif scelta == "modifica":   #modifico uno studente a partire dall'indice
        indice = int(input("Inserisci l'indice dello studente da cambiare:"))
        nome = input("Inserisci il nuovo nome:")
        cur.execute("UPDATE studenti SET nome = ? WHERE id = ?", (nome, indice))

    elif scelta == "elimina":  #elimino uno studente a partire dall'indice
        indice = int(input("Inserisci l'indice dello studente da eliminare:"))
        cur.execute("DELETE FROM studenti WHERE id = ?", (indice,))

    else:  #inserisco altri studenti oltre ai 3
        cur.execute("INSERT INTO studenti (nome) VALUES (?)", (scelta,))

conn.commit()

#seleziono tutti i nomi e li stampo
cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for r in righe:
    print(r)

conn.close()