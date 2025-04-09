import numpy as np

#array unidimensionale
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

#metodi

#output il valore massimo di righe x colonne (r, c)
print("Forma dell'array", arr.shape)
#righe della tabella
print("Dimensioni dell'array:", arr.ndim)
print("Tipo di dati:", arr.dtype)
print("Numero di elementi:", arr.size)
print("Somma degli elementi:", arr.sum())
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print("indice del valore massimo:", arr.argmax())

#creo array che va da 0 a 9
arr3 = np.arange(10)
print(arr3)

#reshape: da una sola riga con 6 valori a 2 righe
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)

#slicing e indexing
arr = np.array([1, 2, 3, 4, 5])

#indexing
print(arr[0])

#slicing
print(arr[1:3])

#boolean indexing
print(arr[arr > 2])

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

#slicing sulle righe
print(arr2d[1:3])

#slicing sulle colonne
print(arr2d[:, 1:3])

#slicing misto
print(arr2d[1:, 1:3])

#altri slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2:7])

#slicing da 1 a 8 con passo 2
print(arr[1:8:2])

print(arr[:5])
print(arr[5:])

print(arr[-5:])
print(arr[:-5])

#fancy indexing
arr = np.array([10, 20, 30, 40, 50])

#uso un array di indici
indices = np.array([1, 3])
print(arr[indices])

#funziona anche con le liste
indices = [0, 2, 4]
print(arr[indices])

