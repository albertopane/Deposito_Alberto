import numpy as np

#creo un array di numeri casuali
arr = np.random.randint(10, 51, 20)

#estrazioni
pezzo2 = arr[:10]
pezzo3 = arr[-5:]
pezzo4 = arr[5:15]
pezzo5 = arr[2:21:3]

#copio i valori di arr in un altro array
arr_modificato = np.array(arr)
#modifico i valori richiesti
arr_modificato[5:10] = 99

#stampe di tutte le modifiche
print("Array originale:", arr)
print("Estrazioni:")
print(pezzo2)
print(pezzo3)
print(pezzo4)
print(pezzo5)
print("Array modificato:")
print(arr_modificato)