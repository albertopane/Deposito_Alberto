#es 1

#ciclo while per continuare a ripetere l'operazione
while True:
    inizio = int(input("Da che numero partiamo? "))
    #ciclo for per stampare i numeri
    for i in range(inizio, -1, -1):
        print(i)
    ripeti = input("Vuoi ripetere? si/no")
    #controllo se ripetere il ciclo o uscire
    if (ripeti == "no"):
        break


#es2 pari
numeri_pari = []

while len(numeri_pari) < 5:
    dato = int(input("Inserisci un numero: "))
    if(dato%2 == 1):
        print("Il numero è dispari.")
    else:
        print("Il numero è pari.")
        numeri_pari.append(dato)

print(numeri_pari)


#es 2 primo
numeri_primi = []

while len(numeri_primi) < 5:
    dato2 = int(input("Inserisci un numero primo: "))
    flag = 0
    for i in range(dato2 - 1, 1, -1):
        if(dato2%i == 0):
            flag +=1
            break

    if(flag == 0):
        print("Il numero è primo!")
        numeri_primi.append(dato2)
    else:
        print("Mi dispiace, il numero non è primo.")

print(numeri_primi)