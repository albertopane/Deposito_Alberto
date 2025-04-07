lista = ["cane", "gatto", "cavallo", "ornitorinco", "colibrì"]

print("Menù: Aggiungi = a, Rimuovi = r, Elimina = e, Modifica = m\n")
scelta = input("Scegli l'operazione: \n")
if (scelta == "a"):
    elemento = input("Cosa vuoi aggiungere? ")
    lista.append(elemento)
    print("Elemento aggiunto in coda.")
elif (scelta == "r"):
    elemento = input("Cosa vuoi rimuovere? ")
    if elemento in lista:
        lista.remove(elemento)
        print("Elemento rimosso dalla lista.")
    else:
        print("Elemento non presente in lista.")
elif (scelta == "e"):
    lista.clear()
    print ("Lista cancellata.")
elif (scelta == "m"):
    indice = int(input("In che posizione è l'elemento da modificare?\n"))
    elemento = input("Cosa vuoi scrivere al suo posto?\n ")
    lista[indice] = elemento
else:
    print("Comando non valido.")

print("Lista finale: ", lista)