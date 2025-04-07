#creazione variabili

id = 0
x = True

while x:
    nome = ""
    password = ""

    nome = input("inserisci il tuo nickname: ")
    password = input("Inserisci la tua password: ")
    id +=1

    #condizioni
    if nome == "":
        print("Non hai valorizzato.")
    else:
        nome_inserito = input("Inserisci il tuo nickname:")
        password_inserita = input("Inserisci la tua password: ")
        if nome_inserito == nome and password_inserita == password:
            print("Sei loggato.")

#condizione di rottura