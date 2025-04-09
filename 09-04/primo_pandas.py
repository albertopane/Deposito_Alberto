import pandas as pd

#caricamento ed esplorazione dei dati
file_path = 'vendite.csv'

df = pd.read_csv(file_path)

#e' fondamentale esplorare i dati all'inizio
print(df.head())

