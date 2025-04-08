numeri = []

#inserisci i numeri nella quantità voluta
while True:
    valore = input("Inserisci un numero. Quando hai finito, scrivi 'ok': ")
    if valore == "ok":
        break
    valore = int(valore)
    numeri.append(valore)

#trova il numero massimo
massimo = -100000
for i in range(len(numeri)):
    if numeri[i] > massimo:
        massimo = numeri[i]

#conta i numeri presenti nella lista
conta = 0

while conta < len(numeri):
    conta +=1

#controllo lunghezza e stampa finale
if len(numeri) == 0:
    print("La lista è vuota.")
else:
    print("Il numero massimo è:", massimo)
    print("La stringa è lunga", conta, " elementi")

