import pandas as pd

#creazione di un dataframe da dizionario di python
data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data)

#stampo il dataframe originale
print(f"DataFrame originale:{df}")

#seleziono le righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23]

#stampo le righe selezionate
print(f"Persone con età superiore a 23 anni:{df_older}")

#aggiungo una nuova colonna Maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

print(f"DataFrame con colonna maggiorenne:{df}")