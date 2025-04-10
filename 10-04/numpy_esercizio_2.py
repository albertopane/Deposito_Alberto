import numpy as np

class StranoArray():
    def __init__(self, numeri):
        self.numeri = numeri
        self.arr = None

    def arr_equidistante(self, inizio, fine):
        self.arr = np.linspace(inizio, fine, self.numeri)
        print(f"L'array con valori equidistanti: {self.arr}")
    
    def arr_casuale(self):
        self.arr = np.random.rand(self.numeri)
        print(f"L'array con valori casuali: {self.arr}")

    def somma_arr(self, arr2):
        arr_somma = StranoArray(self.numeri)
        arr_somma.arr = self.arr + arr2
        print(f"Il nuovo array sommato e': {arr_somma.arr}")
        return arr_somma

    def somma_elementi(self):
        somma = np.sum(self.arr)
        print(f"La somma degli elementi e': {somma}")
    
    def somma_se_maggiore_di(self, limite):
        somma = np.sum(self.arr[self.arr > limite])
        print(f"La somma degli elementi maggiori di {limite} e': {somma}")
        
arr1 = StranoArray(50)
arr1.arr_equidistante(0,10)

arr2 = StranoArray(50)
arr2.arr_casuale()

arr3 = StranoArray(50)
arr3 = arr1.somma_arr(arr2.arr)

arr3.somma_elementi()
arr3.somma_se_maggiore_di(5)

