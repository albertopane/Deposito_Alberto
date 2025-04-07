#tipi numerici
intero = int(input("Inserisci un numero intero: "))
virgola = float(input("Inserisci un numero con la virgola: "))

#tipi semantici
stringa = input("Inserisci una parola: ")

print(stringa[0])
print(stringa.lower())

s = "Ciao, mondo!"
print((len(s)))
print(s.upper())
print(s.split(','))
print(s.replace('mondo','universo'))

carattere = input("Inserisci una singola lettera:")

#tipi booleani

x = False
y = True

print(5>11)
print(13<50)

x = 5
y = 10
z = 7

print(x<y and y>z)
print(x<y or z>y)
print(not(x<y))

#liste

lista_dati = [1, 2, 3, 4, 0]
lista_dati2 = [1, "mirko", True]
lista_dati3 = []

print(lista_dati)
print(lista_dati[2])
print(lista_dati2[1])
lista_dati.sort()
print(lista_dati)

numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]
numeri[0] = 20

print(numeri[0])
print(numeri[2])

inserimento = int(input("Inserisci un numero: "))
lista_dati3.append(inserimento)
inserimento = int(input("Inserisci un numero: "))
lista_dati3.append(inserimento)