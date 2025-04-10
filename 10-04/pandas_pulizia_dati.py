import pandas as pd
import numpy as np

#nan è un valore mancante
data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, np.nan, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data)

print(f"DataFrame originale:{df}")

#rimozione duplicati
df = df.drop_duplicates()

#gestione dati mancanti (rimuovo le righe non piene)
df_cleaned = df.dropna()

#sostituisco dati mancanti con valore di default
df['Età'].fillna(df['Età'].mean(), inplace=True)

#stampo il df pulito
print(f"DataFrame dopo la pulizia:{df_cleaned}")

#stampo il df con dati mancanti sostituiti
print(f"DataFrame con dati mancanti sostituiti:{df}")

