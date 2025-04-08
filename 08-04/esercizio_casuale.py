#libreria random
import random

#creo il numero casuale
numero_da_indovinare = random.randint(1,100)

#definisco funzione per paragonare i valori
def paragona_valori(x):
    if x < numero_da_indovinare:
        print("Prova con un numero più grande.")
    else:
        print("Prova con un numero più piccolo.")

#itero fino a quando l'utente non trova il numero
while True:
    numero_inserito = int(input("Indovina il numero (è tra 1 e 100): "))
    if numero_da_indovinare == numero_inserito:
        scelta = input("Hai indovinato!!\nVuoi uscire? (si = esci, no = nuova partita): ")
        if scelta == "si":
            break
        else:
            continue
    #chiamo la funzione per spiegare all'utente come è andato
    paragona_valori(numero_inserito)
    
