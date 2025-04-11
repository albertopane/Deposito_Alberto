import pandas as pd
import numpy as np

data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'David', 'Eva', 'Francesca', 'Giovanni', 'Hanna', 'Igor', 'Luca',
             'Marta', 'Nina', 'Omar', 'Paola', 'Quirino', 'Rita', 'Stefano', 'Tiziana', 'Ugo', 'Vera', 
             'Walter', 'Xenia', 'Yara', 'Zoe', 'Andrea', 'Bianca', 'Claudio', 'Daniele', 'Elena', 'Fabio'],
    'Età': np.linspace(5, 80, 30),
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Genova', 'Bologna', 'Firenze', 'Palermo', 'Catania', 'Venezia',
              'Verona', 'Bari', 'Reggio Calabria', 'Modena', 'Ancona', 'Lecce', 'Trieste', 'Pescara', 'Salerno', 'Como',
              'Cagliari', 'Sassari', 'Aosta', 'Rimini', 'Vibo Valentia', 'La Spezia', 'Siena', 'Parma', 'Arezzo', 'Ravenna'],
    'Salario': np.random.randint(1000, 8000, 30)
}

df = pd.DataFrame(data)

#preassessment dei dati
print(f"Prime 5 righe:\n{df.head()}\n")
print(f"Ultime 5 righe:\n{df.tail()}\n")

#tipo di dati di ciascuna colonna
print(df.dtypes)

#calcolo statistiche di base di età e salario
print(f"Media Età: {df['Età'].mean()}\n")
print(f"Mediana Età: {df['Età'].median()}\n")
print(f"Deviazione standard Età: {df['Età'].std()}\n")

print(f"Media Salario: {df['Salario'].mean()}\n")
print(f"Mediana Salario: {df['Salario'].median()}\n")
print(f"Deviazione standard Salario: {df['Salario'].std()}\n")

#rimuovo i duplicati
df = df.drop_duplicates()

#gestisco i valori mancanti
df['Età'].fillna(df['Età'].median())
df['Salario'].fillna(df['Salario'].median())

#creazione colonna categoria età
categorie = []
for eta in df['Età']:
    if eta < 18:
        categorie.append('Giovane')
    elif eta >= 18 and eta <= 65:
        categorie.append('Adulto')
    else:
        categorie.append('Anziano')

#aggiunta colonna categoria età
df['Categoria Età'] = categorie

print(f"Prime 5 righe:\n{df.head()}\n")
print(f"Ultime 5 righe:\n{df.tail()}\n")

#salvo in un nuovo file
df.to_csv('dataframe_finale.csv', index=False)