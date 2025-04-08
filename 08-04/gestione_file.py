#lettura del file
file = open("esempio_testo.txt", "r")

tutte_le_righe = file.read()
riga = file.readline()

print(tutte_le_righe)

file.close()

#scrittura del file
file = open("esempio_testo2.txt", "w")

file.write("Sto sostituendo il testo")
file.close()

with open("esempio_testo_nuovo.txt", "w") as file:
    file.write("Auto chiudo la mia chiamata")