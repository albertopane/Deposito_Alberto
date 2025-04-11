import pandas as pd
import numpy as np

#dizionario per il dataframe
data = {
    'Prodotto': ['Prodotto A', 'Prodotto B', 'Prodotto A', 'Prodotto C', 'Prodotto B', 'Prodotto A', 'Prodotto C', 'Prodotto B', 'Prodotto A', 'Prodotto C'],
    'Quantità': [10, 5, 7, 3, 12, 9, 4, 8, 11, np.nan],
    'Prezzo Unitario': [15, 30, 15, 50, 30, 15, 50, np.nan, 15, 50],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Torino', 'Napoli', 'Roma', 'Milano', 'Napoli', 'Roma']
}

#creazione dataframe
df = pd.DataFrame(data)
print(df)

#rimuovo i duplicati
df = df.drop_duplicates()

#gestisco i valori mancanti
df['Quantità'].fillna(df['Quantità'].mean())
df['Prezzo Unitario'].fillna(df['Prezzo Unitario'].mean())

#aggiunta della colonna totale vendite
df['Totale Vendite'] = df['Quantità']*df['Prezzo Unitario']
print(df)

#raggruppa i dati per prodotto e trova il totale vendite di ciascuno
vendite_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
print(f"Vendite per prodotto:\n{vendite_per_prodotto}")

#trova il prodotto più venduto in termini di quantità
quantita_per_prodotto = df.groupby('Prodotto')['Quantità'].sum()
prodotto_piu_venduto = quantita_per_prodotto.idxmax()
print(f"Il prodotto più venduto in termini di quantità è: {prodotto_piu_venduto}")

#raggruppa per città e calcola il totale delle vendite per ciascuna città
vendite_per_città = df.groupby('Città')['Totale Vendite'].sum()
citta_piu_vendite = vendite_per_città.idxmax()
print(f"La città con il maggior volume di vendite totali è: {citta_piu_vendite}")

#crea un dataframe con vendite superiori a 600 euro
df_vendite_superiori_600 = df[df['Totale Vendite'] > 600]
print(f"Vendite superiori a 600 euro:\n{df_vendite_superiori_600}")

#ordina il dataframe per totale vendite in ordine decrescente
df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
print(f"DataFrame ordinato per totale vendite:\n{df_ordinato}")

#visualizza il numero di vendite per ogni città
num_vendite_per_città = df.groupby('Città')['Quantità'].sum()
print(f"Numero di vendite per città:\n{num_vendite_per_città}")

df_ordinato.to_csv('vendite_ordinate.csv', index=False)