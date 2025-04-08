#semantica delle funzioni
def nome_della_funzione ():
    pass

#funzione di esecuzione
def saluta():
    print("Ciao!")

saluta()

#funzione con parametri
def somma(a, b):
    risultato = a + b
    print(risultato)

somma(5,7)

#funzione di ritorno
def riporta_dato(x):
    return x*x

numero = riporta_dato(3)
print(numero)

somma(riporta_dato(3), riporta_dato(3))

#funzione con parametri standard

def funzione_standard(x = 1):
    return x+x

