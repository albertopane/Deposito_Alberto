import numpy as np

#creo l'array da 10 a 49
arr = np.arange(10,50)
print("All'inizio l'array è di tipo:", arr.dtype)

#cambio il tipo in float
arr2 = np.array(arr, dtype="float64")
print("Il nuovo tipo è:", arr2.dtype)

#stampo la forma dell'array
print("Forma dell'array:", arr2.shape)
