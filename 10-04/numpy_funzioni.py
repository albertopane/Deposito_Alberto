import numpy as np

#lispace: genera un array di numeri equidistanti tra 2
#(inizio, fine, quantita')
arr = np.linspace(0, 1, 5)
print(arr)

#random: array di numeri casuali
random_arr = np.random.rand(3, 3)
#matrice 3 x 3 con valori casuali uniformi tra 0 e 1
print(random_arr)

#funzioni su tutto l'array
sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value)
print("Mean:", mean_value)
print("Standard deviation:", std_value)

#esercizio
class Matrice:

    #costruttore della matrice
    def __init__(self, righe, colonne):
        self.righe = righe
        self.colonne = colonne
        self.matrice = []

    def crea_matrice_equidistante(self, inizio, fine):
        #creo un array di 12 numeri equidistanti
        a = np.linspace(inizio, fine, self.righe*self.colonne)
        #trasformo in un array righe x colonne
        self.matrice = a.reshape((self.righe, self.colonne))

    def crea_matrice_casuale(self):
        self.matrice = np.random.rand(self.righe, self.colonne)

numeri_equidistanti = Matrice(3, 4)
numeri_equidistanti.crea_matrice_equidistante(0, 1)
#creo una matrice con numeri tra 0 e 1
matrice_casuale = Matrice(3, 4)
matrice_casuale.crea_matrice_casuale()

#funzione per sommare e stampare
def stampa_somma(x):
    #sommo i singoli valori di una matrice
    somma = np.sum(x.matrice)
    #stampo i valori
    print(f"La somma della matrice e' {somma}")

stampa_somma(numeri_equidistanti)
stampa_somma(matrice_casuale)