#chiedo all'utente il valore massimo
numero = int(input("Inserisci il numero limite per la Serie:"))

def fibonacci(x):
    #creo i valori iniziali da sommare
    a = 0
    b = 1
    while a <= x:
        print(a)
        #creo una variabile temporanea per salvare il valore di a in modo da sommarlo a b
        temp = a
        #il valore di b che diventa il nuovo a
        a = b
        #b diventa sé stesso più il vecchio valore di a
        b = temp + b

#uso la funzione
fibonacci(numero)

