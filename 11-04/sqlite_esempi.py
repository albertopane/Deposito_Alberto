# Importa il modulo per lavorare con SQLite
import sqlite3  

# 1. Connessione (crea un file 'miodatabase.db' se non esiste)
conn = sqlite3.connect('miodatabase.db')

# 2. Cursore per eseguire comandi SQL
cur = conn.cursor()

# 3. Creazione di una tabella (se non esiste)
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# 4. Inserimento di un dato. Il ? serve per sicurezza ad evitare la SQL injection
cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mirko",))

# 5. Salvataggio delle modifiche
conn.commit()

cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mario",))
conn.commit()

cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()

for r in righe:
    print(r)

cur.execute("UPDATE utenti SET nome = ? WHERE id = ?", ("Luigi", 1))
conn.commit()

cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()

for r in righe:
    print(r)

cur.execute("DELETE FROM utenti WHERE id = ?", (1,))
conn.commit()

# 6. Query per leggere i dati
cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()

# 7. Stampa dei risultati
for r in righe:
    print(r)
# 8. Chiusura della connessione
conn.close()

